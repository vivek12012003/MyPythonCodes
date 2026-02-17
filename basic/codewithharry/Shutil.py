
import shutil,os,time,sys


#use for copy files and folders and move them 

# shutil.copy('ATS.pdf','ats2.pdf')




#made for if file exist then copy it



if getattr(sys, 'frozen', False):
    BASE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
 
file_path = 'F:/Testing folder/t1/filecopy.txt'
check_path = 'F:/Testing folder/file.txt'

while True:
    if os.path.exists(check_path):
        shutil.copy(check_path,file_path)
        print('copied')
        break

    time.sleep(1)