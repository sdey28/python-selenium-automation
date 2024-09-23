from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


COLORS_OPTIONS = (By.CSS_SELECTOR, "div[aria-label='Carousel'] li img")
SELECTED_COLORS = (By.CSS_SELECTOR, "[data-test='@web/VariationComponent'] div")


@given('Open Target product {product_id}')
def open_target_page(context, product_id):
    context.driver.get(f'https://www.target.com/p/{product_id}')
    sleep(8)



@then('verify user can click through colors')
def verify_colors(context):
    expected_colors = ['Cream','Green','Gray']
    actual_colors =[]

    colors = context.driver.find_elements(*COLORS_OPTIONS)
    for color in colors:
        color.click()

        selected_color = context.driver.find_element(*SELECTED_COLORS).text
        print('Current color', selected_color)


        selected_color = selected_color.split('\n')[1]
        actual_colors.append(selected_color)
        print(actual_colors)

    assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'

