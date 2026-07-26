# Bir aracın yakıt tipine göre (benzin,dizel) belirtilen bir mesafede ne kadar yakıt masrafı olduğunu
# hesaplayan uygulamayı yapınız.
benzinFiyat = 54.5 # tl/L
dizelFiyat = 55.78  # tl /L

# yakıt masrafı = (gidilen yol(km) * ort yakıt tüketimi (L/km)) * yakıt fiyatı
tip = input("Yakıt tipiniz (benzin, dizel): ")
if tip == "benzin":
    tl = benzinFiyat
elif tip == "dizel":
    tl = dizelFiyat
else:
    print("Yakıt tipi bulunamadı...")
    exit()

mesafe = float(input("Gidilen mesafe (km cinsinden): "))
ortYakitTuketimi = float(input("Aracınızın km başına ort. yakıt tükeimi (L cinsinden): "))

masraf = (mesafe * (ortYakitTuketimi / 100))* tl
# 100 km'de 6 L tüketse 20 km'de kaç tüketir ==> 20 * (6/100)
masraf = round(masraf, 2)
print(f"Gidilen km {mesafe}, yakıt masrafınız {masraf} tl.")
