from app import app
from utility.parseExcel import *
from utility.Questions import *
from flask import request,send_from_directory,send_file
from google.cloud import tasks_v2
import json,os
from utility.BackendScript import BackendClass






@app.route('/psychometric/get-excel-data')
def getExcelData():
	return ExcelParse().getExcelData()



@app.route('/psychometric/get-excel-data-xlrd')
def getExcelDataXlrd():
	return ExcelParse().getExcelDataXlrd()


@app.route('/psychometric/get-questions',methods=['GET','POST'])
def getQuestions(*args,**kwargs):
	print('inside api route')
	traits = request.json['traits']
	#print(traits)
	return Questions().getQuestions(traits)



	


# !Deprecated (Latest alternative route - '/psychometric/generate-report' )
@app.route('/psychometric/post-responses',methods=['POST'])
def postResponses(*args,**kwargs):
	allData = {
		'responses' : request.json['responses'],
		#'reports' : request.json['reports'],
        #'totalScorePerTraits' : request.json['totalScorePerTraits'],
	}
	assessmentID = request.json['assessmentID']
	#print(allData)
	return Questions().postResponses(data = allData,assessmentID = assessmentID)







@app.route('/psychometric/fetch-all-reports',methods=['GET','POST'])
def fetchAllReports(*args,**kwargs):
	return Questions().fetchAllReports()




# !Deprecated
@app.route('/psychometric/create-assessment',methods=['POST'])
def createAssessment(*args,**kwargs):
	return Questions().createAssessment(name = request.json['assessmentName'],traits = request.json['choosenTraits'])



@app.route('/psychometric/get-assessment',methods=['POST'])
def getAssessment(*args,**kwargs):
	id = request.json['assessmentID']
	if not(isinstance(id,int)):
		try:
			id = int(id)
		except:
			return "Invalid assessment"
	return Questions().getAssessment(id = id)











@app.route('/psychometric/fetch-assessment-reports',methods=['GET','POST'])
def fetchAssessmentReports(*args,**kwargs):
	return Questions().fetchAssessmentReports(assessmentID = request.json['assessmentID'])



@app.route('/psychometric/populate-traits-collection',methods=['GET','POST'])
def populateTraitsCollection(*args,**kwargs):
	return Questions().populateTraitsCollection()




'''


#-------------------- Using MySQLDB -----------------------------

@app.route('/create-assessment',methods=['POST'])
def createAssessment(*args,**kwargs):
	return MySQLDB().createAssessment(name = request.json['assessmentName'],traits = request.json['choosenTraits'])



@app.route('/get-assessment',methods=['POST'])
def getAssessment(*args,**kwargs):
	return MySQLDB().getAssessment(id = request.json['assessmentID'])






@app.route('/fetch-all-assessments',methods=['GET','POST'])
def fetchAllAssessments(*args,**kwargs):	
	return MySQLDB().fetchAllAssessments()





@app.route('/fetch-assessment-reports',methods=['GET','POST'])
def fetchAssessmentReports(*args,**kwargs):
	return MySQLDB().fetchAssessmentReports(assessmentID = request.json['assessmentID'])




@app.route('/fetch-all-reports',methods=['GET','POST'])
def fetchAllReports(*args,**kwargs):
	return MySQLDB().fetchAllReports()





@app.route('/get-questions',methods=['GET','POST'])
def getQuestions(*args,**kwargs):
	print('inside api route')
	traits = request.json['traits']
	#print(traits)
	return MySQLDB().getQuestions(traits)



@app.route('/post-responses',methods=['POST'])
def postResponses(*args,**kwargs):
	allData = {
		'responses' : request.json['responses'],
		#'reports' : request.json['reports'],
        #'totalScorePerTraits' : request.json['totalScorePerTraits'],
	}
	assessmentID = request.json['assessmentID']
	#print(allData)
	return MySQLDB().postResponses(data = allData,assessmentID = assessmentID)
'''






#Latest version of backend API


# API Endpoint for getting all traits data
@app.route('/psychometric/getTraits',methods=['GET'])
def getTraits(*args,**kwargs):
	return BackendClass().getTraits()


# Endpoint for creating new assessment
@app.route('/psychometric/createNewAssessment',methods=['POST'])
def createNewAssessment(*args,**kwargs):
	return BackendClass().createNewAssessment(requestData = request.json)


# Endpoint for queuing up the evaluation
@app.route('/psychometric/evaluate-responses',methods=['POST'])
def evaluateResponses(*args,**kwargs):
	return BackendClass().evaluateResponses(responseData = request.json)



@app.route('/psychometric/generate-report',methods=['POST'])
def generateReport(*args,**kwargs):
	return BackendClass().generateReport(responseData = request.json)



@app.route('/psychometric/get-candidate-report',methods=['POST'])
def getCandidateReport(*args,**kwargs):
	return BackendClass().getCandidateReport(reportID = request.json['reportID'])
	
	

@app.route('/psychometric/fetch-all-assessments',methods=['GET','POST'])
def fetchAllAssessments(*args,**kwargs):	
	return BackendClass().fetchAllAssessments()



@app.route('/psychometric/get-all-reports',methods=['GET','POST'])
def getAllReports(*args,**kwargs):	
	assessmentID = request.json['assessmentID']
	return BackendClass().getAllReports(assessmentID=assessmentID)


@app.route('/psychometric/populate-test-taking-interface',methods=['GET','POST'])
def populateTestTakingInterface(*args,**kwargs):	
	assessmentID = request.json['assessmentID']
	companyID = request.json['companyID']
	return BackendClass().populateTestTakingInterface(assessmentID=assessmentID,companyID=companyID)

