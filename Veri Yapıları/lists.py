msg = "Python Kursumuza Hoşgeldiniz. Ben Muhammet Bozbaş".split()

numbers = [1,3,5,7,9]

result = numbers
result = numbers[0] # index sırasına göre yazdırır, sıfırdan başlar.
result = numbers[3]
# result = numbers[6]        # 'Index Error: list index out of range'

names = ['muhammet', 'medine', 'osman', 'fazile']
result = type(names)        # list
result = type(names[2])     # string
result = type(numbers[1])   # integer

# Liste içerisi tek tip olmak zorunda değil str, int... karışık olabilir
listAhmet = ['ahmet', 22]
listMuhammet = ['muhammet', 18]
result = listMuhammet[1] 

# Ayrıca kümeleyebiliriz.
students = (['Ali', 20],['Muhammet', 18])
students2 = (listAhmet, listMuhammet) # Daha önce hazırladığımız listeleri variable içine atatık.

result = students[1]     # "['Muhammet', 18]"
result = students[0][0]  # 0. indexin 0'ını alır. Yani 'Ali' 
result2 = students2[1]


print(result)   
print(result2)   
