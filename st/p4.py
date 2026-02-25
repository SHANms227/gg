from selenium import webdriver 
driver = webdriver.Chrome() 
driver.get("https://example.com") 
driver.save_screenshot("screenshot.png") 
print("Screenshot saved successfully") 
driver.quit() 