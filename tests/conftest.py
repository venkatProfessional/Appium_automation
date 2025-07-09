# conftest.py
import pytest
from utils.driver_factory import create_driver
from pages.login import LoginPage

@pytest.fixture(scope="session")
def logged_in_driver():
    driver = create_driver()
    login_page = LoginPage(driver)
    login_page.wait_for_login_screen()
    login_page.enter_mobile("9999999999")
    login_page.enter_password("Welcome@l1")
    login_page.tap_login()
    yield driver
    # driver.quit()
