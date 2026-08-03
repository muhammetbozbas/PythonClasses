# users.csv
# FirstName, LastNane
# Sadık,Turan
# Çınar,Turan

from csv import writer,DictReader ,reader

# 1- add_user() isminde 2 parametre alan fonksiyon. 
def add_user(FirstName, LastName):
    with open("users.csv","a",encoding="utf-8") as file:
        csv_writer = writer(file)
        csv_writer.writerow([FirstName,LastName])
        
# add_user("Muhammet","Bozbas")


# 2- get_users() isminde tüm bilgileri getiren fonksiyon.
def get_users():
    with open("users.csv") as file:
        csv_reader = DictReader(file)
        for user in csv_reader:
            print(f'{user["FirstName"]} {user["LastName"]}')
# get_users()   

# 3- get_user() isminde firstname ve lastname bilgisine göre kaydın indeksini getiren fonksiyon.
def get_user(first_name, last_name):
    with open("users.csv") as file:
        csv_reader = reader(file)
        for index,row in enumerate(csv_reader):
            if (row[0]==first_name) and (row[1]==last_name):
                return index 
        return "cannot find"

print(get_user("Muhammet","Bozbas"))