from PyQt4 import QtGui, QtCore
import main_design
import requests
import os
from new_report import Report
import json
from random import randint
import time
import re
from resource_class import Resource
from PyQt4.QtCore import QThread, SIGNAL

                    
"""""""""""""""""""""""""""""""""""""""""""""
                    Response

This class is handeling the response after 
API call.


"""""""""""""""""""""""""""""""""""""""""""""        
class Response:
    """""""""""""""""""""""""""""""""
    Initializing the object with
    the basic thing for the program.
    """""""""""""""""""""""""""""""""
    def __init__(self, res, notDownload):

        self.r = res
        self.responseURL = self.r.url
        self.responseStatus = self.r.status_code
        self.responseText = self.r.text
        self.header = self.r.headers
        self.content = self.r.content
        if self.responseStatus == 200 and notDownload:
            self.responseJson = self.r.json()
        else:
            self.responseJson = None

    """""""""""""""""""""""""""
    Returns the requested URL.
    """""""""""""""""""""""""""
    def getURL(self):
        return self.responseURL
    
    """""""""""""""""""""""""""
    Return request status.
    """""""""""""""""""""""""""
    def getStatus(self):
        return self.responseStatus
    
    """""""""""""""""""""""""""
    Returns response as text.
    """""""""""""""""""""""""""
    def getText(self):
        return self.responseText
    """""""""""""""""""""""""""
    Returns response as JSON 
    format.
    """""""""""""""""""""""""""
    def getJson(self):
        return self.responseJson

    def getHeader(self):
        return self.header

    def getContent(self):
        return self.content
        
    """""""""""""""""""""""""""""""""""""""""""""""""""""
    Prints the request and the response in the text editor
    of the program for later review.
    """""""""""""""""""""""""""""""""""""""""""""""""""""
    def report_line_to_main_window(self, reportLine, errorNumber):
        reportLine.print_line(errorNumber)
        reportLine.mark_yellow()
        
    """""""""""""""""""""""""""""""""""""""""""""""""""""
    Find method, if there is a request to find something 
    in the response, this method will find it.
    """""""""""""""""""""""""""""""""""""""""""""""""""""
    def find(self,data, reportLine, errorNumber):
        for findIndex in range(len(data['find'])):
            if data['find'][findIndex] in self.getText() and reportLine.get_color() != "red":
                reportLine.mark_green()
                reportLine.report_line_find(data['find'][findIndex])
            else:
                if len(self.getText()) > 500:
                    reportLine.mark_red(errorNumber)
                    reportLine.report_line_find(data['find'][findIndex])
                else:
                    reportLine.mark_red(errorNumber)
                    reportLine.report_line_find(data['find'][findIndex])
        
    """""""""""""""""""""""""""""""""""""""""""""""""""""
    Check method, if there is certain values to check 
    in the response, this method will check them.
    """""""""""""""""""""""""""""""""""""""""""""""""""""
    def check_value(self, data, reportLine, prevPayload, rsc_uuid, errorNumber):

        with open('./data/words_prices.json') as codeLines_data:
            dataJson = json.load(codeLines_data)

        for valIndex in range(len(data['check'])):

            varToCheck = str(data["check"][valIndex])
            splitVarToCheck = varToCheck.split('-')

            """""""""""""""""""""""""""""""""""""""""""""
            If there is "@" sign it means that there
            is a value to check from previous payload.
            This if will erase the "@" sign and take the
            original value from prev payload to find
            in the new response.
            """""""""""""""""""""""""""""""""""""""""""""
            if splitVarToCheck[0][0] == "@":
                splitVarToCheck[0] = splitVarToCheck[0][1:]

                valueToCheck = prevPayload[0][splitVarToCheck[len(splitVarToCheck)-1]]

            elif varToCheck == 'save-languages':
                with open('./data/languages.json') as codeLines_data:
                    langJson = json.load(codeLines_data)

                with open('./data/languages.json', 'w') as outfile:
                    for results in self.getJson()['results']:
                        for target in results['targets']:
                            langJson.append({results['source']['code'] : target['code']})
                    json.dump(langJson, outfile)

                break

                # If there is no need for prev payload,
                # the value checked is provided in the
                # parameters.

            else:
                valueToCheck = data['value'][valIndex]


            resJson = self.getJson()

            #This will go through the path of the response to find the value we are checking.
            for res in splitVarToCheck:
                if res[0] == '#':
                    resJson = resJson[int(res[1])]
                else:
                    resJson = resJson[res]

            #The files correct format is checked in a different function. Here we check only the name.
            if splitVarToCheck[len(splitVarToCheck) - 1] == "file_name":
                if valueToCheck in str(resJson) and reportLine.get_color() != "red":
                    reportLine.mark_green()
                    reportLine.report_line_check(valueToCheck, str(resJson), splitVarToCheck[len(splitVarToCheck) - 1])
                else:
                    reportLine.mark_red(errorNumber)
                    reportLine.report_line_check(valueToCheck, str(resJson), splitVarToCheck[len(splitVarToCheck) - 1])
                    break

            elif splitVarToCheck[len(splitVarToCheck) - 1] == "wordcount":
                total_words = 0

                if valueToCheck == "pre_defined":
                    with open('./report/test_report.json') as codeLines_data:
                        mainJson = json.load(codeLines_data)
                        total_words = mainJson[len(mainJson)-1]["payload"]["wordcount"]
                else:
                    for uuid in rsc_uuid:
                        total_words += dataJson[0][uuid]['wordcount']


                if int(total_words) >= int(resJson) and reportLine.get_color() != "red":
                    reportLine.mark_green()
                    reportLine.report_line_check(total_words, str(resJson), splitVarToCheck[len(splitVarToCheck) - 1])
                else:
                    reportLine.mark_red(errorNumber)
                    reportLine.report_line_check(total_words, str(resJson), splitVarToCheck[len(splitVarToCheck) - 1])
                    break

            elif splitVarToCheck[len(splitVarToCheck) - 1] == "credits":
                total_price = 0

                if valueToCheck == "regular":
                    for uuid in rsc_uuid:
                        total_price += dataJson[0][uuid]['reg_proj_price']

                if valueToCheck == "expert":
                    for uuid in rsc_uuid:
                        total_price += dataJson[0][uuid]['expert_proj_price']

                if valueToCheck == "proof":
                    for uuid in rsc_uuid:
                        total_price += dataJson[0][uuid]['proof_proj_price']

                if valueToCheck == "combo":
                    for uuid in rsc_uuid:
                        total_price += dataJson[0][uuid]['combo_proj_price']

                if valueToCheck == "transcrip":
                    for uuid in rsc_uuid:
                        total_price += dataJson[0][uuid]['trranscrip_proj_price']

                if total_price >= resJson and reportLine.get_color() != "red":
                    reportLine.mark_green()
                    reportLine.report_line_check(total_price, str(resJson),
                                                 splitVarToCheck[len(splitVarToCheck) - 1])
                else:
                    reportLine.mark_red(errorNumber)
                    reportLine.report_line_check(total_price, str(resJson),
                                                 splitVarToCheck[len(splitVarToCheck) - 1])
                break

            #This is the main search method.
            else:
                if valueToCheck == str(resJson) and reportLine.get_color() != "red":
                    reportLine.mark_green()
                    if splitVarToCheck[len(splitVarToCheck) - 1][0] == "#":
                        reportLine.report_line_check(valueToCheck, str(resJson),
                                                     splitVarToCheck[len(splitVarToCheck) - 2])
                    else:
                        reportLine.report_line_check(valueToCheck, str(resJson),
                                                     splitVarToCheck[len(splitVarToCheck) - 1])
                else:
                    reportLine.mark_red(errorNumber)
                    if splitVarToCheck[len(splitVarToCheck) - 1][0] == "#":
                        reportLine.report_line_check(valueToCheck, str(resJson),
                                                     splitVarToCheck[len(splitVarToCheck) - 2])
                    else:
                        reportLine.report_line_check(valueToCheck, str(resJson),
                                                     splitVarToCheck[len(splitVarToCheck) - 1])
                    break

        
