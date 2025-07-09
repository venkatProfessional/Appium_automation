from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class ResignationMaintenanceClass:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

        # Locators
        self.toggleIcon = (
            AppiumBy.XPATH,
            '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button'
        )

        self.resignation_menu = (
            AppiumBy.XPATH,
            '//android.widget.Button[contains(@content-desc, "Resignation Maintenance")]'
        )

        self.filtericon = (AppiumBy.XPATH,
                           '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.Button')
        self.pending = (AppiumBy.ACCESSIBILITY_ID, "Pending")
        self.approved = (AppiumBy.ACCESSIBILITY_ID, "Approved")
        self.declined = (AppiumBy.ACCESSIBILITY_ID, "Declined")
        self.all = (AppiumBy.ACCESSIBILITY_ID, "All")

        self.card_locator = (
            AppiumBy.XPATH,
            '//android.view.View[contains(@content-desc, "Emp Id")]'
        )

    def click_toggle_menu(self):
        print("☰ Toggling menu...")
        self.wait.until(EC.element_to_be_clickable(self.toggleIcon)).click()

    def click_resignation_menu(self):
        print("📁 Clicking 'Resignation Maintenance' menu...")
        self.wait.until(EC.element_to_be_clickable(self.resignation_menu)).click()

    def click_filter_icon(self):
        print("🔍 Clicking filter icon...")
        self.wait.until(EC.element_to_be_clickable(self.filtericon)).click()
        time.sleep(1)

    def click_filter_option(self, filter_locator, filter_name=""):
        try:
            self.wait.until(EC.element_to_be_clickable(filter_locator)).click()
            print(f"✅ Clicked '{filter_name}' filter.")
            time.sleep(2)
            return True
        except Exception as e:
            print(f"❌ Could not click '{filter_name}' filter → {e}")
            return False

    def check_cards_and_print(self, label):
        try:
            cards = self.driver.find_elements(*self.card_locator)
            print(f"📄 {label}: Found {len(cards)} card(s).")

            for i, card in enumerate(cards[:3]):  # Print top 3 only
                try:
                    desc = card.get_attribute("content-desc")
                    print(f"📝 Card {i+1}: {desc[:100]}..." if len(desc) > 100 else f"📝 Card {i+1}: {desc}")
                except:
                    print(f"⚠️ Could not read content-desc of card {i+1}")

            if len(cards) > 3:
                print(f"📄 ... and {len(cards) - 3} more card(s).")
        except Exception as e:
            print(f"⚠️ Error fetching cards → {e}")

    def verify_all_filters(self):
        print("🔎 Starting filter verification for resignation...")

        self.click_toggle_menu()
        self.click_resignation_menu()
        self.click_filter_icon()

        for label, locator in [
            ("Pending", self.pending),
            ("Approved", self.approved),
            ("Declined", self.declined),
            ("All", self.all)
        ]:
            if self.click_filter_option(locator, label):
                self.check_cards_and_print(label)
                self.click_filter_icon()
            else:
                print(f"⚠️ Skipping card check for '{label}' due to filter click failure")

        print("✅ Resignation filter verification completed.")
