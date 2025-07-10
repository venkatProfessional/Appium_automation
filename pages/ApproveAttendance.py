from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class ApproveAttendanceClass:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.toggle_icon = (
            AppiumBy.XPATH,
            '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button'
        )

        self.approve_attendance_menu = (
            AppiumBy.XPATH,
            '//android.widget.Button[contains(@content-desc, "Approve Attendance")]'
        )

        self.filter_icon = (
            AppiumBy.XPATH,
            '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.Button'
        )

        self.pending_filter = (AppiumBy.ACCESSIBILITY_ID, 'Pending\n0')
        self.present_filter = (AppiumBy.ACCESSIBILITY_ID, 'Present')
        self.absent_filter = (AppiumBy.ACCESSIBILITY_ID, 'Absent')

        self.below_8hrs_filter = (AppiumBy.ACCESSIBILITY_ID, 'Below 8 Hours')
        self.after_8hrs_filter = (AppiumBy.ACCESSIBILITY_ID, 'After 8 Hours')
        self.distant_checkin_filter = (AppiumBy.ACCESSIBILITY_ID, 'Distant Check-In')
        self.no_checkout_filter = (AppiumBy.ACCESSIBILITY_ID, 'No-CheckOut')
        self.no_breaks_filter = (AppiumBy.ACCESSIBILITY_ID, 'No Mark of Breaks')

        self.pending_container = (
            AppiumBy.XPATH,
            '//android.view.View[contains(@content-desc, "Emp Id")]'
        )

        self.action_button = (
            AppiumBy.XPATH,
            '//android.widget.Button'
        )

        self.reason_input = (AppiumBy.XPATH, "//android.widget.EditText")
        self.submit_button = (AppiumBy.ACCESSIBILITY_ID, "Submit")

    def click_toggle_menu(self):
        print("☰ Clicking Toggle menu...")
        self.wait.until(EC.element_to_be_clickable(self.toggle_icon)).click()

    def click_approve_attendance(self):
        print("📝 Clicking Approve Attendance...")
        self.wait.until(EC.element_to_be_clickable(self.approve_attendance_menu)).click()

    def click_filter_and_select(self, filter_locator):
        print("🔍 Clicking Filter icon...")
        self.wait.until(EC.element_to_be_clickable(self.filter_icon)).click()
        time.sleep(1)
        print(f"🎯 Selecting filter: {filter_locator}")
        self.wait.until(EC.element_to_be_clickable(filter_locator)).click()
        time.sleep(2)

    def enter_reason_and_submit(self, reason_text="Automation Approved"):
        try:
            reason = self.wait.until(EC.presence_of_element_located(self.reason_input))
            reason.click()
            time.sleep(0.5)
            reason.send_keys(reason_text)
            print("✍️ Entered reason for approval.")

            entered_text = reason.get_attribute("text")
            if entered_text.strip():
                self.wait.until(EC.element_to_be_clickable(self.submit_button)).click()
                print("✅ Reason submitted successfully.")
            else:
                print("❌ Reason field empty — not submitted.")
        except Exception as e:
            print(f"❌ Failed to submit reason: {e}")

    def process_first_container(self):
        try:
            containers = self.driver.find_elements(*self.pending_container)
            if not containers:
                print("⚠️ No containers found for current filter.")
                return
            container = containers[0]
            container.click()
            print("📦 Clicked container.")
            time.sleep(1)
            self.wait.until(EC.element_to_be_clickable(self.action_button)).click()
            self.enter_reason_and_submit()
        except Exception as e:
            print(f"❌ Error processing container: {e}")

    def run_approve_attendance_flow(self):
        self.click_toggle_menu()
        self.click_approve_attendance()
        time.sleep(2)

        filters = [
            self.pending_filter,
            self.present_filter,
            self.absent_filter,
            # self.below_8hrs_filter,
            # self.after_8hrs_filter,
            self.distant_checkin_filter,
            self.no_checkout_filter,
            self.no_breaks_filter
        ]

        for f in filters:
            self.click_filter_and_select(f)
            self.process_first_container()
