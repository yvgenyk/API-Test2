from PyQt4 import QtGui, QtCore
import main_design
import requests
import os
import json
import time
import re
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
    def __init__(self, res, textEdit):

        self.textEdit = textEdit
        self.r = res
        self.responseURL = self.r.url
        self.responseStatus = self.r.status_code
        self.responseText = self.r.text
        if self.responseStatus == 200:
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
        
    """""""""""""""""""""""""""""""""""""""""""""""""""""
    Prints the request and the response in the text editor
    of the program for later review.
    """""""""""""""""""""""""""""""""""""""""""""""""""""
    def report_line(self, title, textEdit, method):
        
        text = ("------------------------------------------------------------------------------------------------------------------------------------------------------------------\n" + 
                        method + " Request \"" + title + "\":\n" + self.responseURL + "\n\nAPI response:\n" + self.responseText)
        self.textEdit.append(text)

        
    #def AppendText(self):
          #print("\n\nAppended\n\n")
        
    """""""""""""""""""""""""""""""""""""""""""""""""""""
    Find method, if there is a request to find something 
    in the response, this method will find it.
    """""""""""""""""""""""""""""""""""""""""""""""""""""
    def find(self,data, errorFlag, textEdit):
        for findIndex in range(len(data['find'])):
            if data['find'][findIndex] in self.getText():
                pass
            else:
                if len(self.getText()) > 500:
                    textEdit.append("\n\nError 500, long response\n")
                else:
                    textEdit.append("\n\n There was a problem: " + data['find'][findIndex] + " wasn't found in :\n" + self.getText())
                    errorFlag[0] = True
        
    """""""""""""""""""""""""""""""""""""""""""""""""""""
    Check method, if there is certain values to check 
    in the response, this method will check them.
    """""""""""""""""""""""""""""""""""""""""""""""""""""
    def check_value(self, data, errorFlag, textEdit):
        for valIndex in range(len(['value'])):
            #If this is true, the method will check the values with the values from last call/response.
            if data["check"][valIndex*2] == 'prev':
                varToCheck = data["check"][(valIndex*2 + 1)]
                
                if data['value'][valIndex] == str(self.getJson()["results"][varToCheck]):
                    pass
                else:
                    textEdit.append("\n\n There was a problem: " + data["check"][(valIndex*2+1)] + 
                                    ": " + data["value"][valIndex] + " wasn't found in :\n" + self.getText())
                    errorFlag[0] = True
            #Else will check the provided values by the user against the response.                            
            else:
                varToCheck = data["check"][valIndex]
                                
                if data['value'][valIndex] == str(self.getJson()["results"][varToCheck]):
                    pass
                else:
                    textEdit.append("\n\n There was a problem: " + data["check"][valIndex] + 
                                    ": " + data["value"][valIndex] + " wasn't found in :\n" + self.getText())
                    errorFlag[0] = True
        
        
        
