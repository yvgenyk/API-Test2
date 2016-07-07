from PyQt4 import QtGui, QtCore
import new_line_design
import json


class NewLine(QtGui.QMainWindow, new_line_design.Ui_NewLine):
    def __init__(self, newLineTest, parent=None):
        super(NewLine, self).__init__(parent)
        self.setupUi(self)
        self.new_line_window = None
        self.finalLine = None
        self.newLineTest = newLineTest
        self.closeBtn.clicked.connect(self.close_window)
        self.testLineBtn.clicked.connect(self.test_line)
        self.saveMain.clicked.connect(self.save_main)
        """""""""""""""""""""""""""
        Combo boxes initialization
        with predefined options.
        """""""""""""""""""""""""""
        self.boxS_K.addItems(["secret_key", "No Secret Key"])
        self.boxP_K.addItems(["public_key", "No Public Key"])

        self.newMethod.addItems(["POST", "GET"])
        self.paramNameSet = ["None", "textrsc", "filersc", "file_mime", "file_name", "fetch", "resources", "wordcount",
                             "source_language", "target_language", "language_pair", "service", "expertise", "currency",
                             "proofreading", "sources", "callback_url", "notes", "custom0", "custom1", "custom2",
                             "translations"]

        self.paramValueSet_rsc = ["", "empty", "nokey", "oneFile"]

        self.expertise = ["", "automotive-aerospace", "business-finance", "software-it", "legal-certificate",
                          "marketing-consumer-media", "cv", "medical", "patents", "scientific-academic",
                          "technical-engineering", "gaming-video-games", "ad-words-banners", "mobile-applications",
                          "tourism", "certificates-translation"]

        self.dictOfValues = [self.p_one_value, self.p_two_value, self.p_three_value, self.p_four_value, self.p_five_value]

        self.dictOfNames = [self.p_one_name, self.p_two_name, self.p_three_name, self.p_four_name, self.p_five_name]

        self.dictOfManualNames = [self.p_six_name, self.p_seven_name, self.p_eight_name]
        self.dictOfManualValues = [self.p_six_value, self.p_seven_value, self.p_eight_value]

        self.dictOfCheckNames = [self.check_one_name, self.check_two_name, self.check_three_name,
                                 self.check_four_name, self.check_five_name, self.check_six_name]

        self.dictOfCheckValues = [self.check_one_value, self.check_two_value, self.check_three_value,
                                  self.check_four_value, self.check_five_value, self.check_six_value]

        self.dictOfFinds = [self.findOne, self.findTwo, self.findThree]

        for nameField in self.dictOfNames:
            nameField.addItems(self.paramNameSet)

        for nameField in self.dictOfNames:
            nameField.currentIndexChanged.connect(self.change_value_options)

    """""""""""""""""""""""""""""""""
    Dynamic box options change for
    correct selections.
    """""""""""""""""""""""""""""""""
    def change_value_options(self):

        for i in range(len(self.dictOfNames)):

            if self.dictOfNames[i].currentText() == "filersc" or self.dictOfNames[i].currentText() == "textrsc":
                if self.dictOfValues[i].currentText() == '':
                    self.dictOfValues[i].clear()
                    self.dictOfValues[i].addItems(self.paramValueSet_rsc)

            if self.dictOfNames[i].currentText() == "file_mime":
                if self.dictOfValues[i].currentText() == '':
                    self.dictOfValues[i].clear()
                    self.dictOfValues[i].addItems(["", "File type"])

            if self.dictOfNames[i].currentText() == "file_name":
                if self.dictOfValues[i].currentText() == '':
                    self.dictOfValues[i].clear()
                    self.dictOfValues[i].addItems(["", "namecheck"])

            if self.dictOfNames[i].currentText() == "fetch":
                if self.dictOfValues[i].currentText() == '':
                    self.dictOfValues[i].clear()
                    self.dictOfValues[i].addItems(["", "base64"])

            if self.dictOfNames[i].currentText() == "wordcount":
                if self.dictOfValues[i].currentText() == '':
                    self.dictOfValues[i].clear()
                    self.dictOfValues[i].addItems(["", "100", "200", "333"])

            if self.dictOfNames[i].currentText() == "expertise":
                if self.dictOfValues[i].currentText() == '':
                    self.dictOfValues[i].clear()
                    self.dictOfValues[i].addItems(self.expertise)

            if self.dictOfNames[i].currentText() == "source_language" or self.dictOfNames[
                i].currentText() == "target_language" or self.dictOfNames[i].currentText() == "language_pair":
                if self.dictOfValues[i].currentText() == '':
                    self.dictOfValues[i].clear()
                    self.dictOfValues[i].addItems(["Random"])

            if self.dictOfNames[i].currentText() == "currency":
                if self.dictOfValues[i].currentText() == '':
                    self.dictOfValues[i].clear()
                    self.dictOfValues[i].addItems(["", "USD", "EUR"])

            if self.dictOfNames[i].currentText() == "service":
                if self.dictOfValues[i].currentText() == '':
                    self.dictOfValues[i].clear()
                    self.dictOfValues[i].addItems(["", "translation", "transproof", "transcription"])

            if self.dictOfNames[i].currentText() == "proofreading":
                if self.dictOfValues[i].currentText() == '':
                    self.dictOfValues[i].clear()
                    self.dictOfValues[i].addItems(["", "1"])

            if self.dictOfNames[i].currentText() == "resources" or self.dictOfNames[i].currentText() == "sources" or \
                            self.dictOfNames[i].currentText() == "translations":
                if self.dictOfValues[i].currentText() == '':
                    self.dictOfValues[i].clear()
                    self.dictOfValues[i].addItems(["", "oneTxt", "allTxt", "oneFile", "allFile"])

            if self.dictOfNames[i].currentText() == "callback_url":
                if self.dictOfValues[i].currentText() == '':
                    self.dictOfValues[i].clear()
                    self.dictOfValues[i].addItems(["", "https: // yavengy.vagrant.oht.cc / callbacks.php"])

            if self.dictOfNames[i].currentText() == "notes":
                if self.dictOfValues[i].currentText() == '':
                    self.dictOfValues[i].clear()
                    self.dictOfValues[i].addItems(["", "Hello there, please do a good job.",
                                                   "I need you to be very professional on this."])

            if self.dictOfNames[i].currentText() == "custom0":
                if self.dictOfValues[i].currentText() == '':
                    self.dictOfValues[i].clear()
                    self.dictOfValues[i].addItem("Custom 0")

            if self.dictOfNames[i].currentText() == "custom1":
                if self.dictOfValues[i].currentText() == '':
                    self.dictOfValues[i].clear()
                    self.dictOfValues[i].addItem("Custom 1")

            if self.dictOfNames[i].currentText() == "custom2":
                if self.dictOfValues[i].currentText() == '':
                    self.dictOfValues[i].clear()
                    self.dictOfValues[i].addItem("Custom 2")

    def close_window(self):
        self.newLineTest[0] = False
        self.close()

    def test_line(self):
        with open('./data/new_line.json', "w") as new:
            json.dump({}, new)
        newLine = {}
        self.paramTextEdit.setText('')
        self.paramTextEdit.append("Secret Key: " + self.boxS_K.currentText())
        self.paramTextEdit.append("Public Key: " + self.boxP_K.currentText())
        for i in range(len(self.dictOfNames)):
            if self.dictOfNames[i].currentText() != 'None':
                self.paramTextEdit.append(self.dictOfNames[i].currentText() + ': ' + self.dictOfValues[i].currentText())
        for i in range(len(self.dictOfManualNames)):
            if self.dictOfManualNames[i].text() != '':
                self.paramTextEdit.append(self.dictOfManualNames[i].text() + ': ' + self.dictOfManualValues[i].text())

        newLine['method'] = self.newMethod.currentText()
        newLine['address'] = self.newAddress.text()
        newLine['title'] = self.newTitle.text()
        newLine['save'] = "0"
        newLine['params'] = []
        newLine['params'].append(self.boxS_K.currentText())
        newLine['params'].append(self.boxP_K.currentText())
        for i in range(len(self.dictOfNames)):
            if self.dictOfNames[i].currentText() != 'None':
                parameter = {}
                parameter['name'] = self.dictOfNames[i].currentText()
                parameter['value'] = self.dictOfValues[i].currentText()
                newLine['params'].append(parameter)

        for i in range(len(self.dictOfManualNames)):
            if self.dictOfManualNames[i].text() != '':
                parameter = {}
                parameter['name'] = self.dictOfManualNames[i].text()
                parameter['value'] = self.dictOfManualValues[i].text()
                newLine['params'].append(parameter)

        newLine['check'] = []
        for name in self.dictOfCheckNames:
            if name.text() != '':
                newLine['check'].append(name.text())

        newLine['value'] = []
        for value in self.dictOfCheckValues:
            if value.text() != '':
                newLine['value'].append(value.text())

        newLine['find'] = []
        for find in self.dictOfFinds:
            if find.text() != '':
                newLine['find'].append(find.text())

        self.finalLine = {}
        self.finalLine['data'] = []
        self.finalLine['data'].append(newLine)
        self.newLineTest[0] = True
        with open('./data/new_line.json', 'w') as outfile:
            json.dump(self.finalLine, outfile)

    def save_main(self):
        with open('./test_lines/00_Complete_Test.json') as codeLines_data:
            mainJson = json.load(codeLines_data)

        mainJson['data'].append(self.finalLine['data'][0])

        with open('./test_lines/00_Complete_Test.json', 'w') as outfile:
            json.dump(mainJson, outfile)

        self.newLineTest[0] = False