from PyQt4 import QtGui
from callbacks_helper import CallbacksHelper
import json


class CallbacksTest:
    def __init__(self):
        with open('./data/open_projects.json', 'r') as new_list:
            self.project_list = json.load(new_list)

        if len(self.project_list['projects']) == 0:
            print("No projects, run the test first!")
        else:
            self.test = CallbacksHelper()
            self.status_change()

    def status_change(self):
        for i in range(4):
            project_id = self.project_list['projects'][len(self.project_list['projects']) - 20 + (i*5)]
            self.test.project_status_change(project_id, "in_progress")
            self.test.project_status_change(project_id, "submitted")
            self.test.project_status_change(project_id, "signed")
            self.test.project_status_change(project_id, "disputed")
            self.test.project_status_change(project_id, "pending")

        for i in range(4):
            project_id = self.project_list['projects'][len(self.project_list['projects']) - 20 + (i * 5)]
            self.test.check_callback(project_id, "in_progress")
            self.test.check_callback(project_id, "submitted")
            self.test.check_callback(project_id, "signed")
            self.test.check_callback(project_id, "disputed")
            self.test.check_callback(project_id, "pending")
