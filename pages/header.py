from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page

class Header(Page):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    SIGN_IN_BTN = (By.CSS_SELECTOR, "[class='sc-58ad44c0-3 kwbrXj h-margin-r-x3']")
    SIGN_IN_SIDE_BTN = (By.XPATH, "//span[@class='sc-859e7637-0 hHZPQy']")

    def search_product(self, item):
        self.input_text(item, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        sleep(10)


    def sign_in(self):
        self.driver.find_element(*self.SIGN_IN_BTN).click()


    def side_nav_menu(self):
        self.driver.find_element(*self.SIGN_IN_SIDE_BTN).click()
        sleep(5)


