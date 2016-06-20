from PyQt4 import QtGui
import new_report_design
import json


class ViewReport(QtGui.QMainWindow, new_report_design.Ui_Form):
    def __init__(self, tableWidget, parent=None):
        super(ViewReport, self).__init__(parent)
        self.setupUi(self)

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


    def cell_was_clicked(self, row, column):
        with open('./report/test_report.json') as codeLines_data:
            reportJson = json.load(codeLines_data)

        text = ''

        self.urlLable.setText(reportJson[row]['url'])
        for param in reportJson[row]['payload']:
            if param == 'text':
                text += (param + " : \"" + reportJson[row]['payload'][param][:55] + "...\"\n")
            else:
                text += (param + " : " + reportJson[row]['payload'][param] + "\n")

        self.payloadLable.setText(text)

        if reportJson[row]['filePayload'] == None:
            self.fileLoadLable.setText("None")
        else:
            self.fileLoadLable.setText(str(reportJson[row]['filePayload']))

        if len(reportJson[row]['res']) > 60:
            text = ''
            for i in range(int(len(reportJson[row]['res'])/60)):
                text += (reportJson[row]['res'][(i-1)*60:i*60] + "\n")
            self.responseLable.setText(text)
        else:
            self.responseLable.setText(reportJson[row]['res'])