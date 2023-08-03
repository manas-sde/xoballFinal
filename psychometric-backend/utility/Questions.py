import random as rd
from pymongo import MongoClient
from flask import jsonify
from collections import defaultdict as dd
import string
import traceback
import sys,os
#import mysql.connector
from time import perf_counter as pfc

#from app import SQLdb
import json


class Questions:


    client1 = MongoClient('mongodb+srv://xobme:xobme@cluster0.ub2jer1.mongodb.net/?retryWrites=true&w=majority')
    #client = MongoClient('mongodb://localhost:27017')
    client = MongoClient("mongodb+srv://manas:fyTGlHSyD43CCctL@cluster0.rsnix.gcp.mongodb.net/test")

    db = client1['xobin']
    db_new = client['psychometricDb']

    traits = ['Emotional Stability','Integrity','Perfectionism','Openness','Reasoning','Rule consciousness','Team Work','Sensitivity','Conflict Management','Inclusion','Influencing']


    def getQuestions(self,*args,**kwargs):
        
        #print(args)


        db_collection = self.db_new['psychometric_questions']
        #print(list(db_collection.find({"traitID":{"$in" : args[0]}},{"_id":0,"options":{"opScore":0}}))[0])
        quesData = db_collection.find({"traitID":{"$in" : args[0]}},{"_id":0,"options.opScore":0})
        #print(list(quesData))

        # l = [q for q in quesData]

        # print(len(json.dumps(l)))


        finalData = []

        for q in quesData:
            rd.shuffle(q['options'])
            finalData.append({
                'trait_id' : q["traitID"],
                'question_id' : q["questionID"],
                'question': q["question"],
                "options" : q['options'],
            })
        

        rd.shuffle(finalData)
        #print(finalData)
        return finalData



    def postResponses(self,*args,**kwargs):

        start_time = pfc()

        allData = kwargs['data']
        assessmentID = kwargs['assessmentID']

        #print("Checkpoint 0 passed")

        question_collection = self.db_new.psychometric_questions

        response_collection = self.db.psychometric_responses

        reports_collection = self.db.psychometric_reports

        allTraitScores_collections = self.db.psychometric_totalTraitScores

        #print("Checkpoint 00 passed")

        isCollection = response_collection.find_one()
        
        if not(isCollection):
            candID = 101
            responseID = 101
            #print("Checkpoint 2 in if block passed")
            response_collection.insert_one({
            'candID' : 101,
            'responseID' : 101,
            'responses' : allData['responses']
            })
            #print("Checkpoint 3 in if block passed")

        else:
            #print("Checkpoint 1 passed")
            last_collection = response_collection.find({},{'_id':0,'candID':1,'responseID':1}).sort([('_id',-1)]).limit(1)
            last_collection = list(last_collection)[0]
            candID = last_collection['candID'] + 1
            responseID = last_collection['responseID'] + 1
            

            #print("Checkpoint 2 in else block passed")
            response_collection.insert_one({
                'candID' : candID,
                'responseID' : responseID,
                'responses' : allData['responses']
            })

            #print("Checkpoint 2 in else block passed")

        print('Response successfully saved.')


        #print("Checkpoint 00 passed")

        #print('Questions Attempted : ',list(map(int,allData['responses'].keys())))


        scoresData = question_collection.find({"questionID":{"$in" : list(map(int,allData['responses'].keys()))}},{'traitID':1,'questionID':1,'_id':0,'options':{'opID':1,'opScore':1}})

        #print(list(scoresData))


        allData['reports'] = dd(lambda:{})

        allData['totalScorePerTraits'] = dd(lambda:0)

        
        for ques in scoresData:
            for op in ques['options']:
                #print([op['opID']],[allData['responses'][str(ques['questionID'])]])
                if op['opID'] == int(allData['responses'][str(ques['questionID'])]):
                    score_q = op['opScore']
                    break
            
            allData['reports'][self.traits[ques['traitID']-1]][str(ques['questionID'])]=score_q

            allData['totalScorePerTraits'][self.traits[ques['traitID']-1]]+=score_q



        isCollection = reports_collection.find_one()
        
        if not(isCollection):
            #print("Checkpoint 2 in if block passed")
            reports_collection.insert_one({
            'candID' : candID,
            'responseID' : responseID,
            #'reportID' : 101,
            'report_detail' : allData['reports'],
            'scorePerTraits' : allData['totalScorePerTraits'],
            'assessmentID' : assessmentID,
            })
            #print("Checkpoint 3 in if block passed")

        else:
            #print("Checkpoint 1 passed")
            last_collection = reports_collection.find({},{'_id':0,'reportID':1}).sort([('_id',-1)]).limit(1)
            last_collection = list(last_collection)[0]
            
            
            #reportID = last_collection['reportID'] + 1
            

            #print("Checkpoint 2 in else block passed")
            reports_collection.insert_one({
                'candID' : candID,
                'responseID' : responseID,
                #'reportID' : 101,
                'report_detail' : allData['reports'],
                'scorePerTraits' : allData['totalScorePerTraits'],
                'assessmentID' : assessmentID,
            })

            #print("Checkpoint 2 in else block passed")

        print('Report successfully saved.')


        allTraitScores = allTraitScores_collections.find_one({},{'_id':0})

        newScores = dd(lambda:[])

        for trait,score in allData['totalScorePerTraits'].items():

            if trait in allTraitScores.keys():
                newScores[trait] = allTraitScores[trait] +  [{
                                        'candID': candID,
                                        'score': + score
                                    }]

            else:
                newScores[trait] =  [{
                                        'candID': candID,
                                        'score': + score
                                    }]




        allTraitScores_collections.update_one({},{"$set":newScores})

        print('allTraitScores Collection updated')

        
        end_time = pfc()
       #f = open('log.txt','a')
        #f.write(f'\n In MongoDB, response time of route /post-responses : {end_time-start_time}\n')
        


        return {
            'report':allData['reports'],
            'totalScorePerTraits' : allData['totalScorePerTraits'],
            'allTraitScores' : allTraitScores,
        }



    def fetchAllReports(self):
        start_time = pfc()
        reports_collection = self.db.psychometric_reports
        allTraitScores_collections = self.db.psychometric_totalTraitScores

        allReportsData = reports_collection.find({'candID':{"$gt":398}},{'candID':1,'scorePerTraits':1,'_id':0}).sort('_id',-1).limit(50)

        benchmarkScores = allTraitScores_collections.find_one({},{'_id':0})

        end_time = pfc()
       #f = open('log.txt','a')
        #f.write(f'\n In MongoDB, response time of route /fetch-all-reports : {end_time-start_time}\n')
        

        return {
            'allReportsData' : list(allReportsData),
            'benchmarkScores' : benchmarkScores,
        }


    def createAssessment(self,*args,**kwargs):
        start_time = pfc()
        allAssessment_collection = self.db.all_assessment_collection


        assessmentName = kwargs['name']
        choosenTraits = kwargs['traits']

        assessmentID = str(''.join(rd.choices(string.ascii_uppercase + string.digits, k=9)))

        while (True):
            try:
                assessmentData = {
                    '_id' : assessmentID,
                    'assessmentName' : assessmentName,
                    'traits' : choosenTraits,
                }

                allAssessment_collection.insert_one(assessmentData)

                break

            except Exception as e:
                print(e)
                print(traceback.format_exc())
                
        end_time = pfc()
       #f = open('log.txt','a')
        #f.write(f'\n In MongoDB, response time of route /create-assessment : {end_time-start_time}\n')
        
        
        return {'assessmentID' : assessmentID}



    def getAssessment(self,*args,**kwargs):
        start_time = pfc()
        assessmentID = kwargs['id']

        allAssessment_collection = self.db_new.psychometric_assessments

        assessmentData = allAssessment_collection.find_one({'_id':assessmentID})

        allTraits = assessmentData['traits']
        assessmentName = assessmentData['assessmentName']


        allQuestionData = self.getQuestions(allTraits)
        
        end_time = pfc()
       #f = open('log.txt','a')
        #f.write(f'\n In MongoDB, response time of route /get-assessment : {end_time-start_time}\n')
        

        return {
            'questionData' : allQuestionData,
            'assessmentName' : assessmentName,
        }


    def fetchAllAssessments(self):

        start_time = pfc()
        allAssessment_collection = self.db.all_assessment_collection
        

        allAssessmentData = list(allAssessment_collection.find())[::-1]

        end_time = pfc()
       #f = open('log.txt','a')
       #f.write(f'\n In MongoDB, response time of route /fetch-all-assessments : {end_time-start_time}\n')
        

        return allAssessmentData


    def fetchAssessmentReports(self,*args,**kwargs):

        start_time = pfc()

        assessmentID = kwargs['assessmentID']
        #print(assessmentID)
        reports_collection = self.db.psychometric_reports
        allAssessment_collection = self.db.all_assessment_collection

        allTraitScores_collections = self.db.psychometric_totalTraitScores

        allReportsData = reports_collection.find({'candID':{"$gt":398},'assessmentID':assessmentID},{'candID':1,'scorePerTraits':1,'_id':0}).sort('_id',-1).limit(50)

        assessmentName = allAssessment_collection.find_one({'_id':assessmentID})['assessmentName']

        benchmarkScores = allTraitScores_collections.find_one({},{'_id':0})

        end_time = pfc()
       #f = open('log.txt','a')
        #f.write(f'\n In MongoDB, response time of route /fetch-assessment-reports : {end_time-start_time}\n')
        

        return {
            'allReportsData' : list(allReportsData),
            'benchmarkScores' : benchmarkScores,
            'assessmentName' : assessmentName,
        }




