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
driver.get('https://www.target.com/')

# Click SignIn button
driver.find_element(By.XPATH, "//span[@class='sc-58ad44c0-3 kwbrXj h-margin-r-x3']").click()
sleep(10)

# Click SignIn from side navigation
driver.find_element(By.XPATH, "//span[@class='sc-859e7637-0 hHZPQy']").click()
sleep(10)

# verify text is shown "Sign into your Target account"
actual_result = driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']").text
expected_result = 'Sign into your Target account'

# verify SignIn button
driver.find_element(By.ID, 'login')

expected_result in actual_result
print('Test case passed')


# Build a test case yourself from scratch to search for a product on Target (same as shown in the class), make sure it works and you remember selenium commands.

# open the URL
driver.get('https://www.target.com/')

# Search field ==> enter 'coffee'
driver.find_element(By.ID, 'search').send_keys('coffee')

# Click
driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
sleep(5)

# verification
actual_result = driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
expected_result = 'coffee'

assert expected_result in actual_result
print("Test Passed")


