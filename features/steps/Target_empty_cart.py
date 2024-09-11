from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep



@given('Open Target page')
def open_target(context):
    context.driver.get('https://www.target.com/')



@when('Click on Cart icon')
def cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "[href*='/icons/Cart.svg#Cart']").click()


@then('Verify message is shown')
def cart_message(context):
    actual_result = context.driver.find_element(By.CSS_SELECTOR, "[class='sc-fe064f5c-0 dtCtuk']").text
    expected_result = 'Your cart is empty'
    assert expected_result == actual_result


@when('Click Sign In')
def click_signin(context):
    context.driver.find_element(By.CSS_SELECTOR, "[class='sc-58ad44c0-3 kwbrXj h-margin-r-x3']").click()
    sleep(2)

@then('Click on Sign In again')
def click_signin_again(context):
    context.driver.find_element(By.XPATH, "//span[@class='sc-859e7637-0 hHZPQy']").click()
    sleep(10)


@then('Verify Sign In form opened')
def verify_signin_form(context):
    actual_result = context.driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']").text
    expected_result = 'Sign into your Target account'
    assert expected_result == actual_result
