
from pypdf import PdfWriter,PdfReader

read = PdfReader('ATS.PDF')

writter = PdfWriter()

str = ''

for i in range(0,1):

    str += read.pages[0].extract_text()



with open ('test.txt','w') as f:
    f.write(str)