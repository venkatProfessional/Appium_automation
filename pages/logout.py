from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class logout_test:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

        self.toggleIcon = (
            AppiumBy.XPATH,
            '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button'
        )

        self.logout_menu = (
            AppiumBy.XPATH,
            '//android.widget.Button[contains(@content-desc, "Logout")]'
        )

        self.logout_confirm_button = (
            AppiumBy.XPATH,
            '//android.widget.Button[@content-desc="Logout"]'
        )

        self.stay_button = (
            AppiumBy.XPATH,
            '//android.widget.Button[@content-desc="Stay"]'
        )

        self.login_screen_element = (
            AppiumBy.XPATH,
            '//android.widget.EditText[1]'
        )

    def perform_logout_flow(self):
        try:
            print("🔁 [Step 1] Open toggle menu and click Logout")
            self.wait.until(EC.element_to_be_clickable(self.toggleIcon)).click()
            self.wait.until(EC.element_to_be_clickable(self.logout_menu)).click()

            print("🛑 [Step 2] Tap 'Stay' on confirmation dialog")
            self.wait.until(EC.element_to_be_clickable(self.stay_button)).click()

            print("🔁 [Step 3] Reopen menu and tap Logout again")
            self.wait.until(EC.element_to_be_clickable(self.logout_menu)).click()

            print("✅ [Step 4] Tap 'Logout' on confirmation")
            self.wait.until(EC.element_to_be_clickable(self.logout_confirm_button)).click()

            print("🔍 [Step 5] Wait for login screen to verify logout success")
            self.wait.until(EC.presence_of_element_located(self.login_screen_element))

            print("🎉 Logout successful — login screen is visible.")

        except TimeoutException as e:
            raise AssertionError("❌ Logout failed or login screen not found.") from e
