# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jsoncreator.ui'
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

class Ui_JsonCreator(object):
    def setupUi(self, JsonCreator):
        JsonCreator.setObjectName(_fromUtf8("JsonCreator"))
        JsonCreator.resize(719, 460)
        self.verticalLayoutWidget = QtGui.QWidget(JsonCreator)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 701, 441))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.createNewBtn = QtGui.QPushButton(self.verticalLayoutWidget)
        self.createNewBtn.setMinimumSize(QtCore.QSize(97, 60))
        self.createNewBtn.setMaximumSize(QtCore.QSize(97, 60))
        self.createNewBtn.setObjectName(_fromUtf8("createNewBtn"))
        self.horizontalLayout.addWidget(self.createNewBtn)
        self.addNewLine = QtGui.QPushButton(self.verticalLayoutWidget)
        self.addNewLine.setMinimumSize(QtCore.QSize(97, 60))
        self.addNewLine.setMaximumSize(QtCore.QSize(97, 60))
        self.addNewLine.setObjectName(_fromUtf8("addNewLine"))
        self.horizontalLayout.addWidget(self.addNewLine)
        self.loadExFileBtn = QtGui.QPushButton(self.verticalLayoutWidget)
        self.loadExFileBtn.setMinimumSize(QtCore.QSize(97, 60))
        self.loadExFileBtn.setMaximumSize(QtCore.QSize(97, 60))
        self.loadExFileBtn.setObjectName(_fromUtf8("loadExFileBtn"))
        self.horizontalLayout.addWidget(self.loadExFileBtn)
        self.saveBtn = QtGui.QPushButton(self.verticalLayoutWidget)
        self.saveBtn.setMinimumSize(QtCore.QSize(97, 60))
        self.saveBtn.setMaximumSize(QtCore.QSize(97, 60))
        self.saveBtn.setObjectName(_fromUtf8("saveBtn"))
        self.horizontalLayout.addWidget(self.saveBtn)
        self.doneBtn = QtGui.QPushButton(self.verticalLayoutWidget)
        self.doneBtn.setMinimumSize(QtCore.QSize(97, 60))
        self.doneBtn.setMaximumSize(QtCore.QSize(97, 60))
        self.doneBtn.setObjectName(_fromUtf8("doneBtn"))
        self.horizontalLayout.addWidget(self.doneBtn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.textEditFileLoad = QtGui.QTextEdit(self.verticalLayoutWidget)
        self.textEditFileLoad.setObjectName(_fromUtf8("textEditFileLoad"))
        self.verticalLayout.addWidget(self.textEditFileLoad)

        self.retranslateUi(JsonCreator)
        QtCore.QMetaObject.connectSlotsByName(JsonCreator)

    def retranslateUi(self, JsonCreator):
        JsonCreator.setWindowTitle(_translate("JsonCreator", "File Work", None))
        self.createNewBtn.setText(_translate("JsonCreator", "Create New", None))
        self.addNewLine.setText(_translate("JsonCreator", "New Test Line", None))
        self.loadExFileBtn.setText(_translate("JsonCreator", "Load File", None))
        self.saveBtn.setText(_translate("JsonCreator", "Save", None))
        self.doneBtn.setText(_translate("JsonCreator", "Done", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    JsonCreator = QtGui.QDialog()
    ui = Ui_JsonCreator()
    ui.setupUi(JsonCreator)
    JsonCreator.show()
    sys.exit(app.exec_())

