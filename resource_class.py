import PyPDF2
import docx


class Resource:
    def __init__(self, filePath, priceList):
        self.filePath = filePath
        self.priceList = priceList
        self.wordcount = 0
        self.fileType = self.filePath.split(".")
        """
        Ordinary text files.
        """
        if self.fileType[1] == 'txt':
            loadedFile = open(self.filePath, 'r')

            with loadedFile:
                txt = loadedFile.read()

            # Adding 13% more for the word count.
            self.wordcount = len(txt.split(' '))*1.1
        """
        Reading a pdf file isn't as easy as text file.
        """
        if self.fileType[1] == 'pdf':
            pdfFileObj = open(self.filePath, 'rb')
            pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
            for page in range(pdfReader.numPages):
                pageObj = pdfReader.getPage(page)
                self.wordcount += len(pageObj.extractText().split(" "))*1.1
        """
        Word files
        """
        if self.fileType[1] == 'docx':
            doc = docx.Document(self.filePath)
            text = ''
            for para in doc.paragraphs:
                text += para.text
            self.wordcount = len(text.split(" "))*1.2



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