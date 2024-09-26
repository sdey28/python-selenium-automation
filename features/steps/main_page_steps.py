from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


LISTING = (By.CSS_SELECTOR, "[data-test = '@web/site-top-of-funnel/ProductCardWrapper']")
PRODUCT_NAME = (By.XPATH, "//a[@data-test='product-title']")
PRODUCT_IMG = (By.CSS_SELECTOR, 'img')




@given('Open Target main page')
def open_target_main_page(context):
    context.app.main_page.open_main()




@when('Search for {item}')
def search_for(context, item):
    context.app.header.search_product(item)



@then('Verify that correct search result shown for {product}')
def verify_results(context, product):
    context.app.search_results_page.verify_results(product)



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








