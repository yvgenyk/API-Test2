# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_design.ui'
#
# Created: Sat Jul  2 15:31:17 2016
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(915, 645)
        Dialog.setMinimumSize(QtCore.QSize(915, 645))
        Dialog.setMaximumSize(QtCore.QSize(915, 645))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("logo.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet(_fromUtf8("background: rgb(128,128, 128)"))
        self.horizontalLayoutWidget_2 = QtGui.QWidget(Dialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 0, 901, 641))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_5.setMargin(0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.tableWidget = QtGui.QTableWidget(self.horizontalLayoutWidget_2)
        self.tableWidget.setMinimumSize(QtCore.QSize(500, 635))
        self.tableWidget.setMaximumSize(QtCore.QSize(500, 635))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet(_fromUtf8("background:rgb(204,204,204);\n"
"border: 1px solid black;\n"
""))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.horizontalLayout_5.addWidget(self.tableWidget)
        self.line = QtGui.QFrame(self.horizontalLayoutWidget_2)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout_5.addWidget(self.line)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setContentsMargins(0, -1, -1, -1)
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
        self.pushButton_2.setStyleSheet(_fromUtf8("background:rgb(80,80,80);\n"
"color: rgb(204,204,204);"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout_10.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.progressBar = QtGui.QProgressBar(self.horizontalLayoutWidget_2)
        self.progressBar.setMinimumSize(QtCore.QSize(375, 40))
        self.progressBar.setMaximumSize(QtCore.QSize(375, 40))
        self.progressBar.setStyleSheet(_fromUtf8("background:rgb(204,204,204);"))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout.addWidget(self.progressBar)
        self.horizontalLayout_5.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "API Test", None))
        self.settingsBtn.setText(_translate("Dialog", "Settings", None))
        self.checkDisplay.setText(_translate("Dialog", "Whole check display", None))
        self.fileLoad.setText(_translate("Dialog", "Load Test File", None))
        self.startBtn.setText(_translate("Dialog", "Start Test", None))
        self.stopBtn.setText(_translate("Dialog", "Stop Test", None))
        self.reportBtn.setText(_translate("Dialog", "See Report", None))
        self.pushButton_2.setText(_translate("Dialog", "Quit", None))

