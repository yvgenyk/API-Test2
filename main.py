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
from new_report import Report
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
            #self.sleep(1)


class TestApp(QtGui.QMainWindow, main_design.Ui_Dialog):
    def __init__(self, parent=None):
        super(TestApp, self).__init__(parent)
        self.setupUi(self)

        #global txtFilePath
        self.txtFilePath = []

        #global txtFileUUID
        self.txtFileUUID = []

        #global uploadFileUUID
        self.uploadFileUUID = []

        #global testFilePath
        self.testFilePath = []

        #global testFile
        self.testFile = None

        self.printText = ['']
        self.json_work = JsonCreator(self.testFile)
        self.check_code = CheckCode(self.testFile)
        self.new_line_window = None
        self.report = Report()
        self.startBtn.clicked.connect(self.start_test)
        self.pushButton_2.clicked.connect(self.close_application)
        self.fileLoad.clicked.connect(self.file_open)
        self.checkDisplay.clicked.connect(self.check_the_code)
        self.reportBtn.clicked.connect(self.new_report)
        self.lineEdit.setText('aa96e6ebe4c8142ca3203807ee7762d6')
        self.lineEdit_2.setText('JjPBxp9W87LYk42dXRzG')
        self.lineEdit_3.setText('https://oht.vagrant.oht.cc/api/2/')
        self.loadTxtBtn.clicked.connect(self.open_txt)
        self.loadFileBtn.clicked.connect(self.open_test_files)

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


    def start_test(self):
        #global txtFilePath
        #global txtFileUUID
        #global testFilePath
        #global uploadFileUUID
        self.firstResourcesUpload = [False]
        self.secretKey = self.lineEdit.text()
        self.publicKey = self.lineEdit_2.text()
        self.httpAddress = self.lineEdit_3.text()

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

                self.textEdit.append("First files upload\n\n")

                for firstU in firstUpload["data"]:

                    checkLine = PostMethod(firstU, self.printText)
                    checkLine.post_method(self.secretKey, self.publicKey, self.httpAddress, self.txtFilePath, self.txtFileUUID, self.testFilePath,
                                          self.uploadFileUUID, self.prevResponse, self.prevPayload, self.textEdit, self.errorFlag, self.firstResourcesUpload)
                    self.textEdit.append(self.printText[0])



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

            self.textEdit.append("\n\nNEW TEST\n")
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

            """
            for lineIndex in range(len(data["data"])):

                printText = ['']

                #Get line code
                if str.lower(data["data"][lineIndex]["method"]) == 'get':
                    #payload initialization

                    checkLine = GetMethod(data["data"][lineIndex], printText)
                    checkLine.get_method(self.secretKey, self.publicKey, self.httpAddress, self.errorFlag, self.prevResponse,
                                         self.prevPayload, self.textEdit, lineIndex, self.testFilePath, self.uploadFileUUID, self.txtFileUUID)
                    #self.report.mark_green(lineIndex)
                    #self.textEdit.append(printText[0])

                #Post line code
                elif str.lower(data["data"][lineIndex]["method"]) == 'post':
                    checkLine = PostMethod(data["data"][lineIndex], printText)
                    checkLine.post_method(self.secretKey, self.publicKey, self.httpAddress, self.txtFilePath, self.txtFileUUID, self.testFilePath,
                                          self.uploadFileUUID, self.prevResponse, self.prevPayload, self.textEdit, self.errorFlag, self.firstResourcesUpload)
                    #self.report.mark_red(lineIndex)
                    #self.textEdit.append(printText[0])


                #Delete line code
                elif str.lower(data["data"][lineIndex]["method"]) == 'del':
                    print("we have a deleter in line: " + str(lineIndex + 1))


                if self.errorFlag[0] == True:
                    break

                self.progressBar.setValue((100/(len(data["data"]))*(lineIndex+1)))
            """

    def line_print(self, text):
        self.textEdit.append(text)

    def line_exec(self, line):
        if str.lower(line["method"]) == 'get':
            # payload initialization

            checkLine = GetMethod(line, self.printText)
            checkLine.get_method(self.secretKey, self.publicKey, self.httpAddress, self.errorFlag, self.prevResponse,
                                 self.prevPayload, self.textEdit, 0, self.testFilePath, self.uploadFileUUID,
                                 self.txtFileUUID)
            #self.report.mark_green(lineIndex)
            self.textEdit.append(self.printText[0])

        # Post line code
        elif str.lower(line["method"]) == 'post':
            checkLine = PostMethod(line, self.printText)
            checkLine.post_method(self.secretKey, self.publicKey, self.httpAddress, self.txtFilePath, self.txtFileUUID,
                                  self.testFilePath, self.uploadFileUUID, self.prevResponse, self.prevPayload, self.textEdit,
                                  self.errorFlag, self.firstResourcesUpload)
            #self.report.mark_red(lineIndex)
            self.textEdit.append(self.printText[0])

        self.progressBar.setValue(self.progressBar.value() + 1)

    def file_open(self):
        self.json_work = JsonCreator(self.testFile)
        self.json_work.show()

    def check_the_code(self):
        self.check_code.show()

    def new_report(self):
        self.report.show()


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
