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
        self.questions = questions
        self.questionIndex = 0
        self.score = 0

    def getQuestion(self):  #it brings questions 
        return self.questions[self.questionIndex]

    def displayQuestion(self):
        question = self.getQuestion()
        
        print(f"Soru {self.questionIndex + 1}: {question.text}")

        for q in question.choices:
            print('-' + q)

        answer = input("Cevap: ")
        trueFalse = question.checkAnswer(answer)
        if trueFalse == True:
            self.score += 1  #toplam doğru yapılan soru sayısını alır

        self.questionIndex += 1
        self.loadQuestion()

    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.displayScore()
        else:
            self.displayProgress()
            self.displayQuestion()
            
    def displayScore(self):
        puan = 100 / len(self.questions)
        toplamPuan = round(puan * self.score)
        print(f"Toplam {len(self.questions)} sorudan {self.score} tanesini doğru yaptınız.")
        print("Score:", toplamPuan)
    
    def displayProgress(self):
        print(f"Toplam {len(self.questions)} sorunun {self.questionIndex+1}. sorusundasınız".center(100,"*"))


    
q1 = Question("en iyi programlama dili hangisidir?",["python","c#","java","dart"],"python")
q2 = Question("en popüler programlama dili hangisidir?",["python","java","c#","dart"],"python")
q3 = Question("en çok kazandıran programlama dili hangisidir?",["python","java","dart","c#"],"python")
q4 = Question("en sevilen programlama dili hangisidir?",["python","java","dart","c#"],"python")
q5 = Question("en kolay programlama dili hangisidir?",["python","java","dart","c#"],"python")

sorular = [q1,q2,q3,q4,q5]

quiz = Quiz(sorular)
quiz.loadQuestion()


