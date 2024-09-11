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
driver.get('https://www.amazon.com/')



#locate element:
#driver.find_element() #By. / value

driver.find_element(By.ID, 'twotabsearchtextbox')
driver.find_element(By.ID, 'nav-logo-sprites')

# By XPATH using 1 attribute
driver.find_element(By.XPATH, "//img[@alt='Crocs Unisex-Adult Classic Clogs']")
driver.find_element(By.XPATH, "//input[@name='field-keywords']")
driver.find_element(By.XPATH, "//input[@placeholder='Search Amazon']")

# By XPATH using multiple attribute
driver.find_element(By.XPATH, "//a[@class='nav-a  ' and @href='/gp/bestsellers/?ref_=nav_cs_bestsellers' and @tabindex='0']")

driver.quit()
