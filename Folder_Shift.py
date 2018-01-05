import os
from shutil import copyfile
pwd=os.getcwd()
list_dir=os.listdir(pwd)
new_dir='Test'
os.makedirs(new_dir)
dest=pwd+'/'+new_dir
for i in list_dir:
    if(os.path.isdir(i)):
        src=pwd+'/'+i
        temp=os.listdir(src)
        for j in temp:
            temp1=src
            temp2=dest
            temp1+='/'+j
            temp2+='/'+j
            copyfile(temp1,temp2)
