#! python3
# get zize of files in directory

import os, shutil, re, pyinputplus as pyip
from pathlib import Path

#Specify the path to top folder in the tree
check = False
while check == False:
    main_tree = pyip.inputFilepath(
        prompt="Input folder (e.g. " + str(Path(r"C:/Windows" + ") "))    )
    if Path(main_tree).is_dir() == True:
        s = True
    else:
        print("""Path is not valid or file doesn't exist, please try again""")
        s = False
    check = s
    
#Specify file extension
#this code was only used for previous excercise in this chapter, to copy files with certain extension
#check = False
#while check == False:
#    file_extension = pyip.inputStr(prompt = 'input extension> ')
#    if len(file_extension)>5 or len(file_extension)<3:
#        print("""Extension not valid, must be e.g. ".exe", ".docx", etc...""")
#        continue
#    else:
#        if file_extension[0] != '.':
#            print("""Extension not valid, must be e.g. ".exe", ".docx", etc...""")
#        else:
#            if file_extension[1:len(file_extension)].isalpha()==False and file_extension[1:len(file_extension)].isdecimal()==False:
#                print("""Extension not valid, must be e.g. ".exe", ".docx", etc...""")   
#            else:
#                check=True
#p = Path(main_tree)    
#walk the entire tree and output size of files
for foldername, subfolders, filenames in os.walk(main_tree):
    for filename in filenames:
        print(os.path.join(foldername, filename), end=' ')
        print(str(os.path.getsize(os.path.join(foldername, filename))).rjust(70-len(str(os.path.join(foldername, filename)))))
