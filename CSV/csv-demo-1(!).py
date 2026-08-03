#-------- THIS FİLE HAS NOT ANY CSV INFOS
#--------IT IS CREATED WITH NORMAL FILE FEATURES


# users.csv
# FirstName, LastNane
# Sadık,Turan
# Çınar,Turan


import csv
# 1- add_user() isminde 2 parametre alan fonksiyon. 
def add_user(FirstName, LastName):
    with open("users!.csv","a",encoding="utf-8") as file:
        info = FirstName + " " +LastName +"\n"
        file.write(info)

# 2- get_users() isminde tüm bilgileri getiren fonksiyon.
def get_users():
    with open("users!.csv") as file:
        info = file.read()
        print(info)

# 3- get_user() isminde firstname ve lastname bilgisine göre kaydın indeksini getiren fonksiyon.
def get_user(FirstName, LastName):
    with open("users!.csv") as file:
        l = list(file.readlines())
        str = FirstName + " " +LastName +"\n"
        index = l.index(str)
        return index

print(get_user("Medine", "Bozbas"))