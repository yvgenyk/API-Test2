# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_design.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(910, 645)
        Dialog.setMinimumSize(QtCore.QSize(910, 645))
        Dialog.setMaximumSize(QtCore.QSize(910, 645))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("logo.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet(_fromUtf8("background: rgb(128,128, 128)"))
        self.horizontalLayoutWidget_2 = QtGui.QWidget(Dialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 901, 641))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tableWidget = QtGui.QTableWidget(self.horizontalLayoutWidget_2)
        self.tableWidget.setMinimumSize(QtCore.QSize(500, 540))
        self.tableWidget.setMaximumSize(QtCore.QSize(500, 540))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet(_fromUtf8("background:rgb(204,204,204);\n"
"border: 1px solid black;\n"
""))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout_2.addWidget(self.tableWidget)
        spacerItem = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.label = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.label.setMinimumSize(QtCore.QSize(500, 20))
        self.label.setMaximumSize(QtCore.QSize(500, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("background:rgb(255, 224, 102);\n"
"border: 1px solid black;"))
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setMinimumSize(QtCore.QSize(500, 30))
        self.label_2.setMaximumSize(QtCore.QSize(500, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(_fromUtf8("background:rgb(255, 153, 153);\n"
"border: 1px solid black;"))
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.label_3.setMinimumSize(QtCore.QSize(500, 20))
        self.label_3.setMaximumSize(QtCore.QSize(500, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(_fromUtf8("background:rgb(221, 255, 204);\n"
"border: 1px solid black;"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_2.addWidget(self.label_3)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.line = QtGui.QFrame(self.horizontalLayoutWidget_2)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout_5.addWidget(self.line)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.errorNumber = QtGui.QLCDNumber(self.horizontalLayoutWidget_2)
        self.errorNumber.setMinimumSize(QtCore.QSize(375, 130))
        self.errorNumber.setMaximumSize(QtCore.QSize(375, 130))
        self.errorNumber.setStyleSheet(_fromUtf8("color:rgb(77, 0, 0);"))
        self.errorNumber.setObjectName(_fromUtf8("errorNumber"))
        self.verticalLayout.addWidget(self.errorNumber)
        self.settingsBtn = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.settingsBtn.setMinimumSize(QtCore.QSize(375, 60))
        self.settingsBtn.setMaximumSize(QtCore.QSize(375, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.settingsBtn.setFont(font)
        self.settingsBtn.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.settingsBtn.setToolTip(_fromUtf8(""))
        self.settingsBtn.setStyleSheet(_fromUtf8("background:rgb(80,80,80);\n"
"color: rgb(204,204,204);"))
        self.settingsBtn.setObjectName(_fromUtf8("settingsBtn"))
        self.verticalLayout.addWidget(self.settingsBtn)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.checkDisplay = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.checkDisplay.setMinimumSize(QtCore.QSize(180, 60))
        self.checkDisplay.setMaximumSize(QtCore.QSize(180, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkDisplay.setFont(font)
        self.checkDisplay.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.checkDisplay.setStyleSheet(_fromUtf8("background:rgb(80,80,80);\n"
"color: rgb(204,204,204);"))
        self.checkDisplay.setObjectName(_fromUtf8("checkDisplay"))
        self.horizontalLayout_8.addWidget(self.checkDisplay)
        self.fileLoad = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.fileLoad.setMinimumSize(QtCore.QSize(180, 60))
        self.fileLoad.setMaximumSize(QtCore.QSize(180, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.fileLoad.setFont(font)
        self.fileLoad.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.fileLoad.setStyleSheet(_fromUtf8("background:rgb(80,80,80);\n"
"color: rgb(204,204,204);"))
        self.fileLoad.setObjectName(_fromUtf8("fileLoad"))
        self.horizontalLayout_8.addWidget(self.fileLoad)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.startBtn = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(97)
        sizePolicy.setVerticalStretch(60)
        sizePolicy.setHeightForWidth(self.startBtn.sizePolicy().hasHeightForWidth())
        self.startBtn.setSizePolicy(sizePolicy)
        self.startBtn.setMinimumSize(QtCore.QSize(180, 60))
        self.startBtn.setMaximumSize(QtCore.QSize(180, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.startBtn.setFont(font)
        self.startBtn.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.startBtn.setStyleSheet(_fromUtf8("background:rgb(0, 51, 0);\n"
"color: rgb(204,204,204);"))
        self.startBtn.setIconSize(QtCore.QSize(24, 24))
        self.startBtn.setObjectName(_fromUtf8("startBtn"))
        self.horizontalLayout_9.addWidget(self.startBtn)
        self.stopBtn = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.stopBtn.setMinimumSize(QtCore.QSize(180, 60))
        self.stopBtn.setMaximumSize(QtCore.QSize(180, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.stopBtn.setFont(font)
        self.stopBtn.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.stopBtn.setStyleSheet(_fromUtf8("background:rgb(77, 0, 0);\n"
"color: rgb(204,204,204);"))
        self.stopBtn.setObjectName(_fromUtf8("stopBtn"))
        self.horizontalLayout_9.addWidget(self.stopBtn)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.reportBtn = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.reportBtn.setMinimumSize(QtCore.QSize(180, 60))
        self.reportBtn.setMaximumSize(QtCore.QSize(180, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.reportBtn.setFont(font)
        self.reportBtn.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.reportBtn.setStyleSheet(_fromUtf8("background:rgb(80,80,80);\n"
"color: rgb(204,204,204);"))
        self.reportBtn.setObjectName(_fromUtf8("reportBtn"))
        self.horizontalLayout_10.addWidget(self.reportBtn)
        self.pushButton_2 = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_2.setMinimumSize(QtCore.QSize(180, 60))
        self.pushButton_2.setMaximumSize(QtCore.QSize(180, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_2.setStyleSheet(_fromUtf8("background:rgb(80,80,80);\n"
"color: rgb(204,204,204);"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout_10.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.progressBar = QtGui.QProgressBar(self.horizontalLayoutWidget_2)
        self.progressBar.setMinimumSize(QtCore.QSize(375, 60))
        self.progressBar.setMaximumSize(QtCore.QSize(375, 60))
        self.progressBar.setStyleSheet(_fromUtf8("background:rgb(204,204,204);"))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout.addWidget(self.progressBar)
        self.horizontalLayout_5.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "API Test", None))
        self.label.setText(_translate("Dialog", "Line was executed properly. No values were checked or searched for.", None))
        self.label_2.setText(_translate("Dialog", "Line was executed but there was problems: response status isn\'t 200/incorrect value was found in the response.", None))
        self.label_3.setText(_translate("Dialog", "Line was executed with correct status, all values to check were found and correct.", None))
        self.settingsBtn.setText(_translate("Dialog", "Settings", None))
        self.checkDisplay.setToolTip(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#000000;\">You can check individual lines. By clicking here you can select and test individual lines one at a time.</span></p></body></html>", None))
        self.checkDisplay.setText(_translate("Dialog", "Whole Check Display", None))
        self.fileLoad.setToolTip(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#000000;\">To add new test lines click here.</span></p></body></html>", None))
        self.fileLoad.setText(_translate("Dialog", "Add New Line", None))
        self.startBtn.setText(_translate("Dialog", "Start Test", None))
        self.stopBtn.setText(_translate("Dialog", "Stop Test", None))
        self.reportBtn.setToolTip(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;color:black\">Click here to see the report after the test is finished.</span></p></body></html>", None))
        self.reportBtn.setText(_translate("Dialog", "See Report", None))
        self.pushButton_2.setText(_translate("Dialog", "Quit", None))

