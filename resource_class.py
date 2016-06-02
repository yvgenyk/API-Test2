from class_test import Response
import requests

class Resource:
    def __init__(self, UUID, textEdit, priceList):
        self.textEdit = textEdit
        self.UUID = UUID
        self.priceList = priceList
        self.payload = dict()
        self.payload['secret_key'] = '434e3a197da394fac3b756094ae1255b'
        self.payload['public_key'] = '2Hgrq67wJpDdyfYVFkn9'
        self.payload['resources'] = UUID
        self.payload['source_language'] = 'en-us'
        self.payload['target_language'] = 'fr-fr'
        self.httpAddress = "https://oht.vagrant.oht.cc/api/2/tools/quote"
        self.res = Response(requests.get(self.httpAddress, params=self.payload, verify=False), self.textEdit)

        if self.res.getStatus() != 200:
            for i in 3:
                self.res = Response(requests.get(self.httpAddress, params=self.payload, verify=False), self.textEdit)

                if self.res.getStatus() == 200:
                    break

        self.wordcount = self.res.getJson()['results']['total']['wordcount']



    def get_UUID(self):
        return self.UUID

    def get_wordcount(self):
        return self.wordcount

    def get_reg_project_price(self):
        return (int(self.wordcount))*(self.priceList['reg_proj'])

    def get_expert_project_price(self):
        return (int(self.wordcount))*(self.priceList['expert_proj'])

    def get_proof_proj_price(self):
        return (int(self.wordcount)) * (self.priceList['proof_proj'])

    def get_transcript_proj_price(self):
        return (int(self.wordcount)) * (self.priceList['transcript_proj'])

    def get_combo_price(self):
        return (int(self.wordcount)) * (self.priceList['combo_proj'])