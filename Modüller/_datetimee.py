from datetime import datetime
from datetime import timedelta
# from datetime import date
# from datetime import time
# import datetime

result = dir(datetime)
# result = dir(datetime.time)
# result = dir(datetime.date)

result = datetime.now() #anlık tüm tarih saat bilgisi


simdi = datetime.now()
simdi = datetime.today()
#ikisi de aynı bilgiyi verir ztn
result = simdi.year
result = simdi.month
result = simdi.day
result = simdi.hour
result = simdi.minute
result = simdi.second

result = datetime.ctime(datetime.now()) 
result = datetime.ctime(simdi) 
#simdiyle alakalı daha detaylı bilgi verir

result = datetime.strftime(simdi,'%Y') #sadece yıl
result = datetime.strftime(simdi,'%X') #sadece saat
result = datetime.strftime(simdi,'%d') #sadece gün (sayı)
result = datetime.strftime(simdi,'%A') #sadece gün (wed,sat)
result = datetime.strftime(simdi,'%B') #sadece ay (May)
result = datetime.strftime(simdi,'%Y %B %A') #2026 May Wednesday

# t = '21 Nisan 2019'
# gun, ay, yil = t.split()  #ilkel yöntemlerde de gün ay yıl olarak bilgisayara tanıtabiliriz.

t = '6 May 2026 hour 15:23:31'
result = datetime.strptime(t, '%d %B %Y hour %H:%M:%S')
result = result.year

birthday = datetime(1983,5,9,12,30,10)
# 1983-05-09 12:30:10

result = datetime.timestamp(birthday)  #zamanı saniye cinsinden yazar (milattan itibaren 1970)
result = datetime.fromtimestamp(result) # saniye bilgisini datetime formatında verir.
result = datetime.fromtimestamp(0)  #1970-01-01 02:00:00  bilgisayar tarihinin milatı

result = simdi - birthday  #timedelta (iki tarih arası fark demek)

# result = result.days
# result = result.seconds
# result = result.microseconds
result = simdi + timedelta(days=10)  #şimdiki tarihe 10 gün ekledi
result = simdi + timedelta(days=730, minutes=10)  
result = simdi - timedelta(days=10) #şimdiki tarihten 10 gün çıkardı

print(result)
