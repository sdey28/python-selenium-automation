from selenium.webdriver.common.by import By

from pages.base_page import Page


class CartPage(Page):
    EMP_CART_BTN = (By.CSS_SELECTOR, "[href*='/icons/Cart.svg#Cart']")
    EMP_CART_MSG = (By.CSS_SELECTOR, "[class='sc-fe064f5c-0 dtCtuk']")
    VERIFY_CART_ITEM = (By.XPATH, "//div[./span[contains(text(), 'total')]]")


    def emp_cart(self):
        self.click(*self.EMP_CART_BTN)


    def verify_emp_cart_message(self):
        actual_result = self.driver.find_element(*self.EMP_CART_MSG).text
        expected_result = 'Your cart is empty'
        assert expected_result == actual_result, f"Expected '{expected_result}', got '{actual_result}'"


    def verify_cart_item(self,amount):
        cart_summary = self.driver.find_element(*self.VERIFY_CART_ITEM).text
        assert f'{amount} item' in cart_summary, f"Expected {amount} item(s), but got {cart_summary}"