"""""""""""""""""""""""""""""""""""""""""""""""""""
                    Get Method Class

    This class will handle all the get requests.


"""""""""""""""""""""""""""""""""""""""""""""""""""        
class GetMethod:
        
        def __init__(self, data):
            self.testLine = data
            self.rsc_uuid = []
            with open('./data/languages.json') as codeLines_data:
                self.langJson = json.load(codeLines_data)
        """""""""""""""""""""""""""""""""
        The get method itself, will get
        everything it needs from the main 
        class and execute the request. 
        """""""""""""""""""""""""""""""""
        def get_method(self, secretKey, publicKey, httpAddress, prevResponse, prevPayload, tableWidget, testFilePath,
                       uploadFileUUID, txtFileUUID, errorNumber):

            uuidToAddress = 0
            payload = dict()
            downloadResource = 0
            noKeysFlag = False
            
            """""""""""""""""""""""""""""""""""""""""""""
            Collecting all the data from the instruction 
            file to execute the request.
            Including secret key, public key, address
            and any other data needed for the request
            """""""""""""""""""""""""""""""""""""""""""""
            for payIndex in range(len(self.testLine['params'])):
                    
                if self.testLine["params"][payIndex] == "secret_key":
                    payload[self.testLine["params"][payIndex]] = secretKey
                            
                elif self.testLine["params"][payIndex] == "public_key":
                    payload[self.testLine["params"][payIndex]] = publicKey

                elif 'name' in self.testLine["params"][payIndex]:

                    # Randomly Choosing a language pair out of the initialized on site.
                    if self.testLine["params"][payIndex]['name'] == "language_pair":

                        lang_pair = randint(0, len(self.langJson)-1)
                        for source in self.langJson[lang_pair]:
                            payload['source_language'] = source
                            payload['target_language'] = self.langJson[lang_pair][source]

                    # Randomly Choosing source language
                    elif self.testLine["params"][payIndex]['name'] == "source_language":
                        lang_pair = randint(0, len(self.langJson) - 1)
                        for source in self.langJson[lang_pair]:
                            payload['source_language'] = source

                    # Randomly choosing target language.
                    elif self.testLine["params"][payIndex]['name'] == "target_language":
                        lang_pair = randint(0, len(self.langJson) - 1)
                        for source in self.langJson[lang_pair]:
                            payload['target_language'] = self.langJson[lang_pair][source]

                    elif self.testLine["params"][payIndex]['name'] == "resources":
                        self.ex_resource(self.testLine["params"][payIndex], payload, txtFileUUID, uploadFileUUID)
                    else:
                        payload[self.testLine["params"][payIndex]['name']] = self.testLine["params"][payIndex]['value']

                elif self.testLine["params"][payIndex] == "No Secret Key" or self.testLine["params"][payIndex] == "No Public Key":
                    noKeysFlag = True

            """""""""""""""""""""""""""""""""""""""""
            If an input from earlier request is 
            needed, like the resouce uuid, this code 
            will find the relevant uuid and create 
            the new address line.
            """""""""""""""""""""""""""""""""""""""""
            addressCheck = self.testLine["address"]
            if addressCheck[len(addressCheck) - 8:] == 'uuidPrev':
                newAddress = (addressCheck[:len(addressCheck)-8] +
                              (str(prevResponse[0]["results"]))[2:(len(prevResponse[0]["results"])-3)])
                uuidToAddress = 1

            elif addressCheck[len(addressCheck) - 7:] == 'uuidTxt':
                newAddress = (addressCheck[:len(addressCheck) - 7] + txtFileUUID[0])
                uuidToAddress = 1

            elif addressCheck[len(addressCheck) - 8:] == 'uuidFile':
                newAddress = (addressCheck[:len(addressCheck) - 8] + uploadFileUUID[0])
                uuidToAddress = 1

            """""""""""""""""""""""""""""""""""""""""
            If there is a download resource check
            this will set a flag for download method.
            """""""""""""""""""""""""""""""""""""""""
            if addressCheck == 'downloadText':
                newAddress = ("resources/" + txtFileUUID[0] + "/download")
                downloadResource = 1

            if addressCheck == 'downloadFile':
                newAddress = ("resources/" + uploadFileUUID[0] + "/download")
                downloadResource = 1


            if uuidToAddress == 1:
                res = Response(requests.get(httpAddress + newAddress, params=payload, verify=False), True)
                reportLine = Report(tableWidget, self.testLine['title'], res.getStatus())
                reportLine.report_line(httpAddress + newAddress, res.getText(), payload, None)
                print("Payload: " + str(payload))
                res.report_line_to_main_window(reportLine, errorNumber)
                if res.getStatus() != 200:
                    reportLine.mark_red(errorNumber)

                """""""""""""""""""""""""""""""""""""""""
                Download method for both files and text.
                """""""""""""""""""""""""""""""""""""""""
            
            elif downloadResource == 1:
                if noKeysFlag == False:
                    res = Response(requests.get(httpAddress + newAddress,stream=True ,params=payload, verify=False), False)
                    fileName = res.getHeader()['content-disposition']
                    fileName = fileName[22:(len(fileName) - 1)]

                else:
                    res = Response(requests.get(httpAddress + newAddress, stream=True, params=payload, verify=False),
                                   True)

                reportLine = Report(tableWidget, self.testLine['title'], res.getStatus())
                reportLine.report_line(httpAddress + newAddress, "Downloaded file: " + fileName, payload, None)
                print("Payload: " + str(payload))
                reportLine.print_line(errorNumber)
                if res.getStatus() != 200:
                    reportLine.mark_red(errorNumber)
                else:
                    reportLine.mark_yellow()

                if noKeysFlag == False:
                    # finds the name of the file writen on site.
                    fileName = res.getHeader()['content-disposition']
                    # Creates new download folder to download files into.
                    if not os.path.exists("Downloads"):
                        os.makedirs("Downloads")
                    # Creating the path for the new downloaded file.
                    path = os.path.join("Downloads", fileName[22:(len(fileName) - 1)])
                    # Saves the file.
                    with open(path, 'wb') as out_file:
                        out_file.write(res.getContent())

                    """""""""""""""""""""""""""""""""""""""""
                    Checking if file was downloaded
                    and the name of the file is correct.
                    """""""""""""""""""""""""""""""""""""""""
                    # Checking download of the first file (uploaded at the start of the test run)
                    # Text file check.
                    if addressCheck == 'downloadText':
                        # Checking the download directory for the right file name.
                        if os.path.exists("Downloads/oht_" + txtFileUUID[0] + ".txt"):
                            reportLine.mark_green()

                        # If no such file found an error is raised.
                        else:
                            reportLine.mark_red(errorNumber)
                    # File check
                    else:
                        # Comparing the files names - downloaded vs uploaded.
                        fileName = testFilePath[0].split('/')

                        if os.path.exists(fileName[len(fileName) - 1]):
                            reportLine.mark_green()
                        else:
                            reportLine.mark_red(errorNumber)

                else:
                    if len(self.testLine['check']) >= 1 and res.getStatus() != 500:
                        res.check_value(self.testLine, reportLine, prevPayload, self.rsc_uuid, errorNumber)

                return
            else:
                res = Response(requests.get(httpAddress + self.testLine["address"], params=payload, verify=False), True)
                reportLine = Report(tableWidget, self.testLine['title'], res.getStatus())
                reportLine.report_line(httpAddress + self.testLine["address"], res.getText(), payload, None)
                print("Payload: " + str(payload))
                res.report_line_to_main_window(reportLine, errorNumber)
                if res.getStatus() != 200:
                    reportLine.mark_red(errorNumber)
            """""""""""""""""""""""""""""""""""""""""""""""
            If the save option is checked, will save the
            response and the request of the current request
            """""""""""""""""""""""""""""""""""""""""""""""           
            if self.testLine["save"] == '1':
                prevResponse[0] = res.responseJson()
                prevPayload[0] = payload

            if res.getStatus() != 200:
                for i in range(2):
                    res = Response(requests.get(httpAddress + self.testLine["address"], params=payload, verify=False), True)
                    reportLine = Report(tableWidget, self.testLine['title'], res.getStatus())
                    reportLine.report_line(httpAddress + self.testLine["address"], res.getText(), payload, None)
                    res.report_line_to_main_window(reportLine, errorNumber)
                    if res.getStatus() == 200:
                        break
                    else:
                        reportLine.mark_red(errorNumber)
                    
            if res.getStatus() == 200:
                if len(self.testLine['find']) >= 1:
                    res.find(self.testLine, reportLine, errorNumber)
                
                if len(self.testLine['check']) >= 1:
                    res.check_value(self.testLine, reportLine, prevPayload,self.rsc_uuid, errorNumber)

        """""""""""""""""""""""""""""""""""""""""""""""""""""""""
         This method is for requests that need resource UUID to
         execute. The method will check which type of resource is
         needed (Text or File) and execute the request.
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""

        def ex_resource(self, line, payload, txtFileUUID, uploadFileUUID):

            sourcesString = ""
            # Text sources
            if line["value"] == "oneTxt":
                payload[line["name"]] = txtFileUUID[0]
                self.rsc_uuid.append(txtFileUUID[0])

            elif line["value"] == "allTxt":
                for rsc in range(len(txtFileUUID)):
                    if rsc == 0:
                        sourcesString = txtFileUUID[0]
                        self.rsc_uuid.append(txtFileUUID[0])
                    else:
                        sourcesString += "," + txtFileUUID[rsc]
                        self.rsc_uuid.append(txtFileUUID[rsc])

                payload[line["name"]] = sourcesString

            elif line["value"] == "oneFile":
                payload[line["name"]] = uploadFileUUID[0]
                self.rsc_uuid.append(uploadFileUUID[0])

            elif line["value"] == "allFile":
                for rsc in range(len(uploadFileUUID)):
                    if rsc == 0:
                        sourcesString = uploadFileUUID[0]
                        self.rsc_uuid.append(uploadFileUUID[0])
                    else:
                        sourcesString += "," + uploadFileUUID[rsc]
                        self.rsc_uuid.append(uploadFileUUID[rsc])

                payload[line["name"]] = sourcesString

        
"""""""""""""""""""""""""""""""""""""""""""""""""""
                    Post Method
                    
    This class is handling all the POST requests
                    
                    
