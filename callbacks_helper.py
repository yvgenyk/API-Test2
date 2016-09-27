from selenium import webdriver
import time
import json


class CallbacksHelper:
    def __init__(self):
        self.driver = webdriver.Chrome('./chromedriver')
        self.driver.maximize_window()
        self.driver.get("https://oht.vagrant.oht.cc/translation/home")
        assert "Translation Services" in self.driver.title
        elem = self.driver.find_element_by_xpath('//*[@id="header_user_section"]/li/button[1]/strong')
        elem.click()
        elem = self.driver.find_element_by_id("desktop_login_username")
        elem.send_keys("admin")
        elem = self.driver.find_element_by_id("desktop_login_password")
        elem.send_keys("admin")
        elem = self.driver.find_element_by_id("header_login_button")
        elem.click()
        time.sleep(1)

    def project_status_change(self, project_id, status):

        if status == "in_progress":
            self.find_new_translator(project_id)
            if self.driver.find_elements_by_link_text("Start Project"):
                self.driver.find_element_by_link_text("Start Project").click()
                time.sleep(1)
                self.driver.find_element_by_xpath("/html/body/div[11]/form/p/button").click()
                time.sleep(1)
                self.driver.find_element_by_id("confirm_project_note").click()
                time.sleep(1)
                if self.driver.find_elements_by_xpath("//*[contains(text(), 'Translation in progress')]") \
                        or self.driver.find_elements_by_xpath("//*[contains(text(), 'Proofreading in progress')]") \
                        or self.driver.find_elements_by_xpath("//*[contains(text(), 'Transcription in progress')]"):
                    self.change_user(1)
                    return True
                else:
                    print("Not there")

        elif status == "submitted":
            self.change_view_to_translator(project_id)
            time.sleep(1)
            self.driver.find_element_by_css_selector('input[type="file"][name="translation"]').clear()
            self.driver.find_element_by_css_selector('input[type="file"]').send_keys(
                "/home/oht/Downloads/fb-status.json")
            time.sleep(3)
            self.change_user(1)
            # Add some stuff to validate upload.
            return True

        elif status == "signed":
            self.change_view_to_translator(project_id)
            time.sleep(1)
            if self.driver.find_elements_by_link_text("Declare Completed"):
                trans_name = self.driver.find_element_by_xpath(
                    "/html/body/div[5]/div/div[2]/div[1]/div[1]/div[2]/p[1]/b")
                trans_name = trans_name.text
                trans_name = trans_name.split(" ")
                self.driver.find_element_by_link_text("Declare Completed").click()
                time.sleep(1)
                self.driver.find_element_by_id('user-username').send_keys(trans_name[1])
                time.sleep(1)
                self.driver.find_element_by_xpath("/html/body/div[11]/div/div[2]/form/p[3]/button").click()
            if self.driver.find_elements_by_xpath("//*[contains(text(), 'Translation has been submitted')]") \
                    or self.driver.find_elements_by_xpath("//*[contains(text(), 'Proofread submitted')]") \
                    or self.driver.find_elements_by_xpath("//*[contains(text(), 'Transcription has been submitted')]"):
                self.change_user(1)
                return True
            else:
                print("Something went wrong: Signed")

        elif status == "disputed":
            self.change_view_to_customer(project_id)
            time.sleep(1)
            if self.driver.find_elements_by_xpath("/html/body/div[5]/div/div[6]/div[1]/div[3]/p"):
                self.driver.find_element_by_xpath("/html/body/div[5]/div/div[6]/div[1]/div[3]/p").click()
                time.sleep(1)
                self.driver.find_element_by_name("dispute").send_keys(
                    "Please open a dispute only if the issue was not resolved using the discussion board")
                time.sleep(1)
                self.driver.find_element_by_xpath(
                    "/html/body/div[5]/div/div[6]/div[1]/div[3]/div/form/p[3]/button").click()
                time.sleep(1)
                self.change_user(1)
            if self.driver.find_elements_by_xpath("//*[contains(text(), 'Dispute has been submitted')]"):
                return True
            else:
                print("Something went wrong: Dispute")

        elif status == "pending":
            self.driver.get("https://oht.vagrant.oht.cc/project/" + str(project_id))
            time.sleep(1)
            self.driver.find_element_by_xpath("/html/body/div[5]/div/div[3]/div[1]/div[1]").click()
            time.sleep(1)
            self.driver.find_element_by_xpath(
                "/html/body/div[5]/div/div[3]/div[1]/div[2]/div/form/p[1]/input[1]").click()
            if self.driver.find_elements_by_xpath("//*[contains(text(), 'Waiting for a translator')]") \
                    or self.driver.find_elements_by_xpath("//*[contains(text(), 'Waiting for a editor')]") \
                    or self.driver.find_elements_by_xpath("//*[contains(text(), 'Waiting for a transcriber')]"):
                self.change_user(1)
                return True
            else:
                print("Something went wrong: Pending")
        else:
            print("incorrect status")

    def change_view_to_customer(self, project_id):
        self.driver.get("https://oht.vagrant.oht.cc/project/" + str(project_id))
        elem = self.driver.find_element_by_id("toggleAdminFloatPanel")
        elem.click()
        elem = self.driver.find_element_by_id("customerAct")
        elem.click()

    def change_view_to_translator(self, project_id):
        self.driver.get("https://oht.vagrant.oht.cc/project/" + str(project_id))
        elem = self.driver.find_element_by_id("toggleAdminFloatPanel")
        elem.click()
        elem = self.driver.find_element_by_id("translatorAct")
        elem.click()

    def find_new_translator(self, project_id):
        self.driver.get("https://oht.vagrant.oht.cc/project/" + str(project_id))
        elem = self.driver.find_element_by_xpath("/html/body/div[5]/div/div[3]/div[1]/div[1]")
        elem.click()
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

    def check_callback(self, project_id, params):
        self.driver.get("https://oht.vagrant.oht.cc/project/" + str(project_id))
        time.sleep(1)
        elem = self.driver.find_element_by_xpath(
            "/html/body/div[5]/div/div[5]/div[2]/div[1]/div/table/tbody/tr[1]/td[4]").find_element_by_link_text("More")
        elem.click()
        time.sleep(1)
        elem = self.driver.find_element_by_xpath("/html/body/div[12]/div[1]/table/tbody/tr[5]/td[2]/textarea")
        time.sleep(1)
        callback = json.loads(elem.text)

        for param in params:
            param_not_found = False
            for callback_param in callback:
                if callback_param == param:
                    param_not_found = True
                    if callback[param] != params[param]:
                        return "Incorrect param found: " + param + " " + params[param]

            if not param_not_found:
                return "Param not found: " + param

        return "True"

    def change_user(self, new_user):
        elem = self.driver.find_element_by_id("toggleAdminFloatPanel")
        elem.click()
        if new_user == 1:
            self.driver.find_element_by_id("ToggleAdminRights").click()
            time.sleep(1)
        else:
            elem = self.driver.find_element_by_id("uidFloat")
            elem.send_keys(new_user)
            elem = self.driver.find_element_by_id("generalAct")
            time.sleep(1)
            elem.click()

    """
    def find_languages(self, project_id):
        source_language = ""
        target_language = ""
        self.driver.get("https://oht.vagrant.oht.cc/project/" + str(project_id))
        elem = self.driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/h2")
        split = elem.text.split(" ")

        if split[0] == "Translation":
            elem = self.driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/div[1]/div[2]/h3")
            split_lang = elem.text.split(" ")
            source_language = split_lang[0]
            target_language = split_lang[2]
        elif split[0] == "Proofreading":
            elem = self.driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/div[1]/div[1]/h3")
            split_lang = elem.text.split(" ")
            if len(split_lang) == 2:
                source_language = split_lang[0]
                target_language = split_lang[0]
            else:
                source_language = split_lang[0]
                target_language = split_lang[2]
        elif split[0] == "Transcription":
            elem = self.driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/div[1]/div[1]/h3")
            split_lang = elem.text.split(" ")
            source_language = split_lang[0]
            target_language = split_lang[0]

        return [source_language, target_language]
    """