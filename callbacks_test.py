from PyQt4 import QtGui
from callbacks_helper import CallbacksHelper
import json
import requests
import time


class CallbacksTest:
    def __init__(self, table_widget, errorNumber):
        self.table_widget = table_widget
        self.errorNumber = errorNumber

        with open('./data/open_projects.json', 'r') as new_list:
            self.project_list = json.load(new_list)

        with open('./data/setup.json') as codeLines_data:
            self.setupJson = json.load(codeLines_data)

        self.secretKey = self.setupJson['secret_key']
        self.publicKey = self.setupJson['public_key']
        self.httpAddress = self.setupJson['https']
        self.main_user = self.setupJson['user']

        if len(self.project_list['projects']) == 0:
            print("No projects, run the test first!")
        else:
            self.test = CallbacksHelper()
            self.status_change()
            self.new_resource()
            self.comments_check()

    def status_change(self):
        rsc_list = []

        # Going through all the states of a project.
        for i in range(4):
            project_id = self.project_list['projects'][len(self.project_list['projects']) - 20 + (i*5)]
            self.test.project_status_change(project_id, "in_progress")
            time.sleep(2)
            self.test.project_status_change(project_id, "submitted")

            if i == 0:
                rsc_list.append(requests.get(self.httpAddress + "projects/" + project_id,
                                             params={"secret_key": self.secretKey, "public_key": self.publicKey},
                                             verify=False).json()["results"]["resources"]["translations"][0])
            if i == 1 or i == 2:
                rsc_list.append(requests.get(self.httpAddress + "projects/" + project_id,
                                             params={"secret_key": self.secretKey, "public_key": self.publicKey},
                                             verify=False).json()["results"]["resources"]["proofs"][0])

            if i == 3:
                rsc_list.append(requests.get(self.httpAddress + "projects/" + project_id,
                                             params={"secret_key": self.secretKey, "public_key": self.publicKey},
                                             verify=False).json()["results"]["resources"]["transcriptions"][0])
            time.sleep(2)
            self.test.project_status_change(project_id, "signed")
            time.sleep(2)
            self.test.project_status_change(project_id, "disputed")
            time.sleep(2)
            self.test.project_status_change(project_id, "pending")

        # Checking all callbacks params are ok.
        for i in range(4):
            project_id = self.project_list['projects'][len(self.project_list['projects']) - 20 + (i * 5)]
            self.test.check_callback(project_id, {"project_status_code": "in_progress", "project_id": project_id,
                                                  "event": "project.status.update"}, "status",
                                     self.table_widget, self.errorNumber)
            self.test.check_callback(project_id, {"project_status_code": "submitted", "project_id": project_id,
                                                  "resource_uuid": rsc_list[i],
                                                  "event": "project.resources.new"}, "status",
                                     self.table_widget, self.errorNumber)
            self.test.check_callback(project_id, {"project_status_code": "signed", "project_id": project_id,
                                                  "event":"project.status.update"}, "status",
                                     self.table_widget, self.errorNumber)
            self.test.check_callback(project_id, {"project_status_code": "disputed", "project_id": project_id,
                                                  "event": "project.status.update"}, "status",
                                     self.table_widget, self.errorNumber)
            self.test.check_callback(project_id, {"project_status_code": "pending", "project_id": project_id,
                                                  "event": "project.status.update"}, "status",
                                     self.table_widget, self.errorNumber)

    def new_resource(self):

        rsc_list = []
        for i in range(4):
            project_id = self.project_list['projects'][len(self.project_list['projects']) - 19 + (i * 5)]
            self.test.project_status_change(project_id, "in_progress")
            self.test.project_status_change(project_id, "submitted")
            self.test.project_status_change(project_id, "signed")

        # Check resource upload in signed state.
        for i in range(4):
            project_id = self.project_list['projects'][len(self.project_list['projects']) - 19 + (i * 5)]
            if i == 1:
                self.test.project_status_change(project_id, "submitted")
            else:
                self.test.project_status_change(project_id, "submitted_new")

            if i == 0:
                rsc_list.append(requests.get(self.httpAddress + "projects/" + project_id,
                                             params={"secret_key": self.secretKey, "public_key": self.publicKey},
                                             verify=False).json()["results"]["resources"]["translations"][1])
            if i == 1 or i == 2:
                rsc_list.append(requests.get(self.httpAddress + "projects/" + project_id,
                                             params={"secret_key": self.secretKey, "public_key": self.publicKey},
                                             verify=False).json()["results"]["resources"]["proofs"][1])

            if i == 3:
                rsc_list.append(requests.get(self.httpAddress + "projects/" + project_id,
                                             params={"secret_key": self.secretKey, "public_key": self.publicKey},
                                             verify=False).json()["results"]["resources"]["transcriptions"][1])

            self.test.change_user(1)

        for i in range(4):
            project_id = self.project_list['projects'][len(self.project_list['projects']) - 19 + (i * 5)]
            self.test.check_callback(project_id, {"project_status_code": "signed", "project_id": project_id,
                                                  "resource_uuid": rsc_list[i],
                                                  "event": "project.resources.new"}, "resource",
                                     self.table_widget, self.errorNumber)

        rsc_list = []
        for i in range(4):
            project_id = self.project_list['projects'][len(self.project_list['projects']) - 19 + (i * 5)]
            self.test.project_status_change(project_id, "disputed")

        # Check resource upload disputed state.
        project_id = self.project_list['projects'][len(self.project_list['projects']) - 19]
        self.test.project_status_change(project_id, "submitted_new")
        rsc_list.append(requests.get(self.httpAddress + "projects/" + project_id,
                                     params={"secret_key": self.secretKey, "public_key": self.publicKey},
                                     verify=False).json()["results"]["resources"]["translations"][2])

        project_id = self.project_list['projects'][len(self.project_list['projects']) - 4]
        self.test.project_status_change(project_id, "submitted_new")
        rsc_list.append(requests.get(self.httpAddress + "projects/" + project_id,
                                     params={"secret_key": self.secretKey, "public_key": self.publicKey},
                                     verify=False).json()["results"]["resources"]["transcriptions"][2])

        time.sleep(10)

        project_id = self.project_list['projects'][len(self.project_list['projects']) - 19]
        self.test.check_callback(project_id, {"project_status_code": "disputed", "project_id": project_id,
                                              "resource_uuid": rsc_list[0],
                                              "event": "project.resources.new"}, "resource",
                                 self.table_widget, self.errorNumber)

        project_id = self.project_list['projects'][len(self.project_list['projects']) - 4]
        self.test.check_callback(project_id, {"project_status_code": "disputed", "project_id": project_id,
                                              "resource_uuid": rsc_list[1],
                                              "event": "project.resources.new"}, "resource",
                                 self.table_widget, self.errorNumber)

    def comments_check(self):

        self.add_comments("pending", 18)
        self.test.change_user(1)
        self.add_comments("in_progress", 18)
        self.test.change_user(1)
        self.add_comments("submitted", 18)
        self.test.change_user(1)
        self.add_comments("signed", 18)
        self.test.change_user(1)
        self.add_comments("disputed", 18)
        self.test.change_user(1)

    def check_comment_callbacks(self, status, project_index, names):

        self.test.change_user(1)

        for i in range(4):
            project_id = self.project_list['projects'][len(self.project_list['projects']) - project_index + (i * 5)]

            self.test.check_callback(project_id, {"project_status_code": status, "project_id": project_id,
                                                  "event": "project.comments.new", "commenter_name": names[i*3],
                                                  "commenter_role": "customer"}, "customer_comment",
                                     self.table_widget, self.errorNumber)

            self.test.check_callback(project_id, {"project_status_code": status, "project_id": project_id,
                                                  "event": "project.comments.new", "commenter_name": names[i*3 + 1],
                                                  "commenter_role": "admin"}, "admin_comment",
                                     self.table_widget, self.errorNumber)
            if status == "pending":
                self.test.check_callback(project_id, {"project_status_code": status, "project_id": project_id,
                                                      "event": "project.comments.new", "commenter_name": names[i*3 + 2],
                                                      "commenter_role": "potential-provider"}, "trans_comment",
                                         self.table_widget, self.errorNumber)
            else:
                self.test.check_callback(project_id, {"project_status_code": status, "project_id": project_id,
                                                      "event": "project.comments.new",
                                                      "commenter_name": names[i * 3 + 2],
                                                      "commenter_role": "provider"}, "trans_comment",
                                         self.table_widget, self.errorNumber)

    def add_comments(self, status, project_index):
        names_list = []
        project_status_change = False

        for i in range(4):
            project_id = self.project_list['projects'][len(self.project_list['projects']) - project_index + (i * 5)]

            if status == "in_progress" and not project_status_change:
                self.test.project_status_change(project_id, "in_progress")
                project_status_change = True
            elif status == "submitted" and not project_status_change:
                self.test.project_status_change(project_id, "submitted")
                project_status_change = True
            elif status == "signed" and not project_status_change:
                self.test.project_status_change(project_id, "signed")
                project_status_change = True
            elif status == "disputed" and not project_status_change:
                self.test.project_status_change(project_id, "disputed")
                project_status_change = True
            elif status == "pending" and not project_status_change:
                project_status_change = True
            else:
                print("Incorrect project status")
                break

            self.test.open_project_page(project_id)

            names_list.append(self.test.post_comment(self.main_user, status))
            time.sleep(5)
            names_list.append(self.test.post_comment(1, status))
            time.sleep(5)
            if status == "pending":
                new_trans = self.test.find_new_translator(project_id)
                names_list.append(self.test.post_comment(new_trans, status))
            else:
                self.test.change_view_to_translator(project_id)
                names_list.append(self.test.post_comment(0, status))
            project_status_change = False
            self.test.change_user(1)

        self.check_comment_callbacks(status, project_index, names_list)