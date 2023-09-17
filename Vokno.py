from PyQt5.QtWidgets import *
import memor

def vokno():
    window = QDialog()



    questl1 = QLabel("Питання")
    questEdit23 = QLineEdit()

    rightEdit3 = QLineEdit()



    rightAnsweLBl3 = QLabel("Правильна відповідь")


    mainLine = QVBoxLayout()




    h7 = QHBoxLayout()
    h7.addWidget(questl1)
    h7.addWidget(questEdit23)
    mainLine.addLayout(h7)

    h9 = QHBoxLayout()
    h9.addWidget(rightAnsweLBl3)
    h9.addWidget(rightEdit3)
    mainLine.addLayout(h9)






    next3 = QPushButton("ГоТово")

    def addFunc1():
        memor.qeust245.append(
            {
                "питання": questEdit23.text(),
                "Правильна відповідь": rightEdit3.text(),

            }
        )

    next3.clicked.connect(addFunc1)
    mainLine.addWidget(next3)
    window.setLayout(mainLine)
    window.show()
    window.exec()