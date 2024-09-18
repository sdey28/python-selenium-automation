from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep




@given('Open Target help page')
def open_target_help_page(context):
    context.driver.get('https://help.target.com/help ')
    sleep(10)



@then('Verify header title')
def target_help_title(context):
    title_text = context.driver.find_element(By.XPATH, "//*[contains(text(), 'Target Help')]")
    correct_title = 'Target Help'
    assert f'{title_text} in {correct_title}', f"Expected {correct_title}, got {title_text}"



@then('Verify search help box')
def search_help_field(context):
   search_box = context.driver.find_element(By.CSS_SELECTOR, "[class='form-search form-inline'] [id='j_id0:j_id2:j_id32:name']")
   assert search_box, f"Expected search help box was not found"



@then('Verify search button')
def search_help_button(context):
    search_button = context.driver.find_element(By.CSS_SELECTOR, "[class='btn-sm search-btn']")
    assert search_button.is_enabled, f"Expected search button was not found"



@then('Verify what would you like to do box')
def wht_you_want_to_do_box(context):
    help_link_list = context.driver.find_elements(By.CSS_SELECTOR, "[class='col-lg-12'] [class='grid_6']")
    assert len(help_link_list) > 0, f"Expected help box was not found"



@then('Verify customer assistance options')
def customer_assistance_options(context):
    contact_us_option = context.driver.find_elements(By.XPATH, "//h3[(text()='contact us' or text()='product recalls')]")
    assert len(contact_us_option) > 0, f"Expected customer assistance option was not found"



@then('Verify footer title')
def browse_all_help_pages(context):
  actual_text = context.driver.find_element(By.XPATH, "//h2[text()='Browse all Help pages']")
  expected_text = 'Browse all Help pages'
  assert f'{actual_text} in {expected_text}', f"Expected {expected_text}, got {actual_text}"