class MySQLDB:

            
    '''
    db =  mysql.connector.connect(user='root', password='54321',
                                host='localhost',
                                database='xobin_db')

    '''
    #----------------- Adding New Traits to MySQL DB-----------
    def addNewTrait(self):

        try:
            cursor = self.db.cursor()

            query_string = ''' insert into Psychometric_Traits(traitID,trait_name) values(%s,%s)'''

            n = int(input("Enter number of traits you want to add : "))
            nn = n
            i = 3
            while(n):
                n-=1
                cursor.execute(query_string,[i,input("Enter trait name : ")])
                i+=1

            self.db.commit()
            print('data committed')
            cursor.close()
            print("Cursor closed")
            #SQLdb.close()
            #cursor.connection.commit()

            print(f"You have successfully inserted {nn} traits.")
            #n-=1

        except Exception as e:
            print(e)
            print(traceback.format_exc())
            cursor.close()



    #------------ Fetch all questions from json file
    # def getQuestions(self):
    #     f = open('static1/Questions.json','r',encoding='utf-8')
    #     allQuestions = json.load(f)

    #     return allQuestions

    
    #--------------- Uploading questions to MySQL db
    def uploadQuestions(self):
        try:
            allQuestions = self.getQuestions()

            cursor = self.db.cursor()

            insert_questions_query_string = ''' insert into Questions(questionID,traitID,question) values(%s,%s,%s)'''
            insert_options_query_string = ''' insert into Options(optionID,questionID,option_text,opScore) values(%s,%s,%s,%s)'''

            questionID_start = 1001
            optionID = 100
            i = 0
            for ques in allQuestions:
                print(ques['questionID'])
                cursor.execute(insert_questions_query_string,[ques['questionID'],ques['traitID'],ques['question']])

                for op in ques['options']:
                    optionID+=1
                    cursor.execute(insert_options_query_string,[optionID,ques['questionID'],op['option'],op['opScore']])

                self.db.commit()
            

                print(f"Question {i}:{ques['questionID']} uploaded.")
                i+=1


            cursor.close()
            print("Cursor closed")

        except Exception as e:
            print(e)
            print(traceback.format_exc())
            cursor.close()

        self.db.close()



    #------------- Function for creating an assessment----------
    def createAssessment(self,*args,**kwargs):
        start_time = pfc()

        #--------- Creating cursor object with connected db
        try:
            cursor = self.db.cursor()
        except:
            self.db.reconnect()
            cursor = self.db.cursor()

        assessment_name = kwargs['name']
        traits = str(kwargs['traits'])
        companyID = 1

        query_string = '''insert into Assessments(assessment_name,companyID,traits) values(%s,%s,%s) '''

        

        try:
            cursor.execute(query_string,[assessment_name,companyID,traits])
            self.db.commit()
            print('Assessment Created')

            assessmentID = cursor.lastrowid
            cursor.close()
            self.db.close()

        except Exception as e:
            print(e)
            print(traceback.format_exc())
            cursor.close()
            self.db.close()
            return "Assessment has not been created successfully"
        

                
        end_time = pfc()
        #f = open('log.txt','a')
        #f.write(f'\n In MySQLDB, response time of route /create-assessment : {end_time-start_time}\n')
        

        return {'assessmentID' : assessmentID}



    def getAssessment(self,*args,**kwargs):
        start_time = pfc()
        try:
            cursor = self.db.cursor(dictionary=True)
        except:
            self.db.reconnect()
            cursor = self.db.cursor(dictionary=True)

        assessmentID = kwargs['id']

        #allAssessment_collection = self.db.all_assessment_collection

        #assessmentData = allAssessment_collection.find_one({'_id':assessmentID})

        get_assessment_query = ''' select * from Assessments where assessmentID = %s '''

        cursor.execute(get_assessment_query,[assessmentID])

        assessmentData = cursor.fetchall()[0]

        allTraits = assessmentData['traits']
        assessmentName = assessmentData['assessment_name']
        print(allTraits,assessmentName)


        
        allQuestionData = self.getQuestions(allTraits)

        cursor.close()
        self.db.close()


        end_time = pfc()
        #f = open('log.txt','a')
        #f.write(f'\n In MySQLDB, response time of route /get-assessment : {end_time-start_time}\n')
        

        return {
            'questionData' : allQuestionData,
            'assessmentName' : assessmentName,
        }

    


    def getQuestions(self,*args,**kwargs):
        
        traits = args[0]
        traits_parameter = str(tuple(traits)) 
        if len(traits)==0:
            return "No traits selected"
        elif len(traits)==1:
            traits_parameter = traits_parameter[:-2] + ')' 
            
        #print('traits parameter : ',traits_parameter)
        try:
            cursor = self.db.cursor(dictionary=True)
        except:
            self.db.reconnect()
            cursor = self.db.cursor(dictionary=True)

        getQuestions_query = ''' select q.traitID,q.questionID,q.question, group_concat(concat('{ "opID" : ',o.optionID,',"option" : "',o.option_text,'"}')) as options from Questions as q,Options as o where q.questionID=o.questionID and q.traitID in %s group by q.questionID;  '''

        cursor.execute(getQuestions_query%traits_parameter)

        #print(cursor.fetchall())
        quesData = cursor.fetchall()

        # templ = json.dumps(quesData)
        # print(len(templ))

        #print(json.loads('['+quesData[0]['options']+']'))

        print(type(quesData[0]['options']))
        finalData = []

        for q in quesData:
            q['options'] = json.loads('['+ q['options'] + ']')
            rd.shuffle(q['options'])
            finalData.append({
                'trait_id' : q["traitID"],
                'question_id' : q["questionID"],
                'question': q["question"],
                "options" : q['options'],
            })
        

        rd.shuffle(finalData)
        cursor.close()
        self.db.close()
        #print(finalData)
        return finalData


    
    def fetchAllAssessments(self):
        start_time = pfc()
        try:
            cursor = self.db.cursor(dictionary=True)
        except:
            self.db.reconnect()
            cursor = self.db.cursor(dictionary=True)

        companyID=1
        fetchAllAssessments_query = ''' select assessmentID as _id, assessment_name as assessmentName, traits from Assessments where companyID=%s order by _id desc'''
        
        cursor.execute(fetchAllAssessments_query,[companyID])

        allAssessmentData = cursor.fetchall()


        allAssessmentData = list(allAssessmentData)
        for assessment in allAssessmentData:
            assessment['traits'] = json.loads(assessment['traits'])
        cursor.close()
        self.db.close()
        #print(allAssessmentData)

        end_time = pfc()
       #f = open('log.txt','a')
        #f.write(f'\n In MySQLDB, response time of route /fetch-all-assessments : {end_time-start_time}\n')
        


        return allAssessmentData
    



    
        

    def postResponses(self,*args,**kwargs):
        start_time = pfc()
        try:
            cursor = self.db.cursor(dictionary=True)
        except:
            self.db.reconnect()
            cursor = self.db.cursor(dictionary=True)

        allData = kwargs['data']
        assessmentID = kwargs['assessmentID']
        

        allQuestionID = str(tuple([int(x) for x in allData['responses'].keys()]))
        allOptionID = str(tuple([int(x) for x in allData['responses'].values()]))
        #print(allQuestionID)
        candID = 2
        calc_score_query = ''' select Q.traitID,sum(O.opScore) as score from (select questionID,optionID,opScore from Options where optionID in %s) as O,(select traitID,questionID from Questions where questionID in %s) as Q where O.questionID=Q.questionID group by Q.traitID; '''

        print(calc_score_query%(allOptionID,allQuestionID))

        cursor.execute(calc_score_query%(allOptionID,allQuestionID)) 
        
        

        
        allTraitScore = list(cursor.fetchall())  

        insert_report_query = ''' insert into Reports(candID,assessmentID,traitID,score) values %s '''
        print(insert_report_query)
        values = []
        for record in allTraitScore:
            values.append((candID,assessmentID,record['traitID'],int(record['score'])))

        values_str = str(values)[1:-1]

        cursor.execute(insert_report_query%values_str)

        self.db.commit()
        cursor.close()
        self.db.close()



        end_time = pfc()
       #f = open('log.txt','a')
        #f.write(f'\n In MySQLDB, response time of route /post-responses : {end_time-start_time}\n')
        

        return 'Data successfully inserted'



    def fetchAssessmentReports(self,*args,**kwargs):
        start_time = pfc()

        try:
            cursor = self.db.cursor(dictionary=True)
        except:
            self.db.reconnect()
            cursor = self.db.cursor(dictionary=True)

        
        assessmentID = kwargs['assessmentID']
        print(assessmentID)

        if not(kwargs['assessmentID']):
            return "Assessment ID Required to fetch the assessment reports"
        
        assessmentName_query = ''' select assessment_name from Assessments where assessmentID=%s '''

        cursor.execute(assessmentName_query,[assessmentID])

        assessmentName = cursor.fetchone()['assessment_name']

        print(assessmentName)

        allReportsData_query = ''' select R.candID, group_concat('"', P.trait_name,'":',R.score) as scorePerTraits from Reports as R,Psychometric_Traits as P where P.traitID=R.traitID and R.assessmentID = %s group by R.candID;''' % assessmentID

        allReportsData = []

        cursor.execute(allReportsData_query)

        allReportsData_list = list(cursor.fetchall())

        for x in allReportsData_list:
            temp = '{'+x['scorePerTraits']+'}'
            print(temp)
            allReportsData.append({
                'candID' : x['candID'],
                'scorePerTraits' : json.loads(temp)
            })


        print(allReportsData)

        benchmarkScores_query = ''' select P.trait_name, group_concat('{ "candID" : ',R.candID,', "score" : ',R.score,'}') as scores from Reports as R, Psychometric_Traits as P where P.traitID=R.traitID and assessmentID=%s group by R.traitID;''' % assessmentID
        cursor.execute(benchmarkScores_query)
        benchmarkScores_list = list(cursor.fetchall())
        print(benchmarkScores_list)
        benchmarkScores  = {}

        for x in benchmarkScores_list:
            benchmarkScores[x['trait_name']] = json.loads('[' + x['scores'] + ']')

        print(benchmarkScores)

        cursor.close()
        self.db.close()


        end_time = pfc()
       #f = open('log.txt','a')
        #f.write(f'\n In MySQLDB, response time of route /fetch-assessment-reports : {end_time-start_time}\n')
        

        return {
            'allReportsData' : allReportsData,
            'benchmarkScores' : benchmarkScores,
            'assessmentName' : assessmentName,
        }


    def fetchAllReports(self):
        start_time = pfc()

        try:
            cursor = self.db.cursor(dictionary=True)
        except:
            self.db.reconnect()
            cursor = self.db.cursor(dictionary=True)
        

        allReportsData_query = ''' select R.candID, group_concat('"', P.trait_name,'":',R.score) as scorePerTraits from Reports as R,Psychometric_Traits as P where P.traitID=R.traitID group by R.candID;'''

        allReportsData = []

        cursor.execute(allReportsData_query)

        allReportsData_list = list(cursor.fetchall())

        for x in allReportsData_list:
            temp = '{'+x['scorePerTraits']+'}'
            print(temp)
            allReportsData.append({
                'candID' : x['candID'],
                'scorePerTraits' : json.loads(temp)
            })


        #print(allReportsData)

        benchmarkScores_query = ''' select P.trait_name, group_concat('{ "candID" : ',R.candID,', "score" : ',R.score,'}') as scores from Reports as R, Psychometric_Traits as P where P.traitID=R.traitID group by R.traitID;''' 
        cursor.execute(benchmarkScores_query)
        benchmarkScores_list = list(cursor.fetchall())
        print(benchmarkScores_list)
        benchmarkScores  = {}

        for x in benchmarkScores_list:
            benchmarkScores[x['trait_name']] = json.loads('[' + x['scores'] + ']')

        #print(benchmarkScores)


        end_time = pfc()
       #f = open('log.txt','a')
        #f.write(f'\n In MySQLDB, response time of route /fetch-all-reports : {end_time-start_time}\n')
        


        return {
            'allReportsData' : allReportsData,
            'benchmarkScores' : benchmarkScores,
        }




