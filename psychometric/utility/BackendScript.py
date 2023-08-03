#pymongo module helps for establishing connection with Mongo cluster
from pymongo import MongoClient

#importing jsonutil for converting pymongo cursor to json using dumps function
import bson.json_util as jsonutil

#for adding timestamps in documents
import datetime

#for tracing the exceptions
import traceback



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
                                        'questionCount': 1
                                    }
                                }, {
                                    '$sort': {
                                        'traitID': 1
                                    }
                                }
                            ])


        return jsonutil.dumps(traitData)




    
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

    

    

        
