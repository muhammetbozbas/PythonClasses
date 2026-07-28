#1
def dosya_kopyala(dosya_ismi,yeni_dosya_ismi):
    with open(dosya_ismi,encoding="utf-8") as file:
        new_file = file.read()
    
    with open(yeni_dosya_ismi,"w",encoding="utf-8") as file:
        file.write(new_file)

# dosya_kopyala("msg.txt","msg_copy.txt")

#2 (listenin her elemanını tersten yazdırır.)
def ters_cevir(dosya_ismi,yeni_dosya_ismi):
    with open(dosya_ismi,encoding="utf-8") as file:
        new_file = file.read()
    
    with open(yeni_dosya_ismi,"w",encoding="utf-8") as file:
        file.write(new_file[::-1])

#----(listeyi 6,5,4 gibi tersten yazdırır.)----
# def ters_cevir(dosya_ismi,yeni_dosya_ismi):
#     with open(dosya_ismi,encoding="utf-8") as file:
#         new_file = file.readlines()
    
#     with open(yeni_dosya_ismi,"w",encoding="utf-8") as file:
#         file.writelines(new_file[::-1])

# ters_cevir("markalar.txt","markalar_copy.txt")

#3
def bilgilendir(dosya_ismi):
    with open(dosya_ismi,"r+",encoding="utf-8") as file:
        lines = len(file.readlines())
        file.seek(0)
        words = len(file.read().split())
        file.seek(0)
        character = len(file.read())
        
        print(f"satir_sayisi = {lines}, kelime_sayisi = {words}, karakter_sayisi = {character}")

bilgilendir("msg.txt")