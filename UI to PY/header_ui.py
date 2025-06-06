# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'header.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(811, 480)
        Form.setMinimumSize(QtCore.QSize(811, 480))
        Form.setMaximumSize(QtCore.QSize(811, 480))
        Form.setStyleSheet("QWidget {\n"
"    background-color: #f0faff\n"
"\n"
";  /* 부드러운 에그쉘 색 */\n"
"}")
        self.topbar = QtWidgets.QFrame(Form)
        self.topbar.setGeometry(QtCore.QRect(0, 0, 811, 81))
        self.topbar.setStyleSheet("QFrame {\n"
"    background-color: #fefbf6; /* 전체 배경과 통일감 있게 */\n"
"    border: 2px solid #e0e0e0; /* 아주 연한 회색 테두리 */\n"
"    border-radius: 12px;        /* 살짝 둥근 모서리 */\n"
"    padding: 6px;\n"
"}")
        self.topbar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.topbar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.topbar.setObjectName("topbar")
        self.btn_help = QtWidgets.QPushButton(self.topbar)
        self.btn_help.setEnabled(True)
        self.btn_help.setGeometry(QtCore.QRect(14, 20, 40, 42))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_help.sizePolicy().hasHeightForWidth())
        self.btn_help.setSizePolicy(sizePolicy)
        self.btn_help.setMinimumSize(QtCore.QSize(40, 42))
        self.btn_help.setMaximumSize(QtCore.QSize(40, 42))
        self.btn_help.setSizeIncrement(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.btn_help.setFont(font)
        self.btn_help.setStyleSheet("border: 2px solid black;\n"
"border-radius: 6px;\n"
"background-color: white;")
        self.btn_help.setObjectName("btn_help")
        self.label_current_people = QtWidgets.QLabel(self.topbar)
        self.label_current_people.setGeometry(QtCore.QRect(70, 20, 204, 42))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_current_people.sizePolicy().hasHeightForWidth())
        self.label_current_people.setSizePolicy(sizePolicy)
        self.label_current_people.setMinimumSize(QtCore.QSize(0, 42))
        font = QtGui.QFont()
        font.setFamily("GangwonEduAll OTF")
        font.setPointSize(24)
        self.label_current_people.setFont(font)
        self.label_current_people.setObjectName("label_current_people")
        self.label_date_time = QtWidgets.QLabel(self.topbar)
        self.label_date_time.setGeometry(QtCore.QRect(520, 20, 280, 42))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_date_time.sizePolicy().hasHeightForWidth())
        self.label_date_time.setSizePolicy(sizePolicy)
        self.label_date_time.setMinimumSize(QtCore.QSize(280, 42))
        self.label_date_time.setMaximumSize(QtCore.QSize(280, 16777215))
        font = QtGui.QFont()
        font.setFamily("GangwonEduAll OTF")
        font.setPointSize(24)
        self.label_date_time.setFont(font)
        self.label_date_time.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_date_time.setObjectName("label_date_time")
        self.btn_previous_page = QtWidgets.QPushButton(self.topbar)
        self.btn_previous_page.setEnabled(True)
        self.btn_previous_page.setGeometry(QtCore.QRect(430, 20, 70, 42))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_previous_page.sizePolicy().hasHeightForWidth())
        self.btn_previous_page.setSizePolicy(sizePolicy)
        self.btn_previous_page.setMinimumSize(QtCore.QSize(70, 42))
        self.btn_previous_page.setMaximumSize(QtCore.QSize(70, 42))
        self.btn_previous_page.setSizeIncrement(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("GangwonEduAll OTF")
        font.setPointSize(36)
        self.btn_previous_page.setFont(font)
        self.btn_previous_page.setStyleSheet("border: 2px solid black;\n"
"border-radius: 6px;\n"
"background-color: white;")
        self.btn_previous_page.setObjectName("btn_previous_page")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn_help.setText(_translate("Form", "❓"))
        self.label_current_people.setText(_translate("Form", "현재 재실 인원 : 0명"))
        self.label_date_time.setText(_translate("Form", "Fri May 16  10:06PM"))
        self.btn_previous_page.setText(_translate("Form", "↩"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
