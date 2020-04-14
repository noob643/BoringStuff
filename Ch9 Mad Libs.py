#! python3
# madlibs.py - read a text file and replace some words
import re
from pathlib import Path
import pyinputplus as pyip

# Ask user input for file
check = False
while check == False:
    filename = pyip.inputFilepath(
        prompt="Input file path (e.g. " + str(Path(r"C:/Windows/text.txt" + ") "))
    )
    if Path(filename).is_file() == True:
        s = True
    else:
        print("""Path is not valid or file doesn't exist, please try again""")
        s = False
    check = s
# Retrieve the text from text file and find words that need to be replaced
madlibsfile = open(filename)
madlibstext = madlibsfile.read()
madlibsfile.close()

# Find words to be replaced
text_to_replace = re.compile(r"""ADJECTIVE|NOUN|VERB""")
req_inputs = text_to_replace.findall(madlibstext)

# Get replacement words from user
replacement_words = []
for item in req_inputs:
    rep_item = pyip.inputStr(prompt="Enter " + item.lower() + "> ")
    replacement_words.append(rep_item)
    
# Replace words in the text
for i in range(len(req_inputs)):
    madlibstext = madlibstext.replace(req_inputs[i], replacement_words[i], 1)
    
# Output text and save to file:
print(madlibstext)
madlibsoutputfile = open(Path(Path(filename).parent / "madlibsoutput.txt"), "w")
madlibsoutputfile.write(str(madlibstext))
madlibsoutputfile.close()
