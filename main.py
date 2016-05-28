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
from class_test import Response, GetMethod, PostMethod
from doctest import testfile
#from idlelib.ClassBrowser import file_open
from PyQt4.Qt import QListWidgetItem
from PyQt4.QtCore import QThread

            

class TestApp(QtGui.QMainWindow, main_design.Ui_Dialog):
    def __init__(self, parent=None):
        super(TestApp, self).__init__(parent)
        self.setupUi(self)
        
        global txtFilePath
        txtFilePath = []
        
        global txtFileUUID
        txtFileUUID = []
        
        global uploadFileUUID
        uploadFileUUID = []
        
        global testFilePath
        testFilePath = []
        
        global testFile
        testFile = None
        
        
        
        self.json_work = JsonCreator(testFile)
        self.new_line_window = None
        self.startBtn.clicked.connect(self.start_test)
        self.pushButton_2.clicked.connect(self.close_application)
        self.fileLoad.clicked.connect(self.file_open)
        self.lineEdit.setText('6d33c51b2b2ab29a998528309e003444')
        self.lineEdit_2.setText('vc2Dd7kNfwZxYVTJ3XGn')
        self.lineEdit_3.setText('https://yavengy.vagrant.oht.cc/api/2/')
        self.loadTxtBtn.clicked.connect(self.open_txt)
        self.loadFileBtn.clicked.connect(self.open_test_files)

        self.secretKey = self.lineEdit.text()
        self.publicKey = self.lineEdit_2.text()
        self.httpAddress = self.lineEdit_3.text()
        self.errorFlag = [False]
        self.prevResponse = {}
        self.prevPayload = ()
    
        
    def start_test(self):
        global txtFilePath
        global txtFileUUID
        global testFilePath
        global uploadFileUUID
        
        startFlag = 0

        """""""""""""""""""""""""""""""""
        Checking that all necessary
        files are selected and uploading.
        """""""""""""""""""""""""""""""""
        if (self.json_work.testFile):
            if len(txtFilePath) == 0:
                choice = QtGui.QMessageBox.question(self, 'No Text File', "No text file was loaded, would you like to load?",
                                                QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
                if choice == QtGui.QMessageBox.Yes:
                    self.open_txt()
                else:
                    pass
            elif len(testFilePath) == 0:
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

                    checkLine = PostMethod(firstU)
                    checkLine.post_method(self.secretKey, self.publicKey, self.httpAddress, txtFilePath, txtFileUUID, testFilePath,
                                          uploadFileUUID, self.prevResponse, self.prevPayload, self.textEdit, self.errorFlag)

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

            with open(self.json_work.testFile) as codeLines_data:
                data = json.load(codeLines_data)
                
            for lineIndex in range(len(data["data"])):  
                
                
                
                #Get line code
                if str.lower(data["data"][lineIndex]["method"]) == 'get':
                    #payload initialization
                    
                    checkLine = GetMethod(data["data"][lineIndex])
                    checkLine.get_method(self.secretKey, self.publicKey, self.httpAddress, self.errorFlag, self.prevResponse,
                                         self.prevPayload, self.textEdit, lineIndex, testFilePath, uploadFileUUID, txtFileUUID)

                #Post line code
                elif str.lower(data["data"][lineIndex]["method"]) == 'post': 
                    checkLine = PostMethod(data["data"][lineIndex]) 
                    checkLine.post_method(self.secretKey, self.publicKey, self.httpAddress, txtFilePath, txtFileUUID, testFilePath,
                                          uploadFileUUID, self.prevResponse, self.prevPayload, self.textEdit, self.errorFlag)
                                                   
                    
                #Delete line code
                elif str.lower(data["data"][lineIndex]["method"]) == 'del': 
                    print("we have a deleter in line: " + str(lineIndex + 1))
                    
                
                if self.errorFlag[0] == True:
                    break
    
                self.progressBar.setValue((100/(len(data["data"]))*(lineIndex+1)))
                time.sleep(1)
        
        
    def file_open(self): 
        self.json_work = JsonCreator(testFile)
        self.json_work.show()
       
       
        
    def close_application(self):
        #popup messegae before exiting
        choice = QtGui.QMessageBox.question(self, 'Quit', "Quit application?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        
        if choice == QtGui.QMessageBox.Yes:
            sys.exit()
        else:
            pass
        
    def open_txt(self):
        global txtFilePath
        txtFile = QtGui.QFileDialog.getOpenFileName(self, 'Open File', "*.txt")
        txtFilePath.append(txtFile)
        fileName = txtFile.split('/')
        self.txtFilesList.addItem('%s' % fileName[len(fileName)-1])
        
    def open_test_files(self):
        global testFilePath
        testFile = QtGui.QFileDialog.getOpenFileName(self, 'Open File')
        testFilePath.append(testFile)
        fileName = testFile.split('/')
        self.testFilesList.addItem('%s' % fileName[len(fileName)-1])
        
        
        

def main():
    app = QtGui.QApplication(sys.argv)
    form = TestApp()
    form.show()
    app.exec_()
    
if __name__ == '__main__':
    main()
