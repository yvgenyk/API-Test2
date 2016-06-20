from PyQt4 import QtGui, QtCore
import sys
import main_design
import json_creator_design
import new_line_design
import requests
import re
import os
import shutil
import json
import time
from jason_creator import JsonCreator
from check_code import CheckCode
from report_window import ViewReport
from class_test import Response, GetMethod, PostMethod
from resource_class import Resource
from doctest import testfile
#from idlelib.ClassBrowser import file_open
from PyQt4.Qt import QListWidgetItem
from PyQt4.QtCore import QThread, SIGNAL

class LineExec(QThread):

    def __init__(self, mainJson):
        QThread.__init__(self)
        self.mainJson = mainJson

    def run(self):
        for line in self.mainJson:
            self.emit(SIGNAL("line_exec(PyQt_PyObject)"), line)
            self.sleep(1)


class TestApp(QtGui.QMainWindow, main_design.Ui_Dialog):
    def __init__(self, parent=None):
        super(TestApp, self).__init__(parent)
        self.setupUi(self)

        self.txtFilePath = []
        self.txtFileUUID = []
        self.uploadFileUUID = []
        self.testFilePath = []
        self.testFile = None

        self.printText = ['']
        self.json_work = JsonCreator(self.testFile)
        self.check_code = CheckCode(self.testFile)
        self.new_line_window = None
        self.startBtn.clicked.connect(self.start_test)
        self.pushButton_2.clicked.connect(self.close_application)
        self.fileLoad.clicked.connect(self.file_open)
        self.checkDisplay.clicked.connect(self.check_the_code)
        self.reportBtn.clicked.connect(self.new_report)
        self.lineEdit.setText('cde3f5431b6e5770919a199d7f71c4ec')
        self.lineEdit_2.setText('Mn9GDLjBzV83dFKbr2tP')
        self.lineEdit_3.setText('https://oht.vagrant.oht.cc/api/2/')
        self.loadTxtBtn.clicked.connect(self.open_txt)
        self.loadFileBtn.clicked.connect(self.open_test_files)

        self.tableWidget.setColumnCount(2)
        self.tableWidget.setColumnWidth(0, 500)
        self.tableWidget.horizontalHeader().setResizeMode(1, QtGui.QHeaderView.Stretch)

        self.reg_proj.setText('7')
        self.expert_proj.setText('7.9')
        self.proof_proj.setText('7')
        self.transcript_proj.setText('3.316')
        self.combo_proj.setText('12')

        self.errorFlag = [False]
        self.prevResponse = {}
        self.prevPayload = {}

        self.priceList = {"reg_proj":float(self.reg_proj.text()),"expert_proj":float(self.expert_proj.text()),
                          "proof_proj":float(self.proof_proj.text()),"transcript_proj":float(self.transcript_proj.text()),
                          "combo_proj":float(self.combo_proj.text())}

        with open('./report/test_report.json', "w") as new:
            json.dump([], new)

    def start_test(self):

        self.firstResourcesUpload = [False]
        self.secretKey = self.lineEdit.text()
        self.publicKey = self.lineEdit_2.text()
        self.httpAddress = self.lineEdit_3.text()

        while self.tableWidget.rowCount() > 0:
            self.tableWidget.removeRow(0)

        startFlag = 0

        """""""""""""""""""""""""""""""""
        Checking that all necessary
        files are selected and uploading.
        """""""""""""""""""""""""""""""""
        if (self.json_work.testFile) or (self.check_code.testFile):
            self.txtFileUUID = []
            self.uploadFileUUID = []
            self.printText = ['']

            if len(self.txtFilePath) == 0:
                choice = QtGui.QMessageBox.question(self, 'No Text File', "No text file was loaded, would you like to load?",
                                                QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
                if choice == QtGui.QMessageBox.Yes:
                    self.open_txt()
                else:
                    pass
            elif len(self.testFilePath) == 0:
                choice = QtGui.QMessageBox.question(self, 'No test File',
                                                        "No test file was loaded, would you like to load?",
                                                        QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
                if choice == QtGui.QMessageBox.Yes:
                    self.open_test_files()
                else:
                    pass
            else:

                with open('firstUpload.json') as codeLines_data:
                    firstUpload = json.load(codeLines_data)

                for firstU in firstUpload["data"]:

                    checkLine = PostMethod(firstU)
                    checkLine.post_method(self.secretKey, self.publicKey, self.httpAddress, self.txtFilePath, self.txtFileUUID, self.testFilePath,
                                          self.uploadFileUUID, self.prevResponse, self.prevPayload, self.tableWidget, self.firstResourcesUpload)

                self.firstResourcesUpload[0] = True
                startFlag = 1


        else:
            choice = QtGui.QMessageBox.question(self, 'No File', "No file was loaded, would you like to load?",
                                                QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)

            if choice == QtGui.QMessageBox.Yes:
                self.json_work = JsonCreator(testFile)
                self.json_work.show()
            else:
                pass

        if startFlag == 1:
            payload = dict()
            """""""""""""""""""""""""""
            Deletes the existing Downloads
            directory to check up to date
            files.
            """""""""""""""""""""""""""
            if os.path.exists("Downloads"):
                shutil.rmtree("Downloads")

            if self.check_code.testFile:
                with open(self.check_code.testFile) as codeLines_data:
                    data = json.load(codeLines_data)
            else:
                with open(self.json_work.testFile) as codeLines_data:
                    data = json.load(codeLines_data)

            self.progressBar.setMaximum(len(data["data"]))
            self.progressBar.setValue(0)
            self.linePrint = LineExec(data["data"])
            self.connect(self.linePrint, SIGNAL("line_exec(PyQt_PyObject)"), self.line_exec)
            self.linePrint.start()
            self.stopBtn.setEnabled(True)
            self.stopBtn.clicked.connect(self.linePrint.terminate)

    def line_exec(self, line):
        if str.lower(line["method"]) == 'get':
            # payload initialization
            checkLine = GetMethod(line)
            checkLine.get_method(self.secretKey, self.publicKey, self.httpAddress, self.prevResponse,
                                 self.prevPayload, self.tableWidget, self.testFilePath, self.uploadFileUUID,
                                 self.txtFileUUID)

        # Post line code
        elif str.lower(line["method"]) == 'post':
            checkLine = PostMethod(line)
            checkLine.post_method(self.secretKey, self.publicKey, self.httpAddress, self.txtFilePath, self.txtFileUUID,
                                  self.testFilePath, self.uploadFileUUID, self.prevResponse, self.prevPayload,
                                  self.tableWidget, self.firstResourcesUpload)

        self.progressBar.setValue(self.progressBar.value() + 1)

    def file_open(self):
        self.json_work = JsonCreator(self.testFile)
        self.json_work.show()

    def check_the_code(self):
        self.check_code.show()

    def new_report(self):
        self.viewReport = ViewReport(self.tableWidget)
        self.viewReport.show()


    def close_application(self):
        #popup messegae before exiting
        choice = QtGui.QMessageBox.question(self, 'Quit', "Quit application?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)

        if choice == QtGui.QMessageBox.Yes:
            sys.exit()
        else:
            pass

    def open_txt(self):
        #global txtFilePath
        txtFile = QtGui.QFileDialog.getOpenFileName(self, 'Open File', "*.txt")
        if (txtFile):
            self.txtFilePath.append(txtFile)
            fileName = txtFile.split('/')
            self.txtFilesList.addItem('%s' % fileName[len(fileName)-1])

    def open_test_files(self):
        #global testFilePath
        testFile = QtGui.QFileDialog.getOpenFileName(self, 'Open File')
        if (testFile):
            self.testFilePath.append(testFile)
            fileName = testFile.split('/')
            self.testFilesList.addItem('%s' % fileName[len(fileName)-1])




def main():
    app = QtGui.QApplication(sys.argv)
    # QCleanlooksStyle
    app.setStyle('cleanlooks')
    form = TestApp()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
