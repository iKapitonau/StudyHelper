from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QVBoxLayout, QLabel, QWidget, \
    QPushButton, QGridLayout

import dbutil
from dbutil import startWatchHelpMessages

import task

class TeacherWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Study Helper (Teacher)')
        self.layout = QVBoxLayout()
        self.notificationLayout = QGridLayout()

        self.tasksAct = QAction(QIcon('icons/tasks.png'), 'Tasks', self)
        self.tasksAct.triggered.connect(self.tasks)

        self.pupilsAct = QAction(QIcon('icons/pupils.png'), 'Pupils Info', self)
        self.pupilsAct.triggered.connect(self.pupils)

        self.normalHelpIcon = QIcon('icons/helpreq.png')
        self.alertHelpIcon = QIcon('icons/needhelp.png')
        self.helpReqAct = QAction(self.normalHelpIcon, 'Help Requests', self)
        self.helpReqAct.triggered.connect(self.showHelpList)

        self.exitAct = QAction(QIcon('icons/exit.png'), 'Exit', self)
        self.exitAct.triggered.connect(qApp.quit)

        self.toolbar = self.addToolBar('TeacherToolbar')
        self.toolbar.setMovable(False)
        self.toolbar.addAction(self.tasksAct)
        self.toolbar.addAction(self.pupilsAct)
        self.toolbar.addAction(self.helpReqAct)
        self.toolbar.addAction(self.exitAct)

        self.setGeometry(300, 300, 800, 600)
        self.setCentralWidget(QWidget())
        self.centralWidget().setLayout(self.layout)
        startWatchHelpMessages(lambda: self.helpReqAct.setIcon(self.alertHelpIcon))
        self.layout.addLayout(self.notificationLayout)

    def tasks(self):
        # TODO: add tasks action
        print('in tasks')
        self.createTask()
        # |create|
        # #1 oj123j1ok2j | edit | delete |
        # #2 jawdkajwdkj | edit | delete |

    def createTask(self):
        dlg = task.Dialog()
        if not dlg.exec_():
            # accepted
            print(dlg.name, dlg.descr, dlg.problem)

        # add to db

    def editTask(self, task):
        pass

    def deleteTask(self, task):
        pass

    def pupils(self):
        # TODO: add pupils action
        print('in pupils')

    def cleanLayout(self, layout):
        for index in reversed(range(layout.count())):
            layout.itemAt(index).widget().setParent(None)

    def showHelpList(self):
        self.helpReqAct.setIcon(self.normalHelpIcon)
        self.cleanLayout(self.notificationLayout)
        notifications = dbutil.getNotifications()
        i = 0
        for notification in notifications:
            message = "Pupil " + notification["username"] + " asks for help!"
            self.notificationLayout.addWidget(QLabel(message), i, 0)
            button = QPushButton("HELP")
            button.clicked.connect(lambda: self.helpPupilAction(notification))
            self.notificationLayout.addWidget(button, i, 1)
            i += 1

    def helpPupilAction(self, notification):
        dbutil.disableHelpNotification(notification["username"])
        self.showHelpList()
