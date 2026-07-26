# Kendisine gönderilen 2 sayıdan hangisi büyük bulan fonksiyonu yazınız.
"""
def buyukBul(a,b):
  if a > b:
    print(f"Büyük olan sayı: {a}")
  else:
    print(f"Büyük olan sayı: {b}")

buyukBul(10,445)
"""
# Kendisine gönderilen bir string bilgi içinde her karakter kaçar kez tekrarlanmış bulunuz.
"""
def tekrarBul(str):
    return { letter: str.count(letter) for letter in str} # { a: 5 }

print(tekrarBul("muhammet"))
"""  

# Kendisine gönderilen list, command, position ve value bilgilerine göre liste üzerinde güncelleme yapınız.
  # [1,2,3], ("add, remove"), ("beginning | end"), value 
  # list_operation([1,2,3],"add","end","4") => [1,2,3,4]
  # list_operation([1,2,3],"remove","beginning") => [2,3]

""" 1
def update_list(list, command, position, value=None):
    if command=="add":
        if position=="end":
            list.append(value)
            return list
        elif position=="beginning":
            list.insert(0,value)
            return list
        else:
            print("write it again")
    elif command == "remove":
        if position=="end":
            list.pop()
            return list
        elif position=="beginning":
            list.pop(0)
            return list
        else:
            print("write it again")
    else:
        print("write it again")

sonuc = update_list([1,2,3],"remove","beginning")
print(sonuc)
"""

'''  2
def update_list(liste, command, position, value=None):
    if (command == "remove" and position == "end"):
        return liste.pop()
    elif (command=="remove" and position=="beginning"):
        return liste.pop(0)
    elif (command=="add" and position=="end"):
        liste.append(value)
        return liste
    elif (command =="add" and position=="beginning"):
        liste.insert(0,value)
        return liste

sonuc = update_list([1,2,3], "add", "end", 4)
sonuc = update_list([1,2,3], "add", "beginning", 4)
sonuc = update_list([1,2,3], "remove", "beginning")
sonuc = update_list([1,2,3], "remove", "end")
'''

# Kendisine gönderilen renk isimlerinden içinde "blue" rengi varsa True döndüren fonksiyonu yazınız.
"""
def color_finder(*args):
    k = False
    for i in args:
        if i == "blue":
            k = True
            return k
    else:
        return k
    
sonuc = color_finder("blue","red", "brown")
print(sonuc)
"""

'''
def contains_blue(*args):
    if "blue" in args: 
        return True
    return False

sonuc = contains_blue("blue","yellow","red")
sonuc = contains_blue("green","yellow","red","black")

print(sonuc)
'''