# Quiz sınıfı
#   - questions     => soru listesi
#   - questionIndex => gösterilecek soru

# quiz = Quiz(questions)
# quiz.getQuestion()     => soru 1, soru 2... (nesne)
# quiz.displayQuestion()

class Question:
    def __init__(self,text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def checkAnswer(self,ans):
        if ans not in self.choices:
            raise ValueError("wrong information")
        return self.answer == ans
    
class Quiz:
    def __init__(self,questions):
        self.questions = questions  #random.sample(questions, len(questions))
        self.questionIndex = 0

    def getQuestion(self):  #it brings questions 
        return self.questions[self.questionIndex]

    def displayQuestion(self):
        question = self.getQuestion()

        print(f"Soru {self.questionIndex + 1}: {question.text}")

        for q in question.choices:
            print('-' + q)
        


q1 = Question("en iyi programlama dili hangisidir?",["python","c#","java","dart"],"python")
q2 = Question("en popüler programlama dili hangisidir?",["python","java","c#","dart"],"python")
q3 = Question("en çok kazandıran programlama dili hangisidir?",["python","java","dart","c#"],"python")

sorular = [q1,q2,q3]

quiz = Quiz(sorular)
quiz.getQuestion()
print(quiz.displayQuestion())

