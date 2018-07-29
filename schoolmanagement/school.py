from PyQt5.QtWidgets import (QWidget,QMainWindow,QApplication,QDialog)
from PyQt5.QtCore import pyqtSlot,QDateTime,Qt
import sys
from PyQt5.uic import loadUi
import os
from schoolmanagement.pkgcourse import coursewindow
from schoolmanagement.pkgsubjects import subjectwindow
from schoolmanagement.pkgteachers import teacherwindow


dir_path = os.path.dirname(os.path.realpath(__file__))

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi(os.path.join(dir_path,'layouts','main.ui'),self)

        self.courseWindow = coursewindow()
        self.subjectWindow = subjectwindow()
        self.teacherWindow = teacherwindow()

        self.stackedWidget.addWidget(self.courseWindow)
        self.stackedWidget.addWidget(self.subjectWindow)
        self.stackedWidget.addWidget(self.teacherWindow)
        self.stackedWidget.setCurrentWidget(self.teacherWindow)

        self.show()

        



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
    print(dir_path)