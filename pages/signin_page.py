from selenium.webdriver.common.by import By

from pages.base_page import Page


class SigninPage(Page):
    VERIFY_SIGN_IN_FORM = (By.XPATH, "//span[text()='Sign into your Target account']")

    def verify_signin_form_open(self):
        actual_result = self.driver.find_element(*self.VERIFY_SIGN_IN_FORM).text
        expected_result = 'Sign into your Target account'
        assert expected_result == actual_result, f"Expected '{expected_result}', got '{actual_result}'"

