from PyQt4 import QtGui, QtCore
import json_creator_design
from new_line import NewLine

class JsonCreator(QtGui.QMainWindow, json_creator_design.Ui_JsonCreator):
    def __init__(self, testFile, parent=None):
        super(JsonCreator, self).__init__(parent)
        self.setupUi(self)
        self.doneBtn.clicked.connect(self.close_window)
        self.loadExFileBtn.clicked.connect(self.load_file)
        self.createNewBtn.clicked.connect(self.new_file)
        self.saveBtn.clicked.connect(self.save_file)
        self.addNewLine.clicked.connect(self.edit_file)
        
        self.testFile = testFile
        
        
    def close_window(self):
        self.close()
        
    def load_file(self):
    
        self.testFile = QtGui.QFileDialog.getOpenFileName(self, 'Open File', "*.json")
        loadedFile = open(self.testFile, 'r')
        
        with loadedFile:
            text = loadedFile.read()
            self.textEditFileLoad.setText(text)
            
            
    def new_file(self):
        self.textEditFileLoad.setText('{"data":[]}')
        
    def save_file(self):
        fileName = QtGui.QFileDialog.getSaveFileName(self, 'Save File', '.json','*.json')
        file = open(fileName, 'w')
        text = self.textEditFileLoad.toPlainText()
        file.write(text)
        file.close()
        
        
    def edit_file(self):
        
        self.new_line_window = NewLine()
        self.new_line_window.show()