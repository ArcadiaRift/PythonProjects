#! python3
#This program bridges the 'gaps' between files of the same prefix that end with a number. 
#If the delta between the suffix of two files in ascending order is not 1, then the program renames the folders accordingly.

import os, re, shutil

prefixRegex = re.compile(r""" #A regular expression pattern to recognize .txt files with a sepcific format.
    ^(spam) #Our prefix here is "spam". Feel free to change it to any other string of your choice.
    (\d\d\d) #This means that spam is followed by three digits
    (.txt)$ #The extension of the file, which is .txt in this case.
""", re.VERBOSE) 

file_list = os.listdir(os.getcwd())
 
lst = [] #Create an empty list. I feel like this program hinges on this very list.
for i in range(len(file_list)): #Loop through the list
   mo = prefixRegex.search(file_list[i]) #Search for matches in each file in our cwd.
   if mo == None: # i.e. if there are no matches, reiterate the for loop
       continue
   lst.append(int(mo.group(2))) #This appends group 2 of the regex in integer form. Remember that group 2 in our regex is the numbers part.

for j in range(len(lst)): #Now we loop through our newly filled list.
    if lst[j] - lst[j -1] != 1 and file_list[j] != "app.py" and file_list[j -1] != "app.py": #Our list's indices are essentially a projection of the os.listdir() indices, so we can use it to check for the deltas of each corresponding file
        print("Found gap between %s and %s... renaming files to fix gap..." %(file_list[j], file_list[j -1])) 
        shutil.move(os.path.join(os.getcwd(), file_list[j]), os.path.join(os.getcwd(), "spam00" + str(lst[j - 1] + 1 ) + ".txt")) #The shutil.move method allows as to rename the files, allowing us to bridge the gaps between the files.
        print("Done.")
    else:
        continue
    
