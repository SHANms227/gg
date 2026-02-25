from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager 
import time 
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) 
driver.get("https://practicetestautomation.com/practice-test-login/") 
driver.find_element(By.XPATH, "//button[text()='Submit']").click() 
time.sleep(3) 
driver.quit() 