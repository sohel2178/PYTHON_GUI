from PyQt5.QtWidgets import (QWidget,QTableWidgetItem,QPushButton,QTableWidget)
from PyQt5.QtCore import pyqtSlot
from PyQt5.uic import loadUi

import os

dir_path = os.path.dirname(os.path.realpath(__file__))

class SubjectTableView(QWidget):
    def __init__(self):
        super().__init__()
        loadUi(os.path.join(dir_path,'layouts','subject.ui'),self)
        
        # self.refresh_table()

    def test(self):
        print("Test Success")


    def refresh_table(self,subjectList):
            self.subjectList = subjectList
            subjectCounter = len(self.subjectList)
            colCounter =5
            headers = ['Name','Part','Course','Teacher','Class Room']
            self.tableWidget.setRowCount(subjectCounter)
            self.tableWidget.setColumnCount(colCounter)
            self.tableWidget.setHorizontalHeaderLabels(headers)

            for i in range(subjectCounter):
                subject = self.subjectList[i]
                self.tableWidget.setItem(i,0,QTableWidgetItem(subject.name))
                self.tableWidget.setItem(i,1,QTableWidgetItem(subject.part))
                self.tableWidget.setItem(i,2,QTableWidgetItem(subject.course.name))

                if subject.teacher == None:
                    self.teacher_button = QPushButton('Assign')
                    self.teacher_button.setStyleSheet("QPushButton{color:white;background-color:blue;}QPushButton:hover{background-color: #5f99ef;}")
                    self.teacher_button.setObjectName(str(i))
                    self.teacher_button.clicked.connect(self.handle_teacher_button_click)
                    self.tableWidget.setCellWidget(i,3,self.teacher_button)
                else:
                    self.tableWidget.setItem(i,3,QTableWidgetItem(subject.teacher.name))

                if subject.classroom == None:
                    self.classroom_button = QPushButton('Assign')
                    self.classroom_button.setStyleSheet("QPushButton{color:white;background-color:blue;}QPushButton:hover{background-color: #5f99ef;}")
                    self.classroom_button.clicked.connect(self.handle_classroom_button_click)
                    self.tableWidget.setCellWidget(i,4,self.classroom_button)
                else:
                    self.tableWidget.setItem(i,3,QTableWidgetItem(subject.classroom.name))

    

    # @pyqtSlot()
    def handle_teacher_button_click(self):
        print("Clicked")
        button = self.sender()
        subject = self.subjectList[int(button.objectName())]

        print(subject.name)

        

    def handle_classroom_button_click(self):
        pass



class TeacherTableView(QWidget):
    def __init__(self):
        super().__init__()
        loadUi(os.path.join(dir_path,'layouts','teacher.ui'),self)
        
        # self.refresh_table()


    def refresh_table(self,subjectList):
            self.subjectList = subjectList
            subjectCounter = len(self.subjectList)
            colCounter =5
            headers = ['Name','Part','Course','Teacher','Class Room']
            self.tableWidget.setRowCount(subjectCounter)
            self.tableWidget.setColumnCount(colCounter)
            self.tableWidget.setHorizontalHeaderLabels(headers)

            for i in range(subjectCounter):
                subject = self.subjectList[i]
                self.tableWidget.setItem(i,0,QTableWidgetItem(subject.name))
                self.tableWidget.setItem(i,1,QTableWidgetItem(subject.part))
                self.tableWidget.setItem(i,2,QTableWidgetItem(subject.course.name))

                if subject.teacher == None:
                    self.teacher_button = QPushButton('Assign')
                    self.teacher_button.setStyleSheet("QPushButton{color:white;background-color:blue;}QPushButton:hover{background-color: #5f99ef;}")
                    self.teacher_button.setObjectName(str(i))
                    self.teacher_button.clicked.connect(self.handle_teacher_button_click)
                    self.tableWidget.setCellWidget(i,3,self.teacher_button)
                else:
                    self.tableWidget.setItem(i,3,QTableWidgetItem(subject.teacher.name))

                if subject.classroom == None:
                    self.classroom_button = QPushButton('Assign')
                    self.classroom_button.setStyleSheet("QPushButton{color:white;background-color:blue;}QPushButton:hover{background-color: #5f99ef;}")
                    self.classroom_button.clicked.connect(self.handle_classroom_button_click)
                    self.tableWidget.setCellWidget(i,4,self.classroom_button)
                else:
                    self.tableWidget.setItem(i,3,QTableWidgetItem(subject.classroom.name))

    

    # @pyqtSlot()
    def handle_teacher_button_click(self):
        print("Clicked")
        button = self.sender()
        subject = self.subjectList[int(button.objectName())]

        print(subject.name)

        

    def handle_classroom_button_click(self):
        pass
