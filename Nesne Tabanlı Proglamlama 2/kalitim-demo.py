# User
# Moderator

class User:
    active_users = 0

    @classmethod
    def display_active_users(cls):
        return f"{cls.active_users} users are active right now."
    
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        User.active_users += 1
    
    def full_name(self):
        return f"{self.firstname} {self.lastname}"

class Moderator(User):
    active_moderator = 0

    @classmethod
    def display_active_moderators(cls):
        return f"{cls.active_moderator} moderators are active right now."

    def __init__(self, firstname, lastname, community):
        super().__init__(firstname, lastname)
        self.community = community
        Moderator.active_moderator += 1

    def remove_post(self):
        return f"{self.full_name()} has removed a post in {self.community} group!"
    
    def update_post(self):
        return f"{self.full_name()} has updated a post in {self.community} group!"

# print(User.display_active_users())
u1 = User("Ali", "Korkmaz")
m1 = Moderator("Yagmur", "Korkmaz", "Software")
m2 = Moderator("Canan", "Korkmaz", "Cosmetics")

print(m1.remove_post())
print(m1.update_post())
print(m2.update_post())

print(User.display_active_users())
print(Moderator.display_active_moderators())
u1.full_name()


# print(isinstance(u1, User))
# print(isinstance(u1, Moderator))  ==> Kontrol işlemlerini böyle yapabiliriz.

# print(isinstance(m1, User))
# print(isinstance(m1, Moderator))