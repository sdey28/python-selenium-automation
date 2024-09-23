from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


VERIFY_CART_ITEM = (By.XPATH,"//div[./span[contains(text(), 'total')]]")

@then('Verify cart has {amount} item(s)')
def verify_cart(context, amount):
    cart_summary = context.driver.find_element(*VERIFY_CART_ITEM ).text
    assert f'{amount} item'  in cart_summary, f"Expected {amount} item(s), but got {cart_summary}"
