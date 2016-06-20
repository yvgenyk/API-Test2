from PyQt4 import QtGui
import json


class Report:

    def __init__(self, tableWidget, title, status):
        self.tableWidget = tableWidget
        self.title = title
        self.status = status
        self.rows = self.tableWidget.rowCount()

    def print_line(self):
        self.tableWidget.insertRow(self.rows)
        self.tableWidget.setItem(self.rows, 0, QtGui.QTableWidgetItem(self.title))
        self.tableWidget.setItem(self.rows, 1, QtGui.QTableWidgetItem(str(self.status)))
        item = self.tableWidget.item(self.rows, 0)
        self.tableWidget.scrollToItem(item, QtGui.QAbstractItemView.PositionAtCenter)
        self.tableWidget.selectRow(self.rows)
        print(str(self.rows) + ". Title: " + self.title + "  Status: " + str(self.status) + "\n")

    def mark_green(self):
        self.tableWidget.item(self.rows, 0).setBackground(QtGui.QColor(128, 255, 128))
        self.tableWidget.item(self.rows, 1).setBackground(QtGui.QColor(128, 255, 128))

    def mark_red(self):
        self.tableWidget.item(self.rows, 0).setBackground(QtGui.QColor(255, 140, 102))
        self.tableWidget.item(self.rows, 1).setBackground(QtGui.QColor(255, 140, 102))

    def mark_yellow(self):
        self.tableWidget.item(self.rows, 0).setBackground(QtGui.QColor(255, 224, 102))
        self.tableWidget.item(self.rows, 1).setBackground(QtGui.QColor(255, 224, 102))

    def report_line(self, sentURL, response, payload, filePayload):
        with open('./report/test_report.json') as codeLines_data:
            mainJson = json.load(codeLines_data)

        with open('./report/test_report.json', 'w') as outfile:
            entry = {'url' : sentURL, 'res' : response, 'payload' : payload, 'filePayload' : filePayload}
            mainJson.append(entry)
            json.dump(mainJson, outfile)

    def report_line_cf(self, check, checkFound, name):

        with open('./report/test_report.json') as codeLines_data:
            mainJson = json.load(codeLines_data)

        with open('./report/test_report.json', 'w') as outfile:
            if 'check' not in mainJson[len(mainJson)-1]:
                mainJson[len(mainJson) - 1]["check"] = {}
                mainJson[len(mainJson) - 1]["check"][name] = {check: checkFound}
            else:
                mainJson[len(mainJson) - 1]["check"][name] = {check: checkFound}
            json.dump(mainJson, outfile)