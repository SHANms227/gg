from selenium import webdriver
from selenium.webdriver.common.by import By
import time

d = webdriver.Chrome()

d.get("https://www.selenium.dev/selenium/web/alerts.html")

# Click prompt alert
d.find_element(By.LINK_TEXT, "click me").click()

# Switch to alert
alert = d.switch_to.alert

# Print alert message
print("Alert Text:", alert.text)

# Click OK (accept)
alert.accept()

time.sleep(2)

d.quit()