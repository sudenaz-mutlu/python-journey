# Developer: @sudenaz-mutlu
# Proje: Nesne Yönelimli Quiz Uygulaması
# Açıklama: Class yapıları kullanarak oluşturulmuş, skor takibi yapan bir bilgi yarışması.
class Question:
    def __init__(self,text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def checkanswer(self,answer):
        return self.answer == answer
    
class Quiz:
    def __init__(self,questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0

    def getQuestion(self):
        return self.questions[self.questionIndex]
    
    def displayQuestion(self):
        question = self.getQuestion()
        print(f"soru { self.questionIndex + 1}: {question.text}")

        for q in question.choices:
            print("-"+ q)

        answer = input("cevap: ")
        self.guess(answer)
        self.loadQuestion()

    def guess(self,answer):
        question = self.getQuestion()

        if question.checkanswer(answer):
            self.score += 1
        self.questionIndex += 1
   
    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else:
            self.displayQuestion()
    def showScore(self):
        print("score: ", self.score)
    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1
        if questionNumber > totalQuestion:
            print("Quiz bitti.")
        else:
            print(f"Question {questionNumber} of {totalQuestion}".center(100,"*"))

q1 = Question("Dünya'nın en derin gölü olan Baykal gölü hangi ülke sınırları içinde?",["Rusya", "Avustralya", "ABD", "İngiltere"], "Rusya")
q2 = Question("Sahra çölü hangi ülkeleri kapsamaz?",["Mısır","Tunus","Cezayir","Senegal"],"Senegal") 
q3 = Question("Dünyanın en büyük ada ülkesi neresidir?",["Japonya","Grönland","Madagaskar ","Endonezya "],"Grönland")       
q4 = Question("Hangisi Güney Amerika'nın en büyük gölüdür??",["Titicaca Gölü","Maracaibo Gölü ","Cocibolca Gölü", "Llanos Gölü"],"Titicaca Gölü") 
questions = [q1,q2,q3,q4]
quiz = Quiz(questions)
quiz.displayQuestion()
quiz.loadQuestion()
question = quiz.questions[quiz.questionIndex]
print(question.text)
#print(q1.checkannswer("python")) #true değeri çalışır

