from app import app
from utility.parseExcel import *
from utility.Questions import *
from flask import request,send_from_directory,send_file
from google.cloud import tasks_v2
import json,os
from utility.BackendScript import BackendClass




@app.route('/psychometric')
def hello_world():
	return send_file('ffrontendd/.svelte-kit/output/prerendered/pages/psychometric.html')

@app.route("/psychometric/assessment/<assessmentID>")
def specific_assessment(assessmentID):
    return send_file(f'ffrontendd/.svelte-kit/output/prerendered/pages/psychometric/assessment/dynamic_assessment.html')

@app.route("/psychometric/view-reports")
def allreports():
    return send_file(f'ffrontendd/.svelte-kit/output/prerendered/pages/psychometric/view-reports.html')



@app.route("/psychometric/reports/assessments")
def all_assessment_reports():
    return send_file(f'ffrontendd/.svelte-kit/output/prerendered/pages/psychometric/reports/assessments.html')


@app.route("/psychometric/reports/assessments/<assessmentID>")
def specific_assessment_reports(assessmentID):
    return send_file(f'ffrontendd/.svelte-kit/output/prerendered/pages/psychometric/reports/assessments/dynamic_reports.html')



# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def static_route(path):
    return send_file(f'ffrontendd/.svelte-kit/output/client/{path}')




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



@app.route('/psychometric/evaluate-responses',methods=['POST'])
def evaluateResponses(*args,**kwargs):
	#print(request.json)
	
	responses = request.json['responses']
	
	assessmentID = request.json['assessmentID']
	
	
	credential_path = "/home/manas/Downloads/xobin-verification-18678b6bcd87.json"
	os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

	# Create a client.
	client = tasks_v2.CloudTasksClient()

	project = 'xobin-verification'
	queue = 'assessment'
	location = 'us-central1'
	url = 'https://xobin-verification.uc.r.appspot.com/post-responses'
	payload = {
		'responses':responses,
		'assessmentID' : assessmentID
	}
	print('responses : ',responses)
	print('payload : ', payload)

	
	parent = client.queue_path(project, location, queue)



	# Construct the request body.
	task = {
	    "http_request": {  # Specify the type of request.
	        "http_method": tasks_v2.HttpMethod.POST,
	        "url": url,  # The full url path that the task will be sent to.
	    }
	}
	if payload is not None:
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

	return "Data successfully inserted"




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
	return Questions().getAssessment(id = request.json['assessmentID'])






@app.route('/psychometric/fetch-all-assessments',methods=['GET','POST'])
def fetchAllAssessments(*args,**kwargs):	
	return Questions().fetchAllAssessments()





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






#API endpoints asked by Vishal


@app.route('/psychometric/getTraits',methods=['GET'])
def getTraits(*args,**kwargs):
	return BackendClass().getTraits()



@app.route('/psychometric/createNewAssessment',methods=['POST'])
def createNewAssessment(*args,**kwargs):
	return BackendClass().createNewAssessment(requestData = request.json)
