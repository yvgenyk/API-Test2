from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import json
from new_report import Report
import os


class CallbacksHelper:
    def __init__(self):
        self.file_path = os.path.abspath("./Other_Files/Untitled_Document.txt")
        self.driver = webdriver.Chrome('./chromedriver')
        self.driver_wait = WebDriverWait(self.driver, 10)
        self.driver.maximize_window()
        self.driver.get("https://oht.vagrant.oht.cc/translation/home")
        assert "Translation Services" in self.driver.title
        self.driver_wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="header_user_section"]/li/button[1]/strong')))
        elem = self.driver.find_element_by_xpath('//*[@id="header_user_section"]/li/button[1]/strong')
        elem.click()
        self.driver_wait.until(EC.presence_of_element_located((By.ID, "desktop_login_username")))
        elem = self.driver.find_element_by_id("desktop_login_username")
        elem.send_keys("admin")
        self.driver_wait.until(EC.presence_of_element_located((By.ID, "desktop_login_password")))
        elem = self.driver.find_element_by_id("desktop_login_password")
        elem.send_keys("admin")
        self.driver_wait.until(EC.presence_of_element_located((By.ID, "header_login_button")))
        elem = self.driver.find_element_by_id("header_login_button")
        elem.click()
        time.sleep(1)

    def project_status_change(self, project_id, status):

        if status == "in_progress":
            self.find_new_translator(project_id)
            if self.driver_wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Start Project"))):
                self.driver.find_element_by_link_text("Start Project").click()
                time.sleep(1)
                self.driver_wait.until(
                    EC.presence_of_element_located((By.XPATH, "/html/body/div[11]/form/p/button")))
                self.driver.find_element_by_xpath("/html/body/div[11]/form/p/button").click()
                time.sleep(1)
                self.driver_wait.until(EC.presence_of_element_located((By.ID, "confirm_project_note")))
                self.driver.find_element_by_id("confirm_project_note").click()
                time.sleep(1)
                if self.driver.find_elements_by_xpath("//*[contains(text(), 'Translation in progress')]") \
                        or self.driver.find_elements_by_xpath("//*[contains(text(), 'Proofreading in progress')]") \
                        or self.driver.find_elements_by_xpath("//*[contains(text(), 'Transcription in progress')]"):
                    self.change_user(1)
                else:
                    print("Not there")

        elif status == "submitted":
            self.change_view_to_translator(project_id)
            time.sleep(3)
            self.driver_wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="file"][name="translation"]')))
            self.driver.find_element_by_css_selector('input[type="file"][name="translation"]').clear()
            self.driver.find_element_by_css_selector('input[type="file"][name="translation"]').send_keys(self.file_path)
            time.sleep(3)
            self.change_user(1)
            return True

        elif status == "submitted_new":
            self.change_view_to_translator(project_id)
            time.sleep(1)
            self.driver_wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="file"][name="translation"]')))
            self.driver.find_element_by_css_selector('input[type="file"][name="translation"]').clear()
            self.driver.find_element_by_css_selector('input[type="file"][name="translation"]').send_keys(self.file_path)
            time.sleep(1)
            self.driver_wait.until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[12]/form/p[2]/textarea")))
            elem = self.driver.find_element_by_xpath("/html/body/div[12]/form/p[2]/textarea")
            elem.click()
            elem.send_keys("Please leave a comment to the customer regarding what was updated in the translation and why.")
            time.sleep(1)
            self.driver_wait.until(
                EC.presence_of_element_located((By.XPATH, '/html/body/div[12]/form/p[3]/button')))
            self.driver.find_element_by_xpath('/html/body/div[12]/form/p[3]/button').click()
            time.sleep(3)
            self.change_user(1)
            return True

        elif status == "signed":
            self.change_view_to_translator(project_id)
            time.sleep(1)
            if self.driver_wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Declare Completed"))):
                self.driver_wait.until(
                    EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/div/div[2]/div[1]/div[1]/div[2]/p[1]/b")))
                trans_name = self.driver.find_element_by_xpath(
                    "/html/body/div[5]/div/div[2]/div[1]/div[1]/div[2]/p[1]/b")
                trans_name = trans_name.text
                trans_name = trans_name.split(" ")
                self.driver_wait.until(
                    EC.presence_of_element_located((By.LINK_TEXT, "Declare Completed")))
                self.driver.find_element_by_link_text("Declare Completed").click()
                time.sleep(4)
                self.driver_wait.until(
                    EC.presence_of_element_located((By.ID, 'user-username')))
                self.driver.find_element_by_id('user-username').send_keys(trans_name[1])
                time.sleep(1)
                self.driver_wait.until(EC.presence_of_element_located(
                        (By.XPATH, "/html/body/div[11]/div/div[2]/form/p[3]/button")))
                self.driver.find_element_by_xpath("/html/body/div[11]/div/div[2]/form/p[3]/button").click()

            if self.driver.find_elements_by_xpath("//*[contains(text(), 'Translation has been submitted')]") \
                    or self.driver.find_elements_by_xpath("//*[contains(text(), 'Proofread submitted')]") \
                    or self.driver.find_elements_by_xpath("//*[contains(text(), 'Transcription has been submitted')]"):
                self.change_user(1)
            else:
                print("Something went wrong: Signed")

        elif status == "disputed":
            self.change_view_to_customer(project_id)
            time.sleep(1)
            if self.driver_wait.until(EC.presence_of_element_located(
                        (By.XPATH, "/html/body/div[5]/div/div[6]/div[1]/div[3]/p/b"))):
                self.driver.find_element_by_xpath("/html/body/div[5]/div/div[6]/div[1]/div[3]/p/b").click()
                time.sleep(1)
                self.driver_wait.until(EC.presence_of_element_located(
                    (By.NAME, "dispute")))
                self.driver.find_element_by_name("dispute").send_keys(
                    "Please open a dispute only if the issue was not resolved using the discussion board")
                time.sleep(1)
                self.driver_wait.until(EC.presence_of_element_located(
                    (By.XPATH, "/html/body/div[5]/div/div[6]/div[1]/div[3]/div/form/p[3]/button")))
                self.driver.find_element_by_xpath(
                    "/html/body/div[5]/div/div[6]/div[1]/div[3]/div/form/p[3]/button").click()
                time.sleep(1)
                self.change_user(1)
            if not self.driver_wait.until(EC.presence_of_element_located(
                    (By.XPATH, "//*[contains(text(), 'Dispute has been submitted')]"))):
                print("Something went wrong: Dispute")

        elif status == "pending":
            self.driver.get("https://oht.vagrant.oht.cc/project/" + str(project_id))
            time.sleep(1)
            self.driver_wait.until(EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[5]/div/div[3]/div[1]/div[1]")))
            self.driver.find_element_by_xpath("/html/body/div[5]/div/div[3]/div[1]/div[1]").click()
            time.sleep(1)
            self.driver_wait.until(EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[5]/div/div[3]/div[1]/div[2]/div/form/p[1]/input[1]")))
            self.driver.find_element_by_xpath(
                "/html/body/div[5]/div/div[3]/div[1]/div[2]/div/form/p[1]/input[1]").click()
            if self.driver.find_elements_by_xpath("//*[contains(text(), 'Waiting for a translator')]") \
                    or self.driver.find_elements_by_xpath("//*[contains(text(), 'Waiting for a editor')]") \
                    or self.driver.find_elements_by_xpath("//*[contains(text(), 'Waiting for a transcriber')]"):
                self.change_user(1)
            else:
                print("Something went wrong: Pending")
        else:
            print("incorrect status")

    def change_view_to_customer(self, project_id):
        self.driver.get("https://oht.vagrant.oht.cc/project/" + str(project_id))
        self.driver_wait.until(EC.presence_of_element_located(
            (By.ID, "toggleAdminFloatPanel")))
        self.driver.find_element_by_id("toggleAdminFloatPanel").click()
        time.sleep(2)
        self.driver_wait.until(EC.presence_of_element_located(
            (By.ID, "customerAct")))
        self.driver.find_element_by_id("customerAct").click()

    def change_view_to_translator(self, project_id):
        self.driver.get("https://oht.vagrant.oht.cc/project/" + str(project_id))
        self.driver_wait.until(EC.presence_of_element_located(
            (By.ID, "toggleAdminFloatPanel")))
        self.driver.find_element_by_id("toggleAdminFloatPanel").click()
        time.sleep(2)
        self.driver_wait.until(EC.presence_of_element_located(
            (By.ID, "translatorAct")))
        self.driver.find_element_by_id("translatorAct").click()

    def find_new_translator(self, project_id):
        self.driver.get("https://oht.vagrant.oht.cc/project/" + str(project_id))
        self.driver_wait.until(EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[5]/div/div[3]/div[1]/div[1]")))
        elem = self.driver.find_element_by_xpath("/html/body/div[5]/div/div[3]/div[1]/div[1]")
        elem.click()
        self.driver_wait.until(EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[5]/div/div[3]/div[1]/div[2]/div/div[1]/div[1]/table")))
        elem = self.driver.find_element_by_xpath("/html/body/div[5]/div/div[3]/div[1]/div[2]/div/div[1]/div[1]/table")
        translators_array = elem.text.split("\n")
        trans_id = 0
        for trans in translators_array:
            trans = trans.split(" ")
            self.change_user(trans[0])
            time.sleep(1)
            if self.driver.find_elements_by_link_text("Start Project"):
                trans_id = trans[0]
                break

        if trans_id:
            return trans_id
        else:
            print("Something went wrong: No allocated translators")

    def get_callback(self, project_id, entry):
        self.driver.get("https://oht.vagrant.oht.cc/project/" + str(project_id))
        time.sleep(1)
        self.driver_wait.until(EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[5]/div/div[5]/div[2]/div[1]/div/table/tbody/tr[" + str(entry) +"]/td[4]")))
        elem = self.driver.find_element_by_xpath(
            "/html/body/div[5]/div/div[5]/div[2]/div[1]/div/table/tbody/tr[" + str(entry) +"]/td[4]").find_element_by_link_text("More")
        elem.click()
        time.sleep(1)
        self.driver_wait.until(EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[12]/div[1]/table/tbody/tr[5]/td[2]/textarea")))
        elem = self.driver.find_element_by_xpath("/html/body/div[12]/div[1]/table/tbody/tr[5]/td[2]/textarea")
        time.sleep(1)

        return elem.text

    def check_callback(self, project_id, params, check_type, table_widget, errorNumber):
        report_line = Report(table_widget,
                             (check_type + ": Status: " + params["project_status_code"] + " project id: " + project_id), 200)
        if check_type == "status":
            report_line = Report(table_widget, (check_type + " change: " + params["project_status_code"] + " project id: " + project_id), 200)
            if params["project_status_code"] == "in_progress":
                callback = json.loads(self.get_callback(project_id, 5))
            elif params["project_status_code"] == "submitted":
                callback = json.loads(self.get_callback(project_id, 4))
            elif params["project_status_code"] == "signed":
                callback = json.loads(self.get_callback(project_id, 3))
            elif params["project_status_code"] == "disputed":
                callback = json.loads(self.get_callback(project_id, 2))
            elif params["project_status_code"] == "pending":
                callback = json.loads(self.get_callback(project_id, 1))

        elif check_type == "resource":
            report_line = Report(table_widget, (
            check_type + " upload: Project status: " + params["project_status_code"] + " project id " + project_id), 200)
            callback = json.loads(self.get_callback(project_id, 1))

        elif check_type == "customer_comment":
            callback = json.loads(self.get_callback(project_id, 3))

        elif check_type == "admin_comment":
            callback = json.loads(self.get_callback(project_id, 2))

        elif check_type == "trans_comment":
            callback = json.loads(self.get_callback(project_id, 1))

        else:
            print("Error!")

        report_line.print_line(200)
        report_line.report_line("", str(callback), "", "")
        report_line.mark_green()

        for param in params:
            param_found = False
            for callback_param in callback:
                if callback_param == param:
                    param_found = True
                    if callback[param] != params[param]:
                        report_line.mark_red(errorNumber)
                        report_line.report_line_find("Incorrect param found: " + param + " " + params[param])
                    else:
                        report_line.report_line_check(callback[param], params[param], param)

            if not param_found:
                report_line.mark_red(errorNumber)
                report_line.report_line_find("Param not found: " + param)

    def change_user(self, new_user):
        time.sleep(2)
        self.driver_wait.until(EC.presence_of_element_located((By.ID, "toggleAdminFloatPanel")))
        self.driver.find_element_by_id("toggleAdminFloatPanel").click()
        time.sleep(1)
        if new_user == 1:
            if self.driver_wait.until(EC.presence_of_element_located((By.ID, "ToggleAdminRights"))):
                time.sleep(1)
                self.driver.find_element_by_id("ToggleAdminRights").click()
                time.sleep(1)
        else:
            self.driver_wait.until(EC.presence_of_element_located((By.ID, "uidFloat")))
            elem = self.driver.find_element_by_id("uidFloat")
            elem.send_keys(new_user)
            self.driver_wait.until(EC.presence_of_element_located((By.ID, "generalAct")))
            elem = self.driver.find_element_by_id("generalAct")
            time.sleep(1)
            elem.click()

    def open_project_page(self, project_id):
        self.driver.get("https://oht.vagrant.oht.cc/project/" + str(project_id))

    def post_comment(self, user_id, status):

        if user_id != 0:
            self.change_user(user_id)
        time.sleep(1)
        name = self.get_name()
        comment = self.create_comment(status, name)
        self.driver_wait.until(EC.presence_of_element_located((By.ID, "add")))
        self.driver.find_element_by_id("add").find_element_by_name("comment").send_keys(comment)
        self.driver.find_element_by_id("add").find_element_by_css_selector('button[type="submit"]').click()

        return name

    def create_comment(self, status, name):
        return "User: " + name + " comment, project status: " + status

    def get_name(self):
        name = ""
        self.driver_wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[class="user-menu float-r"]')))
        string = self.driver.find_element_by_css_selector('div[class="user-menu float-r"]').text.split("\n")[0]
        string = string.split(" ")
        for n in string:
            if n != "Welcome":
                name += (n + " ")

        return name[:len(name)-1]
