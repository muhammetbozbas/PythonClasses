# sorted(neyi,neye göre)

sayilar = [1,53,45,61,18,98,5]


# sayilar.sort() ==> küçükten büyüğe sıralar fakat direkt ana listeyi değiştirir.

sonuc = sorted(sayilar) #küçükten büyüğe sıralar ana listeyi değiştirmez fonk. bu sonuçta
sonuc = sorted(sayilar, reverse=True) #tam tersine sıralar. küçükten büyüğe
sonuc = sorted((1,53,45,61,18,98,5)) #bu fonk. ile tuple listesini bile sıralayabiliriz.

users = [
    {"username":"muhammetbozbas", "tweets": ["tweet 1","tweet 2"],"email": "info@gmail.com"},
    {"username":"senabozbas", "tweets": []},
    {"username":"medinebozbas", "tweets": ["tweet 1"],"name":"", "phone": "42525255"}
]  
sonuc = sorted(users, key=len)
sonuc = sorted(users, key=len, reverse=True)
sonuc = sorted(users, key=lambda u: u["username"])
# buradaki işlem users içindeki her değerin username'ini alıp onlara göre sıraladı(alfabetik)
sonuc = sorted(users, key=lambda u: len(u["username"]))
# tweet sayısına göre küçükten büyüğe sıraladı 


kurslar = [
    {"title": "pyhton kursu", "students": 25000},
    {"title": "web kursu", "students": 35000},
    {"title": "java kursu", "students": 5000},
]

sonuc = sorted(kurslar, key= lambda k: k["students"]) #öğrenci sayısına göre
sonuc = sorted(kurslar, key= lambda k: k["students"], reverse=True)
#en popüler kursu bulduk.
sonuc = list(map(lambda kurs: kurs["title"],sorted(kurslar, key= lambda k: k["students"], reverse=True)))
#burada da en popülerden sıraladık ancak sadece başlıklarını aldık.
## (map ile listenin istediğimiz kısmını alabiliyoruz!!!)

print(sonuc)