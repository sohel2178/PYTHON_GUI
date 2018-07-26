from PyQt5.QtWidgets import (QWidget,QMainWindow,QApplication,QDialog,QStackedWidget,QListWidgetItem)
from PyQt5.QtCore import pyqtSlot,QDateTime,Qt
from PyQt5.QtGui import QPixmap
import sys
from PyQt5.uic import loadUi
import os

from schoolmanagement.schoolmodels import database,Student