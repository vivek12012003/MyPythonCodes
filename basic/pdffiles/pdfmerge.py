
from pypdf import PdfReader , PdfWriter

writter = PdfWriter()

files = ['Common Intro Pages.pdf','Common Code File.pdf']


for file in files:
    read = PdfReader(file)

    for i in read.pages:        
        writter.add_page(i)

with open('306 - Minor Project (Common).pdf','wb') as f:
    writter.write(f)