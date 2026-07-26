# BankAccount isminde bir sınıf tanımlayınız.
# Üretilen her bir nesne owner isminde bir özelliğe sahip olmalıdır. BankAccount("Sadık Turan")
# Üretilen her bir nesne balance isminde bir özelliğe sahip olup başlangıçta 0.0 değerinde olmalıdır.
# Üretilen her bir nesne için deposit metodu oluşturun ve dışarıdan yatırılacak miktar bilgisini alıp balance
# üzerine ekleyin ve balance miktarını geriye döndürün.
# Üretilen her bir nesne için withdraw metodu oluşturun ve dışarıdan çekilecek miktar bilgisini alıp balance
# değerinden çıkarıp geriye döndürün.

# hesap = BankAccount("Sadık Turan")
# hesap.owner => Sadık Turan
# hesap.balance => 0.0
# hesap.deposit(1000) => 1000.0
# hesap.withdraw(500) => 500.0

class BankAccount:
    def __init__(self,name):
        self.owner = name
        self.balance = 0

    def showBalance(self):
        return self.balance
    
    def deposit(self, depositBalance):
        self.balance += depositBalance
        return self.balance
    
    def withdraw(self, withdrawBalance):
        self.balance -= withdrawBalance 
        return self.balance
        

hesap = BankAccount("Muhammet Bozbaş")

print(hesap.owner)
print(hesap.showBalance())
print(hesap.deposit(1000))
print(hesap.withdraw(500))


# print(result)