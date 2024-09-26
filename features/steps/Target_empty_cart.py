from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


VERIFY_SIGN_IN_FORM = (By.XPATH, "//span[text()='Sign into your Target account']")
SIGN_IN_SIDE_BTN = (By.XPATH, "//span[@class='sc-859e7637-0 hHZPQy']")


@given('Open Target page')
def open_target(context):
    context.app.main_page.open_main()



@when('Click on Cart icon')
def cart_icon(context):
    context.app.cart_page.emp_cart()



@then('Verify “Your cart is empty” message is shown')
def cart_message(context):
    context.app.cart_page.verify_emp_cart_message()



@when('Click Sign In')
def click_signin(context):
    context.driver.find_element(By.CSS_SELECTOR, "[class='sc-58ad44c0-3 kwbrXj h-margin-r-x3']").click()
    context.driver.wait.until(
        EC.visibility_of_element_located(SIGN_IN_SIDE_BTN),
        message = 'Side Sign-in button not available'
    )



@then('Click on Sign In again')
def click_signin_again(context):
    context.driver.find_element(*SIGN_IN_SIDE_BTN).click()
    context.driver.wait.until(
        EC.visibility_of_element_located(VERIFY_SIGN_IN_FORM),
        message = 'Unable to find Sign-in form'
    )



@then('Verify Sign In form opened')
def verify_signin_form(context):
    actual_result = context.driver.find_element(*VERIFY_SIGN_IN_FORM).text
    expected_result = 'Sign into your Target account'
    assert expected_result == actual_result, f"Expected '{expected_result}', got '{actual_result}'"
