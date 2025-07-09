from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class RepairMaintenanceClass:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

        # Locators
        self.toggleIcon = (
            AppiumBy.XPATH,
            '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button'
        )

        self.repair_maintenance_menu = (
            AppiumBy.XPATH,
            '//android.widget.Button[contains(@content-desc, "Repair Maintenance")]'
        )

        self.card_locator = (
            AppiumBy.XPATH,
            '//android.view.View[contains(@content-desc, "\n")]'
        )

        self.close_button = (AppiumBy.XPATH, "//android.widget.Button")

    def click_toggle_menu(self):
        print("☰ Toggling menu...")
        self.wait.until(EC.element_to_be_clickable(self.toggleIcon)).click()

    def click_repair_maintenance_menu(self):
        print("🔧 Clicking 'Repair Maintenance' menu...")
        self.wait.until(EC.element_to_be_clickable(self.repair_maintenance_menu)).click()

    def open_and_close_cards(self, counttotest):
        print("🔄 Opening and closing repair maintenance cards...")

        try:
            for i in range(counttotest):
                # Find all cards fresh every time
                cards = self.driver.find_elements(*self.card_locator)

                if i >= len(cards):
                    print(f"❌ Only {len(cards)} cards found. Cannot click card {i + 1}.")
                    break

                print(f"🗂️ Opening card {i + 1}...")
                self.wait.until(EC.element_to_be_clickable(cards[i])).click()
                time.sleep(1)

                # Close icon
                close_icon = self.wait.until(EC.element_to_be_clickable(self.close_button))
                close_icon.click()
                print(f"❌ Closed card {i + 1}")
                time.sleep(1)

        except Exception as e:
            print(f"⚠️ Error during card handling → {e}")

    def run_repair_maintenance_flow(self, counttotest):
        print("🔍 Starting Repair Maintenance card navigation...")

        self.click_toggle_menu()
        self.click_repair_maintenance_menu()
        self.open_and_close_cards(counttotest)

        print("✅ Repair Maintenance card navigation completed.")