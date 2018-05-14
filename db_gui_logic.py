# GUI LOGIC Parts.
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from db_gui import Ui_MainWindow
import re
import webbrowser
import MySQLdb as mysqlconn
import plotly as plt
import plotly.graph_objs as plt_go


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        # 用来设置tableWidget
        self.tableWidget_modify()
        self.sql_cmd = "select * from"
        self.lineEdit_connect_content = ""
        self.conn_host = ""
        self.conn_user = ""
        self.conn_passwd = ""
        self.conn_dbname = ""
        self.conn_charset = ""
        self.mysql_conn = None
        self.mysql_cursor = None
        self.mysql_all_rows = None
        self.conn_tablename = "demo"
        self.err = None
        self.current_rows = None
        self.pages_of_rows = 0
        self.current_page = 1
        self.is_mysql_connected = False

    def gui_quit(self):
        # QCoreApplication.instance().quit()
        self.close()  # self.btn_quit.released.connect(MainWindow.gui_quit)

    def btn_load_released(self):
        if self.mysql_cursor:
            self.sql_cmd = "SELECT title,salary,job_addr,job_type,degree_need,work_years,url,job_desc FROM " \
                           + self.conn_tablename
            self.mysql_cursor.execute(self.sql_cmd)
            self.mysql_all_rows = self.mysql_cursor.fetchall()
            self.pages_of_rows = (int(len(self.mysql_all_rows)/30) + 1)if (len(self.mysql_all_rows) % 30) != 0 \
                else len(self.mysql_all_rows)/30
            self.current_rows = self.mysql_all_rows[0:30]
            for j in range(0, min(len(self.current_rows), 30)):
                for i in range(0, 8):
                    item = self.tableWidget.item(j, i)
                    item.setText(self.current_rows[j][i])
            self.statusbar.showMessage("数据装载完成,共{page}页,{amount}条数据.(～o￣3￣)～."\
                .format(page=str(int(self.pages_of_rows)), amount=str(len(self.mysql_all_rows))))
            # self.statusbar.showMessage(
            #     f"数据装载完成,共{str(int(self.pages_of_rows))}页,{str(len(self.mysql_all_rows))}条数据.(～o￣3￣)～.")
        else:
            self.statusbar.showMessage("请先和数据库建立连接.=￣ω￣=.")

    def btn_clear_released(self):
        for j in range(0, 30):
            for i in range(0, 8):
                item = self.tableWidget.item(j, i)
                item.setText(' ')
        self.statusbar.showMessage("内容已经清除＞︿＜")

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
                    self.statusbar.showMessage(str(err) + "   数据库连接出错...(￣_￣|||)")
                    return
            # here, you should establish connection with MySQL successfully
            # construct SQL Quote
            self.is_mysql_connected = True
            self.statusbar.showMessage("数据库连接完成...╰(￣ω￣ｏ)")
        else:
            if self.mysql_conn:
                self.mysql_conn.close()
                self.mysql_cursor.close()
                self.mysql_cursor = None
                self.mysql_conn = None
                self.statusbar.showMessage("数据库连接关闭(。>︿<)_θ")
                self.is_mysql_connected = False
            else:
                self.statusbar.showMessage("错误:无法关闭数据库...")

    def btn_up_released(self):
        if not self.is_mysql_connected:
            self.statusbar.showMessage("请先和数据库建立连接.(。・∀・)ノ")
            return
        if self.pages_of_rows == 0:
            self.statusbar.showMessage("无数据.")
            return
        if self.current_page > 1:
            self.current_page -= 1
        if self.current_page > self.pages_of_rows:
            self.current_page = self.pages_of_rows
            self.statusbar.showMessage("已经是最前一页.")
            return
        if self.current_page == self.pages_of_rows:
            self.current_rows = self.mysql_all_rows[((self.current_page-1)*30):]
        else:
            self.current_rows = self.mysql_all_rows[((self.current_page-1)*30):(self.current_page*30)]
        self.btn_clear_released()
        if self.mysql_cursor:
            for j in range(0, min(len(self.current_rows), 30)):
                for i in range(0, 8):
                    item = self.tableWidget.item(j, i)
                    item.setText(self.current_rows[j][i])
            self.statusbar.showMessage("第{page}页数据装载完成.=￣ω￣=.".format(page=str(self.current_page)))
        else:
            self.statusbar.showMessage("数据库连接出错咯😠.")

    def btn_next_released(self):
        if not self.is_mysql_connected:
            self.statusbar.showMessage("请先和数据库建立连接.(。・∀・)ノ")
            return
        if self.pages_of_rows == 0:
            self.statusbar.showMessage("无数据.")
            return
        if self.current_page < self.pages_of_rows:
            self.current_page += 1
        if self.current_page > self.pages_of_rows:
            self.current_page = self.pages_of_rows
            self.statusbar.showMessage("已经是最后一页.")
            return
        if self.current_page == self.pages_of_rows:
            self.current_rows = self.mysql_all_rows[((self.current_page-1)*30):]
        else:
            self.current_rows = self.mysql_all_rows[((self.current_page-1)*30):(self.current_page*30)]
        self.btn_clear_released()
        if self.mysql_cursor:
            for j in range(0, min(len(self.current_rows), 30)):
                for i in range(0, 8):
                    item = self.tableWidget.item(j, i)
                    item.setText(self.current_rows[j][i])
            self.statusbar.showMessage("第{page}页数据装载完成.=￣ω￣=.".format(page=str(self.current_page)))
        else:
            self.statusbar.showMessage("数据库连接出错咯😠.")

    def btn_search_released(self):
        if not self.is_mysql_connected:
            self.statusbar.showMessage("请先和数据库建立连接.(。・∀・)ノ")
            return
        self.btn_clear_released()
        temp_cmd = []
        temp = self.lineEdit_title.text()
        if temp:
            temp_cmd.append('title LIKE ' + '"%' + temp + '%"')
        temp = self.lineEdit_salary.text()
        if temp:
            temp_cmd.append('salary LIKE ' + '"%' + temp + '%"')
        temp = self.lineEdit_position.text()
        if temp:
            temp_cmd.append('job_addr LIKE ' + '"%' + temp + '%"')
        temp = self.lineEdit_workyears.text()
        if temp:
            temp_cmd.append('work_years LIKE ' + '"%' + temp + '%"')
        temp = self.lineEdit_degree.text()
        if temp:
            temp_cmd.append('degree_need LIKE ' + '"%' + temp + '%"')
        temp = self.lineEdit_type.text()
        if temp:
            temp_cmd.append('job_type LIKE ' + '"%' + temp + '%"')
        # 构建sql查询语句
        if not temp_cmd:
            self.statusbar.showMessage("请先输入检索信息哦(*￣3￣)╭")
            return
        sqlcmdstr = ''
        for i in temp_cmd:
            sqlcmdstr += i
            if i != temp_cmd[-1]:
                sqlcmdstr += ' and '
        sqlcmdstr = 'SELECT title,salary,job_addr,job_type,degree_need,work_years,url,job_desc FROM ' + self.conn_tablename \
                    + ' ' + 'WHERE' + ' ' + sqlcmdstr
        # 开始sql语句查询
        if self.mysql_cursor:
            self.mysql_cursor.execute(sqlcmdstr)
            self.mysql_all_rows = self.mysql_cursor.fetchall()
            self.pages_of_rows = (int(len(self.mysql_all_rows) / 30) + 1) if (len(self.mysql_all_rows) % 30) != 0 \
                else len(self.mysql_all_rows) / 30
            self.current_rows = self.mysql_all_rows[0:30]
            for j in range(0, min(len(self.current_rows), 30)):
                for i in range(0, 8):
                    item = self.tableWidget.item(j, i)
                    item.setText(self.current_rows[j][i])
            # self.statusbar.showMessage(f"数据查询完成,共{str(self.pages_of_rows)}页,{str(len(self.mysql_all_rows))}条数据.")
            self.statusbar.showMessage("数据装载完成,共{page}页,{amount}条数据.(～o￣3￣)～."\
                .format(page=str(int(self.pages_of_rows)), amount=str(len(self.mysql_all_rows))))
        else:
            self.statusbar.showMessage("请先和数据库建立连接.(。・∀・)ノ")

    def die(self):
        try:
            self.mysql_cursor.close()
            self.mysql_conn.close()
        except Exception as err:
            print(err)

    def btn_plothisto_released(self):
        if not self.is_mysql_connected:
            self.statusbar.showMessage("请先和数据库建立连接.(。・∀・)ノ")
            return
        # if self.mysql_conn:
        #     salary = [i[1] for i in self.current_rows]
        #     salary = [
        #         max(int(re.match('^(\d.*?)[Kk].*', i).group(1)), int(re.match('.*-(\d.*?)[Kk].*', i).group(1)))
        #         for i in salary
        #     ]
        #     j = [i for i in range(1, len(self.current_rows)+1)]
        #     company = [str(k)+'-'+i[0] for (k, i) in zip(j, self.current_rows)]
        #     data = [plt_go.Bar(
        #         x=company,
        #         y=salary
        #     )]
        #     plt.offline.plot(data, filename='最高薪资水平图.html')
            #####
            salary = [i[1] for i in self.current_rows]
            salary = [
                (int(re.match('^(\d.*?)[Kk].*', i).group(1)) + int(re.match('.*-(\d.*?)[Kk].*', i).group(1))) / 2
                for i in salary
            ]
            j = [i for i in range(1, len(self.current_rows)+1)]
            company = [str(k)+'-'+i[0] for (k, i) in zip(j, self.current_rows)]
            data = [plt_go.Bar(
                x=company,
                y=salary
            )]
            plt.offline.plot(data, filename='./output/average_salary.html')
        #     #####
        #     salary = [i[1] for i in self.current_rows]
        #     salary = [
        #         min(int(re.match('^(\d.*?)[Kk].*', i).group(1)), int(re.match('.*-(\d.*?)[Kk].*', i).group(1)))
        #         for i in salary
        #     ]
        #     j = [i for i in range(1, len(self.current_rows)+1)]
        #     company = [str(k)+'-'+i[0] for (k, i) in zip(j, self.current_rows)]
        #     data = [plt_go.Bar(
        #         x=company,
        #         y=salary
        #     )]
        #     plt.offline.plot(data, filename='最低薪资水平图.html')
        #     self.statusbar.showMessage("薪资直方图绘制完成(ง •_•)ง")
        # else:
        #     return

    def btn_browser_released(self):
        if re.match('.*http.*', self.lineEdit_url.text()):
            self.statusbar.showMessage('浏览页面：' + self.lineEdit_url.text())
            try:
                webbrowser.open(self.lineEdit_url.text())
            except Exception as err:
                self.statusbar.showMessage(str(err))
        else:
            self.statusbar.showMessage("请输入网址或者浏览器路径(。>︿<)_θ")

    def tableWidget_modify(self):
        _translate = QtCore.QCoreApplication.translate
        for i in range(0, 30):
            for j in range(0, 8):
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setItem(i, j, item)
        for i in range(0, 30):
            for j in range(0, 8):
                item = self.tableWidget.item(i, j)
                item.setText(_translate("MainWindow", " "))
