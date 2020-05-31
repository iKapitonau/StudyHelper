import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon

class TeacherWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Study Helper (Teacher)')
        
        tasksAct = QAction(QIcon('icons/tasks.png'), 'Tasks', self)
        tasksAct.triggered.connect(self.tasks)

        pupilsAct = QAction(QIcon('icons/pupils.png'), 'Pupils Info', self)
        pupilsAct.triggered.connect(self.pupils)

        helpReqAct = QAction(QIcon('icons/helpreq.png'), 'Help Requests', self)
        helpReqAct.triggered.connect(self.helpReq)

        exitAct = QAction(QIcon('icons/exit.png'), 'Exit', self)
        exitAct.triggered.connect(qApp.quit)

        self.toolbar = self.addToolBar('Tasks')
        self.toolbar.setMovable(False)
        self.toolbar = self.addToolBar('Pupils Info')
        self.toolbar.setMovable(False)
        self.toolbar = self.addToolBar('Help Requests')
        self.toolbar.setMovable(False)
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.setMovable(False)
        self.toolbar.addAction(tasksAct)
        self.toolbar.addAction(pupilsAct)
        self.toolbar.addAction(helpReqAct)
        self.toolbar.addAction(exitAct)
        
        self.setGeometry(300, 300, 800, 600)

    def tasks(self):
        # TODO: add tasks action
        print('in tasks')

    def pupils(self):
        # TODO: add pupils action
        print('in pupils')

    def helpReq(self):
        # TODO: add help request action
        print('in help req')

    
