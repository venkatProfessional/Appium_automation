from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Approveleaveclass:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

        # ✅ Locators based on your shared XPaths
        self.toggleIcon = (
            AppiumBy.XPATH,
            '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button'
        )

        self.approve_leaves_button = (
            AppiumBy.XPATH,
            '//android.widget.Button[@content-desc="Approve Leaves\n4\n5"]'
        )

        self.pending_leave_item = (
            AppiumBy.XPATH,
            '//android.view.View[@content-desc="Pending\nName\n:\nfghfhg\nEmp Id\n:\n912\nNo.of Days\n:\n1\nLeave Date\n:\n12-07-2025"]'
        )

    def togglebar(self):
        print("☰ Toggling menu...")
        self.wait.until(EC.element_to_be_clickable(self.toggleIcon)).click()

    def click_approve_leaves_menu(self):
        print("📂 Clicking 'Approve Leaves'...")
        approve_btn = self.wait.until(EC.presence_of_element_located(
            (AppiumBy.XPATH, "//android.widget.Button[contains(@content-desc, 'Approve Leaves')]")
        ))
        approve_btn.click()

    from appium.webdriver.common.appiumby import AppiumBy
    def process_permission_requests(self):
        print("🔍 Scanning permission requests...")

        cards = self.driver.find_elements(AppiumBy.XPATH, "//android.view.View[contains(@content-desc, 'Emp Id')]")

        approved = False
        declined = False

        for card in cards:
            try:
                status = card.find_element(
                    AppiumBy.XPATH,
                    ".//android.view.View[contains(@content-desc, 'Approved') or contains(@content-desc, 'Pending')]"
                )
                status_text = status.get_attribute("content-desc")

                if "Approved" in status_text:
                    print("✅ Already Approved – skipping.")
                    continue

                elif "Pending" in status_text:
                    card.click()
                    time.sleep(1)

                    if not approved:
                        print("🟢 Approving request...")
                        self.wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Approve"))).click()
                        reason_input = self.wait.until(
                            EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.EditText")))
                        reason_input.send_keys("Permission approved")
                        self.wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Submit"))).click()
                        print("✅ Approved and submitted.")
                        approved = True

                    elif not declined:
                        print("🔴 Declining request...")
                        self.wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Decline"))).click()
                        reason_input = self.wait.until(
                            EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.EditText")))
                        reason_input.send_keys("Permission declined")

                        # ✅ Re-click Decline to confirm after reason
                        self.wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Decline"))).click()

                        print("✅ Declined with reason.")
                        declined = True

                    if approved and declined:
                        break

            except Exception as e:
                print(f"⚠️ Error processing card: {e}")

        if not approved:
            print("❌ No pending permission request found to approve.")
        if not declined:
            print("❌ No pending permission request found to decline.")


