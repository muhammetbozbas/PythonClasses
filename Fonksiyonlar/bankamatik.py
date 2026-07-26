# bankamatik uygulaması

SadikHesap = {
    'ad': 'Sadık Turan',
    'hesapNo': '12312446',
    'bakiye': 3000,
    'ekHesap': 2000
}
AliHesap = {
    'ad': 'Ali Turan',
    'hesapNo': '13212446',
    'bakiye': 2000,
    'ekHesap': 1000
}
""" my solution
def paraCek(hesap, miktar):
    print(f"----Merhaba {hesap['ad']}----")

    if (hesap['bakiye'] >= miktar):
        kalan = hesap['bakiye'] - miktar
        hesap.update({'bakiye': kalan})
        print("Paranızı alabilirsiniz.")
        print(f"----Kalan Ana Bakiye: {hesap['bakiye']}---")
    elif (hesap['bakiye'] + hesap['ekHesap'] >= miktar):
        ekKullanımı = input("Ek hesap kullanılsın mı? e/h : ")
        if ekKullanımı == 'e':
            ekKalan = hesap['ekHesap'] - (miktar - hesap['bakiye'])
            hesap.update({'ekHesap': ekKalan})
            ekCekilen = miktar - hesap['bakiye']
            print(f"Paranızı alabilirsiniz, ek hesaptan çekilen para: {ekCekilen}  ek hesapta kalan para: {hesap['ekHesap']}")
        else:
            print(f"Ek hesap kullanılmadı. Hesap Bakiyeleriniz: Ana ({hesap['bakiye']}), Ek ({hesap['ekHesap']})")
    else:
        print("Bakiyeniz Yetersiz.")

paraCek(SadikHesap,5000)
"""

def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")

    if (hesap['bakiye'] >= miktar):
        hesap['bakiye'] -= miktar 
        print('paranızı alabilirsiniz.')
        bakiyeSorgula(hesap)
    else:
        toplam = hesap['bakiye'] + hesap['ekHesap']

        if (toplam >= miktar):
            ekHesapKullanimi = input('ek hesap kullanılsın mı (e/h)')

            if ekHesapKullanimi == 'e':
                ekhesapKullanilacakMiktar = miktar - hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ekHesap'] -= ekhesapKullanilacakMiktar
                print('paranızı alabilirsiniz.')
                bakiyeSorgula(hesap)
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} bulunmaktadır.")
        else:
            print('üzgünüz bakiye yetersiz')
            bakiyeSorgula(hesap)


def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır. Ek hesap limitiniz ise {hesap['ekHesap']} TL bulunmaktadır.")

paraCek(SadikHesap, 4000)

print('*****************')

paraCek(SadikHesap, 2000)