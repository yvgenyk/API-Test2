# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings_design.ui'
#
# Created: Tue Jul  5 23:58:00 2016
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
        Form.resize(380, 450)
        Form.setMinimumSize(QtCore.QSize(380, 450))
        Form.setMaximumSize(QtCore.QSize(380, 450))
        Form.setStyleSheet(_fromUtf8("background: rgb(128,128, 128)"))
        Form.setWindowFilePath(_fromUtf8(""))
        self.verticalLayoutWidget = QtGui.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 384, 445))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(60, 30))
        self.label.setMaximumSize(QtCore.QSize(60, 30))
        self.label.setStyleSheet(_fromUtf8("background:rgb(204,204,204);\n"
"border-radius: 5px;"))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.secretKeyLine = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.secretKeyLine.setMinimumSize(QtCore.QSize(305, 30))
        self.secretKeyLine.setMaximumSize(QtCore.QSize(305, 30))
        self.secretKeyLine.setStyleSheet(_fromUtf8("background:rgb(204,204,204);\n"
"border: 2px solid black;\n"
"border-radius: 5px;"))
        self.secretKeyLine.setText(_fromUtf8(""))
        self.secretKeyLine.setObjectName(_fromUtf8("secretKeyLine"))
        self.horizontalLayout.addWidget(self.secretKeyLine)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(60, 30))
        self.label_2.setMaximumSize(QtCore.QSize(60, 30))
        self.label_2.setStyleSheet(_fromUtf8("background:rgb(204,204,204);\n"
"border-radius: 5px;"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.publicKeyLine = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.publicKeyLine.setMinimumSize(QtCore.QSize(305, 30))
        self.publicKeyLine.setMaximumSize(QtCore.QSize(305, 30))
        self.publicKeyLine.setStyleSheet(_fromUtf8("background:rgb(204,204,204);\n"
"border: 2px solid black;\n"
"border-radius: 5px;"))
        self.publicKeyLine.setObjectName(_fromUtf8("publicKeyLine"))
        self.horizontalLayout_2.addWidget(self.publicKeyLine)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_3 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_3.setMinimumSize(QtCore.QSize(60, 30))
        self.label_3.setMaximumSize(QtCore.QSize(60, 30))
        self.label_3.setStyleSheet(_fromUtf8("background:rgb(204,204,204);\n"
"border-radius: 5px;"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.httpLine = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.httpLine.setMinimumSize(QtCore.QSize(305, 30))
        self.httpLine.setMaximumSize(QtCore.QSize(305, 30))
        self.httpLine.setStyleSheet(_fromUtf8("background:rgb(204,204,204);\n"
"border: 2px solid black;\n"
"border-radius: 5px;"))
        self.httpLine.setObjectName(_fromUtf8("httpLine"))
        self.horizontalLayout_3.addWidget(self.httpLine)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_9 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_9.setMinimumSize(QtCore.QSize(60, 30))
        self.label_9.setMaximumSize(QtCore.QSize(60, 30))
        self.label_9.setStyleSheet(_fromUtf8("background:rgb(204,204,204);\n"
"border-radius: 5px;"))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_8.addWidget(self.label_9)
        self.user_id = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.user_id.setMinimumSize(QtCore.QSize(305, 30))
        self.user_id.setMaximumSize(QtCore.QSize(305, 30))
        self.user_id.setStyleSheet(_fromUtf8("background:rgb(204,204,204);\n"
"border: 2px solid black;\n"
"border-radius: 5px;"))
        self.user_id.setObjectName(_fromUtf8("user_id"))
        self.horizontalLayout_8.addWidget(self.user_id)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_4 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_4.setMinimumSize(QtCore.QSize(90, 30))
        self.label_4.setMaximumSize(QtCore.QSize(90, 30))
        self.label_4.setStyleSheet(_fromUtf8("background:rgb(204,204,204);\n"
"border-radius: 5px;"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_5.addWidget(self.label_4)
        self.label_5 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_5.setMinimumSize(QtCore.QSize(90, 30))
        self.label_5.setMaximumSize(QtCore.QSize(90, 30))
        self.label_5.setStyleSheet(_fromUtf8("background:rgb(204,204,204);\n"
"border-radius: 5px;"))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_5.addWidget(self.label_5)
        self.label_6 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_6.setMinimumSize(QtCore.QSize(90, 30))
        self.label_6.setMaximumSize(QtCore.QSize(90, 30))
        self.label_6.setStyleSheet(_fromUtf8("background:rgb(204,204,204);\n"
"border-radius: 5px;"))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_5.addWidget(self.label_6)
        self.horizontalLayout_6.addLayout(self.verticalLayout_5)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.reg_proj = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.reg_proj.setMinimumSize(QtCore.QSize(85, 30))
        self.reg_proj.setMaximumSize(QtCore.QSize(85, 30))
        self.reg_proj.setStyleSheet(_fromUtf8("background:rgb(204,204,204);\n"
"border: 2px solid black;\n"
"border-radius: 5px;"))
        self.reg_proj.setObjectName(_fromUtf8("reg_proj"))
        self.verticalLayout_4.addWidget(self.reg_proj)
        self.expert_proj = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.expert_proj.setMinimumSize(QtCore.QSize(85, 30))
        self.expert_proj.setMaximumSize(QtCore.QSize(85, 30))
        self.expert_proj.setStyleSheet(_fromUtf8("background:rgb(204,204,204);\n"
"border: 2px solid black;\n"
"border-radius: 5px;"))
        self.expert_proj.setObjectName(_fromUtf8("expert_proj"))
        self.verticalLayout_4.addWidget(self.expert_proj)
        self.proof_proj = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.proof_proj.setMinimumSize(QtCore.QSize(85, 30))
        self.proof_proj.setMaximumSize(QtCore.QSize(85, 30))
        self.proof_proj.setStyleSheet(_fromUtf8("background:rgb(204,204,204);\n"
"border: 2px solid black;\n"
"border-radius: 5px;"))
        self.proof_proj.setObjectName(_fromUtf8("proof_proj"))
        self.verticalLayout_4.addWidget(self.proof_proj)
        self.horizontalLayout_6.addLayout(self.verticalLayout_4)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.label_8 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_8.setMinimumSize(QtCore.QSize(90, 30))
        self.label_8.setMaximumSize(QtCore.QSize(90, 30))
        self.label_8.setStyleSheet(_fromUtf8("background:rgb(204,204,204);\n"
"border-radius: 5px;"))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout_7.addWidget(self.label_8)
        self.label_7 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_7.setMinimumSize(QtCore.QSize(90, 30))
        self.label_7.setMaximumSize(QtCore.QSize(90, 30))
        self.label_7.setStyleSheet(_fromUtf8("background:rgb(204,204,204);\n"
"border-radius: 5px;"))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout_7.addWidget(self.label_7)
        spacerItem = QtGui.QSpacerItem(20, 30, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_7.addItem(spacerItem)
        self.horizontalLayout_12.addLayout(self.verticalLayout_7)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.combo_proj = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.combo_proj.setMinimumSize(QtCore.QSize(85, 30))
        self.combo_proj.setMaximumSize(QtCore.QSize(85, 30))
        self.combo_proj.setStyleSheet(_fromUtf8("background:rgb(204,204,204);\n"
"border: 2px solid black;\n"
"border-radius: 5px;"))
        self.combo_proj.setObjectName(_fromUtf8("combo_proj"))
        self.verticalLayout_6.addWidget(self.combo_proj)
        self.transcript_proj = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.transcript_proj.setMinimumSize(QtCore.QSize(85, 30))
        self.transcript_proj.setMaximumSize(QtCore.QSize(85, 30))
        self.transcript_proj.setStyleSheet(_fromUtf8("background:rgb(204,204,204);\n"
"border: 2px solid black;\n"
"border-radius: 5px;"))
        self.transcript_proj.setObjectName(_fromUtf8("transcript_proj"))
        self.verticalLayout_6.addWidget(self.transcript_proj)
        spacerItem1 = QtGui.QSpacerItem(20, 30, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_6.addItem(spacerItem1)
        self.horizontalLayout_12.addLayout(self.verticalLayout_6)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_12)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.loadTxtBtn = QtGui.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loadTxtBtn.sizePolicy().hasHeightForWidth())
        self.loadTxtBtn.setSizePolicy(sizePolicy)
        self.loadTxtBtn.setMinimumSize(QtCore.QSize(144, 30))
        self.loadTxtBtn.setMaximumSize(QtCore.QSize(144, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.loadTxtBtn.setFont(font)
        self.loadTxtBtn.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.loadTxtBtn.setStyleSheet(_fromUtf8("background:rgb(80,80,80);\n"
"color: rgb(204,204,204);\n"
""))
        self.loadTxtBtn.setObjectName(_fromUtf8("loadTxtBtn"))
        self.horizontalLayout_11.addWidget(self.loadTxtBtn)
        self.delTextFile = QtGui.QPushButton(self.verticalLayoutWidget)
        self.delTextFile.setMinimumSize(QtCore.QSize(30, 30))
        self.delTextFile.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.delTextFile.setFont(font)
        self.delTextFile.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.delTextFile.setStyleSheet(_fromUtf8("background:rgb(77, 0, 0);color: rgb(204,204,204);"))
        self.delTextFile.setObjectName(_fromUtf8("delTextFile"))
        self.horizontalLayout_11.addWidget(self.delTextFile)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        self.txtFilesList = QtGui.QListWidget(self.verticalLayoutWidget)
        self.txtFilesList.setEnabled(True)
        self.txtFilesList.setMinimumSize(QtCore.QSize(180, 100))
        self.txtFilesList.setMaximumSize(QtCore.QSize(180, 100))
        self.txtFilesList.setStyleSheet(_fromUtf8("background:rgb(204,204,204);\n"
"border: 2px solid black;\n"
"border-radius: 5px;"))
        self.txtFilesList.setObjectName(_fromUtf8("txtFilesList"))
        self.verticalLayout_2.addWidget(self.txtFilesList)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.loadFileBtn = QtGui.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loadFileBtn.sizePolicy().hasHeightForWidth())
        self.loadFileBtn.setSizePolicy(sizePolicy)
        self.loadFileBtn.setMinimumSize(QtCore.QSize(144, 30))
        self.loadFileBtn.setMaximumSize(QtCore.QSize(144, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.loadFileBtn.setFont(font)
        self.loadFileBtn.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.loadFileBtn.setStyleSheet(_fromUtf8("background:rgb(80,80,80);\n"
"color: rgb(204,204,204);"))
        self.loadFileBtn.setObjectName(_fromUtf8("loadFileBtn"))
        self.horizontalLayout_13.addWidget(self.loadFileBtn)
        self.delFile = QtGui.QPushButton(self.verticalLayoutWidget)
        self.delFile.setMinimumSize(QtCore.QSize(30, 30))
        self.delFile.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.delFile.setFont(font)
        self.delFile.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.delFile.setAutoFillBackground(False)
        self.delFile.setStyleSheet(_fromUtf8("background:rgb(77, 0, 0);color: rgb(204,204,204);"))
        self.delFile.setObjectName(_fromUtf8("delFile"))
        self.horizontalLayout_13.addWidget(self.delFile)
        self.verticalLayout_3.addLayout(self.horizontalLayout_13)
        self.testFilesList = QtGui.QListWidget(self.verticalLayoutWidget)
        self.testFilesList.setMinimumSize(QtCore.QSize(180, 100))
        self.testFilesList.setMaximumSize(QtCore.QSize(180, 100))
        self.testFilesList.setStyleSheet(_fromUtf8("background:rgb(204,204,204);\n"
"border: 2px solid black;\n"
"border-radius: 5px;"))
        self.testFilesList.setObjectName(_fromUtf8("testFilesList"))
        self.verticalLayout_3.addWidget(self.testFilesList)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.saveBtn = QtGui.QPushButton(self.verticalLayoutWidget)
        self.saveBtn.setMinimumSize(QtCore.QSize(180, 30))
        self.saveBtn.setMaximumSize(QtCore.QSize(180, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.saveBtn.setFont(font)
        self.saveBtn.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.saveBtn.setStyleSheet(_fromUtf8("background:rgb(80,80,80);\n"
"color: rgb(204,204,204);"))
        self.saveBtn.setObjectName(_fromUtf8("saveBtn"))
        self.horizontalLayout_5.addWidget(self.saveBtn)
        self.closeBtn = QtGui.QPushButton(self.verticalLayoutWidget)
        self.closeBtn.setMinimumSize(QtCore.QSize(180, 30))
        self.closeBtn.setMaximumSize(QtCore.QSize(180, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.closeBtn.setFont(font)
        self.closeBtn.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.closeBtn.setStyleSheet(_fromUtf8("background:rgb(80,80,80);\n"
"color: rgb(204,204,204);"))
        self.closeBtn.setObjectName(_fromUtf8("closeBtn"))
        self.horizontalLayout_5.addWidget(self.closeBtn)
        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Settings", None))
        self.label.setText(_translate("Form", " Secret Key", None))
        self.label_2.setText(_translate("Form", " Public Key ", None))
        self.label_3.setText(_translate("Form", " http:     ", None))
        self.label_9.setText(_translate("Form", "User ID:", None))
        self.label_4.setText(_translate("Form", " Regular Project", None))
        self.label_5.setText(_translate("Form", " Expert Project", None))
        self.label_6.setText(_translate("Form", " Proofreading", None))
        self.label_8.setText(_translate("Form", " Combo Project", None))
        self.label_7.setText(_translate("Form", " Transcription", None))
        self.loadTxtBtn.setText(_translate("Form", "Load Text Files", None))
        self.delTextFile.setText(_translate("Form", "X", None))
        self.loadFileBtn.setText(_translate("Form", "Load Files", None))
        self.delFile.setText(_translate("Form", "X", None))
        self.saveBtn.setText(_translate("Form", "Save", None))
        self.closeBtn.setText(_translate("Form", "Close", None))

