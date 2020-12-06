import json
from bson import BSON
json_string = ""
with open("data.json", 'r', encoding='utf-8') as json_data:
    for i, line in enumerate(json_data):
        json_string += line
    json_docs = json_loads(json_string)
for key, val in json_docs.items():
    for i, doc in enumerate(json_docs[key]):
        print(doc)
