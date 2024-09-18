from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

Add_To_Cart_Btn = (By.CSS_SELECTOR, "[id*='addToCartButton']")


@when('click on the cart button')
def cart_button(context):
    context.driver.find_element(*Add_To_Cart_Btn).click()



@when('confirm add to cart from the side navigation')
def side_navigation(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']").click()


@when('click cart & check out')
def cart_page(context):
   context.driver.find_element(By.XPATH, "//a[text()='View cart & check out']").click()
   sleep(3)