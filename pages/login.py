import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

        # Locators
        self.mobile_input = (AppiumBy.XPATH, '//android.widget.EditText[1]')
        self.password_input = (AppiumBy.XPATH, '//android.widget.EditText[2]')
        self.login_button = (AppiumBy.XPATH, '//android.widget.Button[@content-desc="LogIn"]')

    def wait_for_login_screen(self):
        self.wait.until(EC.presence_of_element_located(self.mobile_input))

    def enter_mobile(self, mobile):
        self.wait.until(EC.presence_of_element_located(self.mobile_input))
        element = self.driver.find_element(*self.mobile_input)
        element.click()
        element.clear()
        element.send_keys(mobile)

    def enter_password(self, password):
        self.wait.until(EC.presence_of_element_located(self.password_input))
        element = self.driver.find_element(*self.password_input)
        element.click()
        element.clear()
        element.send_keys(password)
        self.driver.press_keycode(66)

    def tap_login(self):
        self.wait.until(EC.element_to_be_clickable(self.login_button)).click()
        time.sleep(2)

    def is_login_screen_displayed(self):
        try:
            self.wait.until(EC.presence_of_element_located(self.mobile_input))
            return True
        except:
            return False

    def is_logged_in_successfully(self):
        try:
            self.wait.until(EC.presence_of_element_located((
                AppiumBy.XPATH, '//android.view.View[contains(@content-desc, "Dashboard")]'
            )))
            return True
        except:
            return False

    def login(self, mobile, password):
        self.wait_for_login_screen()
        self.enter_mobile(mobile)
        self.enter_password(password)
        self.tap_login()

    # ✅ Positive test method

    def test_login_positive_case(self):
        print("🚀 Running positive login test...")

        try:
            # Check for element with Accessibility ID (change this ID to match your app)
            success_element = self.wait.until(
                EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Our Projects"))  # or "Home", etc.
            )
            print("✅ Login successful – element with accessibility id 'Dashboard' is visible.")
        except:
            raise AssertionError("❌ Login failed: expected success element not found.")

    # ❌ Negative test method
    def test_login_negative_cases(self):
        test_data = [
            ("", "", "Empty mobile and password"),
            ("12345", "correctpass", "Invalid mobile format"),
            ("9876543210", "", "Valid mobile, empty password"),
            ("", "correctpass", "Empty mobile, valid password"),
            ("invalid", "invalid", "Invalid mobile and password"),
            ("9876543210", "wrongpass", "Valid mobile, wrong password")
        ]

        for mobile, password, desc in test_data:
            print(f"\n🧪 Negative Test: {desc}")
            self.login(mobile, password)
            assert self.is_login_screen_displayed(), f"❌ Login passed unexpectedly for: {desc}"
            print("✅ Login failed as expected.")
