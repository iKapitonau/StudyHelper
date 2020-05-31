import sys
from PyQt5.QtWidgets import *

import auth
import teacher
import pupil

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = auth.Dialog()
    if not dlg.exec_():
        # TODO: create teacher or pupil window
        print(dlg.who)
