
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

VERIFY_CELLS_PRESENT = (By.CSS_SELECTOR, "[data-test='@web/slingshot-components/CellsComponent/Link']")

@given('Open Target circle page')
def open_target_circle_page(context):
    context.driver.get('https://www.target.com/circle')
    context.driver.wait.until(
        EC.visibility_of_element_located(VERIFY_CELLS_PRESENT),
        message='Cells are not present in the target circle page'
    )


@then('Verify there are {expected_amount} benefit cells')
def verify_cells(context, expected_amount):
    cells = context.driver.find_elements(*VERIFY_CELLS_PRESENT)
    print(cells)
    assert len(cells) == int(expected_amount), f"Expected {expected_amount} benefit cells, got {len(cells)}"
