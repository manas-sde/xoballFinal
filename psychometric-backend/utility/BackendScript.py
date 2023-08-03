#pymongo module helps for establishing connection with Mongo cluster
from pymongo import MongoClient

#importing jsonutil for converting pymongo cursor to json using dumps function
import bson.json_util as jsonutil

#for adding timestamps in documents
import datetime

#for tracing the exceptions
import traceback

#for setting environment variable
import os,json

#GCloud tasks
from google.cloud import tasks_v2

#Importing request module for sending cross origin requests to few Endpoints
import requests

#Importing random module for generating random id and shuffling purpose
import random as rd






#BackendClass responsible for all the methods that will be invoked via API endpoints of backend server for psychometric project.
class BackendClass:

    #Production MongoDB cluster URI
    client = MongoClient("mongodb+srv://manas:fyTGlHSyD43CCctL@cluster0.rsnix.gcp.mongodb.net/test")


    #selecting psychometric database from cluster
    db = client['psychometricDb']


    #Collection containing all traits data like traitID, traitName, traitDefinition,etc
    allTraitsCollection = db['psychometric_traits']
    
    #Psychometric question library containing objects with field such as traitID, questionID,question, options[array]
    allQuestionsCollection = db['psychometric_questions']


    #Collection of all the assessments created
    allAssessmentCollection = db['psychometric_assessments']

    # Collectin for storing candidate report data
    allReportsCollection = db['psychometric_reports']






    #getTraits method returns the list of objects containing trait data (traitID,traitName,questionCount)
    #inputs : None 
    #returns - [{traitID:int,traitName:string,questionCount:integer}]  #questionCount represents number of question in corresponding traits
    def getTraits(self,*args,**kwargs):
        
        #Creating aggregate pipeline for counting number of question in each traits and grouping data to be sent. 
        traitData = self.allQuestionsCollection.aggregate(
                            [
                                {
                                    '$group': {
                                        '_id': '$traitID', 
                                        'traitID': {
                                            '$first': '$traitID'
                                        }, 
                                        'questionCount': {
                                            '$sum': 1
                                        }
                                    }
                                }, {
                                    '$lookup': {
                                        'from': 'psychometric_traits', 
                                        'localField': 'traitID', 
                                        'foreignField': 'traitID', 
                                        'as': 'traitData'
                                    }
                                }, {
                                    '$project': {
                                        '_id': 0, 
                                        'traitID': 1, 
                                        'traitName': {
                                            '$arrayElemAt': [
                                                '$traitData.traitName', 0
                                            ]
                                        },
                                        'traitDefinition': {
                                            '$arrayElemAt': [
                                                '$traitData.traitDefinition', 0
                                            ]
                                        },
                                        'traitPositiveAspects': {
                                            '$arrayElemAt': [
                                                '$traitData.traitPositiveAspects', 0
                                            ]
                                        },
                                        'traitNegativeAspects': {
                                            '$arrayElemAt': [
                                                '$traitData.traitNegativeAspects', 0
                                            ]
                                        },
                                        'traitNeed': {
                                            '$arrayElemAt': [
                                                '$traitData.traitNeed', 0
                                            ]
                                        },
                                        'questionCount': 1,
                                        'traitCatName' : {
                                            '$arrayElemAt': [
                                                '$traitData.traitCatName', 0
                                            ]
                                        }
                                    }
                                }, {
                                    '$sort': {
                                        'traitID': 1
                                    }
                                }
                            ])


        return jsonutil.dumps(traitData)



    # This method creates assessment based on choosen traits.
    '''
    input - requestData
                - assessmentID
                - assessmentName
                - choosenTraits [array of traitID]
                - companyID
    
    returns - JSON of status, comment, error[] (if applicable)
    '''
    
    def createNewAssessment(self,*args,**kwargs):

        errorMessages = []

        try:

            payload = {
                'assessmentID' : kwargs['requestData'].get('assessmentID'),
                'assessmentName' : kwargs['requestData'].get('assessmentName'),
                'choosenTraits' : kwargs['requestData'].get('choosenTraits'),
                'companyID' : kwargs['requestData'].get('companyID')
            }

            for key in payload.keys():
                if not(payload[key]):
                    errorMessages.append(str(key) + 'is required in payload or request')

            

            isAllChoosenTraitsInteger = all(str(traitID).isdigit() for traitID in payload['choosenTraits'])

            

            if not(isAllChoosenTraitsInteger):
                errorMessages.append('All choosen traitID must be an integer')


            
            assessmentData = {
                '_id' : payload['assessmentID'],
                'assessmentName' : payload['assessmentName'],
                'traits' : payload['choosenTraits'],
                'companyID' : payload['companyID'],
                'createdAt': datetime.datetime.utcnow(),
                'lastUpdatedAt': datetime.datetime.utcnow(),
            }

            if not(errorMessages):
                self.allAssessmentCollection.insert_one(assessmentData)

        

        except Exception as e:
            print(e)
            print(traceback.format_exc())
            errorMessages.append(str(e))

        
        if not(errorMessages):
            returnData =  {
                'status' : 'Success',
                'comment' : 'Assessment Created successfully'
            }

        else:
            returnData =  {
                'status' : 'Failed',
                'comment' : "Assessment not created due to some errors.",
                'error' : errorMessages
            }

        return returnData


    # This method is responsible for queuing up the assessment evaluation task in google cloud task queue.
    '''
    input
        - responseData(keyword argument) 
            - candID
            - companyID
            - reportID
            - assessmentID
            - responses : dict(questionID:optionID)
    return 
        returnStatement
            - "Data successfully inserted" 
            OR
            - Error message
    '''
    def evaluateResponses(self, *args, **kwargs):

        try:
            # Storing function argument in local variable
            responseData = kwargs['responseData']

            # Fetching Candidate ID
            candID = responseData["candID"]
            
            #Fetching Company ID
            companyID = responseData["companyID"]

            # Fetching Assessment ID
            assessmentID = responseData['assessmentID']

            # Fetching Report ID
            reportID = responseData['reportID']
            
            # Fetching Responses : dict(questionID:optionID)
            responses = responseData['responses']

            
            
            # Storing the path of service key file
            credential_path = "service_key.json"

            # Storing path of service key in environment variable
            os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

            # Create a client.
            client = tasks_v2.CloudTasksClient()
            
            # GCP project name
            project = 'xobin-verification'
            
            # GCP task queue name
            queue = 'assessment'
            
            # GCP project location
            location = 'us-central1'

            # Creating parent object for GCP task
            parent = client.queue_path(project, location, queue)
            

            # Backend endpoint for for creating report of candidate
            url = 'https://psychometric-backend-aw54llemya-uc.a.run.app/psychometric/generate-report'

            # Payload for API endpoint
            payload = {
                'responses':responses, # reponses dict
                'candID' : candID, # candidate ID
                'companyID' : companyID, # companyID
                'reportID' : reportID, # reportID
                'assessmentID' : assessmentID # assessmentID

            }
            
            #print('responses : ',responses)
            #print('payload : ', payload)




            # Construct the request body.
            task = {
                "http_request": {  # Specify the type of request.
                    "http_method": tasks_v2.HttpMethod.POST,
                    "url": url,  # The full url path that the task will be sent to.
                }
            }

            if payload is not None:

                # Check if payload is of type dict
                if isinstance(payload, dict):
                    # Convert dict to JSON string
                    payload = json.dumps(payload)

                    # specify http content-type to application/json
                    task["http_request"]["headers"] = {"Content-type": "application/json"}

                # The API expects a payload of type bytes.
                converted_payload = payload.encode()

                # Add the payload to the request.
                task["http_request"]["body"] = converted_payload

            #print(payload['responses'],type(payload['responses']))
            response = client.create_task(request={"parent": parent, "task": task})

            print("Created task {}".format(response.name))

            returnStatement = "Data successfully inserted"

        except Exception as e:
            returnStatement = str(e)
            print(traceback.format_exc())

        return returnStatement




    # Method responsible for creating report of candidate
    '''
    input
        - responseData(keyword argument) 
            - candID
            - companyID
            - reportID
            - assessmentID
            - responses : dict(questionID:optionID)
    '''
    def generateReport(self,*args,**kwargs):
        
        

        try:
            # Storing function argument in local variable
            responseData = kwargs['responseData']

            # Fetching Candidate ID
            candID = responseData["candID"]
            
            #Fetching Company ID
            companyID = responseData["companyID"]

            # Fetching Assessment ID
            assessmentID = responseData['assessmentID']

            # Fetching Report ID
            reportID = responseData['reportID']
            
            # Fetching Responses : dict(questionID:optionID)
            responses = responseData['responses']

            # Extracting all questions ID for a particular assessment
            allQuestionsID = list(map(int,responses.keys()))


            

            questionsData = self.allQuestionsCollection.aggregate(
                                       [
                            {
                                '$match': {
                                    'questionID': {
                                        '$in': allQuestionsID
                                    }
                                }
                            }, {
                                '$lookup': {
                                    'from': 'psychometric_traits', 
                                    'localField': 'traitID', 
                                    'foreignField': 'traitID', 
                                    'as': 'traitData'
                                }
                            }, {
                                '$project': {
                                    '_id': 0, 
                                    'questionID': 1, 
                                    'options': {
                                        'opID': 1, 
                                        'opScore': 1
                                    }, 
                                    'traitName': {
                                       "$arrayElemAt": ["$traitData.traitName",0]
                                    }, 
                                    'traitCatName': {
                                       "$arrayElemAt": ["$traitData.traitCatName",0]
                                    }, 
                                    'traitBuckets': {
                                        '$arrayElemAt': [
                                            '$traitData.buckets', 0
                                        ]
                                    }
                                }
                            }
                        ]
            )


            # Storing category wise scores
            categoryWiseResult =  {}

            

            for ques in questionsData:

                # Checking if category name is available
                if 'traitCatName' in ques.keys():

                    traitCatName = ques['traitCatName']

                    for op in ques['options']:

                        if op['opID'] == int(responses[str(ques['questionID'])]):
                            score_q = op['opScore']
                            break

                    # Checking if category is already stored in category wise result dict or not
                    
                    if traitCatName not in list(categoryWiseResult.keys()):
                        categoryWiseResult[traitCatName] = {
                            'categoryObtainedScore' : score_q,
                            'categoryTotalScore' : 3,
                            'categoryTraits' : {
                                ques['traitName'] : {
                                    'traitObtainedScore' : score_q,
                                    'traitTotalScore' : 3
                                }
                            }
                        }

                    else:
                        categoryWiseResult[traitCatName]['categoryObtainedScore']+=score_q
                        categoryWiseResult[traitCatName]['categoryTotalScore']+=3

                        if ques['traitName'] not in list(categoryWiseResult[traitCatName]['categoryTraits'].keys()):
                            categoryWiseResult[traitCatName]['categoryTraits'][ques['traitName']] = {
                                'traitObtainedScore' : score_q,
                                'traitTotalScore' : 3
                            }
                        else:
                            categoryWiseResult[traitCatName]['categoryTraits'][ques['traitName']]['traitObtainedScore'] += score_q
                            categoryWiseResult[traitCatName]['categoryTraits'][ques['traitName']]['traitTotalScore'] += 3

                    obtainedScore = categoryWiseResult[traitCatName]['categoryTraits'][ques['traitName']]['traitObtainedScore']
                    totalScore = categoryWiseResult[traitCatName]['categoryTraits'][ques['traitName']]['traitTotalScore']
                    score_percentage = obtainedScore*100/totalScore
                    for bucket in ques['traitBuckets']:
                        if score_percentage <= bucket['bucketMaxRange']:
                            categoryWiseResult[traitCatName]['categoryTraits'][ques['traitName']]['traitComment'] = bucket['bucketComment']
                            categoryWiseResult[traitCatName]['categoryTraits'][ques['traitName']]['traitDescription'] = bucket['bucketDescription']

            

            # Report Data to be inserted in mongo collection
            reportData = {
                'candID' : candID,
                'companyID' : companyID,
                'assessmentID' : assessmentID,
                'reportID' : reportID,
                'categoryWiseResult' : categoryWiseResult,
                'createdAt': datetime.datetime.utcnow(),
                'lastUpdatedAt': datetime.datetime.utcnow(),
            }
            
            self.allReportsCollection.insert_one(reportData)

            returnStatement = "Report successfully generated"
            
        except Exception as e:
            returnStatement = str(e) 
            print(traceback.format_exc())

        try:
            #Endpoint for changing candidate status
            url = 'https://us-central1-interactapp-202211.cloudfunctions.net/updateInteractStatus'
            payload = {
                "reportID" : reportID
            }
            resp_obj = requests.post(url=url,data=payload)

            #Endpoint for removing candiate from firebase
            url = 'https://us-central1-firehawk-xobin.cloudfunctions.net/user-delete-autopsych'
            payload = {
                "reportID" : reportID,
                "assessmentID": assessmentID,
                "companyID" : companyID
            }
            resp_obj = requests.post(url=url,data=payload)

        except Exception as e:
            print(e)
            print(traceback.format_exc())
        
        return returnStatement


    #Endpoint for fetching Assessment Details from base xobin database
    '''
    Input 
        - assessmentID
    Output
        - response data in json
    '''
    
    def getAssessmentDetails(self,*args,**kwargs):

        assessmentID = kwargs['assessmentID']
    
        #Endpoint for fetching the assessment details
        '''
        Sample Response - 
                            {
                "title": "\"Xobin Co\" Psychometric Assessment - 13/04/2023, 14:45:07",
                "company_name": "Xobin Co",
                "logo": "https://storage.googleapis.com/interactapp-202211.appspot.com/icl3941NZDFSFJ09Sicl3941I34XZ4NS4MXobinLogo.png",
                "email": "vishal@xobin.com",
                "companyid": 3941,
                "paymentid": 8048,
                "uiid": 4649,
                "signin": 0,
                "linktoken": 9516,
                "archived": 0,
                "deleted": 0,
                "oid": 33698
                }
        '''
        url = 'https://us-central1-interactapp-202211.cloudfunctions.net/get-test-details-by-oid'

        payload = {
                "assessmentID" : assessmentID
        }

        #Sending post requests to endpoint
        assessmentData = requests.post(url=url,data=payload).json()

        return assessmentData

    

    # Endpoint for fetching candidate details
    def getCandidateDetails(self,*args,**kwargs):
        try:
            candID = kwargs["candID"]
            print(candID)

            #Endpoint for fetching candidateDetails
            url = 'https://us-central1-interactapp-202211.cloudfunctions.net/getCandidateDetails'

            payload = {
                "candidateIds" : [candID]
            }

            #Sending post requests to endpoint
            candData = requests.post(url=url,data=payload).json()[0]

            print(candData)

            return candData
        except Exception as e:
            print(e)
            print(traceback.format_exc())
            return {
                "name" :'',
                "email" : ''
            }


    # Endpoint for sending candidate report data to frontend
    def getCandidateReport(self,*args,**kwargs):
        
        #Extracting report ID from parameter
        reportID = kwargs['reportID']

        reportData = self.allReportsCollection.find_one({'reportID':reportID},{"_id":0,"categoryWiseResult":1,"createdAt":1,"assessmentID":1,"candID":1})

        candData = self.getCandidateDetails(candID=reportData['candID'])
        
        assessmentDetails = self.getAssessmentDetails(assessmentID = reportData['assessmentID'])

        assessmentName = assessmentDetails["title"]

        reportData["candidateName"] = candData["name"]
        reportData["candidateEmail"] = candData["email"]
        reportData["assessmentName"] = assessmentName
        reportData["companyLogo"] = assessmentDetails["logo"]
        
        return reportData


    

    # Endpoint for fetching all assessments data
    def fetchAllAssessments(self):

        allAssessment_collection = self.allAssessmentCollection

        allAssessmentData = list(allAssessment_collection.find())[::-1]
        #print(allAssessmentData)

        return allAssessmentData


    #Endpoint for fetching all reports
    def getAllReports(self,*args,**kwargs):

        assessmentID = kwargs['assessmentID']

        allReportsCollection = self.allReportsCollection

        allReportsData = list(allReportsCollection.find({"assessmentID":assessmentID},{"_id":0,"lastUpdatedAt":0}))[::-1]

        return allReportsData



    #Endpoint for fetching all questions of given traits
    # Input - Pass list of trait ID as first argument
    # Output - Get json of all question data of given traits
    
    def getQuestions(self,*args,**kwargs):
        
        db_collection = self.allQuestionsCollection

        selectedTraits = kwargs['selectedTraits']
        

        #FIltering all questions and fetching all fata except option scores
        quesData = db_collection.find({"traitID":{"$in" : selectedTraits}},{"_id":0,"options.opScore":0})
        


        finalData = []

        #Shuffling options and formatting them in a manner that is required in frontend
        for q in quesData:
            rd.shuffle(q['options'])
            finalData.append({
                'trait_id' : q["traitID"],
                'question_id' : q["questionID"],
                'question': q["question"],
                "options" : q['options'],
            })
        

        #Shuffling all questions
        rd.shuffle(finalData)
        

        return finalData



    # Endpoint serving frontend of test taking interface
    '''
        Input : 
            - assessmentID
            - companyID

        Output : 
            - questionData
            - assessmentName
            - companyName
            - company_logo
    '''

    def populateTestTakingInterface(self,*args,**kwargs):
        
        assessmentID = kwargs['assessmentID']
        companyID = kwargs['companyID']

        # Fetching list of all selected traits for an assessment
        selectedTraits = self.getSelectedTraits(assessmentID = assessmentID)['selectedTraits']
        print(selectedTraits)
        
        questionData = self.getQuestions(selectedTraits = selectedTraits)

        # Fetching assessment meta data from base xobin database 
        assessmentDetails = self.getAssessmentDetails(assessmentID=assessmentID)

        assessmentName = assessmentDetails['title']
        companyName = assessmentDetails['company_name']
        company_logo = assessmentDetails['logo']


        return {
            'questionData' : questionData,
            'assessmentName' : assessmentName[:35],
            'companyName' : companyName,
            'companyLogo' : company_logo
        }




    

    # Endpoint for finding all traitID of any assessment
    '''
        Input 
            - assessmentID
        Output
            - selectedTraits(type:list)
    '''


    def getSelectedTraits(self,*args,**kwargs):
        
        assessmentID = kwargs['assessmentID']
        

        if not(isinstance(assessmentID,int)):
            try:
                assessmentID = int(assessmentID)
            except:
                assessmentID = assessmentID


        selectedTraits = self.allAssessmentCollection.find_one({'_id':assessmentID},{'_id':0,'traits':1})['traits']

        return {
            'selectedTraits' : selectedTraits
        }






        


    

    

        
