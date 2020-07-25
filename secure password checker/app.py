import re #import the re module to use regular expressions
password = input('Please enter a password: ') #ask the user to enter their password
crit = re.compile(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])[!-~]{8,}$') #the meat of the matter. create a regex object to detect at least one lowercase letter, at least one uppercase letter and at least one digit using positive lookaheads. the password must also be at least 8 characters so i used {8,}

if crit.findall(password) == []: #i.e. if there are no resulting matches because the password did not meet the criteria of the regex
    print('Error: Your password must be at least 8 characters long, include at least one uppercase letter and include one digit.')
else:
    print("That's a secure password!")

