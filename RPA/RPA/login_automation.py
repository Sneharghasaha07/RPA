from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
# Set up the WebDriver
driver = webdriver.Edge()

# URL of the login page
# login_url = 'http://127.0.0.1:5000/login'
login_url = 'https://github.com/login'

# Credentials
username = 'Sneharghasaha07'
password = 'sneharghasaha2025@'

try:
    # Navigate to the login page
    driver.get(login_url)
    time.sleep(2)  # Wait for the page to load

    # Find the username and password input elements
    username_input = driver.find_element(By.ID, 'login_field')
    password_input = driver.find_element(By.ID, 'password')

    # Enter the username and password
    username_input.send_keys(username)
    password_input.send_keys(password)

    # Submit the form
    password_input.send_keys(Keys.RETURN)

    # Wait for the dashboard page to load
    time.sleep(2)

    # Optionally, you can verify the login by checking for some element on the dashboard page
    if 'Welcome to the dashboard' in driver.page_source:
        print('Login successful')
    else:
        print('Login failed')

    # Navigate to a repository to download
        driver.get('https://github.com/Sneharghasaha07/Netflix-Clone.git')
        time.sleep(2)  # Wait for the page to load

        # Click the download button (if exists)
        driver.find_element(By.ID, ":R55ab:").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div/ul/div/ul/li[2]/a/div/span").click()
        time.sleep(5)  # Wait for the download to complete
    

finally:
    # Close the WebDriver
    driver.quit()
