# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_report_design.ui'
#
# Created: Mon Jun 20 10:31:44 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(1133, 737)
        self.tableWidget = QtGui.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 491, 721))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tableWidget.setFont(font)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayoutWidget = QtGui.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(510, 10, 621, 721))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(105, 0))
        self.label.setMaximumSize(QtCore.QSize(105, 16777215))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.urlLable = QtGui.QLabel(self.verticalLayoutWidget)
        self.urlLable.setMinimumSize(QtCore.QSize(500, 0))
        self.urlLable.setMaximumSize(QtCore.QSize(500, 16777215))
        self.urlLable.setAutoFillBackground(False)
        self.urlLable.setStyleSheet(_fromUtf8("background-color: rgb(204, 204, 204)"))
        self.urlLable.setText(_fromUtf8(""))
        self.urlLable.setObjectName(_fromUtf8("urlLable"))
        self.horizontalLayout.addWidget(self.urlLable)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_3.setMinimumSize(QtCore.QSize(105, 0))
        self.label_3.setMaximumSize(QtCore.QSize(105, 16777215))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.payloadLable = QtGui.QLabel(self.verticalLayoutWidget)
        self.payloadLable.setMinimumSize(QtCore.QSize(500, 0))
        self.payloadLable.setMaximumSize(QtCore.QSize(500, 16777215))
        self.payloadLable.setStyleSheet(_fromUtf8("background-color: rgb(204, 204, 204)"))
        self.payloadLable.setText(_fromUtf8(""))
        self.payloadLable.setObjectName(_fromUtf8("payloadLable"))
        self.horizontalLayout_2.addWidget(self.payloadLable)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_7 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_7.setMinimumSize(QtCore.QSize(105, 0))
        self.label_7.setMaximumSize(QtCore.QSize(105, 16777215))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_4.addWidget(self.label_7)
        self.fileLoadLable = QtGui.QLabel(self.verticalLayoutWidget)
        self.fileLoadLable.setMinimumSize(QtCore.QSize(500, 0))
        self.fileLoadLable.setMaximumSize(QtCore.QSize(500, 16777215))
        self.fileLoadLable.setStyleSheet(_fromUtf8("background-color: rgb(204, 204, 204)"))
        self.fileLoadLable.setText(_fromUtf8(""))
        self.fileLoadLable.setObjectName(_fromUtf8("fileLoadLable"))
        self.horizontalLayout_4.addWidget(self.fileLoadLable)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_5 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_5.setMinimumSize(QtCore.QSize(105, 0))
        self.label_5.setMaximumSize(QtCore.QSize(105, 16777215))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_3.addWidget(self.label_5)
        self.responseLable = QtGui.QLabel(self.verticalLayoutWidget)
        self.responseLable.setMinimumSize(QtCore.QSize(500, 0))
        self.responseLable.setMaximumSize(QtCore.QSize(500, 16777215))
        self.responseLable.setStyleSheet(_fromUtf8("background-color: rgb(204, 204, 204)"))
        self.responseLable.setText(_fromUtf8(""))
        self.responseLable.setObjectName(_fromUtf8("responseLable"))
        self.horizontalLayout_3.addWidget(self.responseLable)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "URL:", None))
        self.label_3.setText(_translate("Form", "PayLoad:", None))
        self.label_7.setText(_translate("Form", "FileLoad:", None))
        self.label_5.setText(_translate("Form", "Response:", None))

