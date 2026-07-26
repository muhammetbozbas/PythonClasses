class Pet:
    species = ["cat","dog","bird"]
    def __init__(self,name,kind):
        if kind not in Pet.species:
            raise ValueError(f"{kind} is not kind of a pet")
        self.name = name
        self.kind = kind

    def set_kind(self,kind):
        if kind not in Pet.species: #classtan aldığımız için Pet.species demek zorundayız
            raise ValueError(f"{kind} is not kind of a pet")
        self.kind = kind



boncuk = Pet("boncuk","cat")
karabas = Pet("karabas","dog")

boncuk.set_kind("lion")

# kral = Pet("kral","lion")

# print(boncuk.kind)
# print(karabas.kind)
# print(kral.kind)


# boncuk.species.append("fish")
# Pet.species.append("rat")

# print(Pet.species)
# print(boncuk.species)  # every instance can access the list
# print(karabas.species)
        