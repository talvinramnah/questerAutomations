import requests
import time
import pyautogui

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import re


# Set up Chrome options
chrome_options = Options()
#chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-dev-shm-usage")

# Initialize the Chrome driver with the specified options
service = Service(executable_path=r"C:\Program Files (x86)\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get('https://quester.io')
wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds

# INTERACT HERE
username = 'talvinQuester'
password = 'hlhothaYom6&ApH01rod'
questName = 'Chamath Palihapitiya: What I read this week 22-07-22'

#create email
def CreateEmail():
    import requests
    url = "https://gmailnator.p.rapidapi.com/generate-email"

    payload = { "options": [2] }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "ca263c054amshf7a16421e4dd1eap1126cdjsn1de0f0140b58",
        "X-RapidAPI-Host": "gmailnator.p.rapidapi.com"
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.ok:
        # Extracting the email address from the response
        email_address = response.json().get('email', 'No email found')
        print(email_address)
        return email_address
    else:
        print("Error:", response.status_code)

def SignInFlow(email_address):
    login_button_xpath = '//*[@id="root"]/div/div[2]/div[1]/div[3]/div[1]/div[5]/div[2]/div/div[2]/div/div[3]/div[3]/span'
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, login_button_xpath)))
    login_button.click()
    time.sleep(1)
    register_button_xpath = '//*[@id="kc-registration"]/span/a'
    register_button = wait.until(EC.element_to_be_clickable((By.XPATH, register_button_xpath)))
    register_button.click()
    time.sleep(1)
    email_xpath = '//*[@id="email"]' 
    email_button = wait.until(EC.element_to_be_clickable((By.XPATH, email_xpath)))
    email_button.click()
    email_button.send_keys(email_address)
    time.sleep(1)
    username_xpath = '//*[@id="username"]'
    username_button = wait.until(EC.element_to_be_clickable((By.XPATH, username_xpath)))
    username_button.click()
    username_button.send_keys(username)
    time.sleep(1)
    password_xpath = '//*[@id="password"]'
    password_button = wait.until(EC.element_to_be_clickable((By.XPATH, password_xpath)))
    password_button.click()
    password_button.send_keys(password)
    time.sleep(1)
    confirm_password_xpath = '//*[@id="password-confirm"]'
    confirm_password_button = wait.until(EC.element_to_be_clickable((By.XPATH, confirm_password_xpath)))
    confirm_password_button.click()
    confirm_password_button.send_keys(password)
    time.sleep(1)
    register_submit_xpath = '//*[@id="kc-form-buttons"]/input'
    register_submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, register_submit_xpath)))
    register_submit_button.click()
    # username_xpath = '//*[@id="username"]'
    # username_button = wait.until(EC.element_to_be_clickable((By.XPATH, username_xpath)))
    # username_button.click()
    # username_button.send_keys('TalvinQuester')
    # password_xpath = '//*[@id="password"]'
    # password_button = wait.until(EC.element_to_be_clickable((By.XPATH, password_xpath)))
    # password_button.click()
    # password_button.send_keys('hlhothaYom6&ApH01rod')
    # sign_in_xpath = '//*[@id="kc-login"]'
    # sign_in_button = wait.until(EC.element_to_be_clickable((By.XPATH, sign_in_xpath)))
    # sign_in_button.click()


