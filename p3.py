from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager 
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) 
driver.get("https://practicetestautomation.com/practice-test-login/") 
driver.find_element(By.ID, "username").send_keys("student") 
driver.find_element(By.ID, "password").send_keys("Password123") 
driver.find_element(By.XPATH, "//button[text()='Submit']").click() 
print("Login Successful") 
driver.quit()