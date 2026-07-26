class User:
    active_users = 0

    @classmethod
    def display_active_users(cls):
        return f"There are {cls.active_users} active users."
    
    @classmethod
    def from_string(cls,data_str):
        first,last,age = data_str.split(',')
        return cls(first,last,age)


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

    
# u1 = User("Muhammet", "Bozbaş", 19)
# u2 = User("Medine", "Bozbaş", 17)

ali = User.from_string("Ali,Korkmaz,20")   #str kullanarak da nesne oluşturabiliriz. class method aracılığıyla
print(ali.first)

# print(User.display_active_users())


### normal dict'e değer oluşturmak için
# {"key":"value"} ===> bunu kullanırdık
# dict.fromkeys() ===> ancak bu metodu da kullanabiliriz.

