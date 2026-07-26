class NewDict(dict):
    def __repr__(self):
        print("__repr__ metodundan mesaj var.")
        return super().__repr__()
    
    def __missing__(self,key):  #olmayan key aranırsa __missing__ çalışır
        print("olmayan key bilgisi arıyorsunuz.")
    
    def __getitem__(self, key):
        print("bir eleman çağırıyorsunuz.")
        return super().__getitem__(key)
    
    def __setitem__(self, key, value):
        print("listeye eleman ekliyorsunuz.")
        return super().__setitem__(key, value)
    
    def __contains__(self, item): #arama yapmak istediğimiz zaman bu çalışır.
        return super().__contains__(item)
    
data = NewDict({"first":"Muhammet","second": "Bozbas"})

print(data)
data["age"]
data["first"] = "Medine"
print(data)

print("first" in data)