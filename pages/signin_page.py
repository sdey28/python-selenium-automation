from selenium.webdriver.common.by import By

from pages.base_page import Page


class SigninPage(Page):
    VERIFY_SIGN_IN_FORM = (By.XPATH, "//span[text()='Sign into your Target account']")
    TARGET_TC_LINK = (By.XPATH, "//a[text()='Target terms and conditions']")

    def verify_signin_form_open(self):
        actual_result = self.driver.find_element(*self.VERIFY_SIGN_IN_FORM).text
        expected_result = 'Sign into your Target account'
        assert expected_result == actual_result, f"Expected '{expected_result}', got '{actual_result}'"

    def open_signin_page(self):
        self.open('https://www.target.com/login')

    def click_target_tc_link(self):
        self.wait_to_be_clickable_click(*self.TARGET_TC_LINK)

    def verify_target_tc_opened(self):
        self.verify_partial_url('terms-conditions/')