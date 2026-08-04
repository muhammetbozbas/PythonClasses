data = [
    {
    "userName": "muhammetbozbas",
    "firstName": "Muhammet",
    "lastName": "Bozbas"
    },
    {
    "userName": "sadikturan",
    "firstName": "Sadik",
    "lastName": "Turan"   
    }
]
# with open("users.json","w") as file:
#     json.dump(data,file,ensure_ascii=False,indent=2)


#halihazırda oluşturulmuş bir doysaya yeni bir eleman ekleme
import json
user = {
    "userName": "medinebozbas",
    "firstName": "Medine",
    "lastName": "Bozbas"
    }

with open("users.json") as file:
    users = json.load(file)

# users.append(user)


#elemanları konsolda yazdırma
# for user in users:
    # print(user)


#bilgi güncelleme
# for user in users:
#     if user["userName"] == "sadikturan":
#         user["userName"] = "sadik_turan"

#eleman silme
# users.remove(users[0])

with open("users.json","w") as file:
    json.dump(users,file,ensure_ascii=False,indent=2)