"""""""""""""""""""""""""""""""""""""""""""""""""""
                    Get Method Class

    This class will handle all the get requests.


"""""""""""""""""""""""""""""""""""""""""""""""""""        
class GetMethod:
        
        def __init__(self, data):
            self.testLine = data
            
        """""""""""""""""""""""""""""""""
        The get method itself, will get
        everything it needs from the main 
        class and execute the request. 
        """""""""""""""""""""""""""""""""
        def get_method(self, secretKey, publicKey, httpAddress, errorFlag, prevResponse, prevPayload, textEdit, lineIndex, testFilePath, uploadFileUUID, txtFileUUID):
            
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

                elif self.testLine["params"][payIndex] == "No Secret Key" or self.testLine["params"][payIndex] == "No Public Key":
                    noKeysFlag = True

                else:
                    payload[self.testLine["params"][payIndex]['name']] = self.testLine["params"][payIndex]['value']
                            
                            
            """""""""""""""""""""""""""""""""""""""""
            If an input from earlier request is 
            needed, like the resouce uuid, this code 
            will find the relevant uuid and create 
            the new address line.
            """""""""""""""""""""""""""""""""""""""""
            addressCheck = self.testLine["address"]
            if addressCheck[len(addressCheck)-4:] == 'uuid':
                newAddress = (addressCheck[:len(addressCheck)-4] +
                             (str(prevResponse[0]["results"]))[2:(len(prevResponse[0]["results"])-3)])
                uuidToAddress = 1

            """""""""""""""""""""""""""""""""""""""""
            If there is a download resource check
            this will set a flag for download method.
            """""""""""""""""""""""""""""""""""""""""
            if addressCheck == 'downloadText':
                newAddress = ("resources/" + txtFileUUID[0] + "/download")
                textEdit.append("\n------------------------------------------------------------------------------------------------------------------------------------------------------------------\n" +
                                self.testLine['title'] + "\n")
                downloadResource = 1

            if addressCheck == 'downloadFile':
                newAddress = ("resources/" + uploadFileUUID[0] + "/download")
                textEdit.append("\n------------------------------------------------------------------------------------------------------------------------------------------------------------------\n" +
                                self.testLine['title'] + "\n")
                downloadResource = 1


            if uuidToAddress == 1:
                res = Response(requests.get(httpAddress + newAddress, params=payload, verify=False), textEdit)

                """""""""""""""""""""""""""""""""""""""""
                Download method for both files and text.
                """""""""""""""""""""""""""""""""""""""""
            
            elif downloadResource == 1:
                res = requests.get(httpAddress + newAddress,stream=True ,params=payload, verify=False)
                if noKeysFlag == False:
                    #finds the name of the file writen on site.
                    fileName = res.headers['content-disposition']
                    #Creates new download folder to download files into.
                    if not os.path.exists("Downloads"):
                        os.makedirs("Downloads")
                    #Creating the path for the new downloaded file.
                    path = os.path.join("Downloads", fileName[22:(len(fileName) - 1)])
                    #Saves the file.
                    with open(path, 'wb') as out_file:
                        out_file.write(res.content)

                    """""""""""""""""""""""""""""""""""""""""
                    Checking if file was downloaded
                    and the name of the file is correct.
                    """""""""""""""""""""""""""""""""""""""""
                    #Checking download of the first file (uploaded at the start of the test run)
                    #Text file check.
                    if addressCheck == 'downloadText':
                        #Checking the download directory for the right file name.
                        if os.path.exists("Downloads/oht_" + txtFileUUID[0] + ".txt"):
                            textEdit.append("\nText file: oht_" + txtFileUUID[0] + ".txt was successfully downloaded.\n" )
                        #If no such file found an error is raised.
                        else:
                            textEdit.append("\nError: Text file: oht_" + txtFileUUID[0] + ".txt wasn't successfully downloaded.\n")
                            errorFlag[0] = True
                    #File check
                    else:
                        #Comparing the files names - downloaded vs uploaded.
                        fileName = testFilePath[0].split('/')

                        if os.path.exists("Downloads/" + fileName[len(fileName) - 1]):
                            textEdit.append("\nFile:" + fileName[len(fileName) - 1] + " was downloaded successfully.\n")
                        else:
                            textEdit.append("\nError: File:" + fileName[len(fileName) - 1] + "was not dowloaded.\n")
                            errorFlag[0] = True

                else:
                    for findIndex in range(len(self.testLine['find'])):
                        if self.testLine['find'][findIndex] in res.text:
                            textEdit.append(res.text)
                        else:
                            textEdit.append("\n\n There was a problem: " + self.testLine['find'][findIndex] +
                                            " wasn't found in :\n" + res.text)
                            errorFlag[0] = True


                return
            else:
                res = Response(requests.get(httpAddress + self.testLine["address"], params=payload, verify=False), textEdit)
            """""""""""""""""""""""""""""""""""""""""""""""
            If the save option is checked, will save the
            response and the request of the current request
            """""""""""""""""""""""""""""""""""""""""""""""           
            if self.testLine["save"] == '1':
                prevResponse = res.responseJson()
                prevPayload = payload
                    
            if res.getStatus() == 200:
                res.report_line(self.testLine['title'], textEdit, "GET")
                    
                if len(self.testLine['find']) >= 1:
                    res.find(self.testLine, errorFlag, textEdit)
                
                if len(self.testLine['check']) >= 1:
                    res.check_value(self.testLine, errorFlag, textEdit)
                    
            else:
                textEdit.append("Error: %d" % res.getStatus())
                errorFlag[0] = True
        
        
