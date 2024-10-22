from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open sign in page')
def open_sign_in_page(context):
    context.app.signin_page.open_signin_page()
    sleep(5)


@when('Store original window')
def store_original_window(context):
    context.original_window = context.app.signin_page.get_current_window()
    print('Original window', context.original_window)


@when('Click on Target terms and conditions link')
def target_terms_conditions_link(context):
      context.app.signin_page.click_target_tc_link()


@when('Switch to the newly opened window')
def switch_window(context):
    context.app.signin_page.switch_to_new_window()
    print('After switched', context.app.signin_page.get_current_window())



@then('Verify Terms and Conditions page is opened')
def verify_tc_opened(context):
      context.app.signin_page.verify_target_tc_opened()
      sleep(3)


@then('User can close new window')
def close_window(context):
       context.app.signin_page.close()
       sleep(1)

@then('switch back to original')
def switch_back(context):
    context.app.signin_page.switch_to_new_window_by_id(context.original_window)
    sleep(1)