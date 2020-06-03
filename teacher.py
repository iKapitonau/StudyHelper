import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon
from dbutil import startWatchHelpMessages

class TeacherWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Study Helper (Teacher)')
        
        self.tasksAct = QAction(QIcon('icons/tasks.png'), 'Tasks', self)
        self.tasksAct.triggered.connect(self.tasks)

        self.pupilsAct = QAction(QIcon('icons/pupils.png'), 'Pupils Info', self)
        self.pupilsAct.triggered.connect(self.pupils)

        self.normalHelpIcon = QIcon('icons/helpreq.png')
        self.alertHelpIcon = QIcon('icons/needhelp.png')
        self.helpReqAct = QAction(self.normalHelpIcon, 'Help Requests', self)
        self.helpReqAct.triggered.connect(self.helpReq)

        self.exitAct = QAction(QIcon('icons/exit.png'), 'Exit', self)
        self.exitAct.triggered.connect(qApp.quit)

        self.toolbar = self.addToolBar('TeacherToolbar')
        self.toolbar.setMovable(False)
        self.toolbar.addAction(self.tasksAct)
        self.toolbar.addAction(self.pupilsAct)
        self.toolbar.addAction(self.helpReqAct)
        self.toolbar.addAction(self.exitAct)
        
        self.setGeometry(300, 300, 800, 600)
        
        startWatchHelpMessages(lambda: self.helpReqAct.setIcon(self.alertHelpIcon))

    def tasks(self):
        # TODO: add tasks action
        print('in tasks')

    def pupils(self):
        # TODO: add pupils action
        print('in pupils')

    def helpReq(self):
        # TODO: add help request action
        print('in help req')
        self.helpReqAct.setIcon(self.normalHelpIcon)
        notifications = dbutil.getNotifications()
        for i in notifications:
        # TODO: notifications output
            pass

