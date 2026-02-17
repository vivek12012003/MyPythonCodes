
from pypdf import PdfReader
import os

os.chdir('E:\\Study\\')

search = 'Write a Java program to calculate the factorial of a given numbers.'
file = 'frm_download_file.pdf'

read = PdfReader(file)

count = 0
for page in read.pages:

    count +=1 
    text = page.extract_text()
    
    if search in text:
        
        print('Founded :-')
        print('Page no. : ',count)

