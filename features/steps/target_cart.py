from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep




@then('Verify cart has {amount} item(s)')
def verify_cart(context, amount):
    cart_summary = context.driver.find_element(By.XPATH,"//div[./span[contains(text(), 'total')]]").text
    assert f'{amount} item'  in cart_summary, f"Expected {amount} item(s), but got {cart_summary}"
