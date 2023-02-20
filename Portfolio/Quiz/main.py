
from dataclasses import dataclass

def GetInfo():
    @dataclass
    class QuizQ:
        question: str = ""
        ans1: str = ""
        ans2: str = ""
        ans3: str = ""
        ans4: str = ""
        correctanswers: str = ""

    questionans = []

    quizimport = open("quiz.txt" , "r")

    for line in quizimport:
        row = line.split(",")
        tempanswers = QuizQ(row[0],row[1],row[2],row[3],row[4],row[5])
        questionans.append(tempanswers)

    quizimport.close()
    return questionans

def DisplayQ(questionans):
    counter = 0
    answers = []
    for x in range (len(questionans)):
        print (questionans[x].question)

        print (questionans[x].ans1, " " ,questionans[x].ans2, " ", questionans[x].ans3, " " ,questionans[x].ans4)

        tAnswer = input("What is your answer?")

    if tAnswer == questionans[x].correctanswers:
            counter = counter + 1
            answers.append(tAnswer)

    print(answers)
    print(counter)
        ####Main Program###
    questionans = GetInfo()
    DisplayQ(questionans)
