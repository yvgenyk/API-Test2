from PyQt4 import QtGui
from callbacks_helper import CallbacksHelper
import json
import requests


class CallbacksTest:
    def __init__(self):
        with open('./data/open_projects.json', 'r') as new_list:
            self.project_list = json.load(new_list)

        with open('./data/setup.json') as codeLines_data:
            self.setupJson = json.load(codeLines_data)

        self.secretKey = self.setupJson['secret_key']
        self.publicKey = self.setupJson['public_key']
        self.httpAddress = self.setupJson['https']

        if len(self.project_list['projects']) == 0:
            print("No projects, run the test first!")
        else:
            self.test = CallbacksHelper()
            self.status_change()
            self.new_resource()

    def status_change(self):
        rsc_list = []

        # Going through all the states of a project.
        for i in range(4):
            project_id = self.project_list['projects'][len(self.project_list['projects']) - 20 + (i*5)]
            self.test.project_status_change(project_id, "in_progress")
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

            self.test.project_status_change(project_id, "signed")
            self.test.project_status_change(project_id, "disputed")
            self.test.project_status_change(project_id, "pending")

        # Checking all callbacks params are ok.
        for i in range(4):
            project_id = self.project_list['projects'][len(self.project_list['projects']) - 20 + (i * 5)]
            self.test.check_callback(project_id, {"project_status_code": "in_progress", "project_id": project_id,
                                                  "event": "project.status.update"}, "status")
            self.test.check_callback(project_id, {"project_status_code": "submitted", "project_id": project_id,
                                                  "resource_uuid": rsc_list[i], "event": "project.resources.new"}, "status")
            self.test.check_callback(project_id, {"project_status_code": "signed", "project_id": project_id,
                                                  "event":"project.status.update"}, "status")
            self.test.check_callback(project_id, {"project_status_code": "disputed", "project_id": project_id,
                                                  "event": "project.status.update"}, "status")
            self.test.check_callback(project_id, {"project_status_code": "pending", "project_id": project_id,
                                                  "event": "project.status.update"}, "status")

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

        for i in range(4):
            project_id = self.project_list['projects'][len(self.project_list['projects']) - 19 + (i * 5)]
            self.test.check_callback(project_id, {"project_status_code": "signed", "project_id": project_id,
                                                  "resource_uuid": rsc_list[i], "event": "project.resources.new"}, "resource")

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

        project_id = self.project_list['projects'][len(self.project_list['projects']) - 19]
        self.test.check_callback(project_id, {"project_status_code": "disputed", "project_id": project_id,
                                              "resource_uuid": rsc_list[0], "event": "project.resources.new"}, "resource")

        project_id = self.project_list['projects'][len(self.project_list['projects']) - 4]
        self.test.check_callback(project_id, {"project_status_code": "disputed", "project_id": project_id,
                                              "resource_uuid": rsc_list[1], "event": "project.resources.new"}, "resource")