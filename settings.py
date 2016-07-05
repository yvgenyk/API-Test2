from PyQt4 import QtGui
import settings_design
import json
import os


class Settings(QtGui.QMainWindow, settings_design.Ui_Form):
    def __init__(self, parent=None):
        super(Settings, self).__init__(parent)
        self.setupUi(self)
        self.txtFilePath = []
        self.testFilePath = []

        with open('./data/setup.json') as codeLines_data:
            self.setupJson = json.load(codeLines_data)

        self.secretKeyLine.setText(self.setupJson['secret_key'])
        self.publicKeyLine.setText(self.setupJson['public_key'])
        self.httpLine.setText(self.setupJson['https'])
        self.user_id.setText(self.setupJson['user'])
        self.reg_proj.setText(self.setupJson['reg_proj'])
        self.expert_proj.setText(self.setupJson['expert_proj'])
        self.proof_proj.setText(self.setupJson['proof_proj'])
        self.combo_proj.setText(self.setupJson['transcript_proj'])
        self.transcript_proj.setText(self.setupJson['combo_proj'])
        self.read_txt_files()
        self.read_files()
        self.loadTxtBtn.clicked.connect(self.open_txt)
        self.loadFileBtn.clicked.connect(self.open_test_files)
        self.delTextFile.clicked.connect(self.del_txt)
        self.delFile.clicked.connect(self.del_file)
        self.closeBtn.clicked.connect(self.close)
        self.saveBtn.clicked.connect(self.save_params)

    def read_txt_files(self):
        files = os.listdir("./Text_Files/")
        for fileItem in files:
            self.txtFilesList.addItem(fileItem)
            path = os.path.abspath("Text_Files")
            self.txtFilePath.append(path + "/" + fileItem)

    def read_files(self):
        files = os.listdir("./Other_Files/")
        for fileItem in files:
            self.testFilesList.addItem(fileItem)
            path = os.path.abspath("Other_Files")
            self.testFilePath.append(os.path.abspath(path + "/" + fileItem))

    def open_txt(self):
        txtFile = QtGui.QFileDialog.getOpenFileName(self, 'Open File', "*.txt")
        if (txtFile):
            self.txtFilePath.append(txtFile)
            fileName = txtFile.split('/')
            self.txtFilesList.addItem('%s' % fileName[len(fileName) - 1])

    def open_test_files(self):
        testFile = QtGui.QFileDialog.getOpenFileName(self, 'Open File')
        if (testFile):
            self.testFilePath.append(testFile)
            fileName = testFile.split('/')
            self.testFilesList.addItem('%s' % fileName[len(fileName)-1])

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

    def get_txt_path(self):
        return self.txtFilePath

    def get_file_path(self):
        return self.testFilePath

    def save_params(self):
        with open('./data/setup.json', 'w+') as outfile:
            self.setupJson['secret_key'] = self.secretKeyLine.text()
            self.setupJson['public_key'] = self.publicKeyLine.text()
            self.setupJson['https'] = self.httpLine.text()
            self.setupJson['user'] = self.user_id.text()
            self.setupJson['reg_proj'] = self.reg_proj.text()
            self.setupJson['expert_proj'] = self.expert_proj.text()
            self.setupJson['proof_proj'] = self.proof_proj.text()
            self.setupJson['transcript_proj'] = self.combo_proj.text()
            self.setupJson['combo_proj'] = self.transcript_proj.text()
            json.dump(self.setupJson, outfile)