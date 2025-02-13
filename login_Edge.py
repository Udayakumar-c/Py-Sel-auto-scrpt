import value
import time
from selenium import webdriver
from selenium.webdriver.edge.webdriver import Service
from selenium.webdriver.common.by import By


# Path to the edge WebDriver executable
service1=Service(executable_path="D:\Python\workspace\Drivers for python\edgedriver_win64\msedgedriver.exe")

# Initialize the edge service
driver=webdriver.Edge(service=service1)

# Open the OrangeHRM login page
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(5)# Wait for the page to load

# Find the username, password fields, and the login button
username= driver.find_element(By.NAME,"username")
password=driver.find_element(By.NAME,"password")
login_button=driver.find_element(By.XPATH,"//button[@type='submit']")

# Input credentials and click login
username.send_keys("Admin")
password.send_keys("admin123")
login_button.click()

# Wait for the page to load after login
time.sleep(5)# Wait after login


# Verify the title of the page
actual_title =driver.title
expected_title="OrangeHRM"

if expected_title not in actual_title:
    raise AssertionError ("Title failed")

print("Loging successful and title verified" )

# Close the browser
driver.close()