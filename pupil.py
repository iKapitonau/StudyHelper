import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon

class PupilWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Study Helper (Pupil)')
        
        exitAct = QAction(QIcon('exit.png'), 'Exit', self)
        exitAct.triggered.connect(qApp.quit)

        helpMeAct = QAction(QIcon('helpme.png'), 'HELP ME!', self)
        helpMeAct.triggered.connect(self.helpMe)
        
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(helpMeAct)
        self.toolbar.addAction(exitAct)

        self.setGeometry(300, 300, 800, 600)

    def helpMe(self):
        # TODO: add help action
        print('kek')
