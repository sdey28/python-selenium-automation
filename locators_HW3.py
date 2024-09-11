from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/ap/register?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_signin&prevRID=12N8QRW9RJRJCX2FBPV3&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&prepopulatedLoginId=&failedSignInCount=0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=usflex&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')
sleep(5)

# Amazon Logo
driver.find_element(By.CSS_SELECTOR, ".a-icon.a-icon-logo")


# create account
driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small")

# your name field
driver.find_element(By.ID, "ap_customer_name")

#Mobile number or email field
driver.find_element(By.ID, "ap_email")

# Password field
driver.find_element(By.ID, "ap_password")

# Re-enter Password field
driver.find_element(By.ID, "ap_password_check")

driver.find_element(By.ID, "continue")

# condition of use link
driver.find_element(By.CSS_SELECTOR, "[href*='notification_condition_of_use']")

# privacy Notice link
driver.find_element(By.CSS_SELECTOR, "[href*='notification_privacy_notice']")

# signin link
driver.find_element(By.CSS_SELECTOR, "[href*='ap/signin']")