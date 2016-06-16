from PyQt4 import QtGui, QtCore
import json
import new_report_design


class Report(QtGui.QMainWindow, new_report_design.Ui_Form):
    def __init__(self, parent=None):
        super(Report, self).__init__(parent)
        self.setupUi(self)

        with open('./test_lines/00_Complete_Test.json') as codeLines_data:
            self.mainJson = json.load(codeLines_data)

        self.maxLines = len(self.mainJson['data'])

        hLabels = ('Line', 'Status')

        self.tableWidget.setRowCount(self.maxLines)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(hLabels)
        self.tableWidget.setColumnWidth(0, 500)
        self.tableWidget.horizontalHeader().setResizeMode(1, QtGui.QHeaderView.Stretch)

        for index in range(self.maxLines):
            self.tableWidget.setItem(index, 0, QtGui.QTableWidgetItem(self.mainJson['data'][index]['title']))
            self.tableWidget.setItem(index, 1, QtGui.QTableWidgetItem("ok"))


    def mark_green(self, index):
        self.tableWidget.item(index, 0).setBackground(QtGui.QColor(128, 255, 128))
        self.tableWidget.item(index, 1).setBackground(QtGui.QColor(128, 255, 128))

    def mark_red(self, index):
        self.tableWidget.item(index, 0).setBackground(QtGui.QColor(255, 140, 102))
        self.tableWidget.item(index, 1).setBackground(QtGui.QColor(255, 140, 102))