# 'w': (Write) Yazma modu
#    ** Dosyayı konumda oluşturur.
#    ** Eğer konumda aynı dosya varsa onu siler yeni oluşturur.

with open("/users/muhammett/downloads/newfilee.txt", "w", encoding="UTF-8") as file:
    file.write("Muhammet Bozbaş \n")
    file.write("Medine Bozbaş")
    print(file)

with open("newfile.txt") as file:
    print(file.read()) 