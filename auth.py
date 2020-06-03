from PyQt5.QtWidgets import *
from dbutil import insertUser, findUser
from PyQt5 import QtCore, QtGui
import bcrypt

class Dialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('TP')
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        dlgLayout = QVBoxLayout()
        formLayout = QFormLayout()

        self.label = QLabel()
        pal = self.label.palette()
        pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("red"))
        self.label.setPalette(pal)
        formLayout.addRow(self.label)

        self.login_field = QLineEdit()
        formLayout.addRow('Login:', self.login_field)
        self.passwd_field = QLineEdit(echoMode=QLineEdit.Password)
        formLayout.addRow('Password:', self.passwd_field)

        self.who = 'Nobody'
        rb_teach = QRadioButton('Teacher')
        rb_teach.toggled.connect(lambda: self.who_are_you(rb_teach))
        rb_pup = QRadioButton('Pupil')
        rb_pup.toggled.connect(lambda: self.who_are_you(rb_pup))
        formLayout.addRow(rb_teach)
        formLayout.addRow(rb_pup)

        dlgLayout.addLayout(formLayout)
        btns = QDialogButtonBox()
        btns.setStandardButtons(QDialogButtonBox.Cancel)
        btns.rejected.connect(self.reject)

        signUpButton = QPushButton('SignUp')
        signInButton = QPushButton('SignIn')
        signUpButton.clicked.connect(self.signUp)
        signInButton.clicked.connect(self.signIn)

        btns.addButton(signUpButton, QDialogButtonBox.ActionRole)
        btns.addButton(signInButton, QDialogButtonBox.ActionRole)

        dlgLayout.addWidget(btns)
        self.setLayout(dlgLayout)

    def who_are_you(self, btn):
        if btn.text() == 'Teacher':
            if btn.isChecked():
                self.who = 'Teacher'
        elif btn.text() == 'Pupil':
            if btn.isChecked():
                self.who = 'Pupil'

    def extractUser(self):
        return {
            'username': self.login_field.text(),
            'password': self.passwd_field.text().encode('utf-8'),
            'role': self.who
        }

    def signIn(self):
        user = Dialog.extractUser(self)
        foundUser = findUser(user['username'])
        errorMsg = ''
        if foundUser == None or user['username'] != foundUser['username']:
            errorMsg = 'User not found.'
        elif not bcrypt.checkpw(user['password'], foundUser['password']):
            errorMsg = 'Incorrect password.'
        elif user['role'] == 'Nobody':
            errorMsg = 'Incorrect role.'

        if not errorMsg:
            self.username = self.login_field.text()
            self.done(0)
        else:
            self.label.setText(errorMsg)

    def signUp(self):
        user = Dialog.extractUser(self)
        foundUser = findUser(user['username'])
        errorMsg = ''
        if user['username'] == '' or user['password'] == '':
            errorMsg = 'Fill all fields.'
        elif user['role'] == 'Nobody':
            errorMsg = 'Incorrect role.'
        elif foundUser != None:
            errorMsg = 'User with such name already exists.'
        
        if not errorMsg:
            insertUser(user)
            self.username = self.login_field.text()
            self.done(0)
        else:
            self.label.setText(errorMsg)

    def reject(self):
        self.done(1)
