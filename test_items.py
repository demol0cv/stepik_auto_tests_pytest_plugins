import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_basket_button(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    WebDriverWait(browser, timeout=3).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR,"form#add_to_basket_form>button[type=\"submit\"]"),
            ),
    )
    add_to_basket_button = browser.find_element(By.CSS_SELECTOR, "form#add_to_basket_form>button[type=\"submit\"]")
    assert add_to_basket_button.is_displayed(), "Кнопка не отображается"
