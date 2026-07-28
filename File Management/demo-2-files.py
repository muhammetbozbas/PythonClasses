# 1- Kullanıcıdan aldığı ürün bilgisini (ad, fiyat) urunler.txt dosyasına kayıt eden fonksiyon.
def urun_ekle(ad,fiyat):
    with open("urunler.txt","w",encoding="utf-8") as file:
        urunler = f"urun adi: {ad}, urun fiyati {fiyat}"
        file.write(urunler)
        print(urunler)

# urun_ekle('iphone 13', 33000)

# 2- dosya ismi, eski kelime ve yeni kelime parametrelerini alarak dosyada bir güncelleme
# yapan fonksiyon.

def update(dosya_ismi, eski_kelime, yeni_kelime):
    with open(dosya_ismi,"r+",encoding="utf-8") as file:
        dosya = file.read()
        yeni = dosya.replace(eski_kelime,yeni_kelime)
        file.seek(0)
        file.write(yeni)
        file.truncate()  #cursorun olduğu yerden sonrasını tamamen siler.içine yazılan sayı kadar karakter siler.hiç yazmazsan kalanının tamamını siler.
        


update("urunler.txt","25000","0")