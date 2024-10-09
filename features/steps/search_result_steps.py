from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



VERIFY_CART_ITEM = (By.XPATH,"//div[./span[contains(text(), 'total')]]")


@when('click on the cart button')
def cart_button(context):
    context.app.search_results_page.cart_button()



@when('confirm add to cart from the side navigation')
def side_navigation(context):
    context.app.search_results_page.side_nav_carts()



@when('click cart & check out')
def cart_page(context):
   context.app.search_results_page.cart_and_check_out()