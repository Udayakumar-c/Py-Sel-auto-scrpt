import value
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver

# Path to the Firefox WebDriver executable (geckodriver)
service1=Service(executable_path="D:\Python\workspace\Drivers for python\geckodriver-v0.35.0-win-aarch64\geckodriver.exe")

# Initialize the Firefox driver
driver=webdriver.Firefox(service=service1)
# driver=webdriver.geckodriver(service=service1)

# Open the OrangeHRM login page
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(5)# Wait for the page to load

# Find the username, password fields, and the login button
username=driver.find_element(By.NAME, "username")
password=driver.find_element(By.NAME,'password')
login_button=driver.find_element(By.XPATH,"//button[@type='submit']")

# Input credentials and click login
username.send_keys("Admin")
password.send_keys("admin123")
login_button.click()

# Wait for the page to load after login
time.sleep(5) # Wait after login

# Verify the title of the page
actual_title=driver.title
expected_title="OrangeHRM"

if expected_title not in actual_title:
    raise AssertionError("Title Failed")

print("loging successful and title verified")

# Close the browser
driver.close()


