from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import schedule
import os

def startBot(username, password, url, download_url):
    driver = webdriver.Edge()

    try:
        driver.get(url)  # Open the login page
        time.sleep(5)  # Wait for the page to load

        # Enter username
        driver.find_element(By.NAME, "login").send_keys(username)

        # Enter password
        driver.find_element(By.NAME, "password").send_keys(password)

        # Click login button
        driver.find_element(By.NAME, "commit").click()
        time.sleep(10)  # Wait for the login process to complete

        # Navigate to a repository to download
        driver.get(download_url)
        time.sleep(10)  # Wait for the page to load

        # Click the download button (if exists)
        driver.find_element(By.XPATH, "//get-repo//summary").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//a[contains(@href, '/zipball/')]").click()
        time.sleep(10)  # Wait for the download to complete

    finally:
        driver.quit()

def job():
    username = 'Sneharghasaha07'
    password = 'sneharghasaha20'
    login_url = 'https://github.com/login'
    download_url = 'https://github.com/username/repository'  # Replace with actual repository URL
    
    startBot(username, password, login_url, download_url)

# Schedule the job at a specific time
schedule.every().day.at("10:00").do(job)  # Set to the time you want

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)
