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



# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--disable-dev-shm-usage")

# Initialize the Chrome driver with the specified options
service = Service(executable_path=r"C:\Program Files (x86)\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get('https://quester.io')
wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds

#INTERACT HERE
AccountUsername = 'Tyler L. Wallace'
AccountPassword = 'BeHU$BpR!QJib6V'
LinkToGoogleSheet = 'Trigonometry'
partyName = 'wallacestem'
questName = 'Trigonometry'
questDescription = 'Trigonometry'

# Function to get links from a Google Sheet
def get_links_from_sheet(sheet_name, worksheet_index=0):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name('C:\\Users\\talvi\\Downloads\\cellular-hybrid-405418-5ed70024484f.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open(sheet_name).get_worksheet(worksheet_index)
    links = sheet.col_values(1)  # Assuming links are in the first column
    titles = sheet.col_values(2)
    print(links)
    print(titles)
    return links, titles 

def ButtonClick(xpath):
    button_xpath = ''
    button = wait.until(EC.element_to_be_clickable((By.XPATH, button_xpath)))
    button.click()

    
def SignInFlow():
    login_button_xpath = '//*[@id="root"]/div/div[2]/div[1]/div[3]/div[1]/div[5]/div[2]/div/div[2]/div/div[3]/div[3]/span'
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, login_button_xpath)))
    login_button.click()
    username_xpath = '//*[@id="username"]'
    username_button = wait.until(EC.element_to_be_clickable((By.XPATH, username_xpath)))
    username_button.click()
    username_button.send_keys(AccountUsername)
    password_xpath = '//*[@id="password"]'
    password_button = wait.until(EC.element_to_be_clickable((By.XPATH, password_xpath)))
    password_button.click()
    password_button.send_keys(AccountPassword)
    sign_in_xpath = '//*[@id="kc-login"]'
    sign_in_button = wait.until(EC.element_to_be_clickable((By.XPATH, sign_in_xpath)))
    sign_in_button.click()

def navigateToParty():
    navigate_xpath = '//*[@id="root"]/div/div[2]/div[1]/div[3]/div[1]/div[5]/div[2]/div/div[2]/div/div[2]/div/span'
    navigate_button = wait.until(EC.element_to_be_clickable((By.XPATH, navigate_xpath)))
    navigate_button.click()
    search_xpath = '//*[@id="root"]/div/div[2]/div[1]/div[3]/div[2]/div/div/div/div/div[1]/div[1]/input'
    search_button = wait.until(EC.element_to_be_clickable((By.XPATH, search_xpath)))
    search_button.click()
    search_button.send_keys(partyName)
    top_result_xpath = '//*[@id="root"]/div/div[2]/div[1]/div[3]/div[2]/div/div/div/div/div[4]/a/div[2]/div[1]'
    top_result_button = wait.until(EC.element_to_be_clickable((By.XPATH, top_result_xpath)))
    top_result_button.click()

def createQuest():
    print('HELLO 1')
    NewQuest_xpath = '//*[@id="root"]/div/div[2]/div[1]/div[6]/div/div/div/div/div/div[2]/div[3]/div[2]/div/button'
    NewQuest_button = wait.until(EC.element_to_be_clickable((By.XPATH, NewQuest_xpath)))
    driver.execute_script("arguments[0].click();", NewQuest_button)
    print('HELLO 2')
    questName_xpath = '//*[@id="root"]/div/div[2]/div[1]/div[6]/div[1]/div/div/div[2]/div[1]/div[1]/input'
    questName_button = wait.until(EC.element_to_be_clickable((By.XPATH, questName_xpath)))
    questName_button.click()
    questName_button.send_keys(questName)
    print('HELLO 3')
    questDescription_xpath = '//*[@id="root"]/div/div[2]/div[1]/div[6]/div[1]/div/div/div[2]/div[1]/div[2]/textarea'
    questDescription_button = wait.until(EC.element_to_be_clickable((By.XPATH, questDescription_xpath)))
    questDescription_button.click()
    questDescription_button.send_keys(questDescription)
    time.sleep(1)
    # edit_xpath = '//*[@id="root"]/div/div[2]/div[1]/div[6]/div[1]/div/div/div/div[2]/div[1]/div[4]/div[2]/div/div/span'
    # edit_button = wait.until(EC.element_to_be_clickable((By.XPATH, edit_xpath)))
    # edit_button.click()
    # print('pressed edit')

def click_new():
    new_button_class_name = 'addQuestBulkButton'
    new_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, new_button_class_name)))
    driver.execute_script("arguments[0].click();", new_button)


def paste_link():
    links, titles = get_links_from_sheet(LinkToGoogleSheet)
    print(links)
    paste_xpath = '//*[@id="root"]/div/div[2]/div[1]/div[6]/div[1]/div/div/div[2]/div[3]/div/div[2]/div/div/div/input'
    
    for link, title in zip(links, titles):
        # Paste the link
        paste_button = wait.until(EC.element_to_be_clickable((By.XPATH, paste_xpath)))
        paste_button.click()
        paste_button.clear()
        paste_button.send_keys(link)
        paste_button.send_keys(Keys.ENTER)
        time.sleep(2)
        # Wait for title elements to be available and find them
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#root > div > div:nth-child(2) > div.mainLayoutWrapper > div.mainArea > div.css-1ndrsdj.questEditModeMegaWrap > div > div > div.container-fluid > div.resourceListMegaWrapper > div > div.resourceList > div.resource.editResource > div.resourceLeft > div.resourceInfo > div.resourceTitle > input")))
        title_buttons = driver.find_elements(By.CSS_SELECTOR, "#root > div > div:nth-child(2) > div.mainLayoutWrapper > div.mainArea > div.css-1ndrsdj.questEditModeMegaWrap > div > div > div.container-fluid > div.resourceListMegaWrapper > div > div.resourceList > div.resource.editResource > div.resourceLeft > div.resourceInfo > div.resourceTitle > input")


        if title_buttons:
            last_title_button = title_buttons[-1]
            last_title_button.click()

            # Clear the field using a sequence of backspaces
            last_title_button.send_keys(Keys.CONTROL + "a")
            last_title_button.send_keys(Keys.DELETE)

            # Now send the title
            last_title_button.send_keys(title)
            time.sleep(2)


            # Optional: add a short delay to ensure changes are processed
            time.sleep(1)
        else:
            print("No title buttons found")

        click_new()

        # Optional: add a delay before processing the next link
        time.sleep(2)




def upload_resource():
    click_new()
    paste_link()

def press_done():
    done_xpath = '//*[@id="root"]/div/div[2]/div[1]/div[6]/div[1]/div/div/div[2]/div[2]/div[2]/div[2]'
    done_button = wait.until(EC.presence_of_element_located((By.XPATH, done_xpath)))
    driver.execute_script("arguments[0].click();", done_button)


try:
    driver.maximize_window()

    SignInFlow()
    navigateToParty()
    createQuest()
    upload_resource()
    press_done()
    

except NoSuchElementException as e:
    print("Element not found:", e)
except TimeoutException as e:
    print("Loading took too much time:", e)
except Exception as e:
    print("An error occurred:", e)

finally:
    time.sleep(10)
    driver.quit()  # This will close the browser
