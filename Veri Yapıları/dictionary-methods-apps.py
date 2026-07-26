'''
    player 1: 
        id           => 1
        name         => Cristiano Ronaldo
        yearOfBirth  => 1985
        nationality  => Portugal
        current_team => Portugal
        history      => Juventus,Real Madrid,Portugal

    player 2: 
        id           => 2
        name         => Lionel Messi
        yearOfBirth  => 1987
        nationality  => Argentina
        current_team => Barcelona,
        history      => Barcelona,Argentina,Portugal
'''
# 1- Yukarıda verilen bilgileri liste içerisinde saklayınız.
players = {
    '1' :  {
        # "id": 1 , 
        "name": "Cristiano Ronaldo",
        "yearOfBirth" : 1985,
        "nationality" : "Portugal",
        "current_team":"Portugal",
        "history" : "Juventus,Real Madrid,Portugal"
    },
    '2' : {
        # "id" : 2, 
        "name": "Lionel Messi",
        "yearOfBirth" : 1987,
        "nationality" : "Argentina",
        "current_team": "Barcelona",
        "history" : "Barcelona,Argentina,Portugal"
    }
}

# 2- id' e göre arama yapınız.
id = input("aramak istediğiniz oyuncu id: ")
player = players.get(id)
print(f"name: {player["name"]}, age: {2025 - player.get("yearOfBirth")}")


""" (ayni isi format ile yaptim)
ages = player.get("yearOfBirth")
print("name: {}, age: {}".format(player["name"],2025 - ages))
"""


# 3- id' e göre bilgi kayıt siliniz.
delete = input("silmek istediğiniz oyuncu id: ")
# players.pop(delete)

