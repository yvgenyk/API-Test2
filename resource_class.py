

class Resource:
    def __init__(self, filePath, priceList):
        self.filePath = filePath
        self.priceList = priceList

        loadedFile = open(self.filePath, 'r')

        with loadedFile:
            txt = loadedFile.read()

        # Adding 13% more for the word count.
        self.wordcount = len(txt.split(' '))*1.13



    def get_wordcount(self):
        return self.wordcount

    def get_reg_project_price(self):
        return (self.wordcount)*(self.priceList['reg_proj'])

    def get_expert_project_price(self):
        return (int(self.wordcount))*(self.priceList['expert_proj'])

    def get_proof_proj_price(self):
        return (int(self.wordcount)) * (self.priceList['proof_proj'])

    def get_transcript_proj_price(self):
        return (int(self.wordcount)) * (self.priceList['transcript_proj'])

    def get_combo_price(self):
        return (int(self.wordcount)) * (self.priceList['combo_proj'])