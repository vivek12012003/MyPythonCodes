
from pypdf import PdfReader,PdfWriter


file = "E:\Study\frm_download_file.pdf"

read = PdfReader(file)
page1 = read.pages[0]

p1_text = page1.extract_text()

for i in p1_text:
    print(i,end='')


for i,page in enumerate (read.pages):

    print(f'Page {i+1} Text : ')
    print(page.extract_text(),end='')






# print(len(reader.pages))

# p1 = reader.pages[0]

# t1 = p1.extract_text()


# for i in t1:
#     if i == " ":
#         print(" ",end="")
#     if i == "\n":
#         print()
#     else: 
#         print(i,end="")


# r = PdfReader('ATS.pdf')


# for i , page in enumerate(r.pages):
#     print(f'Pages {i+1} - Text : ')
#     print(page.extract_text())

