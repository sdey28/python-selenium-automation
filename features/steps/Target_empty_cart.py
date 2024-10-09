from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC





@given('Open Target page')
def open_target(context):
    context.app.main_page.open_main()



@when('Click on Cart icon')
def cart_icon(context):
    context.app.cart_page.emp_cart()



@then('Verify “Your cart is empty” message is shown')
def cart_message(context):
    context.app.cart_page.verify_emp_cart_message()



