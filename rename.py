import os
pwd=os.getcwd()
lid=os.listdir(pwd)
for i in lid:
    print i
    username=raw_input("Enter the file name: ")
    os.rename(i,username)
