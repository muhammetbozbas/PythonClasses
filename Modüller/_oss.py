# işletim sistemi ile alakalı bir bilgi veya klasör, dosya vb.
import os
import datetime
result = dir(os)
result = os.name  #posix (mac)  , nt (win)

#--------dizin değiştirme---------
# os.chdir('..') ==> bir üste geçer
# os.chdir('..//..')  ==> iki üst dizine geçer
# os.chdir("/Users/muhammett")

#-------etkin dizin öğrenme------------
# result = os.getcwd()

#------dizinde klasör oluşturanlar-------
# os.mkdir("newdirctory") 
# os.makedirs("newdirectory/yeni klasör")
# os.rename("newdirector","yeni klasör")  #yeniden adlandırır
# os.rmdir("newdirectory") #ilgili klasörü siler(alt klasörü varsa diğer method)
# os.removedirs("newdirectory/yeni klasör") #yazılan alt dizinlerle beraber siler

#--------listeleme----------
# result = os.listdir()  #dizindeki dosyaları listeler
# result = os.listdir('/Users')
'''
for dosya in os.listdir():
    if dosya.endswith('.py'):
        print(dosya)
'''

# result = os.stat('_datetimee.py')  #dosyanın tüm istatistikleri

#o istatisliklerle ilgili işlemler:

# result = result.st_size  bayt cinsinden (1836)
# result = result.st_size/1024   mb cinsinden (1.79296875)
# result = datetime.datetime.fromtimestamp(result.st_ctime) #created time
# result = datetime.datetime.fromtimestamp(result.st_atime) #accessed time
# result = datetime.datetime.fromtimestamp(result.st_mtime) #modified time

# os.system('..')  #yazılan uygulamayı başlatır

# path
result = os.path.abspath("_oss.py")  # dosyanın konumunu alırız. (kendi dahil yazılır)
#tam konumu verilen dosyanın dizin ismini alma:
result = os.path.dirname("/Users/muhammett/Desktop/python/udemy/terminal_class/Modüller/_oss.py") 

result = os.path.dirname(os.path.abspath('_oss.py'))
#====> /Users/muhammett/Desktop/python/udemy/terminal_class/Modüller

result = os.path.exists("_datetimee.py")
result = os.path.exists("_oss.py")
#mesela bir resim upload etmek istediğimizde o resmin adıyla başka bir dosya var mı yok mu
# ona bakmak için kullanabiliriz

#adresteki dosya türü (direktory,file): (True,False)
result = os.path.isdir("/Users/muhammett/Desktop/python/udemy/terminal_class/Modüller")  #True
result = os.path.isdir("/Users/muhammett/Desktop/python/udemy/terminal_class/Modüller/_oss.py")  #False
result = os.path.isfile("/Users/muhammett/Desktop/python/udemy/terminal_class/Modüller/_oss.py")  #True

result = os.path.join("Users/deneme/adaad") #exist ile bakarsak false verir ancak böyle dizin oluşturabiliyoruz
result = os.path.split("/Users/dede") #dizini bölüyoruz.
result = os.path.splitext("_oss.py")  #dosya adı ve uzantısını ayırıyor
# result = result[0]
# result = result[1]


print(result)
