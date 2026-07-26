    # def toplam():
    #     return f"Toplam: {10+20}"

'''
def toplam():
    return f"Toplam: {10+20}"
# a = toplam()
# print(a)

# print(toplam())
# print(toplam())
'''

def toplam():
    return 10+20 

sonuc = toplam() + 50
# print(sonuc)


#yasHesapla
def yil():  #bilgisayarın şuanki yılı
    import datetime
    return datetime.datetime.now().year

def yasHesapla():  #şuanki yılın kaydedildiği fonksiyonu kullanarak yas hesapladık.
    return yil() - 1983

sonuc = yasHesapla()


def saat():  #bilgisayarın şuanki saat bilgisini alan bir fonksiyon ayarladık.
    import datetime
    return datetime.datetime.now().hour

def selamla():
    if saat() < 12:
        return 'Günaydın'
    else:
        return 'Merhabalar'

sonuc = selamla()
print(sonuc)