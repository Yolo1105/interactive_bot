from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# Initialize Firefox WebDriver
service = Service('/path/to/geckodriver')  # Replace with your geckodriver path if needed
driver = webdriver.Firefox(service=service)

# Open ChatGPT login page
driver.get("https://chat.openai.com")

# Wait for the page to load
time.sleep(5)

# Check if already logged in by looking for an element that exists after login
try:
    chat_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//textarea[@data-id='chat-input']"))
    )
    print("Already logged in")
except:
    # If not logged in, perform login
    print("Not logged in, proceeding with login")

    # Click on the login button
    login_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Log in')]")
    login_button.click()

    # Wait for the login page to load and enter email and password
    time.sleep(5)
    
    email_input = driver.find_element(By.NAME, "email")
    email_input.send_keys("your-email@example.com")  # Replace with your email
    email_input.send_keys(Keys.RETURN)

    time.sleep(5)

    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys("your-password")  # Replace with your password
    password_input.send_keys(Keys.RETURN)

    # Wait for login to complete
    time.sleep(10)

# Once logged in, find the input box and send a question
chat_input = driver.find_element(By.XPATH, "//textarea[@data-id='chat-input']")
chat_input.send_keys("What is the capital of France?")  # Replace with your question
chat_input.send_keys(Keys.RETURN)

# Wait for response to be sent
time.sleep(5)

# Close the browser
driver.quit()
