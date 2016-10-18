from PyQt4 import QtGui
import json

"""
This class is handling all the report methods.
- Print line to the main screen.
- Add color to the line on main screen.
- Saving all the data sent or recieved to/from the sites API.
"""


class Report:

    def __init__(self, tableWidget, title, status):
        self.tableWidget = tableWidget
        self.title = title
        self.status = status
        self.rows = self.tableWidget.rowCount()
        self.color = "None"
    """
    Printing the line to the main table.
    This is critical. without the print the row won't be painted
    and there will be an exception.
    """
    def print_line(self, errorNumber):
        self.tableWidget.insertRow(self.rows)
        self.tableWidget.setItem(self.rows, 0, QtGui.QTableWidgetItem(self.title))
        self.tableWidget.setItem(self.rows, 1, QtGui.QTableWidgetItem(str(self.status)))
        if self.status != 200:
            self.mark_red(errorNumber)

        item = self.tableWidget.item(self.rows, 0)
        self.tableWidget.scrollToItem(item, QtGui.QAbstractItemView.PositionAtCenter)
        self.tableWidget.selectRow(self.rows)
        print(str(self.rows) + ". Title: " + self.title + "  Status: " + str(self.status) + "\n")

    def mark_green(self):
        self.tableWidget.item(self.rows, 0).setBackground(QtGui.QColor(221, 255, 204))
        self.tableWidget.item(self.rows, 1).setBackground(QtGui.QColor(221, 255, 204))
        self.color = "green"

    def mark_red(self, errorNumber):
        if self.color != "red":
            errorNumber.display(errorNumber.value() + 1)
        self.tableWidget.item(self.rows, 0).setBackground(QtGui.QColor(255, 153, 153))
        self.tableWidget.item(self.rows, 1).setBackground(QtGui.QColor(255, 153, 153))
        self.color = "red"

    def mark_yellow(self):
        if self.color != 'red':
            self.tableWidget.item(self.rows, 0).setBackground(QtGui.QColor(255, 224, 102))
            self.tableWidget.item(self.rows, 1).setBackground(QtGui.QColor(255, 224, 102))
            self.color = "yellow"

    def get_color(self):
        return self.color
    """
    This method will add lines to the test_report.json which is
    a sort of logging. After the test is finished the user can see each and every
    executed lines status, payload, sent url and response.
    """
    def report_line(self, sentURL, response, payload, filePayload):
        with open('./report/test_report.json') as codeLines_data:
            mainJson = json.load(codeLines_data)

        with open('./report/test_report.json', 'w') as outfile:
            entry = {'url' : sentURL, 'res' : response, 'payload' : payload, 'filePayload' : filePayload}
            mainJson.append(entry)
            json.dump(mainJson, outfile)
            print("Test report Lines: " + str(len(mainJson)) + "\n")
    """
    This will add all the checked parameters to test_report.json
    """
    def report_line_check(self, check, checkFound, name):

        with open('./report/test_report.json') as codeLines_data:
            mainJson = json.load(codeLines_data)

        with open('./report/test_report.json', 'w') as outfile:
            if 'check' not in mainJson[len(mainJson)-1]:
                mainJson[len(mainJson) - 1]["check"] = {}
                mainJson[len(mainJson) - 1]["check"][name] = {check: checkFound}
            else:
                mainJson[len(mainJson) - 1]["check"][name] = {check: checkFound}

            json.dump(mainJson, outfile)

    """
    Finally adding the find parameters which were, if they were searched and found
    or not. This too is added to test_report.json
    """
    def report_line_find(self, find):
        with open('./report/test_report.json') as codeLines_data:
            mainJson = json.load(codeLines_data)

        with open('./report/test_report.json', 'w') as outfile:
            if 'find' not in mainJson[len(mainJson) - 1]:
                mainJson[len(mainJson) - 1]["find"] = []
                mainJson[len(mainJson) - 1]["find"].append(find)
            else:
                mainJson[len(mainJson) - 1]["find"].append(find)
            json.dump(mainJson, outfile)