from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep




@then('Verify cart has {amount} item(s)')
def verify_cart(context, amount):
    context.app.cart_page.verify_cart_item(amount)