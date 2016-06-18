from PyQt4 import QtGui, QtCore
import json
import new_report_design


class Report(QtGui.QMainWindow, new_report_design.Ui_Form):
    def __init__(self, tableWidget, title, status,parent=None):
        super(Report, self).__init__(parent)
        self.setupUi(self)

        self.tableWidget = tableWidget
        self.title = title
        self.status = status
        self.rows = self.tableWidget.rowCount()

        """
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

        """

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