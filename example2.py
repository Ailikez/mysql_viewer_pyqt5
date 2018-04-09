# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'D:/nihao.ui'
#
# Created: Fri Apr 01 15:28:59 2016
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
import MySQLdb

try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	def _fromUtf8(s):
		return s

try:
	_encoding = QtGui.QApplication.UnicodeUTF8
	
	
	def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
	def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig)


class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		
		self.conn = MySQLdb.connect(host = 'localhost', user = 'root', passwd = '', db = 'mysql', #
				charset = 'utf8', )
		self.cur = self.conn.cursor()
		
		self.sqlstring = "select * from students where "
		MainWindow.setObjectName(_fromUtf8("MainWindow"))
		MainWindow.resize(760, 440)
		self.centralwidget = QtGui.QWidget(MainWindow)
		self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
		self.frame = QtGui.QFrame(self.centralwidget)
		self.frame.setGeometry(QtCore.QRect(10, 10, 491, 121))
		self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
		self.frame.setFrameShadow(QtGui.QFrame.Raised)
		self.frame.setObjectName(_fromUtf8("frame"))
		self.check_Sid = QtGui.QCheckBox(self.frame)
		self.check_Sid.setGeometry(QtCore.QRect(20, 10, 71, 16))
		self.check_Sid.setObjectName(_fromUtf8("check_Sid"))
		self.check_Sage = QtGui.QCheckBox(self.frame)
		self.check_Sage.setGeometry(QtCore.QRect(20, 70, 71, 16))
		self.check_Sage.setObjectName(_fromUtf8("check_Sage"))
		self.check_Sname = QtGui.QCheckBox(self.frame)
		self.check_Sname.setGeometry(QtCore.QRect(20, 40, 71, 16))
		self.check_Sname.setObjectName(_fromUtf8("check_Sname"))
		self.check_Ssex = QtGui.QCheckBox(self.frame)
		self.check_Ssex.setGeometry(QtCore.QRect(20, 100, 71, 16))
		self.check_Ssex.setObjectName(_fromUtf8("check_Ssex"))
		self.Sid = QtGui.QLineEdit(self.frame)
		self.Sid.setGeometry(QtCore.QRect(90, 10, 113, 16))
		self.Sid.setObjectName(_fromUtf8("Sid"))
		self.Sname = QtGui.QLineEdit(self.frame)
		self.Sname.setGeometry(QtCore.QRect(90, 40, 113, 16))
		self.Sname.setObjectName(_fromUtf8("Sname"))
		self.first_Sage = QtGui.QLineEdit(self.frame)
		self.first_Sage.setGeometry(QtCore.QRect(90, 70, 41, 16))
		self.first_Sage.setObjectName(_fromUtf8("first_Sage"))
		self.Ssex = QtGui.QLineEdit(self.frame)
		self.Ssex.setGeometry(QtCore.QRect(90, 100, 113, 16))
		self.Ssex.setObjectName(_fromUtf8("Ssex"))
		self.label = QtGui.QLabel(self.frame)
		self.label.setGeometry(QtCore.QRect(140, 70, 16, 16))
		self.label.setObjectName(_fromUtf8("label"))
		self.last_Sage = QtGui.QLineEdit(self.frame)
		self.last_Sage.setGeometry(QtCore.QRect(160, 70, 41, 16))
		self.last_Sage.setObjectName(_fromUtf8("last_Sage"))
		self.check_Sdept = QtGui.QCheckBox(self.frame)
		self.check_Sdept.setGeometry(QtCore.QRect(270, 40, 71, 16))
		self.check_Sdept.setObjectName(_fromUtf8("check_Sdept"))
		self.Sdept = QtGui.QLineEdit(self.frame)
		self.Sdept.setGeometry(QtCore.QRect(340, 40, 113, 16))
		self.Sdept.setObjectName(_fromUtf8("Sdept"))
		self.Sclass = QtGui.QLineEdit(self.frame)
		self.Sclass.setGeometry(QtCore.QRect(340, 10, 113, 16))
		self.Sclass.setObjectName(_fromUtf8("Sclass"))
		self.check_Sclass = QtGui.QCheckBox(self.frame)
		self.check_Sclass.setGeometry(QtCore.QRect(270, 10, 71, 16))
		self.check_Sclass.setObjectName(_fromUtf8("check_Sclass"))
		self.Saddr = QtGui.QLineEdit(self.frame)
		self.Saddr.setGeometry(QtCore.QRect(340, 70, 113, 16))
		self.Saddr.setObjectName(_fromUtf8("Saddr"))
		self.check_Saddr = QtGui.QCheckBox(self.frame)
		self.check_Saddr.setGeometry(QtCore.QRect(270, 70, 71, 16))
		self.check_Saddr.setObjectName(_fromUtf8("check_Saddr"))
		self.find = QtGui.QPushButton(self.frame)
		self.find.setGeometry(QtCore.QRect(380, 100, 75, 21))
		self.find.setObjectName(_fromUtf8("find"))
		self.sql_out = QtGui.QTextBrowser(self.centralwidget)
		self.sql_out.setGeometry(QtCore.QRect(10, 140, 740, 61))
		self.sql_out.setObjectName(_fromUtf8("sql_out"))
		self.result_out = QtGui.QTableWidget(self.centralwidget)
		self.result_out.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)  # 不可编辑表格
		self.result_out.setGeometry(QtCore.QRect(10, 210, 740, 171))
		self.result_out.setObjectName(_fromUtf8("result_out"))
		self.result_out.setColumnCount(7)
		self.result_out.setRowCount(10)
		self.result_out.resizeColumnsToContents()
		self.result_out.resizeRowsToContents()
		item = QtGui.QTableWidgetItem()
		self.result_out.setHorizontalHeaderItem(0, item)
		item = QtGui.QTableWidgetItem()
		self.result_out.setHorizontalHeaderItem(1, item)
		item = QtGui.QTableWidgetItem()
		self.result_out.setHorizontalHeaderItem(2, item)
		item = QtGui.QTableWidgetItem()
		self.result_out.setHorizontalHeaderItem(3, item)
		item = QtGui.QTableWidgetItem()
		self.result_out.setHorizontalHeaderItem(4, item)
		item = QtGui.QTableWidgetItem()
		self.result_out.setHorizontalHeaderItem(5, item)
		item = QtGui.QTableWidgetItem()
		self.result_out.setHorizontalHeaderItem(6, item)
		self.result_out.horizontalHeader().setDefaultSectionSize(100)
		self.result_out.horizontalHeader().setMinimumSectionSize(25)
		self.result_out.verticalHeader().setDefaultSectionSize(30)
		self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
		self.pushButton_2.setGeometry(QtCore.QRect(675, 390, 75, 21))
		self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtGui.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 509, 23))
		self.menubar.setObjectName(_fromUtf8("menubar"))
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtGui.QStatusBar(MainWindow)
		self.statusbar.setObjectName(_fromUtf8("statusbar"))
		MainWindow.setStatusBar(self.statusbar)
		
		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)
	
	def retranslateUi(self, MainWindow):
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
		self.check_Sid.setText(_translate("MainWindow", "学号", None))
		self.check_Sage.setText(_translate("MainWindow", "年龄自", None))
		self.check_Sname.setText(_translate("MainWindow", "姓名", None))
		self.check_Ssex.setText(_translate("MainWindow", "性别", None))
		self.label.setText(_translate("MainWindow", "到", None))
		self.check_Sdept.setText(_translate("MainWindow", "系", None))
		self.check_Sclass.setText(_translate("MainWindow", "班级", None))
		self.check_Saddr.setText(_translate("MainWindow", "地址", None))
		self.find.setText(_translate("MainWindow", "查询", None))
		self.sql_out.setText(self.sqlstring)
		item = self.result_out.horizontalHeaderItem(0)
		item.setText(_translate("MainWindow", "Sid", None))
		item = self.result_out.horizontalHeaderItem(1)
		item.setText(_translate("MainWindow", "Sname ", None))
		item = self.result_out.horizontalHeaderItem(2)
		item.setText(_translate("MainWindow", "Sage", None))
		item = self.result_out.horizontalHeaderItem(3)
		item.setText(_translate("MainWindow", "Ssex", None))
		item = self.result_out.horizontalHeaderItem(4)
		item.setText(_translate("MainWindow", "Sclass", None))
		item = self.result_out.horizontalHeaderItem(5)
		item.setText(_translate("MainWindow", "Sdept", None))
		item = self.result_out.horizontalHeaderItem(6)
		item.setText(_translate("MainWindow", "Saddr", None))
		self.pushButton_2.setText(_translate("MainWindow", "退出", None))
	
	def mousePressEvent(self, event):
		if event.self.find() == QtCore.Qt.LeftButton:
			print
			"nihao"
	
	def buttonTest(self):
		temp_sqlstring = self.sqlstring
		is_first = True
		if self.check_Sid.isChecked():
			mystr = self.Sid.text()
			if is_first:
				is_first = False
				if mystr.find("%") == -1:
					temp_sqlstring += "Sid = '" + self.Sid.text() + "'"
				else:
					temp_sqlstring += "Sid like '" + self.Sid.text() + "'"
			else:
				if mystr.find("%") == -1:
					temp_sqlstring += " and Sid = '" + self.Sid.text() + "'"
				else:
					temp_sqlstring += " and Sid like '" + self.Sid.text() + "'"
		
		if self.check_Sname.isChecked():
			if is_first:
				mystr = self.Sname.text()
				is_first = False
				if mystr.find("%") == -1:
					temp_sqlstring += "Sname = '" + self.Sname.text() + "'"
				else:
					temp_sqlstring += "Sname like '" + self.Sname.text() + "'"
			else:
				if mystr.find("%") == -1:
					temp_sqlstring += " and Sname = '" + self.Sname.text() + "'"
				else:
					temp_sqlstring += " and Sname like '" + self.Sname.text() + "'"
		
		if self.check_Sage.isChecked():
			if is_first:
				is_first = False
				temp_sqlstring += "Sage >= " + self.first_Sage.text() + " and Sage <= " + self.last_Sage.text()
			else:
				temp_sqlstring += " and Sage >= " + self.first_Sage.text() + " and Sage <= " + self.last_Sage.text()
		
		if self.check_Ssex.isChecked():
			if is_first:
				is_first = False
				temp_sqlstring += "Ssex = '" + self.Ssex.text() + "'"
			else:
				temp_sqlstring += " and Ssex = '" + self.Ssex.text() + "'"
		
		if self.check_Sclass.isChecked():
			if is_first:
				mystr = self.Sclass.text()
				is_first = False
				if mystr.find("%") == -1:
					temp_sqlstring += "Sclass = '" + self.Sclass.text() + "'"
				else:
					temp_sqlstring += "Sclass like '" + self.Sclass.text() + "'"
			else:
				if mystr.find("%") == -1:
					temp_sqlstring += " and Sclass = '" + self.Sclass.text() + "'"
				else:
					temp_sqlstring += " and Sclass like '" + self.Sclass.text() + "'"
		
		if self.check_Sdept.isChecked():
			if is_first:
				mystr = self.Sdept.text()
				is_first = False
				if mystr.find("%") == -1:
					temp_sqlstring += "Sdept = '" + self.Sdept.text() + "'"
				else:
					temp_sqlstring += "Sdept like '" + self.Sdept.text() + "'"
			else:
				if mystr.find("%") == -1:
					temp_sqlstring += " and Sdept = '" + self.Sdept.text() + "'"
				else:
					temp_sqlstring += " and Sdept like '" + self.Sdept.text() + "'"
		
		if self.check_Saddr.isChecked():
			if is_first:
				mystr = self.Saddr.text()
				is_first = False
				if mystr.find("%") == -1:
					temp_sqlstring += "Saddr = '" + self.Saddr.text() + "'"
				else:
					temp_sqlstring += " and Saddr like '" + self.Saddr.text() + "'"
			else:
				if mystr.find("%") == -1:
					temp_sqlstring += " and Saddr = '" + self.Saddr.text() + "'"
				else:
					temp_sqlstring += " and Saddr like '" + self.Saddr.text() + "'"
		
		self.result_out.clearContents()  # 每一次查询时清除表格中信息
		if not (is_first):
			self.cur.execute(temp_sqlstring)
			k = 0
			for i in self.cur:
				w = 0
				for j in i:
					if type(j) == long:
						newItem = QtGui.QTableWidgetItem(str(j))
					else:
						newItem = QtGui.QTableWidgetItem(j)
					self.result_out.setItem(k, w, newItem)
					w += 1
				k += 1
		
		self.sql_out.setText("")
		self.sql_out.append(temp_sqlstring)
		print
		"find button pressed"
	
	def buttonExit(self):
		self.conn.commit()
		self.cur.close()
		self.conn.close()
		self.close()
	
	def keyPressEvent(self, e):
		if e.key() == QtCore.Qt.Key_Escape:
			self.buttonExit()


class MyWindow(QtGui.QMainWindow, Ui_MainWindow):
	def __init__(self):
		super(MyWindow, self).__init__()
		self.setupUi(self)
		self.connect(self.find, QtCore.SIGNAL('clicked()'), self.buttonTest)
		self.connect(self.pushButton_2, QtCore.SIGNAL('clicked()'), self.buttonExit)


if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	app.aboutToQuit.connect(app.deleteLater)
	myshow = MyWindow()
	myshow.show()
	sys.exit(app.exec_())  # app.exec_()  # sys.exit(0)