from app import app
from flask import request

from utility.frametest import TestReact

@app.route('/')
def home():
	return "Welcome to home page"

@app.route('/frametest/compile-and-evaluate',methods=['POST'])
def populateTestTakingInterface(*args,**kwargs):	
	#print('Inside route')
	#print(request.json)
	code = request.json['code']
	type = request.json['questionType']
	reportID = request.json['reportID']
	
    
	#print("Calling")
	if type=="react":
		return TestReact().testReactCode(code=code,reportID=reportID)
	else:
		return None

