# x = 10
# kendimiz bir hata mesajı hazırlayalım

# if x > 5:
#     raise ValueError("x 5 den büyük olamaz")

def colorize(text,color):
    colors = ("blue","red","white","black","orange")
    if type(text) is not str:
        raise TypeError("text str tipinde olmalıdır")
    if type(color) is not str:
        raise TypeError("color str tipinde olmalıdır")
    if color not in colors:
        raise ValueError("geçersiz bir renk ismi")
    
    print(f"{text} {color} olarak yazdırıldı")

# colorize(19,'blue') ==> TypeError: text str tipinde olmalıdır
# colorize("merhaba",10) ==> TypeError: color str tipinde olmalıdır
# colorize("merhaba","yellow") ==> ValueError: geçersiz bir renk ismi

# try:
#     colorize("selam","yellow")
# except Exception as ex:
#     print(ex )

try:
    colorize("selam","red")
except (TypeError,ValueError) as ex:
    print(ex)