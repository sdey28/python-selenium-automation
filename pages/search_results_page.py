from time import sleep

from selenium.webdriver.common.by import By

from pages.base_page import Page

class SearchResultsPage(Page):
    SEARCH_RESULT_HEADER = (By.XPATH, "//div[@data-test='resultsHeading']")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
    SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")
    CART_CHECK_OUT = (By.XPATH, "//a[text()='View cart & check out']")

    def verify_results(self, product):
        actual_result = self.driver.find_element(*self.SEARCH_RESULT_HEADER).text
        assert product in actual_result, f'Expected {product}, got actual {actual_result}'


    def cart_button(self):
        self.driver.find_element(*self.ADD_TO_CART_BTN).click()


    def side_nav_carts(self):
        self.driver.find_element(*self.SIDE_NAV_PRODUCT_NAME).click()


    def cart_and_check_out(self):
        self.driver.find_element(*self.CART_CHECK_OUT).click()
        sleep(6)




