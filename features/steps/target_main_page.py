from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


LISTING = (By.CSS_SELECTOR, "[data-test = '@web/site-top-of-funnel/ProductCardWrapper']")
PRODUCT_NAME = (By.XPATH, "//a[@data-test='product-title']")
PRODUCT_IMG = (By.CSS_SELECTOR, 'img')




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
    context.driver.execute_script("window.scrollBy(0, 2000)", "")
    sleep(5)
    context.driver.execute_script("window.scrollBy(0, 2000)", "")


    all_products = context.driver.find_elements(*LISTING)

    for product in all_products:
        print(product)
        name = product.find_element(*PRODUCT_NAME).text
        assert name, 'product name not listed'
        print(name)
        product.find_element(*PRODUCT_IMG)








