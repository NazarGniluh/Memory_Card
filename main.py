from PyQt5.QtWidgets import *

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
answersLine = QVBoxLayout()
answersLine.addWidget(answer1)
answersLine.addWidget(answer2)
answersLine.addWidget(answer3)
answersLine.addWidget(answer4)
answerGroup.setLayout(answersLine)
mainLine.addWidget(answerGroup)



mainLine.addWidget(fhwej)

window.setLayout(mainLine)
window.show()
app.exec()