from PyQt4 import QtGui, QtCore
import check_code_design
import json

class CheckCode(QtGui.QMainWindow, check_code_design.Ui_Lines_presentation):
    def __init__(self,testFile ,parent=None):
        super(CheckCode, self).__init__(parent)
        self.setupUi(self)

        self.testFile = testFile
        self.index = 0
        self.maxLines = 0
        self.lineClicked = 0
        self.displayedLine = ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]

        self.codeLinesDict = [self.displayLine_1, self.displayLine_2, self.displayLine_3, self.displayLine_4,
                              self.displayLine_5, self.displayLine_6, self.displayLine_7, self.displayLine_8,
                              self.displayLine_9, self.displayLine_10]

        self.codeLinesCounterDict = [self.line_counter_1, self.line_counter_2, self.line_counter_3, self.line_counter_4,
                                     self.line_counter_5, self.line_counter_6, self.line_counter_7, self.line_counter_8,
                                     self.line_counter_9, self.line_counter_10]

        self.paramNameDict = [self.pName_1, self.pName_2, self.pName_3, self.pName_4, self.pName_5, self.pName_6,
                              self.pName_7, self.pName_8, self.pName_9, self.pName_10]

        self.paramValueDict = [self.pValue_1, self.pValue_2, self.pValue_3, self.pValue_4, self.pValue_5, self.pValue_6,
                               self.pValue_7, self.pValue_8, self.pValue_9, self.pValue_10]

        self.checkNameDict = [self.cName_1, self.cName_2, self.cName_3, self.cName_4, self.cName_5, self.cName_6]

        self.checkValueDict = [self.cValue_1, self.cValue_2, self.cValue_3, self.cValue_4, self.cValue_5, self.cValue_6]

        self.findDict = [self.find_1, self.find_2, self.find_3]

        self.codeLinesDict[0].clicked.connect(self.lineOne)
        self.codeLinesDict[1].clicked.connect(self.lineTwo)
        self.codeLinesDict[2].clicked.connect(self.lineThree)
        self.codeLinesDict[3].clicked.connect(self.lineFour)
        self.codeLinesDict[4].clicked.connect(self.lineFive)
        self.codeLinesDict[5].clicked.connect(self.lineSix)
        self.codeLinesDict[6].clicked.connect(self.lineSeven)
        self.codeLinesDict[7].clicked.connect(self.lineEight)
        self.codeLinesDict[8].clicked.connect(self.lineNine)
        self.codeLinesDict[9].clicked.connect(self.lineTen)

        self.nextBtn.clicked.connect(self.next_btn)
        self.prevBtn.clicked.connect(self.prev_btn)
        self.saveBtn.clicked.connect(self.save_line)
        self.oneLineCheck.clicked.connect(self.one_line_test)

        with open('./test_lines/00_Complete_Test.json') as codeLines_data:
            self.mainJson = json.load(codeLines_data)

        self.maxLines = len(self.mainJson['data'])
        self.show_lines()


    def show_lines(self):

        for i in range(10):
            self.codeLinesCounterDict[i].display(self.index+i+1)
            self.codeLinesCounterDict[i].setStyleSheet("color: red")

            if (self.index + i) < self.maxLines:
                self.codeLinesDict[i].setText(self.mainJson['data'][self.index + i]['title'])
                self.codeLinesDict[i].setStyleSheet("background-color: rgb(179, 179, 255)")
            else:
                self.codeLinesDict[i].setText('')

    def next_btn(self):
        if (self.index + 10) > (self.maxLines):
            pass
        else:
            self.index += 10
            self.show_lines()

    def prev_btn(self):
        if (self.index - 10) < 0:
            pass
        else:
            self.index -= 10
            self.show_lines()

    def lineOne(self):
        self.clear_lines()
        self.codeLinesDict[0].setStyleSheet("background-color: #ffffb3")
        self.display_line(0)

    def lineTwo(self):
        self.clear_lines()
        self.codeLinesDict[1].setStyleSheet("background-color: #ffffb3")
        self.display_line(1)

    def lineThree(self):
        self.clear_lines()
        self.codeLinesDict[2].setStyleSheet("background-color: #ffffb3")
        self.display_line(2)

    def lineFour(self):
        self.clear_lines()
        self.codeLinesDict[3].setStyleSheet("background-color: #ffffb3")
        self.display_line(3)

    def lineFive(self):
        self.clear_lines()
        self.codeLinesDict[4].setStyleSheet("background-color: #ffffb3")
        self.display_line(4)

    def lineSix(self):
        self.clear_lines()
        self.codeLinesDict[5].setStyleSheet("background-color: #ffffb3")
        self.display_line(5)

    def lineSeven(self):
        self.clear_lines()
        self.codeLinesDict[6].setStyleSheet("background-color: #ffffb3")
        self.display_line(6)

    def lineEight(self):
        self.clear_lines()
        self.codeLinesDict[7].setStyleSheet("background-color: #ffffb3")
        self.display_line(7)

    def lineNine(self):
        self.clear_lines()
        self.codeLinesDict[8].setStyleSheet("background-color: #ffffb3")
        self.display_line(8)

    def lineTen(self):
        self.clear_lines()
        self.codeLinesDict[9].setStyleSheet("background-color: #ffffb3")
        self.display_line(9)

    def display_line(self, line):

        self.displayedLine[line] = '1'

        if (self.index + line) > self.maxLines:
            pass
        else:
            self.methodDisplay.setText(str(self.mainJson['data'][self.index + line]['method']))
            self.addressDisplay.setText("api/2/" + str(self.mainJson['data'][self.index + line]['address']))
            self.titleDisplay.setText(str(self.mainJson['data'][self.index + line]['title']))

            for param in self.mainJson['data'][self.index + line]['params']:
                currentIndex = self.mainJson['data'][self.index + line]['params'].index(param)

                if currentIndex == 0 or currentIndex == 1:
                    self.paramNameDict[currentIndex].setText(param)

                else:
                    self.paramNameDict[currentIndex].setText(param['name'])
                    self.paramValueDict[currentIndex].setText(param['value'])

            for check in self.mainJson['data'][self.index + line]['check']:
                currentIndex = self.mainJson['data'][self.index + line]['check'].index(check)
                self.checkNameDict[currentIndex].setText(check)

            for value in self.mainJson['data'][self.index + line]['value']:
                currentIndex = self.mainJson['data'][self.index + line]['value'].index(value)
                self.checkValueDict[currentIndex].setText(value)

            for find in self.mainJson['data'][self.index + line]['find']:
                currentIndex = self.mainJson['data'][self.index + line]['find'].index(find)
                self.findDict[currentIndex].setText(find)

    def clear_lines(self):
        if self.displayedLine != ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]:
            self.codeLinesDict[self.displayedLine.index('1')].setStyleSheet("background-color: rgb(179, 179, 255)")

        self.methodDisplay.setText('')
        self.addressDisplay.setText('')
        self.titleDisplay.setText('')

        for name in self.paramNameDict:
            name.setText('')

        for value in self.paramValueDict:
            value.setText('')

        for cname in self.checkNameDict:
            cname.setText('')

        for cvalue in self.checkValueDict:
            cvalue.setText('')

        for find in self.findDict:
            find.setText('')

        self.displayedLine = ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]

    def save_line(self):

        line = self.displayedLine.index('1') + self.index

        if self.methodDisplay.text() != self.mainJson['data'][line]['method']:
            self.mainJson['data'][line]['method'] = self.methodDisplay.text()

        if self.addressDisplay.text()[6:] != self.mainJson['data'][line]['address']:
            self.mainJson['data'][line]['address'] = self.addressDisplay.text()

        if self.titleDisplay.text() != self.mainJson['data'][line]['title']:
            self.mainJson['data'][line]['title'] = self.titleDisplay.text()

        for name in self.paramNameDict:
            currentIndex = self.paramNameDict.index(name)
            if currentIndex == 0 or currentIndex == 1:
                if name.text() != self.mainJson['data'][line]['params'][currentIndex]:
                    self.mainJson['data'][line]['params'][currentIndex] = name.text()

            elif currentIndex < len(self.mainJson['data'][line]['params']):
                if name.text() != self.mainJson['data'][line]['params'][currentIndex]['name']:
                    self.mainJson['data'][line]['params'][currentIndex]['name'] = name.text()

                if self.paramValueDict[currentIndex].text() != self.mainJson['data'][line]['params'][currentIndex]['value']:
                    self.mainJson['data'][line]['params'][currentIndex]['value'] = self.paramValueDict[currentIndex].text()

            elif name.text() != '':
                self.mainJson['data'][line]['params'].append({"name": name.text(), "value": self.paramValueDict[currentIndex].text()})

        for check in self.checkNameDict:
            if check == '':
                pass
            else:
                currentIndex = self.checkNameDict.index(check)
                if currentIndex < len(self.mainJson['data'][line]['check']):
                    if check.text() != self.mainJson['data'][line]['check'][currentIndex]:
                        self.mainJson['data'][line]['check'][currentIndex] = check.text()

                    if self.checkValueDict[currentIndex].text() != self.mainJson['data'][line]['value'][currentIndex]:
                        self.mainJson['data'][line]['value'][currentIndex] = self.checkValueDict[currentIndex].text()

                elif check.text() != '':
                    self.mainJson['data'][line]['check'].append(check.text())
                    self.mainJson['data'][line]['value'].append(self.checkValueDict[currentIndex].text())


        for find in self.findDict:

            currentIndex = self.findDict.index(find)
            if currentIndex < len(self.mainJson['data'][line]['find']):
                if find.text() != self.mainJson['data'][line]['find'][currentIndex]:
                    self.mainJson['data'][line]['find'][currentIndex] = find.text()

            elif find.text() != '':
                self.mainJson['data'][line]['find'].append(find.text())

        with open('./test_lines/00_Complete_Test.json', 'w') as outfile:
            json.dump(self.mainJson, outfile)


    def one_line_test(self):

        flag = False

        for i in self.displayedLine:
            if i == "1" and (self.displayedLine.index('1') + self.index) < self.maxLines:
                flag = True

        if flag == True:
            line = self.displayedLine.index('1') + self.index

            lineInfo = {}
            lineInfo['data'] = [self.mainJson['data'][line]]
            # lineInfo = "{\"data\":[" + str(self.mainJson['data'][line]) + "]}"
            with open('./test_lines/one_line_test.json', 'w') as outfile:
                json.dump(lineInfo, outfile)

            self.testFile = "./test_lines/one_line_test.json"

            self.close()







