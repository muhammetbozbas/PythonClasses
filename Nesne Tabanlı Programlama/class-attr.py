#oluşturulan nesnelere göre değişmeyen bir özellik varsa onu direkt class seviyesinde 
# tanımlayabiliriz.

class User:
    active_users = 0

    def __init__(self,first,last,age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1  #class'tan tanımladık oradan çağırıyoruz

    def full_name(self):   #instance method
        return f"{self.first} {self.last}"
    
    def log_out(self):
        User.active_users -= 1
        return f"{self.full_name()} has logged out."

    
print(User.active_users)
u1 = User("Muhammet", "Bozbaş", 19)
u2 = User("Medine", "Bozbaş", 17)
print(User.active_users)
print(u2.log_out())
print(User.active_users)

# print(u1.full_name())
# print(u2.full_name())


        