"""""""""""""""""""""""""""""""""""""""""""""""""""
class PostMethod:
    
    def __init__(self, data):
        self.testLine = data
        self.rsc_uuid = []
        with open('./data/languages.json') as codeLines_data:
            self.langJson = json.load(codeLines_data)
    
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""
    This is the main method, gets the line to execute and 
    sort between the types of requests.
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""
    def post_method(self, secretKey, publicKey, httpAddress, txtFilePath, txtFileUUID, testFilePath, uploadFileUUID,
                    prevResponse, prevPayload, tableWidget, firstResourcesUpload, errorNumber):
        payload = dict()
        uploadedrscFlag = [False]
        for payIndex in range(len(self.testLine['params'])):

            if self.testLine["params"][payIndex] == "No Secret Key" or self.testLine["params"][payIndex] == "No Public Key":
                pass

            elif self.testLine["params"][payIndex] == "secret_key":
                payload[self.testLine["params"][payIndex]] = secretKey
                            
            elif self.testLine["params"][payIndex] == "public_key":
                payload[self.testLine["params"][payIndex]] = publicKey

            elif 'name' in self.testLine["params"][payIndex]:

                # Randomly Choosing a language pair out of the initialized on site.
                if self.testLine["params"][payIndex]['name'] == "language_pair":
                    lang_pair = randint(0, len(self.langJson) - 1)
                    for source in self.langJson[lang_pair]:
                        payload['source_language'] = source
                        payload['target_language'] = self.langJson[lang_pair][source]

                # Randomly Choosing source language
                elif self.testLine["params"][payIndex]['name'] == "source_language":
                    lang_pair = randint(0, len(self.langJson) - 1)
                    for source in self.langJson[lang_pair]:
                        payload['source_language'] = source

                # Randomly choosing target language.
                elif self.testLine["params"][payIndex]['name'] == "target_language":
                    lang_pair = randint(0, len(self.langJson) - 1)
                    for source in self.langJson[lang_pair]:
                        payload['target_language'] = self.langJson[lang_pair][source]

                # Text upload
                elif self.testLine["params"][payIndex]["name"] == "textrsc":
                    self.text_upload(httpAddress, payIndex, payload, txtFilePath, prevResponse, prevPayload, txtFileUUID,
                                     uploadedrscFlag, firstResourcesUpload, tableWidget, errorNumber)
                
                # File upload
                elif self.testLine["params"][payIndex]["name"] == "filersc":
                    self.file_upload(httpAddress, payload, payIndex, testFilePath, prevResponse, prevPayload,
                                     uploadFileUUID, uploadedrscFlag, firstResourcesUpload, tableWidget, errorNumber)
                
                # Use existing resources
                elif self.testLine["params"][payIndex]["name"] == "sources" or self.testLine["params"][payIndex]["name"] == "translations":
                    self.ex_resource(self.testLine["params"][payIndex], payload, txtFileUUID, uploadFileUUID)
                
                else:
                    payload[self.testLine["params"][payIndex]["name"]] = self.testLine["params"][payIndex]["value"]
                
                        
        if uploadedrscFlag[0] == False:        
            res = Response(requests.post(httpAddress + self.testLine["address"], data=payload, verify=False), True)
            reportLine = Report(tableWidget, self.testLine['title'], res.getStatus())
            reportLine.report_line(httpAddress + self.testLine["address"], res.getText(), payload, None)
            print("Payload: " + str(payload))
            res.report_line_to_main_window(reportLine, errorNumber)
            if res.getStatus() != 200:
                reportLine.mark_red(errorNumber)
                
            if self.testLine["save"] == '1':
                prevResponse[0] = res.getJson()
                prevPayload[0] = payload

            if res.getStatus() != 200:
                for i in range(2):
                    res = Response(requests.post(httpAddress + self.testLine["address"], data=payload, verify=False), True)
                    reportLine = Report(tableWidget, self.testLine['title'], res.getStatus())
                    reportLine.report_line(httpAddress + self.testLine["address"], res.getText(), payload, None)
                    res.report_line_to_main_window(reportLine, errorNumber)

                    if res.getStatus() == 200:
                        break
                    else:
                        reportLine.mark_red(errorNumber)
                        
            if res.getStatus() == 200:
                if len(self.testLine['find']) >= 1:
                    res.find(self.testLine, reportLine, errorNumber)

                if len(self.testLine['check']) >= 1:
                    res.check_value(self.testLine, reportLine, prevPayload, self.rsc_uuid, errorNumber)

    """""""""""""""""""""""""""""""""""""""""""""""""""""""""
      This method will upload a text resource from file.
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""    
    def text_upload(self, httpAddress, payIndex, payload, txtFilePath, prevResponse, prevPayload, txtFileUUID,
                    uploadedrscFlag, firstResourcesUpload, tableWidget, errorNumber):
        
        if self.testLine["params"][payIndex]["value"] == "empty":
            pass
        elif self.testLine["params"][payIndex]["value"] == "nokey":
            pass
                            
        else:
                            
            if len(txtFilePath) == 0:
                pass
            elif len(txtFilePath) >= 1:

                for txtIndex in range(len(txtFilePath)):

                    loadedFile = open(txtFilePath[txtIndex], 'r')
                                
                    with loadedFile:
                        txt = loadedFile.read()

                    payload['text'] = txt

                    res = Response(requests.post(httpAddress + self.testLine["address"], data=payload, verify=False), True)
                    reportLine = Report(tableWidget, self.testLine['title'], res.getStatus())
                    reportLine.report_line(httpAddress + self.testLine["address"], res.getText(), payload, None)
                    print("Payload: " + str(payload))
                    res.report_line_to_main_window(reportLine, errorNumber)
                    if res.getStatus() != 200:
                        reportLine.mark_red(errorNumber)
                                        
                    if self.testLine["save"] == '1':
                        prevResponse[0] = res.getJson()
                        prevPayload[0] = payload

                    """""""""""""""""""""""""""""""""
                    In case there is 500 error, will
                    try to upload 2 more times.
                    """""""""""""""""""""""""""""""""
                    if res.getStatus() != 200:
                        for i in range(2):
                            res = Response(requests.post(httpAddress + self.testLine["address"], data=payload, verify=False), True)
                            reportLine = Report(tableWidget, self.testLine['title'], res.getStatus())
                            reportLine.report_line(httpAddress + self.testLine["address"], res.getText(), payload, None)
                            res.report_line_to_main_window(reportLine, errorNumber)
                            if res.getStatus() == 200:
                                break
                            else:
                                reportLine.mark_red(errorNumber)

                    if res.getStatus() == 200:
                        if len(self.testLine['find']) >= 1:
                            res.find(self.testLine, reportLine, errorNumber)

                        if len(self.testLine['check']) >= 1:
                            res.check_value(self.testLine, reportLine, prevPayload, self.rsc_uuid, errorNumber)

                        if firstResourcesUpload[0] == False:
                            uuidTxt = str(res.getJson()["results"])
                            txtFileUUID.append(uuidTxt[2:(len(uuidTxt)-2)])

                        uploadedrscFlag[0] = True
        
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""
            This method will upload a file resource
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""
    def file_upload(self, httpAddress, payload, payIndex, testFilePath, prevResponse, prevPayload,
                    uploadFileUUID, uploadedrscFlag, firstResourcesUpload, tableWidget, errorNumber):

        #uploadFlag = False
        
        if self.testLine["params"][payIndex]["value"] == "empty":
            pass
        elif self.testLine["params"][payIndex]["value"] == "nokey":
            pass
                            
        else:
            if len(testFilePath) == 0:
                pass
                                
            elif len(testFilePath) >= 1:
                                
                for fileIndex in range(len(testFilePath)):
                                
                    loadedFile = {'@upload': open(testFilePath[fileIndex], 'rb')}

                    res = Response(requests.post(httpAddress + self.testLine["address"], files = loadedFile, data = payload, verify=False), True)
                    reportLine = Report(tableWidget, self.testLine['title'], res.getStatus())
                    reportLine.report_line(httpAddress + self.testLine["address"], res.getText(), payload, str(loadedFile))
                    print("Payload: " + str(payload))
                    res.report_line_to_main_window(reportLine, errorNumber)
                    if res.getStatus() != 200:
                        reportLine.mark_red(errorNumber)
                                        
                    if self.testLine["save"] == '1':
                        prevResponse[0] = res.getJson()
                        prevPayload[0] = payload

                    """""""""""""""""""""""""""""""""
                    In case there is 500 error, will
                    try to upload 2 more times.
                    """""""""""""""""""""""""""""""""
                    if res.getStatus() != 200:
                        for i in range(2):
                            res = Response(
                                requests.post(httpAddress + self.testLine["address"], files=loadedFile, data=payload,
                                              verify=False), True)
                            reportLine = Report(tableWidget, self.testLine['title'], res.getStatus())
                            reportLine.report_line(httpAddress + self.testLine["address"], res.getText(), payload, None)
                            res.report_line_to_main_window(reportLine, errorNumber)
                            if res.getStatus() == 200:
                                break
                            else:
                                reportLine.mark_red(errorNumber)

                    if res.getStatus() == 200:
                        if len(self.testLine['find']) >= 1:
                            res.find(self.testLine, reportLine, errorNumber)

                        if len(self.testLine['check']) >= 1:
                            res.check_value(self.testLine, reportLine, prevPayload, self.rsc_uuid, errorNumber)

                        if firstResourcesUpload[0] == False:
                            uuidFile = str(res.getJson()["results"])
                            uploadFileUUID.append(uuidFile[2:(len(uuidFile)-2)])

                        uploadedrscFlag[0] = True

    """""""""""""""""""""""""""""""""""""""""""""""""""""""""
     This method is for requests that need resource UUID to
     execute. The method will check which type of resource is
     needed (Text or File) and execute the request.
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""

    def ex_resource(self, line, payload, txtFileUUID, uploadFileUUID):

        sourcesString = ""
        # Text sources
        if line["value"] == "oneTxt":
            payload[line["name"]] = txtFileUUID[0]
            self.rsc_uuid.append(txtFileUUID[0])

        elif line["value"] == "allTxt":
            for rsc in range(len(txtFileUUID)):
                if rsc == 0:
                    sourcesString = txtFileUUID[0]
                    self.rsc_uuid.append(txtFileUUID[0])
                else:
                    sourcesString += "," + txtFileUUID[rsc]
                    self.rsc_uuid.append(txtFileUUID[rsc])

            payload[line["name"]] = sourcesString

        elif line["value"] == "oneFile":
            payload[line["name"]] = uploadFileUUID[0]
            self.rsc_uuid.append(uploadFileUUID[0])

        elif line["value"] == "allFile":
            for rsc in range(len(uploadFileUUID)):
                if rsc == 0:
                    sourcesString = uploadFileUUID[0]
                    self.rsc_uuid.append(uploadFileUUID[0])
                else:
                    sourcesString += "," + uploadFileUUID[rsc]
                    self.rsc_uuid.append(uploadFileUUID[rsc])

            payload[line["name"]] = sourcesString
    
