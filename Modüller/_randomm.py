import random

# result = dir(random)
# result = help(random) #bunu kullanmak yerine internetten bak

result = random.random() # 0.0 - 1.0 arası sayı üretir
result = random.random() * 100 # 0.0 - 1.0 arası sayı üretir 100 ile çarpar
result = random.uniform(10,100)  #iki sayı arasında random sayı üretir (float)

result = int(random.uniform(10,100))  #iki sayı arasında random sayı üretir (int olur)
result = random.randint(1,100) # yukarıdakinin modülü

greeting = 'hello my boy'
names = ['ali','yagmur','deniz','cenk','ahmet','efe']  #listeden rastgele eleman istiyoruz
result = names[random.randint(0,len(names)-1)] 
#listeden rastgele eleman aldık üst sınır dinamik olabileceği için listenin uzunluğundan bir eksik olarak ayarladık.
result = random.choice(names) #üsttte yaptığımızın ayarlanmış olanı 
result = random.choice(greeting) #str ifadenin her harfini ayrı aldığı için oradan sadece rastgele bir harf gelir.

liste = list(range(10))
random.shuffle(liste) #elemanlar karışık halde çıkar
result = liste

liste = range(100)
result = random.sample(liste, 3) #listenin içinden rastgele 3 sayı isteyebiliriz
result = random.sample(names, 3) #names listesinden rastgele 3 isim isteyebiliriz

print(result)
