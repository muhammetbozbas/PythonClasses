#formati bu sekilde ayarlarsak o kullanıcıda yapılacak güncelleme daha kolay olur.
data = {
    "muhammetbozbas": {
        "firstName": "Muhammet",
        "lastName": "Bozbas"
    },
    "sadikturan": {
        "firstName" : "Sadik",
        "lastName" : "Turan"
    }
}
import json
with open("users2.json","w") as file:
    json.dump(data,file,ensure_ascii=False,indent=2)

with open("users2.json") as file:
    users = json.load(file)

# print(users["sadikturan"])

users.update({
    "emelturan":{
        "firstName":"Emel",
        "lastName": "Turan",
        "age": 30
    }
})

# users.pop("sadikturan") #pop ile key yazılan eleman silinir.

with open("users2.json","w") as file:
    json.dump(users,file,ensure_ascii=False,indent=2)