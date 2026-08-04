#serialize = code to json

#deserialize = json to code


#load => dosyadan yükleyeceksen
#loads => str olan bir kodu json formatına çevireceksen.
import json
"""
with open("person.json") as file:
    data = json.load(file)
"""

#json-string
data = """
    {
        "firstName":"Muhammet",
        "lastName":"Bozbas",
        "hobbies":["sport","software"],
        "age":19,
        "friends":[
            {
                "firstName":"Nidai",
                "age":"19"
                
            },
            {
                "firstName":"Asaf",
                "age":"19"
                
            }
        ]
    }
"""
data = json.loads(data)  #strden gelen dosyayı dict formatına çevirdik
print(data)
print(type(data))

print(data["firstName"]) 
print(data["hobbies"][0]) 

