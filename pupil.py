from datetime import datetime

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QComboBox, QLabel, \
    QWidget, QVBoxLayout, QPlainTextEdit, QPushButton

from dbutil import getTasks, insertHelpNotification


class PupilWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Study Helper (Pupil)')

        self.layout = QVBoxLayout()
        self.taskLayout = QVBoxLayout()
        self.tasks = getTasks()
        self.answers = [{'enabled': True, 'text': '', 'submitTime': None} for i in range(len(self.tasks))]

        exitAct = QAction(QIcon('icons/exit.png'), 'Exit', self)
        exitAct.triggered.connect(qApp.quit)

        helpMeAct = QAction(QIcon('icons/helpme.png'), 'HELP ME!', self)
        helpMeAct.triggered.connect(self.helpMe)

        self.toolbar = self.addToolBar('PupilToolbar')
        self.toolbar.setMovable(False)
        self.toolbar.addAction(helpMeAct)
        self.toolbar.addAction(exitAct)

        self.initTaskComboBox()
        self.selectTaskAction(0)

        self.setCentralWidget(QWidget(self))
        self.centralWidget().setLayout(self.layout)
        self.setGeometry(300, 300, 800, 600)

    def selectTaskAction(self, i):
        currentTask = self.tasks[i]

        for index in reversed(range(self.taskLayout.count())):
            self.taskLayout.itemAt(index).widget().setParent(None)

        self.taskLayout.addWidget(QLabel(currentTask["name"]))
        self.taskLayout.addWidget(QLabel(currentTask["description"]))
        self.taskLayout.addWidget(QLabel(currentTask["full"]))
        self.taskLayout.addWidget(QLabel("Enter solution:"))

        answer = QPlainTextEdit(self)
        answer.insertPlainText(self.answers[i]['text'])
        answer.setEnabled(self.answers[i]['enabled'])
        answer.textChanged.connect(lambda: self.writeAnswerAction(i, answer.toPlainText()))
        self.taskLayout.addWidget(answer)

        button = QPushButton("Submit")
        button.setEnabled(self.answers[i]['enabled'])
        button.clicked.connect(lambda: self.submitTaskAction(i, answer, button))
        self.taskLayout.addWidget(button)

    def writeAnswerAction(self, i, text):
        self.answers[i]['text'] = text

    def submitTaskAction(self, i, answer, button):
        self.answers[i]['enabled'] = False
        answer.setEnabled(False)
        button.setEnabled(False)
        self.answers[i]['submitTime'] = datetime.now()

    def helpMe(self):
        # TODO: pass real userId
        insertHelpNotification('testUserIdFromHelpMeFunc')

    def initTaskComboBox(self):
        cb = QComboBox()
        for i in self.tasks:
            item = i["name"] + " - " + i["description"]
            cb.addItem(item)
        cb.currentIndexChanged.connect(self.selectTaskAction)
        self.layout.addWidget(cb)
        self.layout.addLayout(self.taskLayout)
