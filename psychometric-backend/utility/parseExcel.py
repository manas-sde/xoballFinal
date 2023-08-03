import random as rd
import pandas as pd
import excel2json
import json
import xlrd
from flask import jsonify




class ExcelParse:

    #--No use----------------
    def getExcelDataXlrd(self):
        return True
        

    

    #-For parsing questions data to store it in db
    def parse(self,x):
        ids = [rd.randint(1000,9999) for i in range(4)]

        while len(set(ids))!=4:
            ids.append(rd.randint(1000,9999))

        data = {
            'options' : [
                {
                    'opID':ids[0]
                },
                {
                    'opID':ids[1]
                },
                {
                    'opID':ids[2]
                },
                {
                    'opID':ids[3]
                },
            ]
        }

        for k,v in x.items():
            if k=='Trait ID':
                data['traitID'] = v 
            
            elif k == "Question code":
                data['questionID'] = 1000 + v

            elif k == "Question ":
                data['question'] = v

            elif k == "Option A" :
                data['options'][0]['option'] = v
            
            elif k == "Option A Score" :
                data['options'][0]['opScore'] = v

            elif k == "Option B" :
                data['options'][1]['option'] = v
            
            elif k == "Option B Score" :
                data['options'][1]['opScore'] = v

            elif k == "Option C" :
                data['options'][2]['option'] = v
            
            elif k == "Option C Score" :
                data['options'][2]['opScore'] = v

            elif k == "Option D" :
                data['options'][3]['option'] = v
            
            elif k == "Option D Score" :
                data['options'][3]['opScore'] = v

        


        return data







    def getExcelData(self):
        
        excelFile = pd.ExcelFile('/home/manas/Downloads/Questions (4).xlsx')
        #print(excelData)
        #jsonData = excelData.to_json()

        allTraits = excelFile.sheet_names
        dataDict = {}

        with open('static/Questions.json','a') as jsonfile:
            finalData = []
            for trait in allTraits[:10]:
                traitData = excelFile.parse(trait)
                #print(type(traitData))

                jsonData = traitData.to_dict(orient='records')
                #print(jsonData)
                
                for x in jsonData:
                    y = self.parse(x)
                    finalData.append(y)
                    continue
                    jsonfile.write(json.dump(y,indent=4))
                    jsonfile.write(',')

            json.dump(finalData,jsonfile)
            #jsonfile.write(',')

 
        return "Excel Data parsed"




