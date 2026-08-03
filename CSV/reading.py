import csv

# with open("products.csv") as file:
#     print(file.read())

with open("products.csv") as file:
    csv_reader = csv.reader(file)
    next(csv_reader) #Iterator'u bir birim öteliyoruz ki başlık yazdırılmasın.
    print(list(csv_reader))
    for p in csv_reader:
        if p[2] == "True":    #published bilgileri yazdırdık.
            print(f"ürün adı: {p[0]}, Fiyat {p[1]}")
