def ort_oku(satir):
    satir = satir[:-1] #newline'lardan kurtulduk.
    satir = satir.split(':')# iki elemanlı liste elde ettik
    ad = satir[0]
    notlar = satir[1].split(',')
    ort_cal = sum(int(nots) for nots in notlar) / 3

    if 90<= ort_cal <= 100:
        harf = "AA"
    elif 85<= ort_cal <90:
        harf = "BA"
    elif 80<= ort_cal <85:
        harf = "BC"
    elif 75<= ort_cal <80:
        harf = "BC"
    elif 70<= ort_cal <75:
        harf = "BC"
    elif 65<= ort_cal <70:
        harf = "BC"
    elif 60<= ort_cal <65:
        harf = "BC"
    elif 50<= ort_cal <60:
        harf = "BC"
    else:
        harf = "FF"

    return f"{ad}: {harf}"


def notlari_oku():
    with open("sinav_notlari.txt",encoding="utf-8") as file:
        for satir in file:
            # satir = satir.strip()
            print(f"{ort_oku(satir)}")

def not_gir():  
    while True:
        try:
            ad = input("Ogrenci Adi: ")
            soyad = input("Ogrenci Soyad: ")
            if (ad.isdigit() or soyad.isdigit() is True):
                raise ValueError
        except Exception:
            print("Tekrar Deneyiniz. Ad-Soyad bilgisi str ifade olmalidir.")
            continue
       
        try: 
            not1 = int(input("not 1: "))
            not2 = int(input("not 2: "))
            not3 = int(input("not 3: "))
            if (0<= not1 or not2 or not3 <= 100):
                pass
            else:
                raise ValueError
        except Exception:
            print("Girilen not bilgileri 0-100 aralığında olmalıdır.")
            continue
        else:
            with open("sinav_notlari.txt","a",encoding="utf-8") as file:
                file.write(f"{ad.capitalize()} {soyad.capitalize()} : {not1}, {not2}, {not3}\n")
            break
def kayit_et():
    with open("sinav_notlari.txt",encoding="utf-8") as file:
        list = []
        for satir in file:
            list.append(ort_oku(satir))
        
        with open("sonuclar.txt",'w',encoding="utf-8") as file2:
            for i in list:
                file2.write(i+'\n')


while True:
    islem = input("\n---Not Uygulamasi:\n1- Notlari Oku\n2- Not Gir\n3- Notlari Kayit Et\n4- Cikis\n")
    if islem == "1":
        notlari_oku()
    elif islem == "2":
        not_gir()
    elif islem == "3":
        kayit_et()
    else:
        break