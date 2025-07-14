from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
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

        self.pending_filter = (
            AppiumBy.XPATH,
            '//android.widget.Button[contains(@content-desc, "Pending")]'
        )

        self.present_filter = (AppiumBy.ACCESSIBILITY_ID, 'Present')
        self.absent_filter = (AppiumBy.ACCESSIBILITY_ID, 'Absent')
        self.distant_checkin_filter = (AppiumBy.ACCESSIBILITY_ID, 'Distant Check-In')
        self.no_checkout_filter = (AppiumBy.ACCESSIBILITY_ID, 'No-CheckOut')
        self.no_breaks_filter = (AppiumBy.ACCESSIBILITY_ID, 'No Mark of Breaks')

        self.pending_container = (
            AppiumBy.XPATH,
            '//android.view.View[contains(@content-desc, "Emp Id")]'
        )

        self.reason_input = (AppiumBy.XPATH, "//android.widget.EditText")
        self.submit_button = (AppiumBy.XPATH, '//android.widget.Button[@content-desc="Submit"]')

        # Approve/Reject buttons within the container dialog
        self.approve_button = (AppiumBy.XPATH,
                               '//android.widget.Button[contains(@content-desc, "Approve") or contains(@content-desc, "Present")]')
        self.reject_button = (AppiumBy.XPATH,
                              '//android.widget.Button[contains(@content-desc, "Reject") or contains(@content-desc, "Absent")]')

        self.close_button = (
            AppiumBy.XPATH,
            '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.Button'
        )

    def click_toggle_menu(self):
        """Click the toggle menu button"""
        try:
            print("☞ Clicking Toggle menu...")
            toggle_element = self.wait.until(EC.element_to_be_clickable(self.toggle_icon))
            toggle_element.click()
            time.sleep(1)  # Wait for menu to open
            return True
        except TimeoutException:
            print("❌ Failed to find toggle menu button")
            return False

    def click_approve_attendance(self):
        """Click the Approve Attendance menu option"""
        try:
            print("📝 Clicking Approve Attendance...")
            approve_element = self.wait.until(EC.element_to_be_clickable(self.approve_attendance_menu))
            approve_element.click()
            time.sleep(2)  # Wait for page to load
            return True
        except TimeoutException:
            print("❌ Failed to find Approve Attendance menu")
            return False

    def click_filter_and_select(self, filter_locator):
        """Click filter icon and select a specific filter"""
        try:
            print("🔍 Clicking Filter icon...")
            filter_element = self.wait.until(EC.element_to_be_clickable(self.filter_icon))
            filter_element.click()
            time.sleep(1)

            print(f"🎯 Selecting filter: {filter_locator[1]}")
            filter_option = self.wait.until(EC.element_to_be_clickable(filter_locator))
            filter_option.click()
            time.sleep(2)  # Wait for filter to apply
            return True
        except TimeoutException as e:
            print(f"❌ Failed to click filter icon or select filter: {e}")
            return False

    def click_approve_present_button(self):
        """Click the Approve/Present button within the container dialog"""
        try:
            # Try multiple possible selectors for approve/present button
            approve_selectors = [
                (AppiumBy.XPATH, '//android.widget.Button[contains(@content-desc, "Present")]'),
                (AppiumBy.XPATH, '//android.widget.Button[contains(@content-desc, "Approve")]'),
                (AppiumBy.ACCESSIBILITY_ID, 'Present'),
                (AppiumBy.ACCESSIBILITY_ID, 'Approve'),
                (AppiumBy.XPATH, '//android.widget.Button[contains(text(), "Present")]'),
                (AppiumBy.XPATH, '//android.widget.Button[contains(text(), "Approve")]')
            ]

            for selector in approve_selectors:
                try:
                    element = self.wait.until(EC.element_to_be_clickable(selector))
                    element.click()
                    print("✅ Approve/Present button clicked successfully")
                    time.sleep(1)
                    return True
                except TimeoutException:
                    continue

            print("❌ Could not find Approve/Present button")
            return False

        except Exception as e:
            print(f"❌ Error clicking approve button: {e}")
            return False

    def click_reject_absent_button(self):
        """Click the Reject/Absent button within the container dialog"""
        try:
            # Try multiple possible selectors for reject/absent button
            reject_selectors = [
                (AppiumBy.XPATH, '//android.widget.Button[contains(@content-desc, "Absent")]'),
                (AppiumBy.XPATH, '//android.widget.Button[contains(@content-desc, "Reject")]'),
                (AppiumBy.ACCESSIBILITY_ID, 'Absent'),
                (AppiumBy.ACCESSIBILITY_ID, 'Reject'),
                (AppiumBy.XPATH, '//android.widget.Button[contains(text(), "Absent")]'),
                (AppiumBy.XPATH, '//android.widget.Button[contains(text(), "Reject")]')
            ]

            for selector in reject_selectors:
                try:
                    element = self.wait.until(EC.element_to_be_clickable(selector))
                    element.click()
                    print("✅ Reject/Absent button clicked successfully")
                    time.sleep(1)
                    return True
                except TimeoutException:
                    continue

            print("❌ Could not find Reject/Absent button")
            return False

        except Exception as e:
            print(f"❌ Error clicking reject button: {e}")
            return False

    def click_close_button_or_back(self):
        """Close the current dialog or go back"""
        try:
            close_btn = self.driver.find_element(*self.close_button)
            close_btn.click()
            print("✅ Close button clicked.")
            time.sleep(1)
        except NoSuchElementException:
            print("❌ Close button not found. Going back...")
            self.driver.back()
            time.sleep(1)

    def submit_reason(self, reason_text):
        """Submit reason for approval/rejection"""
        try:
            # Clear existing text and enter new reason
            reason_element = self.wait.until(EC.presence_of_element_located(self.reason_input))
            reason_element.clear()
            reason_element.send_keys(reason_text)

            # Click submit button
            submit_element = self.wait.until(EC.element_to_be_clickable(self.submit_button))
            submit_element.click()
            print(f"✅ Reason submitted: {reason_text}")
            time.sleep(2)  # Wait for submission to complete
            return True
        except TimeoutException:
            print("❌ Failed to submit reason.")
            return False

    def process_pending_tab(self):
        """Process the pending tab with approve/reject logic"""
        print("🔁 Handling Pending tab...")

        # Select pending filter
        if not self.click_filter_and_select(self.pending_filter):
            print("❌ Failed to select pending filter")
            return

        try:
            containers = self.driver.find_elements(*self.pending_container)
            if not containers:
                print("⚠️ No containers found in Pending tab.")
                return

            print(f"📋 Found {len(containers)} container(s) in Pending tab")

            processed_count = 0
            for i, container in enumerate(containers):
                if processed_count >= 2:  # Limit to 2 containers as per original logic
                    break

                status_text = container.get_attribute("content-desc") or ""
                if "Rejected" in status_text:
                    print(f"❌ Skipping rejected container ({status_text})")
                    continue

                print(f"📦 Processing container {processed_count + 1}...")
                container.click()
                time.sleep(2)  # Wait for container dialog to open

                # Determine action based on container index
                if processed_count == 0:
                    # First container - approve as present
                    print("✅ Clicking Approve/Present button...")
                    if self.click_approve_present_button():
                        self.submit_reason("Approved - Present")
                else:
                    # Second container - reject as absent
                    print("❌ Clicking Reject/Absent button...")
                    if self.click_reject_absent_button():
                        self.submit_reason("Declined - Absent")

                self.click_close_button_or_back()
                processed_count += 1
                time.sleep(1)  # Brief pause between containers

            print(f"✅ Completed processing {processed_count} containers in Pending tab")

        except Exception as e:
            print(f"❌ Error in process_pending_tab: {e}")

    def process_container_for_other_tabs(self):
        """Process containers for non-pending tabs (just view and close)"""
        try:
            print("🔍 Looking for containers in current filter tab...")
            time.sleep(2)  # Wait for filter to load data

            containers = self.driver.find_elements(*self.pending_container)
            if not containers:
                print("⚠️ No data present — no containers found in this filter tab.")
                return

            print(f"📋 Found {len(containers)} container(s) in this filter tab")

            # Process only the first container (as per original logic)
            for i, container in enumerate(containers):
                status_text = container.get_attribute("content-desc") or ""
                print(f"📦 Container {i + 1} status: {status_text}")

                if "Rejected" in status_text:
                    print(f"❌ Skipping rejected container ({status_text})")
                    continue

                print(f"📦 Opening container {i + 1}...")
                container.click()
                time.sleep(2)  # Wait for container to open

                # For other tabs, we just view the container and close it
                print("👀 Viewing container details...")
                time.sleep(1)

                self.click_close_button_or_back()
                print(f"✅ Finished viewing container in this filter tab")
                break  # Only process first valid container

        except Exception as e:
            print(f"❌ Error processing container for other tabs: {e}")

    def run_approve_attendance_flow(self):
        """Main method to run the complete approval flow"""
        print("🚀 Starting Approve Attendance Flow...")

        # Navigate to approve attendance page
        if not self.click_toggle_menu():
            print("❌ Failed to open toggle menu. Exiting.")
            return False

        if not self.click_approve_attendance():
            print("❌ Failed to navigate to approve attendance. Exiting.")
            return False

        # Process pending tab first
        self.process_pending_tab()

        print("✅ Finished processing Pending tab. Moving to other filter tabs...")

        # Process other filter tabs
        filters = [
            ("Present", self.present_filter),
            ("Absent", self.absent_filter),
            ("Distant Check-In", self.distant_checkin_filter),
            ("No-CheckOut", self.no_checkout_filter),
            ("No Mark of Breaks", self.no_breaks_filter)
        ]

        for filter_name, filter_locator in filters:
            print(f"🔁 Processing filter tab: {filter_name}")
            if self.click_filter_and_select(filter_locator):
                self.process_container_for_other_tabs()
                time.sleep(1)  # Brief pause between filter tabs
            else:
                print(f"❌ Failed to select filter: {filter_name}")

        print("✅ Approve Attendance Flow completed!")
        return True