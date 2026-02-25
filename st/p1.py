from selenium import webdriver 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By 
import time
# Launch Chrome browser 
driver = webdriver.Chrome() 
# Open Google homepage 
driver.get("https://www.google.com") 
# Retrieve and display page title 
time.sleep(5)
print("Page Title is:", driver.title) 
# Close the browser 
driver. quit() 