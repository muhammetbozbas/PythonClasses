#serialize
import json
person = {
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

print(person)
print(type(person))

#json stringini uygulama tarafında kullanmak
"""
result = json.dumps(person,ensure_ascii=False,indent=2)  #code to json (serialize), ensure kısmı tr karakterlerde sorun çıkmasın diye, tek satır yazmasın diye indentatiton yani parantezden kaç satır içeri yazdırılacağını ayarlarız.
print(result)
print(type(result))
"""

#dosyaya bilgi kaydetmek
#json dict yapısını str formatına çevirmek için metot(dump)
with open("person.json","w") as file:
    json.dump(person,file,ensure_ascii=False,indent=2)