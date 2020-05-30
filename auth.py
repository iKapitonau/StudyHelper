from PyQt5.QtWidgets import *
from PyQt5 import QtCore

class Dialog(QDialog):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.setWindowTitle('TP')
		self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
		dlgLayout = QVBoxLayout()
		formLayout = QFormLayout()

		self.label = QLabel()
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
		btns.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
		dlgLayout.addWidget(btns)
		self.setLayout(dlgLayout)
		btns.accepted.connect(self.accept)
		btns.rejected.connect(self.reject)

	def who_are_you(self, btn):
		if btn.text() == 'Teacher':
			if btn.isChecked():
				self.who = 'Teacher'
		elif btn.text() == 'Pupil':
			if btn.isChecked():
				self.who = 'Pupil'
	
	def accept(self):
		# TODO: Login and password check
		if self.login_field.text() == 'kek' and self.passwd_field.text() == 'lol' \
			and self.who in ['Teacher', 'Pupil']:
			self.label.setText('Logged as ' + self.who)
			self.done(0)
		else:
		# TODO: Add more informative text
			self.label.setText('Wrong something!')

	def reject(self):
		self.done(1)

