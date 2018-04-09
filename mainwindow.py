# GUI LOGIC Parts.
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from ui_mainwindow import Ui_MainWindow


# MyMainWindow definition.
class MyMainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self, parent=None):
		super(MyMainWindow, self).__init__(parent)
		self.setupUi(self)
	
	# slots functions.
	def btn_click_released(self):
		QtWidgets.QMessageBox.information(self.pushButton, "Demo", "Demo gui program")