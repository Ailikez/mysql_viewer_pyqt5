import sys
from db_gui_logic import MyMainWindow
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MyMainWindow()
    main_win.show()
    sys.exit(app.exec_())
