
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep



@given('Open Target circle page')
def open_target_circle_page(context):
    context.driver.get('https://www.target.com/circle')
    sleep(5)


@then('Verify there are {expected_amount} benefit cells')
def verify_cells(context, expected_amount):
    cells = context.driver.find_elements(By.CSS_SELECTOR, "[data-test='@web/slingshot-components/CellsComponent/Link']")
    print(cells)
    assert len(cells) == int(expected_amount), f"Expected {expected_amount} benefit cells, got {len(cells)}"
