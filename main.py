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
from settings import Settings
from check_code import CheckCode
from additional_testing import AdditionalTesting
from new_line import NewLine
from report_window import ViewReport
from class_test import Response, GetMethod, PostMethod, DeleteMethod
from resource_class import Resource
from callbacks_test import CallbacksTest
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
        self.newLineTest = [False]
        self.testFile = None

        self.errorNumber.display(0)

        self.printText = ['']
        self.json_work = JsonCreator(None, self.newLineTest)
        self.check_code = CheckCode(None)
        self.new_line = NewLine(self.newLineTest)
        self.settings = Settings()
        self.additional_tests = AdditionalTesting()
        self.new_line_window = None
        self.startBtn.clicked.connect(self.start_test)
        self.pushButton_2.clicked.connect(self.close_application)
        self.fileLoad.clicked.connect(self.file_open)
        self.checkDisplay.clicked.connect(self.check_the_code)
        self.reportBtn.clicked.connect(self.new_report)
        self.settingsBtn.clicked.connect(self.settings_window)
        self.ad_proj.clicked.connect(self.callbacks_test)

        self.tableWidget.setColumnCount(2)
        self.tableWidget.setColumnWidth(0, 400)
        self.tableWidget.setHorizontalHeaderLabels("Title;Status".split(";"))
        self.tableWidget.horizontalHeader().setResizeMode(1, QtGui.QHeaderView.Stretch)

        self.errorFlag = [False]
        self.prevResponse = {}
        self.prevPayload = {}

        self.priceList = {}

    def start_test(self):
        self.txtFileUUID = []
        self.uploadFileUUID = []
        self.firstResourcesUpload = [False]
        with open('./data/setup.json') as codeLines_data:
            self.setupJson = json.load(codeLines_data)

        self.secretKey = self.setupJson['secret_key']
        self.publicKey = self.setupJson['public_key']
        self.httpAddress = self.setupJson['https']
        self.txtFilePath = self.settings.get_txt_path()
        self.testFilePath = self.settings.get_file_path()
        self.priceList = {"reg_proj": float(self.setupJson['reg_proj']),
                          "expert_proj": float(self.setupJson['expert_proj']),
                          "proof_proj": float(self.setupJson['proof_proj']),
                          "transcript_proj": float(self.setupJson['transcript_proj']),
                          "combo_proj": float(self.setupJson['combo_proj'])}
        self.errorNumber.display(0)

        if self.check_code.testFile:
            with open(self.check_code.testFile) as codeLines_data:
                data = json.load(codeLines_data)
        elif self.newLineTest[0]:
            with open('./data/new_line.json') as codeLines_data:
                data = json.load(codeLines_data)
        else:
            with open('./test_lines/00_Complete_Test.json') as codeLines_data:
                data = json.load(codeLines_data)

        while self.tableWidget.rowCount() > 0:
            self.tableWidget.removeRow(0)

        with open('./report/test_report.json', "w") as new:
            json.dump([], new)

        with open('./data/languages.json', "w") as new:
            json.dump([], new)

        with open('./data/open_projects.json', "w") as new:
            json.dump({"projects": []}, new)

        with open('./data/words_prices.json', "w") as new:
            json.dump([], new)

        with open('./data/firstUpload.json') as codeLines_data:
            firstUpload = json.load(codeLines_data)

        for firstU in firstUpload["data"]:
            if str.lower(firstU["method"]) == 'post':
                checkLine = PostMethod(firstU)
                checkLine.post_method(self.secretKey, self.publicKey, self.httpAddress, self.txtFilePath,
                                      self.txtFileUUID, self.testFilePath, self.uploadFileUUID,
                                      self.prevResponse, self.prevPayload, self.tableWidget,
                                      self.firstResourcesUpload, self.errorNumber)

            elif str.lower(firstU["method"]) == 'get':
                checkLine = GetMethod(firstU)
                checkLine.get_method(self.secretKey, self.publicKey, self.httpAddress, self.prevResponse,
                                     self.prevPayload, self.tableWidget, self.testFilePath, self.uploadFileUUID,
                                     self.txtFileUUID, self.errorNumber)

        self.firstResourcesUpload[0] = True

        # payload = dict()
        """""""""""""""""""""""""""
        Deletes the existing Downloads
        directory to check up to date
        files.
        """""""""""""""""""""""""""
        if os.path.exists("Downloads"):
            shutil.rmtree("Downloads")

        self.initialize_data()

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
                                 self.txtFileUUID, self.errorNumber)

        # Post line code
        elif str.lower(line["method"]) == 'post':
            checkLine = PostMethod(line)
            checkLine.post_method(self.secretKey, self.publicKey, self.httpAddress, self.txtFilePath, self.txtFileUUID,
                                  self.testFilePath, self.uploadFileUUID, self.prevResponse, self.prevPayload,
                                  self.tableWidget, self.firstResourcesUpload, self.errorNumber)

        elif str.lower(line["method"]) == 'delete':
            checkLine = DeleteMethod(line)
            checkLine.delete_method(self.secretKey, self.publicKey, self.httpAddress, self.txtFilePath, self.txtFileUUID,
                                  self.testFilePath, self.uploadFileUUID, self.prevResponse, self.prevPayload,
                                  self.tableWidget, self.firstResourcesUpload, self.errorNumber)

        self.progressBar.setValue(self.progressBar.value() + 1)

    def file_open(self):
        self.new_line_window = NewLine(self.newLineTest)
        self.new_line_window.show()

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

    def settings_window(self):
        self.settings.show()

    def additional_window(self):
        self.additional_tests = AdditionalTesting()
        self.additional_tests.show()

    def callbacks_test(self):
        CallbacksTest(self.tableWidget, self.errorNumber)

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

    def flush(self):
        pass

def main():
    """# Logging - commented off, else On
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
