from schoolmanagement import mainwindow
from schoolmanagement.schoolmodels import database
import sys
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = mainwindow()
    # print(database.get_all_course())
    sys.exit(app.exec_())
    
    # print(dir_path)