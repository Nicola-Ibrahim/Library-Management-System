

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFrame, QHBoxLayout, QLabel, QLineEdit,QVBoxLayout


class CustomEmployeeFrame(QFrame):

    def __init__(self, parent):
        super().__init__(parent=parent)

        self.employee_detail_frame = QFrame(self.employees_frame)
        self.employee_detail_frame.setMinimumSize(QSize(500, 300))
        self.employee_detail_frame.setMaximumSize(QSize(500, 16777215))
        self.employee_detail_frame.setStyleSheet("#employee_detail_frame{\n"
"    border-radius:10px;\n"
"    background: rgb(244, 154, 32);\n"
"\n"
"}")
        self.employee_detail_frame.setFrameShape(QFrame.StyledPanel)
        self.employee_detail_frame.setFrameShadow(QFrame.Raised)
        self.employee_detail_frame.setObjectName("employee_detail_frame")
        self.horizontalLayout_27 = QHBoxLayout(self.employee_detail_frame)
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.verticalLayout_72 = QVBoxLayout()
        self.verticalLayout_72.setObjectName("verticalLayout_72")
        self.employee_image_lbl = QLabel(self.employee_detail_frame)
        self.employee_image_lbl.setMinimumSize(QSize(200, 200))
        self.employee_image_lbl.setMaximumSize(QSize(200, 200))
        self.employee_image_lbl.setStyleSheet("QLabel{\n"
"    \n"
"    border:2px solid transparent; \n"
"    border-radius: 50px;\n"
"    background-color: transparent;\n"
"\n"
"}")
        self.employee_image_lbl.setText("")
        self.employee_image_lbl.setPixmap(QPixmap("../../employees_image/unknown_male.jpg"))
        self.employee_image_lbl.setScaledContents(True)
        self.employee_image_lbl.setObjectName("employee_image_lbl")
        self.verticalLayout_72.addWidget(self.employee_image_lbl)
        self.employee_name_lbl = QLabel(self.employee_detail_frame)
        self.employee_name_lbl.setStyleSheet("color:rgb(0, 31, 98) ;")
        self.employee_name_lbl.setAlignment(Qt.AlignCenter)
        self.employee_name_lbl.setObjectName("employee_name_lbl")
        self.verticalLayout_72.addWidget(self.employee_name_lbl)
        self.employee_job_type_lbl = QLabel(self.employee_detail_frame)
        self.employee_job_type_lbl.setStyleSheet("color:rgb(0, 31, 98) ;")
        self.employee_job_type_lbl.setAlignment(Qt.AlignCenter)
        self.employee_job_type_lbl.setObjectName("employee_job_type_lbl")
        self.verticalLayout_72.addWidget(self.employee_job_type_lbl)
        self.horizontalLayout_27.addLayout(self.verticalLayout_72)
        self.line_4 = QFrame(self.employee_detail_frame)
        self.line_4.setStyleSheet("border:4px solid rgb(255, 255, 255);\n"
"")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.horizontalLayout_27.addWidget(self.line_4)
        self.verticalLayout_76 = QVBoxLayout()
        self.verticalLayout_76.setObjectName("verticalLayout_76")
        self.verticalLayout_73 = QVBoxLayout()
        self.verticalLayout_73.setSpacing(0)
        self.verticalLayout_73.setObjectName("verticalLayout_73")
        self.label_56 = QLabel(self.employee_detail_frame)
        self.label_56.setMinimumSize(QSize(0, 0))
        self.label_56.setMaximumSize(QSize(16777215, 40))
        self.label_56.setObjectName("label_56")
        self.verticalLayout_73.addWidget(self.label_56)
        self.employee_username_lbl = QLabel(self.employee_detail_frame)
        self.employee_username_lbl.setMinimumSize(QSize(0, 0))
        self.employee_username_lbl.setMaximumSize(QSize(16777215, 40))
        self.employee_username_lbl.setObjectName("employee_username_lbl")
        self.verticalLayout_73.addWidget(self.employee_username_lbl)
        self.verticalLayout_76.addLayout(self.verticalLayout_73)
        self.verticalLayout_74 = QVBoxLayout()
        self.verticalLayout_74.setSpacing(0)
        self.verticalLayout_74.setObjectName("verticalLayout_74")
        self.label_65 = QLabel(self.employee_detail_frame)
        self.label_65.setMinimumSize(QSize(0, 0))
        self.label_65.setMaximumSize(QSize(16777215, 40))
        self.label_65.setObjectName("label_65")
        self.verticalLayout_74.addWidget(self.label_65)
        self.employee_password_lbl = QLineEdit(self.employee_detail_frame)
        self.employee_password_lbl.setMinimumSize(QSize(0, 0))
        self.employee_password_lbl.setMaximumSize(QSize(16777215, 40))
        self.employee_password_lbl.setStyleSheet("background:transparent;\n"
"border: none;\n"
"color: rgb(255, 255, 255);\n"
"")
        self.employee_password_lbl.setEchoMode(QLineEdit.Password)
        self.employee_password_lbl.setReadOnly(True)
        self.employee_password_lbl.setObjectName("employee_password_lbl")
        self.verticalLayout_74.addWidget(self.employee_password_lbl)
        self.verticalLayout_76.addLayout(self.verticalLayout_74)
        self.verticalLayout_75 = QVBoxLayout()
        self.verticalLayout_75.setSpacing(0)
        self.verticalLayout_75.setObjectName("verticalLayout_75")
        self.label_71 = QLabel(self.employee_detail_frame)
        self.label_71.setMinimumSize(QSize(0, 0))
        self.label_71.setMaximumSize(QSize(16777215, 40))
        self.label_71.setObjectName("label_71")
        self.verticalLayout_75.addWidget(self.label_71)
        self.employee_num_workdays_lbl = QLabel(self.employee_detail_frame)
        self.employee_num_workdays_lbl.setMinimumSize(QSize(0, 0))
        self.employee_num_workdays_lbl.setMaximumSize(QSize(16777215, 40))
        self.employee_num_workdays_lbl.setObjectName("employee_num_workdays_lbl")
        self.verticalLayout_75.addWidget(self.employee_num_workdays_lbl)
        self.verticalLayout_76.addLayout(self.verticalLayout_75)
        self.horizontalLayout_27.addLayout(self.verticalLayout_76)