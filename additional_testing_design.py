# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'additional_testing_design.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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
        Form.resize(415, 180)
        Form.setMinimumSize(QtCore.QSize(415, 180))
        Form.setMaximumSize(QtCore.QSize(415, 180))
        self.verticalLayoutWidget = QtGui.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 410, 179))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_5 = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout.addWidget(self.label_5)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(200, 30))
        self.label.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.reg_proj = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.reg_proj.setMinimumSize(QtCore.QSize(200, 30))
        self.reg_proj.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.reg_proj.setFont(font)
        self.reg_proj.setObjectName(_fromUtf8("reg_proj"))
        self.horizontalLayout.addWidget(self.reg_proj)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(200, 30))
        self.label_2.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.proof_one = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.proof_one.setMinimumSize(QtCore.QSize(200, 30))
        self.proof_one.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.proof_one.setFont(font)
        self.proof_one.setObjectName(_fromUtf8("proof_one"))
        self.horizontalLayout_2.addWidget(self.proof_one)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_3 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_3.setMinimumSize(QtCore.QSize(200, 30))
        self.label_3.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.proof_two = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.proof_two.setMinimumSize(QtCore.QSize(200, 30))
        self.proof_two.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.proof_two.setFont(font)
        self.proof_two.setObjectName(_fromUtf8("proof_two"))
        self.horizontalLayout_3.addWidget(self.proof_two)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_4 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_4.setMinimumSize(QtCore.QSize(200, 30))
        self.label_4.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_4.addWidget(self.label_4)
        self.transcript = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.transcript.setMinimumSize(QtCore.QSize(200, 30))
        self.transcript.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.transcript.setFont(font)
        self.transcript.setObjectName(_fromUtf8("transcript"))
        self.horizontalLayout_4.addWidget(self.transcript)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayoutWidget.raise_()
        self.proof_two.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Additional Testing", None))
        self.label_5.setText(_translate("Form", "             Projects for additional tests", None))
        self.label.setText(_translate("Form", "Regular:", None))
        self.label_2.setText(_translate("Form", "Proofreading (Source):", None))
        self.label_3.setText(_translate("Form", "Proofreading (Source + Target):", None))
        self.label_4.setText(_translate("Form", "Transcription:", None))

