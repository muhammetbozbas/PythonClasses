# with bloğundan çıktığımız an dosya kapanır.
# try-except ile yanlış doysa ismi sorununu ele alabiliriz.
# encoding ile de okuma şeklini değiştiririz.
# encoding="Windows-1252"(türkçe karakter okuyamaz), encoding="utf-8", ...
try:
    with open("msg.txt","r",encoding="utf-8") as file:
        print(file.read())
        print(file.closed)
        print(file.tell())  # cursorun nerede olduğunu söyler.
        file.seek(0)
        # for i in file:
        #     print(i)
        for i in file:
            print(i, end="")    #==> her satırdan sonraki boşlukları kaldırmak için.
except FileNotFoundError as e:
    print("Dosya okuma hatası: ", e)
finally:
    print("Dosya kapandı")
