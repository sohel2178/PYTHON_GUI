from PyQt5.QtWidgets import (QWidget,QMainWindow,QApplication
            ,QDialog,QStackedWidget,QListWidgetItem,QTableWidgetItem,QPushButton,QVBoxLayout)
from PyQt5.QtCore import pyqtSlot,QDateTime,Qt
from PyQt5.QtGui import QPixmap
import sys
from PyQt5.uic import loadUi
import os

from schoolmanagement.schoolmodels import database,Subject,Course
from schoolmanagement.utils.utils import SubjectTableView


dir_path = os.path.dirname(os.path.realpath(__file__))
root_path = os.path.dirname(dir_path)



class SubjectMainWindow(QStackedWidget):
    def __init__(self):
        super().__init__()
        loadUi(os.path.join(dir_path,'layouts','main.ui'),self)
        self.openingWidget = self.OpeningWindow()
        self.openingWidget.btn_add_subject.clicked.connect(self.load_subject_form)
        self.addWidget(self.openingWidget)

        self.subjectForm = self.SubjectForm()
        self.subjectForm.btn_cancel.clicked.connect(self.load_opening_widget)
        self.subjectForm.btn_save.clicked.connect(self.add_subject)
        self.addWidget(self.subjectForm)
        self.part_list=['A','B','C','D']
        self.course_list = database.get_all_course()
        self.teacher_list = database.get_all_teacher()
        self.classroom_list = database.get_all_classroom()

        self.subjectForm.cbo_part.addItems(self.part_list)
        self.subjectForm.cbo_course.addItems([x.name for x in self.course_list])
        self.subjectForm.cbo_teacher.addItems([x.first_name for x in self.teacher_list])
        self.subjectForm.cbo_class_room.addItems([x.name for x in self.classroom_list])


        if len(self.course_list)==0:
            self.subjectForm.lbl_response.setText('Please Entry Some Course Befor Entry Subject')
            self.subjectForm.lbl_response.setStyleSheet("QLabel {color:red;background-color:#e9ebff}")

        


    def load_opening_widget(self):
        self.setCurrentWidget(self.openingWidget)

    def load_subject_form(self):
        self.setCurrentWidget(self.subjectForm)

    def add_subject(self):
        if len(self.subjectForm.txt_subject_name.text().strip())<=0:
            self.subjectForm.lbl_response.setText('Please Enter Subject Name')
            self.subjectForm.lbl_response.setStyleSheet("QLabel {color:red;background-color:#e9ebff}")
            self.subjectForm.txt_subject_name.setFocus()

        name = self.subjectForm.txt_subject_name.text().strip()

        
        subject = Subject(name=name,part=self.part_list[self.subjectForm.cbo_part.currentIndex()],
                    course_id=self.course_list[self.subjectForm.cbo_course.currentIndex()].id)

        try:
            subject.teacher_id = self.course_list[self.subjectForm.cbo_course.currentIndex()].id
        except:
            pass

        try:
            subject.classroom_id= self.teacher_list[self.subjectForm.cbo_teacher.currentIndex()].id
        except:
            pass

        sub,message = database.add_subject(subject)
        # Display Messages
        self.subjectForm.lbl_response.setText(message)

        if sub != None:
            self.subjectForm.txt_subject_name.setText("")
            self.subjectForm.lbl_response.setStyleSheet("QLabel {color:green;background-color:#e9ebff}")



            # Todo Here Add Subject
            self.openingWidget.table.refresh_table(database.get_all_subject())

        else:
            self.subjectForm.lbl_response.setStyleSheet("QLabel {color:red;background-color:#e9ebff}")  




    class SubjectForm(QWidget):
        def __init__(self):
            super().__init__()
            loadUi(os.path.join(dir_path,'layouts','subject_form.ui'),self)


    class OpeningWindow(QWidget):
        def __init__(self):
            super().__init__()
            loadUi(os.path.join(dir_path,'layouts','opening.ui'),self)
            self.subjectList = database.get_all_subject()

            self.table = SubjectTableView()
            self.table.refresh_table(self.subjectList)
            self.verticalLayout.addWidget(self.table)

                    
            
                    


            
       
        
        



        
    

