# GUI LOGIC Parts.
# from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from db_gui import Ui_MainWindow
# from PyQt5.QtCore import QCoreApplication
import re
# import os
import webbrowser
import MySQLdb as mysqlconn
import plotly as plt
import plotly.graph_objs as plt_go


# MyMainWindow definition.
class MyMainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self, parent = None):
		super(MyMainWindow, self).__init__(parent)
		self.setupUi(self)
		self.sql_cmd = "select * from lagou_job"
		self.lineEdit_connect_content = ""
		self.conn_host = ""
		self.conn_user = ""
		self.conn_passwd = ""
		self.conn_dbname = ""
		self.conn_charset = ""
		self.mysql_conn = None
		self.mysql_cursor = None
		self.mysql_rows = None
		self.conn_tablename = "demo"
		self.err = None
	# slots functions.
	# def btn_click_released(self):
	# 	QtWidgets.QMessageBox.information(self.pushButton, "Demo", "Demo gui program")
	
	def gui_quit(self):
		# QCoreApplication.instance().quit()
		self.close()  # self.btn_quit.released.connect(MainWindow.gui_quit)
	
	def btn_load_released(self):
		if self.mysql_cursor:
			self.sql_cmd = "SELECT title,salary,job_addr,job_type,degree_need,work_years,url,job_desc FROM " + self.conn_tablename
			self.mysql_cursor.execute(self.sql_cmd)
			self.mysql_rows = self.mysql_cursor.fetchall()

			for j in range(0, len(self.mysql_rows)):
				for i in range(0, 8):
					item = self.tableWidget.item(j, i)
					item.setText(self.mysql_rows[j][i])
			self.statusbar.showMessage("数据装载完成.")
		
		else:
			self.statusbar.showMessage("请先和数据库建立连接.")
	
	def btn_clear_released(self):
		for j in range(0, 10):
			for i in range(0, 8):
				item = self.tableWidget.item(j, i)
				item.setText(' ')
		self.statusbar.showMessage("所查询内容已经清除.")
	
	def btn_connect_released(self):
		if self.btn_connect.isChecked():
			# Use re.match() to grab text
			self.statusbar.showMessage("数据库连接开始...")
			self.lineEdit_connect_content = self.lineEdit_connect.text()
			temp = re.match(".*host=(.*?),.*", self.lineEdit_connect_content)
			if temp:
				self.conn_host = temp.group(1)
			else:
				self.statusbar.showMessage("输入错误,未检测到host字段.")
				return
			temp = re.match(".*user=(.*?),.*", self.lineEdit_connect_content)
			if temp:
				self.conn_user = temp.group(1)
			else:
				self.statusbar.showMessage("输入错误,未检测到user字段.")
				return
			temp = re.match(".*passwd=(.*?),.*", self.lineEdit_connect_content)
			if temp:
				self.conn_passwd = temp.group(1)
			else:
				self.statusbar.showMessage("输入错误,未检测到passwd字段.")
				return
			temp = re.match(".*db=(.*?),.*", self.lineEdit_connect_content)
			if temp:
				self.conn_dbname = temp.group(1)
			else:
				self.statusbar.showMessage("输入错误,未检测到db字段.")
				return
			temp = re.match(".*tab=(.*)", self.lineEdit_connect_content)
			if temp:
				self.conn_tablename = temp.group(1)
			else:
				self.statusbar.showMessage("输入错误,未检测到db字段.")
				return
			# connect with MySQL
			if not self.mysql_conn:
				try:
					self.mysql_conn = mysqlconn.connect(
							host=self.conn_host,
							user=self.conn_user,
							password=self.conn_passwd,
							database=self.conn_dbname,
							charset="utf8",
							use_unicode=True)
					self.mysql_cursor = self.mysql_conn.cursor()
				except Exception as err:
					self.err = err
					self.statusbar.showMessage(str(err) + "   数据库连接出错...")
					return
			# here, you should establish connection with MySQL successfully
			# construct SQL Quote
			self.statusbar.showMessage("数据库连接完成...")
		else:
			if self.mysql_conn:
				self.mysql_conn.close()
				self.mysql_cursor.close()
				self.mysql_cursor = None
				self.mysql_conn = None
				self.statusbar.showMessage("数据库连接关闭...")
			else:
				self.statusbar.showMessage("错误:无法关闭数据库...")
	
	def btn_up_released(self):
		pass
	
	def btn_next_released(self):
		pass
		
	def btn_execute_released(self):
		pass
	
	def btn_search_released(self):
		self.statusbar.showMessage("检索完成...")
		pass

	def die(self):
		try:
			self.mysql_cursor.close()
			self.mysql_conn.close()
		except Exception as err:
			print(err)
	
	def btn_plothisto_released(self):
		if self.mysql_conn:
			salary = [i[1] for i in self.mysql_rows]
			salary = [
				max(int(re.match('^(\d.*?)[Kk].*', i).group(1)), int(re.match('.*-(\d.*?)[Kk].*', i).group(1)))
				for i in salary
			]
			company = [i[0] for i in self.mysql_rows]
			data = [plt_go.Bar(
				x=company,
				y=salary
			)]
			plt.offline.plot(data, filename='最高薪资水平图.html')
			#####
			salary = [i[1] for i in self.mysql_rows]
			salary = [
				(int(re.match('^(\d.*?)[Kk].*', i).group(1))+int(re.match('.*-(\d.*?)[Kk].*', i).group(1)))/2
				for i in salary
			]
			company = [i[0] for i in self.mysql_rows]
			data = [plt_go.Bar(
				x=company,
				y=salary
			)]
			plt.offline.plot(data, filename='平均薪资水平图.html')
			#####
			salary = [i[1] for i in self.mysql_rows]
			salary = [
				min(int(re.match('^(\d.*?)[Kk].*', i).group(1)), int(re.match('.*-(\d.*?)[Kk].*', i).group(1)))
				for i in salary
			]
			company = [i[0] for i in self.mysql_rows]
			data = [plt_go.Bar(
				x=company,
				y=salary
			)]
			plt.offline.plot(data, filename='最低薪资水平图.html')
			self.statusbar.showMessage("薪资直方图绘制完成...")
		else:
			return
	
	def btn_browser_released(self):
		if re.match('.*http.*', self.lineEdit_url.text()):
			self.statusbar.showMessage('浏览页面：' + self.lineEdit_url.text())
			try:
				webbrowser.open(self.lineEdit_url.text())
			except Exception as err:
				self.statusbar.showMessage(str(err))
		else:
			self.statusbar.showMessage("请输入网址或者浏览器路径...")
