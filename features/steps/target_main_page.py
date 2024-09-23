from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep



@given('Open Target main page')
def open_target_main_page(context):
    context.driver.get('https://www.target.com/')


@when('Search for {item}')
def search_for(context, item):
    context.driver.find_element(By.ID, 'search').send_keys(item)
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(10)



@then('Verify that correct search result shown for {item}')
def verify_results(context, item):
    actual_result = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    assert item in actual_result, f'Expected {item}, got actual {actual_result}'





@then('Verify each product with a name and an image')
def verify_search_result(context):


    products = context.driver.find_elements(By.CSS_SELECTOR, "[data-test='@web/ProductCard/body']")
    for product in products:
        name = context.driver.find_element(By.CSS_SELECTOR, "[data-test='product-title']").text
        img = context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/ProductCard/ProductCardImage']").get_attribute('src')

        assert name != "" and img != "", f'Expected each product with name {name}, and a image {img}'