"""""""""""""""""""""""""""""""""""""""""""""""""""
                    Post Method
                    
    This class is handling all the POST requests
                    
                    
"""""""""""""""""""""""""""""""""""""""""""""""""""
class PostMethod:
    
    def __init__(self, data):
            self.testLine = data
    
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""
    This is the main method, gets the line to execute and 
    sort between the types of requests.
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""
    def post_method(self, secretKey, publicKey, httpAddress, txtFilePath, txtFileUUID, testFilePath, uploadFileUUID, prevResponse, prevPayload, textEdit, errorFlag):
        payload = dict()
        uploadedrscFlag = [False]
        for payIndex in range(len(self.testLine['params'])):

            if self.testLine["params"][payIndex] == "No Secret Key" or self.testLine["params"][payIndex] == "No Public Key":
                pass

            elif self.testLine["params"][payIndex] == "secret_key":
                payload[self.testLine["params"][payIndex]] = secretKey
                            
            elif self.testLine["params"][payIndex] == "public_key":
                payload[self.testLine["params"][payIndex]] = publicKey  
                
            #Text upload  
            elif self.testLine["params"][payIndex]["name"] == "textrsc":  
                self.text_upload(httpAddress, payIndex, payload, txtFilePath, textEdit, prevResponse, prevPayload, txtFileUUID, uploadedrscFlag, errorFlag)
                
            #File upload  
            elif self.testLine["params"][payIndex]["name"] == "filersc": 
                self.file_upload(httpAddress, payload, payIndex, testFilePath, textEdit, prevResponse, prevPayload, uploadFileUUID, uploadedrscFlag, errorFlag)
                
            #Use existing resources    
            elif self.testLine["params"][payIndex]["name"] == "sources":   
                self.ex_resource(payload, txtFileUUID, uploadFileUUID, textEdit, errorFlag)
                
            else:
                payload[self.testLine["params"][payIndex]["name"]] = self.testLine["params"][payIndex]["value"]
                
                        
        if uploadedrscFlag[0] == False:        
            res = Response(requests.post(httpAddress + self.testLine["address"], data=payload, verify=False), textEdit)
                
            if self.testLine["save"] == '1':
                prevResponse[0] = res.getJson()
                prevPayload = payload
                        
            if res.getStatus() == 200:
                res.report_line(self.testLine['title'], textEdit, "POST")
            else:
                    textEdit.append("Error: %d" % res.getStatus())
                    errorFlag[0] = True
             
                            
            if len(self.testLine['find']) >= 1:
                res.find(self.testLine, errorFlag, textEdit)     
                         
            if len(self.testLine['check']) >= 1:
                res.check_value(self.testLine, errorFlag, textEdit)
            
                
        
        
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""
      This method will upload a text resource from file.
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""    
    def text_upload(self, httpAddress, payIndex, payload, txtFilePath, textEdit, prevResponse, prevPayload, txtFileUUID, uploadedrscFlag, errorFlag):    
        
        if self.testLine["params"][payIndex]["value"] == "empty":
            pass
        elif self.testLine["params"][payIndex]["value"] == "nokey":
            pass
                            
        else:
                            
            if len(txtFilePath) == 0:
                textEdit.append("No text file was added\n")
                                
            elif len(txtFilePath) >= 1:
                                
                for txtIndex in range(len(txtFilePath)):
                                
                    loadedFile = open(txtFilePath[txtIndex], 'r')
                                
                    with loadedFile:
                        txt = loadedFile.read()
                                    
                    payload['text'] = txt
                                        
                    res = Response(requests.post(httpAddress + self.testLine["address"], data=payload, verify=False), textEdit)
                                        
                    if self.testLine["save"] == '1':
                        prevResponse[0] = res.getJson()
                        prevPayload = payload

                    """""""""""""""""""""""""""""""""
                    In case there is 500 error, will
                    try to upload 2 more times.
                    """""""""""""""""""""""""""""""""
                    if res.getStatus() != 200:
                        for i in range(2):
                            res = Response(
                                requests.post(httpAddress + self.testLine["address"], data=payload, verify=False),
                                textEdit)

                            if res.getStatus() == 200:
                                break

                    if res.getStatus() == 200:
                        res.report_line(self.testLine['title'], textEdit, "POST")
                                
                        uuidTxt = str(res.getJson()["results"])
                        txtFileUUID.append(uuidTxt[2:(len(uuidTxt)-2)])
                        uploadedrscFlag[0] = True 
                                            
                    else:
                        textEdit.append("Error: %d" % res.getStatus())
                        errorFlag[0] = True
        
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""
            This method will upload a file resource
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""
    def file_upload(self, httpAddress, payload, payIndex, testFilePath, textEdit, prevResponse, prevPayload, uploadFileUUID, uploadedrscFlag, errorFlag):

        uploadFlag = False
        
        if self.testLine["params"][payIndex]["value"] == "empty":
            pass
        elif self.testLine["params"][payIndex]["value"] == "nokey":
            pass
                            
        else:
            if len(testFilePath) == 0:
                textEdit.append("No file was selected\n")
                                
            elif len(testFilePath) >= 1:
                                
                for fileIndex in range(len(testFilePath)):
                                
                    loadedFile = {'@upload': open(testFilePath[fileIndex], 'rb')}
                                        
                    res = Response(requests.post(httpAddress + self.testLine["address"], files = loadedFile, data = payload, verify=False), textEdit)
                                        
                    if self.testLine["save"] == '1':
                        prevResponse[0] = res.getJson()
                        prevPayload = payload
                    """""""""""""""""""""""""""""""""
                    In case there is 500 error, will
                    try to upload 2 more times.
                    """""""""""""""""""""""""""""""""
                    if res.getStatus() != 200:
                        for i in range(2):
                            res = Response(
                                requests.post(httpAddress + self.testLine["address"], files=loadedFile, data=payload,
                                              verify=False), textEdit)
                            if res.getStatus() == 200:
                                break

                    if res.getStatus() == 200:
                        res.report_line(self.testLine['title'], textEdit, "POST")
                                
                        uuidFile = str(res.getJson()["results"])
                        uploadFileUUID.append(uuidFile[2:(len(uuidFile)-2)])
                        uploadedrscFlag[0] = True 
                    
                    else:
                        textEdit.append("Error: %d" % res.getStatus())
                        errorFlag[0] = True    
    
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""
     This method is for requests that need resource UUID to
     execute. The method will check which type of resource is
     needed (Text or File) and execute the request.
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""
    def ex_resource(self, payload, txtFileUUID, uploadFileUUID, textEdit, errorFlag):   
        
        #Text sources
        if self.testLine["params"][payIndex]["value"] == "txt":
            sourcesString = ""
        if len(txtFileUUID)>1:
            for rsc in range(len(txtFileUUID)):
                sourcesString += "," + txtFileUUID[rsc]
                                        
                payload[self.testLine["params"][payIndex]["name"]] = sourcesString
                                    
        elif len(txtFileUUID)==1:
            payload[self.testLine["params"][payIndex]["name"]] = txtFileUUID[0]
                                
        elif len(txtFileUUID)==0:
            textEdit.append("No text resources found!")
            errorFlag[0] = True
                                    
        #File sources
        else:
            sourcesString = ""
            if len(uploadFileUUID)>1:
                for rsc in range(len(uploadFileUUID)):
                    sourcesString += "," + uploadFileUUID[rsc]
                                        
                    payload[self.testLine["params"][payIndex]["name"]] = sourcesString
                                
            elif len(uploadFileUUID)==1:
                payload[self.testLine["params"][payIndex]["name"]] = uploadFileUUID[0]
                                
            elif len(uploadFileUUID)==0:
                textEdit.append("No file resources found!")
                errorFlag[0] = True
    
        