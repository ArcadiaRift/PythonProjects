from selenium import webdriver
import time, os, pyperclip

print('Welcome to my very, very sophisticated tweeter! Tweet without having to endure the swaths of cancer on Twitter!')
time.sleep(1)
print('This is a semi-automated program. Once you\'re prompted to make a tweet, just paste the tweet from your clipboard (this will be done for you).')
os.chdir(r'C:\Users\alija\Desktop\Semi-Automated Twitter')
passFile = open('PASS.txt', 'r') #Access my password
password = passFile.readline() #Read the first line which contains my password
time.sleep(1)

twit = input('Enter a tweet:\n') 
pyperclip.copy(twit) #Copy the tweet to the clipboard
browser = webdriver.Firefox() #Open Firefox
browser.get('https://twitter.com/compose/tweet') #Launches the link to the compose tweet page
time.sleep(10)
usernameElem = browser.find_elements_by_tag_name('input')[5] #Find the username input field
usernameElem.send_keys('alilaridumbo') #Send my username to the username field
passwordElem = browser.find_elements_by_tag_name('input')[6] #Find the password input field
passwordElem.send_keys(password) #Send my password to the password field
time.sleep(2)
usernameElem.submit() #Submit to log in

print('Your input tweet has been copied to the clipboard. Just paste the tweet and hit tweet :)') #This print statement is shown right after the tweet box shows up
