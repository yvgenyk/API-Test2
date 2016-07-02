from PyQt4 import QtGui
import new_report_design
import json

"""
This class handles the report screen, it loads the report file - test_report.json
and print every line with all the parameters sent and resieved.
"""


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

        # Copying the table from the main window to the report window.
        for row in range(tableWidget.rowCount()):
            item = tableWidget.item(row, 0)
            self.tableWidget.setItem(row, 0, QtGui.QTableWidgetItem(item))
            item = tableWidget.item(row, 1)
            self.tableWidget.setItem(row, 1, QtGui.QTableWidgetItem(item))

    """
    When a cell is clicked this method will print all the relevant parameters
    for in deep review of each and every line.
    """
    def cell_was_clicked(self, row):
        with open('./report/test_report.json') as codeLines_data:
            reportJson = json.load(codeLines_data)

        text = ''
        # Url print
        self.urlLable.setText(reportJson[row]['url'])
        for param in reportJson[row]['payload']:
            if param == 'text':
                # No need to print all of the uploaded text
                text += (param + " : \"" + reportJson[row]['payload'][param][:50] + "...\"\n")
            else:
                if param == '':
                    pass
                else:
                    text += (param + " : " + reportJson[row]['payload'][param] + "\n")
        # payload print
        self.payloadLable.setText(text)
        # Checkig if a file was uploaded, if it was, will print file path.
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
            # Print the response of the site after the call.
            self.responseLable.setText(text)
        else:
            self.responseLable.setText(reportJson[row]['res'])

        # If checks were checked while executing the line, will print the searched value and the found value.
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
                        text += "\n\n"

                    else:
                        text += ("S: " + check + ": " + param + "\n" +
                                 "F: " + check + ": " + reportJson[row]['check'][check][param] + "\n")

            self.checkLable.setText(text)
        else:
            text = ''
            self.checkLable.setText(text)

        # If something was supposed to be found will print it in the appropriate field.
        if 'find' in reportJson[row]:

            text = 'Found:\n'
            for find in reportJson[row]['find']:
                text += (find + "\n")

            self.findLable.setText(text)

        else:
            self.findLable.setText('')