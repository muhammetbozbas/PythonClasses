# value types => str, number(int, float)
x = 5
y = 25

x = y
 
y = 20
'''
print(x,y)
'''
# x ve y için değer belirledik sonra y değerini x' e aktardık ve y' yi tekrar değiştirdik.
# ikinci y değişikliği x' i etkilemedi
# x ve y farklı bloklar oldukları için birinde sonradan yapılan değişiklik diğerini etkilemez.

# reference types => list
listA = ["banana", "apple"]
listB = ["banana", "apple"]

listA = listB
listB[0] = ["grape"]
print(listA, listB)
#list metotlarındaki eşitlik durumlarında listenin referans numarası eşitlenir,
#bu yüzden bir listede yapılan değişiklik diğerini de etkiler.
