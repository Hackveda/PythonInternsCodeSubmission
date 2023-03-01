from selenium import webdriver
import time

# Set the path to the geckodriver executable file
gecko_path = r"D:\selenium\geckodriver-v0.32.2-win64\geckodriver.exe"

# Create a new Firefox driver instance using the geckodriver executable
browser = webdriver.Firefox(executable_path=gecko_path)

# Maximize the browser window
browser.maximize_window()

# Open the Website
browser.get("https://www.saucedemo.com/")
time.sleep(10)

# Finding the element by id 
username = browser.find_element_by_id("user-name")
time.sleep(10)

password = browser.find_element_by_id("password")
time.sleep(10)

button =browser.find_element_by_id("login-button")
time.sleep(10)


# Sending value to the feild
username.send_keys("standard_user")
password.send_keys("secret_sauce")
button.click()
