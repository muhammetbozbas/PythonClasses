#__iter__ kullanarak Counter nesnesini iterable yaptık, next ile de bir sonrakine geçirdik. For kullanarak da iterator tanımlattık.
#for kullanmadan da iterator yapabiliriz.
class Counter:
    def __init__(self,start,stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start <= self.stop:
            x = self.start
            self.start +=1
            return x
        else:
            raise StopIteration
    
# for i in Counter(10,20):
#     print(i)


iterator = iter(Counter(10,20)) 
while True:
    try:
        x = next(iterator)
        print(x)
    except StopIteration:
        break

