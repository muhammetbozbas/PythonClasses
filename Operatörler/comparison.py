# email, password => data base

# email == 'info@satikturan.com
# password == '12345'

a, b, c, d = 5, 5, 20, 4
username = 'sadikturan'
password = '12345'

#parantez açmasak da olur
sonuc = (a == b) # a, b' ye eşit mi diye sorar. (True)
sonuc = (a != b) # a, b' ye eşit değil mi diye sorar. (True)
sonuc = (a == c) # False
sonuc = (username == "sadikturan")  # True
sonuc = (username == "sadikturn")  # False

# kıyaslama soruları sorarız
sonuc = (b < a) # False
sonuc = (c > a) # True
sonuc = (c >= a) # True
sonuc = (b <= a) # True
sonuc = (True == 1) # True
sonuc = (False == 0 ) # True
sonuc = True + False + 50 # 51

print(int(True)) # 1 yazar.
print(sonuc)