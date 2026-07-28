# with open("markalar.txt","a") as file:
#     file.write("6-Bmw\n")

"""
with open("markalar.txt","r+",encoding="utf-8") as file:
    markalar = file.read() #önce hepsini okuyup kaydettik
    markalar = "1-Toyota\n" + markalar  #sonra ilk başa toyota ekleyip sonra markaları ekledik
    file.seek(0) #cursor konumunu başa aldık
    file.write(markalar) #dosya içindeki bilgileri silip baştan bizim ayarladığımız markalar değişkenini kullanarak tekrar yazdırdık.
"""
with open("markalar.txt","r+",encoding="utf-8") as file:
    markalar = file.readlines()
    markalar.insert(2,"3-Renault\n")
    file.seek(0)
    # for marka in markalar:
    #     file.write(marka)
    file.writelines(markalar)

with open("markalar.txt") as file:  #hiçbir şey girmezsek okuma moduyla açar.
    print(file.read())