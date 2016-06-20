from PyQt4 import QtGui
import new_report_design
import json


class ViewReport(QtGui.QMainWindow, new_report_design.Ui_Form):
    def __init__(self, tableWidget, parent=None):
        super(ViewReport, self).__init__(parent)
        self.setupUi(self)

        while self.tableWidget.rowCount() > 0:
            self.tableWidget.removeRow(0)
            
        self.tableWidget.setRowCount(tableWidget.rowCount())
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setColumnWidth(0, 400)
        self.tableWidget.horizontalHeader().setResizeMode(1, QtGui.QHeaderView.Stretch)
        self.tableWidget.cellClicked.connect(self.cell_was_clicked)

        for row in range(tableWidget.rowCount()):
            item = tableWidget.item(row, 0)
            self.tableWidget.setItem(row, 0, QtGui.QTableWidgetItem(item))
            item = tableWidget.item(row, 1)
            self.tableWidget.setItem(row, 1, QtGui.QTableWidgetItem(item))


    def cell_was_clicked(self, row):
        with open('./report/test_report.json') as codeLines_data:
            reportJson = json.load(codeLines_data)

        text = ''

        self.urlLable.setText(reportJson[row]['url'])
        for param in reportJson[row]['payload']:
            if param == 'text':
                text += (param + " : \"" + reportJson[row]['payload'][param][:50] + "...\"\n")
            else:
                text += (param + " : " + reportJson[row]['payload'][param] + "\n")

        self.payloadLable.setText(text)

        if reportJson[row]['filePayload'] == None:
            self.fileLoadLable.setText("None")
        else:
            self.fileLoadLable.setText(str(reportJson[row]['filePayload'][37:len(str(reportJson[row]['filePayload']))-2]))

        if len(reportJson[row]['res']) > 50:
            text = ''
            for i in range(len(reportJson[row]['res'])):
                text += (reportJson[row]['res'][i])
                if i % 70 == 0 and i != 0:
                    text = "%s%s" % (text, "\n")
            self.responseLable.setText(text)
        else:
            self.responseLable.setText(reportJson[row]['res'])

        if 'check' in reportJson[row]:
            text = ''
            for check in reportJson[row]['check']:
                for param in reportJson[row]['check'][check]:
                    if len(param) > 40:
                        text += ("S: " + check + ": ")
                        for i in range(len(param)):
                            text += param[i]
                            if i % 40 == 0 and i != 0:
                                text += "\n"

                        text += ("\nF: " + check + ": ")
                        if len(reportJson[row]['check'][check][param]) > 40:
                            for i in range(len(reportJson[row]['check'][check][param])):
                                text += reportJson[row]['check'][check][param][i]
                                if i % 40 == 0 and i != 0:
                                    text += "\n"
                        text += "\n"

                    else:
                        text += ("S: " + check + ": " + param + "\n" +
                                 "F: " + check + ": " + reportJson[row]['check'][check][param] + "\n")

            self.checkLable.setText(text)
        else:
            text = ''
            self.checkLable.setText(text)