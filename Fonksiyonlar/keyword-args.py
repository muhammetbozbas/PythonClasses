#   arguments - parameters
#firstname,lastname olarak ifade edilen kısım ==> parameter
#'Muhammet , 'Bozbaş olarak yazdığımız yer ==> argument (bizim belirlediğimiz yani)

def full_name(firstname, lastname):
    return f"Your name is {firstname} {lastname}."

sonuc = full_name("Muhammet","Bozbaş")

#sırasını yanlış yazmamız durumunda fonksiyonu çağırırken argümanları atayabiliyoruz.
sonuc = full_name(lastname='Bozbaş', firstname='Muhammet') 
#bu işlemi fonk. yazarken yaptığımız durumda default belirliyoruz, aynı değil.

print(sonuc)
