from PyQt5.QtWidgets import (QWidget,QMainWindow,QApplication
            ,QDialog,QStackedWidget,QTableWidgetItem,QPushButton,QFileDialog)
from PyQt5.QtCore import pyqtSlot,QDateTime,Qt
from PyQt5.QtGui import QPixmap
import sys
from PyQt5.uic import loadUi
import os
import secrets


from schoolmanagement.schoolmodels import database,Subject,Course,Teacher
from schoolmanagement.utils.utils import SubjectTableView


dir_path = os.path.dirname(os.path.realpath(__file__))
root_path = os.path.dirname(dir_path)


class TeacherMainWindow(QStackedWidget):
    def __init__(self):
        super().__init__()
        loadUi(os.path.join(dir_path,'layouts','main.ui'),self)
        self.openingWidget = self.OpeningWindow()
        self.openingWidget.btn_add_teacher.clicked.connect(self.load_teacher_form)
        self.addWidget(self.openingWidget)

        self.teacherForm = self.TeacherForm()
        self.addWidget(self.teacherForm)


    def load_opening_widget(self):
        self.setCurrentWidget(self.openingWidget)

    def load_teacher_form(self):
        self.setCurrentWidget(self.teacherForm)

    def add_teacher(self):
        if len(self.teacherForm.txt_subject_name.text().strip())<=0:
            self.teacherForm.lbl_response.setText('Please Enter Subject Name')
            self.teacherForm.lbl_response.setStyleSheet("QLabel {color:red;background-color:#e9ebff}")
            self.teacherForm.txt_subject_name.setFocus()

        name = self.teacherForm.txt_subject_name.text().strip()

        
        subject = Subject(name=name,part=self.part_list[self.teacherForm.cbo_part.currentIndex()],
                    course_id=self.course_list[self.teacherForm.cbo_course.currentIndex()].id)

        try:
            subject.teacher_id = self.course_list[self.teacherForm.cbo_course.currentIndex()].id
        except:
            pass

        try:
            subject.classroom_id= self.teacher_list[self.teacherForm.cbo_teacher.currentIndex()].id
        except:
            pass

        sub,message = database.add_subject(subject)
        # Display Messages
        self.teacherForm.lbl_response.setText(message)

        if sub != None:
            self.teacherForm.txt_subject_name.setText("")
            self.teacherForm.lbl_response.setStyleSheet("QLabel {color:green;background-color:#e9ebff}")

            # Todo Here Add Subject

        else:
            self.teacherForm.lbl_response.setStyleSheet("QLabel {color:red;background-color:#e9ebff}")  




    class TeacherForm(QWidget):
        def __init__(self):
            super().__init__()
            loadUi(os.path.join(dir_path,'layouts','teacher_form.ui'),self)

            self.btn_cancel.clicked.connect(self.cancel_clicked)
            self.btn_save.clicked.connect(self.save_teacher)

            self.btn_select_image.clicked.connect(self.select_image)
            

            # self.btn_cancel.clicked.connec()

        def save_teacher(self):

            # Add Some validation
            if len(self.txt_first_name.text().strip())<=0:
                self.lbl_response.setText('Please Enter First Name')
                self.lbl_response.setStyleSheet("QLabel {color:red;background-color:#e9ebff}")
                self.txt_first_name.setFocus()
                return

            if len(self.txt_last_name.text().strip())<=0:
                self.lbl_response.setText('Please Enter Last Name')
                self.lbl_response.setStyleSheet("QLabel {color:red;background-color:#e9ebff}")
                self.txt_last_name.setFocus()
                return

            if len(self.txt_email.text().strip())<=0:
                self.lbl_response.setText('Please Enter Email')
                self.lbl_response.setStyleSheet("QLabel {color:red;background-color:#e9ebff}")
                self.txt_email.setFocus()
                return

            if len(self.txt_cell_phone.text().strip())<=0:
                self.lbl_response.setText('Please Enter Cell Phone')
                self.lbl_response.setStyleSheet("QLabel {color:red;background-color:#e9ebff}")
                self.txt_cell_phone.setFocus()
                return

            if len(self.txt_nid.text().strip())<=0:
                self.lbl_response.setText('Please Enter NID')
                self.lbl_response.setStyleSheet("QLabel {color:red;background-color:#e9ebff}")
                self.txt_nid.setFocus()
                return

            if self.lbl_image.pixmap() == None:
                self.lbl_response.setText('Please Select an Image')
                self.lbl_response.setStyleSheet("QLabel {color:red;background-color:#e9ebff}")
                self.btn_select_image.setFocus()
                return

            random_hex = secrets.token_hex(8)
            pic_name = random_hex+".png"
            file_name = os.path.join(dir_path,'images',pic_name)

            self.lbl_image.pixmap().save(file_name)

            fName = self.txt_first_name.text()
            lName = self.txt_last_name.text()
            email = self.txt_email.text()
            cell_phone = self.txt_cell_phone.text()
            nid = self.txt_nid.text()

            teacher = Teacher(first_name=fName,last_name=lName,
                email = email,passport_number=nid,cell_phone=cell_phone,image=file_name)

            teac,message = database.add_teacher(teacher)

            # Display Messages
            self.lbl_response.setText(message)

            if teac != None:
                self.txt_first_name.setText("")
                self.txt_last_name.setText("")
                self.txt_email.setText("")
                self.txt_cell_phone.setText("")
                self.txt_nid.setText("")
                self.lbl_image.clear()
                self.lbl_response.setStyleSheet("QLabel {color:green;background-color:#e9ebff}")



                # Todo Here Add Subject
                # self.openingWidget.table.refresh_table(database.get_all_subject())

            else:
                self.lbl_response.setStyleSheet("QLabel {color:red;background-color:#e9ebff}")
                

            
            
            # self.imScale.save(os.path.join(dir_path,'images','1.png'))
            # self.imScale=None

        def cancel_clicked(self):
            self.parent().load_opening_widget()
            

        def select_image(self):
            print("Works")
            # options = QFileDialog.options()

            # name = QFileDialog.getOpenFileName(self,'Open File')
            # file = open(name,'r')
            fname,_ = QFileDialog.getOpenFileName(self, 'Open file', os.path.join(os.environ["HOMEPATH"], "Desktop"),"Image files (*.jpg *.gif)")

            image = QPixmap(fname)
            imScale = image.scaled(125,125)
            self.lbl_image.setPixmap(imScale)
            # self.lbl_image.setMinimumSize(1,1)
            


    class OpeningWindow(QWidget):
        def __init__(self):
            super().__init__()
            loadUi(os.path.join(dir_path,'layouts','opening.ui'),self)
            self.teacherList = database.get_all_teacher()

            # self.table = SubjectTableView()
            # self.table.refresh_table(self.subjectList)
            # self.verticalLayout.addWidget(self.table)
