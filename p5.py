from selenium import webdriver
from selenium.webdriver.common.by import By
import time
d = webdriver.Chrome()
d.get("https://tinyurl.com/autoform5")
d.find_element(By.NAME,"firstname").send_keys("John")
d.find_element(By.NAME,"lastname").send_keys("Doe")
d.execute_script("document.getElementById('sex-0').click()")
d.execute_script("document.getElementById('exp-2').click()")
d.execute_script("document.getElementById('submit').click()")
time.sleep(3)
print(" Form submitted successfully")
d.quit()