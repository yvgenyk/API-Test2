from PyQt4 import QtGui, QtCore
import new_line_design


class NewLine(QtGui.QMainWindow, new_line_design.Ui_NewLine):
    def __init__(self, parent=None):
        super(NewLine, self).__init__(parent)
        self.setupUi(self)
        self.new_line_window = None
        
        self.saveBtn.clicked.connect(self.continueFile)
        self.addBtn.clicked.connect(self.addNew)
        self.closeBtn.clicked.connect(self.close_window)
        """""""""""""""""""""""""""
        Combo boxes initialization
        with predefined options.
        """""""""""""""""""""""""""
        self.boxS_K.addItems(["secret_key", "No Secret Key"])
        self.boxP_K.addItems(["public_key", "No Public Key"])

        self.newMethod.addItems(["POST", "GET"])
        self.paramNameSet = ["None", "textrsc", "filersc", "file_mime", "file_name", "fetch", "resources", "wordcount",
                             "source_language", "target_language", "service", "expertise", "currency", "proofreading",
                             "sources", "callback_url", "notes", "custom0", "custom1", "custom2", "translations"]

        self.paramValueSet_rsc = ["", "empty", "nokey"]

        self.expertise = ["", "automotive-aerospace", "business-finance", "software-it", "legal-certificate",
                          "marketing-consumer-media", "cv", "medical", "patents", "scientific-academic",
                          "technical-engineering", "gaming-video-games", "ad-words-banners", "mobile-applications",
                          "tourism", "certificates-translation"]



        self.dictOfValues = [self.p_one_value, self.p_two_value, self.p_three_value, self.p_four_value,
                             self.p_five_value, self.p_six_value, self.p_seven_value, self.p_eight_value]

        self.dictOfNames = [self.p_one_name, self.p_two_name, self.p_three_name, self.p_four_name,
                             self.p_five_name, self.p_six_name, self.p_seven_name, self.p_eight_name]

        for nameField in self.dictOfNames:
            nameField.addItems(self.paramNameSet)

        for nameField in self.dictOfNames:
            nameField.currentIndexChanged.connect(self.change_value_options)

    """""""""""""""""""""""""""""""""
    Dynamic box options change for
    correct selections.
    """""""""""""""""""""""""""""""""
    def change_value_options(self, name):

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

            if self.dictOfNames[i].currentText() == "source_language":
                if self.dictOfValues[i].currentText() == '':
                    self.dictOfValues[i].clear()
                    self.dictOfValues[i].addItems(["", "en-us"])

            if self.dictOfNames[i].currentText() == "target_language":
                if self.dictOfValues[i].currentText() == '':
                    self.dictOfValues[i].clear()
                    self.dictOfValues[i].addItems(["", "fr-fr"])

            if self.dictOfNames[i].currentText() == "target_language":
                if self.dictOfValues[i].currentText() == '':
                    self.dictOfValues[i].clear()
                    self.dictOfValues[i].addItems(["", "fr-fr"])

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
        self.close()
        
    def addNew(self):
        self.saveNewLine_file(1)

    def continueFile(self):
        self.saveNewLine_file(0)

    def saveNewLine_file(self, add):
        
        #read the file
        nameOfFile = QtGui.QFileDialog.getOpenFileName(self, 'Open File', "*.json")
        loadedFile = open(nameOfFile, 'r')
        
        #convert to text
        with loadedFile:
            text = loadedFile.read()
        
        #prepare to write
        loadedFile = open(nameOfFile, 'w')
        if add == 1:
            line = ('{\"method\":\"' + self.newMethod.currentText() + '\",\"address\":\"' + self.newAddress.text() +
                    '\",\"title\":\"' + self.newTitle.text())
        else:
            line = (',{\"method\":\"' + self.newMethod.currentText() + '\",\"address\":\"' + self.newAddress.text() +
                    '\",\"title\":\"' + self.newTitle.text())

        if self.saveForNext.isChecked():
            line += ('\",\"save\":\"1\",\"params\":[\"' + self.boxS_K.currentText() + '\",\"' + self.boxP_K.currentText() + '\"]}')
        else:
            line += ('\",\"save\":\"0\",\"params\":[\"' + self.boxS_K.currentText() + '\",\"' + self.boxP_K.currentText() + '\"]}')

        for index in range(len(self.dictOfNames)):
            if self.dictOfNames[index].currentText() != 'None':
                line = (line[:len(line) - 2] + ',{\"name\":\"' + self.dictOfNames[index].currentText() +
                        '\",\"value\":\"' + self.dictOfValues[index].currentText() + '\"}' + line[len(line) - 2:])

        
        if self.findOne.text() != '':
            line = (line[:len(line)-1] + ',\"find\":[\"' + self.findOne.text() + '\"]' + line[len(line)-1:])
            
            if self.findTwo.text() != '':
                line = (line[:len(line)-2] + ',\"' + self.findTwo.text() + '\"' + line[len(line)-2:])
                
                if self.findThree.text() != '':
                    line = (line[:len(line)-2] + ',\"' + self.findThree.text() + '\"' + line[len(line)-2:])
        else:
            line = (line[:len(line)-1] + ',\"find\":[]' + line[len(line)-1:])
                
                
        
        if self.check_one_name.text() != '':        
            if self.checkPrevValue_1.isChecked():
                line = (line[:len(line)-1] + ',\"check\":[\"@' + self.check_one_name.text() + '\"]' + line[len(line)-1:])
        
            else:         
                line = (line[:len(line)-1] + ',\"check\":[\"' + self.check_one_name.text() + '\"]' + line[len(line)-1:])
            
            if self.check_two_name.text() != '':
                if self.checkPrevValue_2.isChecked():
                    line = (line[:len(line)-2] + ',\"@' + self.check_two_name.text() + '\"' + line[len(line)-2:])
                else:    
                    line = (line[:len(line)-2] + ',\"' + self.check_two_name.text() + '\"' + line[len(line)-2:])
                
            if self.check_three_name.text() != '':
                if self.checkPrevValue_3.isChecked():
                    line = (line[:len(line)-2] + ',\"@' + self.check_three_name.text() + '\"' + line[len(line)-2:])
                else:
                    line = (line[:len(line)-2] + ',\"' + self.check_three_name.text() + '\"' + line[len(line)-2:])
        else:
             line = (line[:len(line)-1] + ',\"check\":[]' + line[len(line)-1:])
                    
        
        if self.check_one_value.text() != '':            
            line = (line[:len(line)-1] + ',\"value\":[\"' + self.check_one_value.text() + '\"]' + line[len(line)-1:])
            
            if self.check_two_value.text() != '':
                line = (line[:len(line)-2] + ',\"' + self.check_two_value.text() + '\"' + line[len(line)-2:])
                
                if self.check_three_value.text() != '':
                    line = (line[:len(line)-2] + ',\"' + self.check_three_value.text() + '\"' + line[len(line)-2:])
        else:
            line = (line[:len(line)-1] + ',\"value\":[]' + line[len(line)-1:])

        
        #find the place where to add the new line
        fileEnd = len(text)-2
        
        #create new text
        newText = text[:fileEnd] + line + text[fileEnd:]
        
        #overwrite the existing file with new content
        loadedFile.write(newText)
        loadedFile.close()