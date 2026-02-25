from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.saucedemo.com")

# Login
driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")
driver.find_element(By.ID,"login-button").click()

time.sleep(2)

# Add product directly from inventory page ✅
driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()

driver.save_screenshot("product_added.png")

# Open cart
driver.find_element(By.CLASS_NAME,"shopping_cart_link").click()
time.sleep(2)

print("Product added to cart")

# Checkout
driver.find_element(By.ID,"checkout").click()

# Checkout details
driver.find_element(By.ID,"first-name").send_keys("Shan")
driver.find_element(By.ID,"last-name").send_keys("MS")
driver.find_element(By.ID,"postal-code").send_keys("673001")

driver.find_element(By.ID,"continue").click()

driver.save_screenshot("checkout.png")

time.sleep(3)
driver.quit()