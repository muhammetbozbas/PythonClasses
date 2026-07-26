# Her bir soruyu temsil edecek question nesnesi oluşturunuz.

# Question sınıfı
#   - text    => soru
#   - choices => cevap şıkları
#   - answer  => soru

# checkAnswer() metodu ile cevap kontrolü yapınız.

# q1.checkAnswer('cevap') => True
# q1.checkAnswer('cevap') => False

class Question:
    def __init__(self,text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def checkAnswer(self,ans):
        if ans not in self.choices:
            raise ValueError("wrong information")
        return self.answer == ans
        
q1 = Question("en iyi programlama dili hangisidir?",["python","c#","java","dart"],"python")
q2 = Question("en popüler programlama dili hangisidir?",["python","java","c#","dart"],"python")
q3 = Question("en çok kazandıran programlama dili hangisidir?",["python","java","dart","c#"],"python")

sorular = [q1,q2,q3]

print(q2.checkAnswer('java'))
print(q1.text)
print(q1.choices)
