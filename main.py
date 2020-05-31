import sys
from PyQt5.QtWidgets import *

import auth
import teacher
import pupil

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = auth.Dialog()
    if not dlg.exec_():
        if dlg.who == 'Pupil':
            window = pupil.PupilWindow()
            window.show()
        elif dlg.who == 'Teacher':
            window = teacher.TeacherWindow()
            window.show()
    sys.exit(app.exec_())
    