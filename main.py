from PyQt4 import QtGui, QtCore
import sys
import main_design
import json_creator_design
import new_line_design
import requests
import re
import os
from os import listdir
from os.path import isfile, join
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
import logging

class LineExec(QThread):

    def __init__(self, mainJson):
        QThread.__init__(self)
        self.mainJson = mainJson

    def run(self):
        for line in self.mainJson:
            self.emit(SIGNAL("line_exec(PyQt_PyObject)"), line)
            self.sleep(2)


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
        with open('./data/setup.json') as codeLines_data:
            self.setupJson = json.load(codeLines_data)
        self.lineEdit.setText(self.setupJson[0]['secret_key'])
        self.lineEdit_2.setText(self.setupJson[1]['public_key'])
        self.lineEdit_3.setText(self.setupJson[3]['https'])
        self.loadTxtBtn.clicked.connect(self.open_txt)
        self.loadFileBtn.clicked.connect(self.open_test_files)
        self.read_files()
        self.delTextFile.clicked.connect(self.del_txt)
        self.delFile.clicked.connect(self.del_file)

        self.tableWidget.setColumnCount(2)
        self.tableWidget.setColumnWidth(0, 400)
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

    def start_test(self):

        self.firstResourcesUpload = [False]
        self.secretKey = self.lineEdit.text()
        self.publicKey = self.lineEdit_2.text()
        self.httpAddress = self.lineEdit_3.text()

        while self.tableWidget.rowCount() > 0:
            self.tableWidget.removeRow(0)

        with open('./report/test_report.json', "w") as new:
            json.dump([], new)

        with open('./data/languages.json', "w") as new:
            json.dump([], new)

        with open('./data/words_prices.json', "w") as new:
            json.dump([], new)

        with open('./data/setup.json', 'w+') as outfile:
            self.setupJson[0]['secret_key'] = self.lineEdit.text()
            self.setupJson[1]['public_key'] = self.lineEdit_2.text()
            self.setupJson[3]['https'] = self.lineEdit_3.text()
            json.dump(self.setupJson, outfile)

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

                with open('./data/firstUpload.json') as codeLines_data:
                    firstUpload = json.load(codeLines_data)

                for firstU in firstUpload["data"]:
                    if str.lower(firstU["method"]) == 'post':
                        checkLine = PostMethod(firstU)
                        checkLine.post_method(self.secretKey, self.publicKey, self.httpAddress, self.txtFilePath,
                                              self.txtFileUUID, self.testFilePath, self.uploadFileUUID,
                                              self.prevResponse, self.prevPayload, self.tableWidget,
                                              self.firstResourcesUpload)

                    elif str.lower(firstU["method"]) == 'get':
                        checkLine = GetMethod(firstU)
                        checkLine.get_method(self.secretKey, self.publicKey, self.httpAddress, self.prevResponse,
                                             self.prevPayload, self.tableWidget, self.testFilePath, self.uploadFileUUID,
                                             self.txtFileUUID)

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
            self.initialize_data()
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

    def initialize_data(self):
        entry = {}
        with open('./data/words_prices.json') as codeLines_data:
            mainJson = json.load(codeLines_data)

        with open('./data/words_prices.json', 'w') as outfile:

            for txtUUID in self.txtFileUUID:
                uploaded_file = Resource(self.txtFilePath[self.txtFileUUID.index(txtUUID)], self.priceList)
                entry[txtUUID] = {'wordcount': uploaded_file.get_wordcount(),
                                  'reg_proj_price': uploaded_file.get_reg_project_price(),
                                  'expert_proj_price': uploaded_file.get_expert_project_price(),
                                  'proof_proj_price': uploaded_file.get_proof_proj_price(),
                                  'trranscrip_proj_price': uploaded_file.get_transcript_proj_price(),
                                  'combo_proj_price': uploaded_file.get_combo_price()}

                mainJson.append(entry)

            for fileUUID in self.uploadFileUUID:
                uploaded_file = Resource(self.testFilePath[self.uploadFileUUID.index(fileUUID)], self.priceList)
                entry[fileUUID] = {'wordcount': uploaded_file.get_wordcount(),
                                   'reg_proj_price': uploaded_file.get_reg_project_price(),
                                   'expert_proj_price': uploaded_file.get_expert_project_price(),
                                   'proof_proj_price': uploaded_file.get_proof_proj_price(),
                                   'trranscrip_proj_price': uploaded_file.get_transcript_proj_price(),
                                   'combo_proj_price': uploaded_file.get_combo_price()}
                mainJson.append(entry)

            json.dump(mainJson, outfile)

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
        # popup messegae before exiting
        choice = QtGui.QMessageBox.question(self, 'Quit', "Quit application?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)

        if choice == QtGui.QMessageBox.Yes:
            sys.exit()
        else:
            pass

    def open_txt(self):
        txtFile = QtGui.QFileDialog.getOpenFileName(self, 'Open File', "*.txt")
        if (txtFile):
            self.txtFilePath.append(txtFile)
            print(str(self.txtFilePath))
            fileName = txtFile.split('/')
            self.txtFilesList.addItem('%s' % fileName[len(fileName)-1])

    def open_test_files(self):
        testFile = QtGui.QFileDialog.getOpenFileName(self, 'Open File')
        if (testFile):
            self.testFilePath.append(testFile)
            fileName = testFile.split('/')
            self.testFilesList.addItem('%s' % fileName[len(fileName)-1])

    def read_files(self):
        files = os.listdir("./Text_Files/")
        for file in files:
            path = os.path.abspath("Text_Files")
            self.txtFilePath.append(path + "/" + file)
            self.txtFilesList.addItem(file)

        files = os.listdir("./Other_Files/")
        for file in files:
            path = os.path.abspath("Other_Files")
            self.testFilePath.append(os.path.abspath(path + "/" + file))
            self.testFilesList.addItem(file)

    def del_txt(self):
        row = self.txtFilesList.currentRow()
        if row >= 0 and row < len(self.txtFilePath):
            self.txtFilesList.takeItem(self.txtFilesList.currentRow())
            self.txtFilePath.remove(self.txtFilePath[row])
        else:
            pass

    def del_file(self):
        row = self.testFilesList.currentRow()
        if row >= 0 and row < len(self.testFilePath):
            self.testFilesList.takeItem(self.testFilesList.currentRow())
            self.testFilePath.remove(self.testFilePath[row])
        else:
            pass

class StreamToLogger(object):
    """
    Fake file-like stream object that redirects writes to a logger instance.
    """

    def __init__(self, logger, log_level=logging.INFO):
        self.logger = logger
        self.log_level = log_level
        self.linebuf = ''

    def write(self, buf):
        for line in buf.rstrip().splitlines():
            self.logger.log(self.log_level, line.rstrip())


    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s:%(levelname)s:%(name)s:%(message)s',
        filename="main_log.log",
        filemode='w+')


def main():
    """ Logging - commented off, else On
    stdout_logger = logging.getLogger('STDOUT')
    sl = StreamToLogger(stdout_logger, logging.INFO)
    sys.stdout = sl

    stderr_logger = logging.getLogger('STDERR')
    sl = StreamToLogger(stderr_logger, logging.ERROR)
    sys.stderr = sl
    """
    app = QtGui.QApplication(sys.argv)
    app.setStyle('cleanlooks')
    form = TestApp()
    form.show()
    app.exec_()
    sys.stdout = sys.__stdout__
    sys.stderr = sys.__stderr__
if __name__ == '__main__':
    main()
