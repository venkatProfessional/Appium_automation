from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class FeedbackPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

        # Locators
        self.toggle_icon = (
            AppiumBy.XPATH,
            '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button'
        )
        self.feedback_menu = (AppiumBy.ACCESSIBILITY_ID, "Feedback")
        self.feedback_card = (
            AppiumBy.XPATH,
            '//android.view.View[@content-desc="YFHGFHGH\ntesrtrr"]'
        )
        self.close_button = (AppiumBy.ACCESSIBILITY_ID, "Close")

    def click_toggle_menu(self):
        print("☰ Clicking toggle menu...")
        self.wait.until(EC.element_to_be_clickable(self.toggle_icon)).click()

    def click_feedback_menu(self):
        print("📝 Clicking Feedback menu...")
        self.wait.until(EC.element_to_be_clickable(self.feedback_menu)).click()

    def open_and_close_feedback_cards(self,counttotest):
        print("🔄 Opening and closing feedback cards...")

        try:
            for i in range(counttotest):
                # Find all feedback cards fresh every time to avoid stale elements
                cards = self.driver.find_elements(
                    AppiumBy.XPATH,
                    '//android.view.View[contains(@content-desc, "\n")]'
                )

                if i >= len(cards):
                    print(f"❌ Only {len(cards)} feedback cards found. Cannot click card {i + 1}.")
                    break

                print(f"🗂️ Opening feedback card {i + 1}...")
                self.wait.until(EC.element_to_be_clickable(cards[i])).click()
                time.sleep(1)

                # Close icon by XPath
                close_icon = self.wait.until(EC.element_to_be_clickable((
                    AppiumBy.XPATH, "//android.widget.Button"
                )))
                close_icon.click()
                print(f"❌ Closed feedback card {i + 1}")
                time.sleep(1)

        except Exception as e:
            print(f"⚠️ Error during feedback card handling → {e}")



