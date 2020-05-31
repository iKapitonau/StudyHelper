import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon
from dbutil import insertHelpNotification

class PupilWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Study Helper (Pupil)')
        
        exitAct = QAction(QIcon('icons/exit.png'), 'Exit', self)
        exitAct.triggered.connect(qApp.quit)

        helpMeAct = QAction(QIcon('icons/helpme.png'), 'HELP ME!', self)
        helpMeAct.triggered.connect(self.helpMe)
        
        self.toolbar = self.addToolBar('PupilToolbar')
        self.toolbar.setMovable(False)
        self.toolbar.addAction(helpMeAct)
        self.toolbar.addAction(exitAct)

        self.setGeometry(300, 300, 800, 600)

    def helpMe(self):
        #TODO: pass real userId
        insertHelpNotification('testUserIdFromHelpMeFunc')
