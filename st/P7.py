from selenium import webdriver
from selenium.webdriver.common.by import By
import csv, time

driver = webdriver.Chrome()

with open("login_data.csv") as file:
    data = csv.DictReader(file)

    for row in data:
        driver.get("https://practicetestautomation.com/practice-test-login/") 
        driver.find_element(By.ID, "username").send_keys(row["username"])
        driver.find_element(By.ID, "password").send_keys(row["password"])
        driver.find_element(By.XPATH, "//button[text()='Submit']").click() 

        time.sleep(2)

        if "success" in driver.current_url:
            result="PASS"
        else:
            result="FAIL"

        print(row["username"], result)
        driver.save_screenshot(row["username"]+".png")

driver.quit()