def getVerificationEmail(email_address, attempts=3, delay=5):
    # Inbox
    url = "https://gmailnator.p.rapidapi.com/inbox"
    payload = {"email": email_address, "limit": 1}
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "your_api_key",
        "X-RapidAPI-Host": "gmailnator.p.rapidapi.com"
    }

    attempt = 0
    while attempt < attempts:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            response_json = response.json()
            print("Response:", response_json)
            if response_json and isinstance(response_json, list) and len(response_json) > 0:
                message_id = response_json[0].get('id', None)
                if message_id:
                    return message_id
                else:
                    print("Email found but no message ID.")
                    return
            else:
                print("No emails found, retrying...")
        else:
            print("Error with response, status code:", response.status_code)
            return

        time.sleep(delay)
        attempt += 1

    print("Failed to retrieve email after multiple attempts.")
    

    # Message
    url = "https://gmailnator.p.rapidapi.com/messageid"
    querystring = {"id": message_id}
    headers = {
        "X-RapidAPI-Key": "ca263c054amshf7a16421e4dd1eap1126cdjsn1de0f0140b58",
        "X-RapidAPI-Host": "gmailnator.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    print(response.json())
    email_content = response.json().get('content', '')
    print(email_content)

    # Extract the verification link using regular expression
    verification_link = extract_verification_link(email_content)
    if verification_link:
        # Use Selenium to open the verification link
        driver.get(verification_link)
    else:
        print("Verification link not found in the email content.")

    # except IndexError:
    #     print("No emails found in the inbox.")
    # except Exception as e:
    #     print("An error occurred:", e)

def extract_verification_link(email_content):
    # Use regular expression to find the URL
    urls = re.findall(r'https?://[^\s<>"]+|www\.[^\s<>"]+', email_content)
    if urls:
        return urls[0]  # Assuming the first URL is the verification link
    return None

#go to verification link enter credentials


#login to fake account
def SignInFlow():
    login_button_xpath = '//*[@id="root"]/div/div[2]/div[1]/div[3]/div[1]/div[5]/div[2]/div/div[2]/div/div[3]/div[3]/span'
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, login_button_xpath)))
    login_button.click()
    username_xpath = '//*[@id="username"]'
    username_button = wait.until(EC.element_to_be_clickable((By.XPATH, username_xpath)))
    username_button.click()
    username_button.send_keys(username)
    password_xpath = '//*[@id="password"]'
    password_button = wait.until(EC.element_to_be_clickable((By.XPATH, password_xpath)))
    password_button.click()
    password_button.send_keys(password)
    sign_in_xpath = '//*[@id="kc-login"]'
    sign_in_button = wait.until(EC.element_to_be_clickable((By.XPATH, sign_in_xpath)))
    sign_in_button.click()

#Go to the quest to vote and comment on 
def navigateToQuest():
    navigate_xpath = '//*[@id="root"]/div/div[2]/div[1]/div[3]/div[1]/div[5]/div[2]/div/div[2]/div/div[2]/div/span'
    navigate_button = wait.until(EC.element_to_be_clickable((By.XPATH, navigate_xpath)))
    navigate_button.click()
    search_xpath = '//*[@id="root"]/div/div[2]/div[1]/div[3]/div[2]/div/div/div/div/div[1]/div[1]/input'
    search_button = wait.until(EC.element_to_be_clickable((By.XPATH, search_xpath)))
    search_button.click()
    search_button.send_keys(questName)
    top_result_xpath = '//*[@id="root"]/div/div[2]/div[1]/div[3]/div[2]/div/div/div/div/div[4]/a/div[2]/div[1]'
    top_result_button = wait.until(EC.element_to_be_clickable((By.XPATH, top_result_xpath)))
    top_result_button.click()
    
#interact with number datapoint 

#interact with select datapoint 
def voteOnSelectDatapoint():
    # Adjusted selector to target all elements with class 'resource'
    resourceList = driver.find_elements(By.CSS_SELECTOR, ".resource")
    print(len(resourceList))
    for resource in resourceList:
        selectDatapoint_class = 'communityValue'
        selectDatapoint_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, selectDatapoint_class))
        )
        driver.execute_script("arguments[0].click();", selectDatapoint_button)
        time.sleep(2)
        option1_css_selector = "#root > div > div:nth-child(2) > div.mainLayoutWrapper > div.mainArea > div:nth-child(1) > div > div > div > div.container-fluid > div.resourceListAndQuestCommentsWrapper > div.resourceListMegaWrapper > div > div.resourceList > div:nth-child(1) > div.resourceRight > div > div > div:nth-child(2) > div > div.otherValues > div.otherValue.red > span.title > div"
        option1_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, option1_css_selector))
        )
        driver.execute_script("arguments[0].click();", option1_button)
        time.sleep(2)
        closeDropdown_class = 'closeDropdown'
        closeDropdown_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, closeDropdown_class))
        )
        driver.execute_script("arguments[0].click();", closeDropdown_button)



#call ChatGPT to write a comment

#type a comment and tag a resource




try:
    # driver.maximize_window()
    # email_address = CreateEmail()  # Capture the email address
    # if email_address:
    #     SignInFlow(email_address)  # Pass email_address to SignInFlow
    #     time.sleep(20)
    #     getVerificationEmail(email_address)  # Pass email_address to getVerificationEmail
    # else:
    #     print("Failed to create email address")
    driver.maximize_window()
    SignInFlow()
    navigateToQuest()
    time.sleep(5)
    voteOnSelectDatapoint()

except NoSuchElementException as e:
    print("Element not found:", e)
except TimeoutException as e:
    print("Loading took too much time:", e)
except Exception as e:
    print("An error occurred:", e)

finally:
    time.sleep(15)
    driver.quit()  # This will close the browser
