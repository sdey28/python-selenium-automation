from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




@when('Click Sign In')
def click_signin(context):
    context.app.header.sign_in()



@then('Click on Sign In again')
def click_signin_again(context):
    context.app.header.side_nav_menu()



@then('Verify Sign In form opened')
def verify_signin_form(context):
    context.app.signin_page.verify_signin_form_open()