from PyQt4 import QtGui
import additional_testing_design
import json


class AdditionalTesting(QtGui.QMainWindow, additional_testing_design.Ui_Form):
    def __init__(self, parent=None):
        super(AdditionalTesting, self).__init__(parent)
        self.setupUi(self)

        self.show_projects()

    def show_projects(self):
        with open('./data/open_projects.json', 'r') as new_list:
            project_list = json.load(new_list)

        self.reg_proj.setText("")
        self.proof_one.setText("")
        self.proof_two.setText("")
        self.transcript.setText("")

        if len(project_list["projects"]) > 20:
            projects = ''
            for i in range(5):
                projects += ("#" + project_list["projects"][len(project_list["projects"]) - 20 + i] + " ")
            self.reg_proj.setText(projects)

            projects = ''
            for i in range(5):
                projects += ("#" + project_list["projects"][len(project_list["projects"]) - 15 + i] + " ")
            self.proof_one.setText(projects)

            projects = ''
            for i in range(5):
                projects += ("#" + project_list["projects"][len(project_list["projects"]) - 10 + i] + " ")
            self.proof_two.setText(projects)

            projects = ''
            for i in range(5):
                projects += ("#" + project_list["projects"][len(project_list["projects"]) - 5 + i] + " ")
            self.transcript.setText(projects)
