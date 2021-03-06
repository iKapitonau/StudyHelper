from functools import partial

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QVBoxLayout, QLabel, QWidget, \
    QPushButton, QGridLayout

import dbutil
import task


class TeacherWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Study Helper (Teacher)')
        self.layout = QVBoxLayout()
        self.notificationLayout = QGridLayout()
        self.tasksLayout = QGridLayout()

        self.tasks = []

        self.tasksAct = QAction(QIcon('icons/tasks.png'), 'Tasks', self)
        self.tasksAct.triggered.connect(self.showTaskList)

        self.pupilsAct = QAction(QIcon('icons/pupils.png'), 'Pupils Info', self)
        self.pupilsAct.triggered.connect(self.pupils)

        self.normalHelpIcon = QIcon('icons/helpreq.png')
        self.alertHelpIcon = QIcon('icons/needhelp.png')
        self.helpReqAct = QAction(self.normalHelpIcon, 'Help Requests', self)
        self.helpReqAct.triggered.connect(self.showHelpList)

        self.exitAct = QAction(QIcon('icons/exit.png'), 'Exit', self)
        self.exitAct.triggered.connect(qApp.quit)

        self.createTaskAct = QAction(QIcon('icons/create.png'), 'Create Task', self)
        self.createTaskAct.triggered.connect(self.createTask)

        self.toolbar = self.addToolBar('TeacherToolbar')
        self.toolbar.setMovable(False)
        self.toolbar.addAction(self.createTaskAct)
        self.toolbar.addAction(self.tasksAct)
        self.toolbar.addAction(self.pupilsAct)
        self.toolbar.addAction(self.helpReqAct)
        self.toolbar.addAction(self.exitAct)

        self.setGeometry(300, 300, 800, 600)
        self.setCentralWidget(QWidget())
        self.centralWidget().setLayout(self.layout)
        dbutil.startWatchHelpMessages(lambda: self.helpReqAct.setIcon(self.alertHelpIcon))

    def updateLayout(self, layout):
        self.tasks = dbutil.getTasks()
        self.layout = layout
        self.setCentralWidget(QWidget())
        self.centralWidget().setLayout(self.layout)

    def showTaskList(self):
        self.tasksLayout = QGridLayout()
        self.updateLayout(self.tasksLayout)
        i = 0
        for t in self.tasks:
            message = t["name"] + " - " + t["description"] + "\n" + t["full"]
            self.tasksLayout.addWidget(QLabel(message), i, 0)
            buttonEdit = QPushButton("EDIT")
            buttonEdit.clicked.connect(partial(self.editTaskAction, t))
            self.tasksLayout.addWidget(buttonEdit, i, 1)
            buttonDel = QPushButton("DELETE")
            buttonDel.clicked.connect(partial(self.deleteTaskAction, t))
            self.tasksLayout.addWidget(buttonDel, i, 2)
            i += 2

    def extractTask(self, dlg):
        return {
                'name': dlg.name,
                'description': dlg.descr,
                'full': dlg.problem
                }

    def createTask(self):
        dlg = task.Dialog()
        if not dlg.exec_():
            dbutil.upsertTask(self.extractTask(dlg))
        self.showTaskList()

    def editTaskAction(self, taskdescr):
        dlg = task.Dialog(taskdescr['name'], taskdescr['description'], taskdescr['full'])
        if not dlg.exec_():
            dbutil.upsertTask(self.extractTask(dlg))
        self.showTaskList()

    def deleteTaskAction(self, t):
        dbutil.deleteTask(t['_id'])
        self.showTaskList()

    def pupils(self):
        # TODO: add pupils action
        print('in pupils')

    def cleanLayout(self, layout):
        for index in reversed(range(layout.count())):
            layout.itemAt(index).widget().setParent(None)

    def showHelpList(self):
        self.notificationLayout = QGridLayout()
        self.updateLayout(self.notificationLayout)
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
