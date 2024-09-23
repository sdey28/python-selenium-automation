from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")
VERIFY_CART_ITEM = (By.XPATH,"//div[./span[contains(text(), 'total')]]")


@when('click on the cart button')
def cart_button(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()
    context.driver.wait.until(
        EC.visibility_of_element_located(SIDE_NAV_PRODUCT_NAME),
        message = 'side navigation product name not visible'
    )


@when('confirm add to cart from the side navigation')
def side_navigation(context):
    context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).click()


@when('click cart & check out')
def cart_page(context):
   context.driver.find_element(By.XPATH, "//a[text()='View cart & check out']").click()
   context.driver.wait.until(
       EC.visibility_of_element_located(VERIFY_CART_ITEM),
       message = 'cart item not visible'
   )