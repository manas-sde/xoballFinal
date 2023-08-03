from pymongo import MongoClient
import pandas as pd
import json

client = MongoClient('mongodb+srv://manas:fyTGlHSyD43CCctL@cluster0.rsnix.gcp.mongodb.net/test')

db = client['psychometricDb']

traits_collection = db['psychometric_traits']

# traits_collection.update_one({"traitName":"Integrity"},{"$set":{"traitCatName":"NewCateg"}})

# print(traits)

Excel = pd.read_excel('/home/manas/Downloads/35 core traits (1).xlsx', sheet_name='Sheet1')

Json = json.loads(Excel.to_json(orient='records'))

newData = {}
print(type(Json))
for datafield in Json:
    print(datafield)
    print(datafield["Now available with 10 questions and corresponding reports"])
    print(datafield["Type of trait"])
    if datafield["Now available with 10 questions and corresponding reports"]:
        traits_collection.update_one({"traitName": datafield["Now available with 10 questions and corresponding reports"].strip()}, {"$set": {"traitCatName": datafield["Type of trait"].strip()}})
    #newData[datafield["Now available with 10 questions and corresponding reports"]] = datafield["Type of trait"]

#print(newData)


# traits_collection.update({"traitName": b["_id"]}, {"$set": {"geolocCountry": myGeolocCountry}})

allTraitDocuments = list(traits_collection.find())

# for trait in allTraitDocuments:
#     trait["traitCatName"] = newData[trait["traitName"]]

print(list(allTraitDocuments)[0])
print(list(allTraitDocuments)[0].keys())







print("Done")