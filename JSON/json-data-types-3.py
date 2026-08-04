db = {
    "users":{
        "muhammetbozbas": {
        "firstName":"Muhammet",
        "lastName":"Bozbas"
        },
        "medinebozbas": {
        "firstName":"Medine",
        "lastName":"Bozbas"
        }
    },
    "products": {
        "1":{
            "productName": "IPhone 8",
            "price":5000
        },
        "2":{
            "productName": "IPhone 13",
            "price": 8000
        }
    }
}

import json
# with open("db.json","w") as file:
#     json.dump(db,file,ensure_ascii=False,indent=2)

with open("db.json") as file:
    db = json.load(file)

# print(db["users"]["muhammetbozbas"]["firstName"])
# print(db["products"]["1"]["productName"])
# print(db["products"]["1"]["price"])

db["products"].update({
    "3": {
        "productName": "IPhone 11",
        "price": 7600
    }
})
db["users"].update({
    "senabozbas": {
      "firstName": "Sena",
      "lastName": "Bozbas"
    }
})

with open("db.json","w") as file:
    json.dump(db,file,ensure_ascii=False,indent=2)