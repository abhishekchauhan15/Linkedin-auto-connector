from selenium import webdriver
import os 
import time
from webdriver_manager.chrome import ChromeDriver, ChromeDriverManager

driver= webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.linkedin.com/login')

email=os.environ.get('LINKEDIN_EMAIL')
password=os.environ.get('LINKEDIN_password')

email='abhishekchauhan1509@gmail.com'
password='5u*rBEm)_6W!fF%'


driver.find_element_by_id("username").send_keys(email)
driver.find_element_by_id("password").send_keys(password)

driver.find_element_by_css_selector(".btn__primary--large").click()
time.sleep(2)

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
        
