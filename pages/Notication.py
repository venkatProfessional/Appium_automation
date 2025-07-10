from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
import time

class NotificationMaintenanceClass:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Toggle menu icon (☰)
        self.toggleIcon = (
            AppiumBy.XPATH,
            '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button'
        )

        # Notification menu item
        self.notification_menu = (
            AppiumBy.XPATH,
            '//android.widget.Button[contains(@content-desc, "Notification")]'
        )

        # Notification container blocks (dynamic content-desc)
        self.notification_containers = (
            AppiumBy.XPATH,
            '//android.view.View[@content-desc and @class="android.view.View"]'
        )

    def click_toggle_menu(self):
        print("☰ Clicking toggle menu...")
        self.wait.until(EC.element_to_be_clickable(self.toggleIcon)).click()

    def click_notification_menu(self):
        print("🔔 Clicking notification menu...")
        self.wait.until(EC.element_to_be_clickable(self.notification_menu)).click()

    def click_notifications_one_by_one(self, count=5):
        print(f"👆 Clicking {count} notification blocks one by one...")
        for i in range(count):
            try:
                containers = self.wait.until(EC.presence_of_all_elements_located(self.notification_containers))

                if len(containers) > i:
                    print(f"➡️ Trying to click notification block {i + 1}")
                    try:
                        self.wait.until(EC.element_to_be_clickable(containers[i]))
                        containers[i].click()
                        print(f"✅ Clicked notification block {i + 1}")
                        time.sleep(1)
                        self.driver.back()
                        time.sleep(1)
                    except (TimeoutException, WebDriverException):
                        print(f"❌ Notification block {i + 1} is not clickable.")
                else:
                    print(f"⚠️ Only {len(containers)} notification blocks found.")
                    break
            except Exception as e:
                print(f"❌ Error clicking notification block {i + 1}: {e}")
                break

    def run_notification_maintenance_flow(self):
        self.click_toggle_menu()
        self.click_notification_menu()
        self.click_notifications_one_by_one(count=5)
