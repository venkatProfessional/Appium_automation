from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC

import pytest
from utils.driver_factory import create_driver
from pages.login import LoginPage

# This fixture creates the driver WITHOUT logging in
@pytest.fixture(scope="session")
def driver():
    driver = create_driver()
    yield driver
    # driver.quit()

# This fixture logs in after test starts (for positive tests only)
# @pytest.fixture(scope="session")
# def logged_in_driver(driver):
#     login_page = LoginPage(driver)
#     login_page.wait_for_login_screen()
#     login_page.enter_mobile("9999999999")  # ✅ Use real credentials
#     login_page.enter_password("Welcome@l1")
#     login_page.tap_login()
#     yield driver

@pytest.fixture(scope="session")
def logged_in_driver(driver):
    login_page = LoginPage(driver)
    login_page.wait_for_login_screen()
    login_page.enter_mobile("9999999999")  # ✅ Replace with actual number
    login_page.enter_password("Welcome@l1")
    login_page.tap_login()

    try:
        # ✅ Check for successful login using accessibility ID
        login_page.wait.until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Our Projects"))  # adjust if needed
        )
        print("✅ Login verified: 'Our Projects' screen is visible.")
    except:
        raise AssertionError("❌ Login failed during fixture setup. Element 'Our Projects' not found.")

    yield driver