import random
from PyQt5.QtWidgets import *
import memor
import MenuWindow

app = QApplication([])
window = QWidget()

window.resize(500, 500)
mainLine = QVBoxLayout()

menuBTn = QPushButton("Меню")
restBTn = QPushButton("Відпочити")
TimeSpb = QSpinBox()
timebls = QLabel("хвилин")

forst = QLabel("В якому році почалася повномаштабна війна в Україні? ")
fhwej = QPushButton("Відповісти")
next1 = QPushButton("НАСТУПНЕ ПИТАННЯ")

next1.hide()

firstLine = QHBoxLayout()
firstLine.addWidget(menuBTn)
firstLine.addWidget(restBTn)
firstLine.addWidget(TimeSpb)
firstLine.addWidget(timebls)
mainLine.addLayout(firstLine)

mainLine.addWidget(forst)

answerGroup = QGroupBox("Відповіді")
answer1 = QRadioButton("2012")
answer2 = QRadioButton("2015")
answer3 = QRadioButton("2022")
answer4 = QRadioButton("2023")
answers5 = [answer1, answer2, answer3, answer4]

answersLine = QVBoxLayout()
answersLine.addWidget(answer1)
answersLine.addWidget(answer2)
answersLine.addWidget(answer3)
answersLine.addWidget(answer4)

resul = QLabel("Результат")
answersLine.addWidget(resul)
resul.hide()

answerGroup.setLayout(answersLine)
mainLine.addWidget(answerGroup)

def setQuest():
    random.shuffle(answers5)
    forst.setText(memor.qeust[memor.currentQuest]["питання"])
    answers5[0].setText(memor.qeust[memor.currentQuest]["Правильна відповідь"])
    answers5[1].setText(memor.qeust[memor.currentQuest]["Неправильна1"])
    answers5[2].setText(memor.qeust[memor.currentQuest]["Неправильна2"])
    answers5[3].setText(memor.qeust[memor.currentQuest]["Неправильна3"])




setQuest()



def showResults():
    answers5[0].hide()
    answers5[1].hide()
    answers5[2].hide()
    answers5[3].hide()

    resul.show()
    next1.show()
    fhwej.hide()
    if answers5[0].isChecked():
        resul.setText("Правильно")
    else:
        resul.setText("Не правильно")


def nextFunc():
    answers5[0].show()
    answers5[1].show()
    answers5[2].show()
    answers5[3].show()
    next1.show()
    resul.hide()
    memor.currentQuest += 1
    setQuest()


fhwej.clicked.connect(showResults)
next1.clicked.connect(nextFunc)
mainLine.addWidget(fhwej)
mainLine.addWidget(next1)

menuBTn.clicked.connect(MenuWindow.menuWind)
window.setLayout(mainLine)
window.show()
app.exec()