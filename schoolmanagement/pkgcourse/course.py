from PyQt5.QtWidgets import (QWidget,QMainWindow,QApplication,QDialog,QStackedWidget,QListWidgetItem,
        QPushButton,QTableWidgetItem)
from PyQt5.QtCore import pyqtSlot,QDateTime,Qt
from PyQt5.QtGui import QPixmap
import sys
from PyQt5.uic import loadUi
import os

from schoolmanagement.schoolmodels import database,Course




dir_path = os.path.dirname(os.path.realpath(__file__))
root_path = os.path.dirname(dir_path)





class CourseForm(QDialog):
    def __init__(self):
        super().__init__()
        loadUi(os.path.join(dir_path,'layouts','course_form.ui'),self)
        self.btn_save.clicked.connect(self.accept)
        self.btn_cancel.clicked.connect(self.reject)

    @staticmethod
    def get_course_name():
        dialog = CourseForm()
        result = dialog.exec_()
        
        if result == QDialog.Accepted:
            name = dialog.le_course_name.text()
            return name


class CourseMainWindow(QStackedWidget):
    def __init__(self):
        super().__init__()
        loadUi(os.path.join(dir_path,'layouts','main.ui'),self)

        self.openingWindow = self.OpeningWindow()
        self.addWidget(self.openingWindow)
        self.openingWindow.btn_add_course.clicked.connect(self.open_course_form)

        for x in database.get_all_course():
            # print(x.subjects)
            item = self.openingWindow.Item(x)
            self.add_item(item)

        self.detailWindow = self.DetailWindow()
        self.addWidget(self.detailWindow)
        self.detailWindow.btn_back.clicked.connect(self.load_opening_window)

        self.load_opening_window()
        

    def load_opening_window(self):
        self.setCurrentWidget(self.openingWindow)

    def load_detail_window(self):
        self.setCurrentWidget(self.detailWindow)


    def add_item(self,item):
            myQListWidgetItem = QListWidgetItem(self.openingWindow.listWidget)
            # Set size hint
            myQListWidgetItem.setSizeHint(item.size())

            self.openingWindow.listWidget.addItem(myQListWidgetItem)
            self.openingWindow.listWidget.setItemWidget(myQListWidgetItem, item)


    def open_course_form(self):
        name = CourseForm.get_course_name()

        if name != None:
            name = name.strip()

        if name != None and len(name)>4:
            course = Course(name=name)
        # database.add_course(course)
        # self.listWidget.addItem(course.name)

            if database.add_course(course):
                course = database.get_course_by_name(course.name)
                item = self.openingWindow.Item(course)
                self.add_item(item)

    
    class OpeningWindow(QWidget):
        def __init__(self):
            super().__init__()
            loadUi(os.path.join(dir_path,'layouts','opening.ui'),self)
            

        class Item(QWidget):
            def __init__(self,course):
                super().__init__()
                self.course = course
                loadUi(os.path.join(dir_path,'layouts','item.ui'),self)

                self.lbl_name.setText(course.name)
                self.btn_view.clicked.connect(self.view_clicked)

                self.lbl_image.setPixmap(QPixmap(os.path.join(root_path,'icons','classroom.png')))

                self.lbl_students.setText(f'({len(course.students)}) nos')
                self.lbl_subjects.setText(f'({len(course.subjects)}) nos')

            def view_clicked(self):
                print()
                self.parent().parent().parent().parent().detailWindow.init_course(self.course)
                self.parent().parent().parent().parent().load_detail_window()
        
    class DetailWindow(QWidget):
        def __init__(self):
            super().__init__()
            loadUi(os.path.join(dir_path,'layouts','detail.ui'),self)

            


        def refresh_table(self):
            self.subjectList = self.course.subjects
            subjectCounter = len(self.subjectList)
            colCounter =5
            headers = ['Name','Part','Course','Teacher','Class Room']
            self.tableSubject.setRowCount(subjectCounter)
            self.tableSubject.setColumnCount(colCounter)
            self.tableSubject.setHorizontalHeaderLabels(headers)



            

            for i in range(subjectCounter):
                subject = self.subjectList[i]
                self.tableSubject.setItem(i,0,QTableWidgetItem(subject.name))
                self.tableSubject.setItem(i,1,QTableWidgetItem(subject.part))
                self.tableSubject.setItem(i,2,QTableWidgetItem(subject.course.name))

                if subject.teacher == None:
                    self.teacher_button = QPushButton('Assign')
                    self.teacher_button.setStyleSheet("QPushButton{color:white;background-color:blue;}QPushButton:hover{background-color: #5f99ef;}")
                    self.teacher_button.setObjectName(str(i))
                    # self.teacher_button.clicked.connect(self.handle_teacher_button_click)
                    self.tableSubject.setCellWidget(i,3,self.teacher_button)
                else:
                    self.tableSubject.setItem(i,3,QTableWidgetItem(subject.teacher.name))

                if subject.classroom == None:
                    self.classroom_button = QPushButton('Assign')
                    self.classroom_button.setStyleSheet("QPushButton{color:white;background-color:blue;}QPushButton:hover{background-color: #5f99ef;}")
                    # self.classroom_button.clicked.connect(self.handle_classroom_button_click)
                    self.tableSubject.setCellWidget(i,4,self.classroom_button)
                else:
                    self.tableSubject.setItem(i,3,QTableWidgetItem(subject.classroom.name))


        


        def init_course(self,course):
            self.course = course
            self.lbl_course_name.setText(self.course.name)
            self.refresh_table()


    
 
