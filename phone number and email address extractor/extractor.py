#! python3
# This script finds and prints out Email addresses and North American phone numbers from the clipboard

import pyperclip, re # import the necessary modules - pyperclip and re - which will access the clipboard and compile regex pattern objects, respectively.

phoneRegex = re.compile(r'''(                         #create a phone number regex object to detect North American numbers which follow a specific format as shown in the code
    (\d{3}|\(\d{3}\))? #area code
    (\s|-|\.)?        #seperator
    (\d{3})           #first 3 digits
    (\s|-|\.)         #seperator
    (\d{4})           #last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    #extension  
)''', re.VERBOSE)

emailRegex = re.compile(r'''(                       #create an email regex object       
  [a-zA-Z0-9._%+-]+ # username
  @ # @ symbol
  [a-zA-Z0-9.-]+ # domain name
 )''', re.VERBOSE)

text = str(pyperclip.paste()) #create a text variable which includes the string of the text in our clipboard. this text is what the regex will be applied on
matches = [] #create an empty list called matches in which we can store the results of the regex

for groups in phoneRegex.findall(text): #for loop for each group in the collection of tuples found after using a .findall method
    phoneNumber = '-'.join([groups[1], groups[3], groups[5]]) #create a single phone number by joining all the relevant parts of each group and using a specific format (i.e. using hyphens to seperate the digits)
    if groups[8] != '': #if the extension is not empty
        phoneNumber += 'x' + groups[8] #add an x followed by the extension
    matches.append(phoneNumber) #once the phone number is made, it is appended to the matches list 


for groups in emailRegex.findall(text): #another for loop for each group in the email. in this case, there is only one item in each tuple
    matches.append(groups)  #there is no need to use a .join method or anything of the sort as the email is already formatted to be in one group

if len(matches) > 0:    #i.e. if there are email addresses and/or phone numbers 
    pyperclip.copy('\n'.join(matches)) #copy all the email addresses and phone numbers, including a newline after each one
    print('Copied to Clipboard:')   
    print('\n'.join(matches))   #this will print said emails and numbers to show what was copied into the clipboard. very convenient if you ask me
else:   #if there are no email addresses and/or phone numbers:
    print('No phone numbers or email addresses found.') #prints the following to show that the inital text had no phone numbers or email addresses as the regular expression returned None