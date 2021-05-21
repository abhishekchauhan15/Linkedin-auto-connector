from selenium import webdriver
import os 
import time
from webdriver_manager.chrome import ChromeDriver, ChromeDriverManager

driver= webdriver.Chrome(ChromeDriverManager().install())

#opens the linkedin login page 
driver.get('https://www.linkedin.com/login')

#sets email id and password (set your email and password as an environment variable )
email=os.environ.get('LINKEDIN_EMAIL')
password=os.environ.get('LINKEDIN_password')

#if you don't know how to set environment variables simply comment out 12th and 13th line and and uncomment 16th and 17th line
#email='enter your linkedin email ID'
#password='enter your linkedin password'


#finds the element and send keys to the id 
driver.find_element_by_id("username").send_keys(email)
driver.find_element_by_id("password").send_keys(password)

#clicks on the login button
driver.find_element_by_css_selector(".btn__primary--large").click()
time.sleep(2)

#after running this line ,terminal will ask you to enter you disered company's employe you want to send connection request 
driver.get('https://www.linkedin.com/search/results/people/?keywords={}&network=%5B%22S%22%5D&origin=FACETED_SEARCH'.format(input("enter you disered company: ")))    

connect=[]
while len(connect)==0:
    connect=driver.find_elements_by_xpath("//button[@class='artdeco-button artdeco-button--2 artdeco-button--secondary ember-view'] ")
    


for button in connect:
    sendButton=None
   
    
    button.click()
    sendButton=driver.find_element_by_xpath("//button[@class='ml1 artdeco-button artdeco-button--3 artdeco-button--primary ember-view']")
    


    if sendButton:
        sendButton.click()
        time.sleep(2)

