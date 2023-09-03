from PyQt5.QtWidgets import *
import memor
def menuWind():
    window = QDialog()


    questl = QLabel("Питання")
    questEdit = QLineEdit()
    frostEdit = QLineEdit()
    jroginEdit = QLineEdit()
    leftEdit = QLineEdit()
    rightEdit = QLineEdit()



    rightAnsweLBl = QLabel("Правильна відповідь")
    leftanswerlbL = QLabel("Неправильна відповідь")
    jriginansLbl = QLabel("Неправильна відповідь")
    frostanswerLbl = QLabel("Неправильна відповідь")

    mainLine = QVBoxLayout()




    h1 = QHBoxLayout()
    h1.addWidget(questl)
    h1.addWidget(questEdit)
    mainLine.addLayout(h1)

    h2 = QHBoxLayout()
    h2.addWidget(rightAnsweLBl)
    h2.addWidget(rightEdit)
    mainLine.addLayout(h2)

    h3 = QHBoxLayout()
    h3.addWidget(leftanswerlbL)
    h3.addWidget(leftEdit)
    mainLine.addLayout(h3)

    h4 = QHBoxLayout()
    h4.addWidget(jriginansLbl)
    h4.addWidget(jroginEdit)
    mainLine.addLayout(h4)

    h5 = QHBoxLayout()
    h5.addWidget(frostanswerLbl)
    h5.addWidget(frostEdit)
    mainLine.addLayout(h5)




    next2 = QPushButton("Добавити")

    def addFunc():
        memor.qeust.append(
            {
                "питання": questEdit.text(),
                "Правильна відповідь": rightEdit.text(),
                "Неправильна1": leftEdit.text(),
                "Неправильна2": jroginEdit.text(),
                "Неправильна3": frostEdit.text(),
            }
        )

    next2.clicked.connect(addFunc)
    mainLine.addWidget(next2)
    window.setLayout(mainLine)
    window.show()
    window.exec()