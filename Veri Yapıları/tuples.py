# Tuple'ın List'ten tek farkı değiştirilemez olması.
# List [] ile ancak Tuple () ile veya hiç parantez kullanmadan oluşturulabilir.
# Sadece 'count (kaç kere tekrarlanıyor)' ve 'index (hangi indexte)' metotlarını kullanabiliyoruz.

_list = [1,2,3]
_tuple = (1,"iki",True) # int, str, bool gibi istediğimiz türden yazabiliriz.
_tuple2 = (5,6,2,4)

print(type(_list))
print(type(_tuple))

# Listede olduğu gibi Tuple'da da index numarasına göre yazdırma yapabiliriz.
print(_list[1])
print(_tuple[1])

# Değer sayısı alabiliriz. (aynı yöntem)
print(len(_list))
print(len(_tuple))

_list[0] = 5
# _tuple[0] = 8
print(_list)
# print(_tuple) => "TypeError: 'tuple' object does not support item assignment"

print(_tuple.count(1)) # 'True' ifadesini de '1' olarak gördüğü için sonuç iki çıkar.
 
print(_tuple + _tuple2) # Tuple üzerinde bir değişiklik yapmaya çalışmadığımız için error vermez.

# Listeyi Tuple'a çevirebiliriz.
_t = tuple([1,5,7,4]) # [] içinde liste iken tuple yazıp paranteze alarak o listeyi tuple yaptık.
print(type(_t))

# Eğer daha sonra değiştirmeyeceğim ve uygulamam daha performanslı olsun, listem daha az yer kaplasın istiyorsan tuple kullan.
