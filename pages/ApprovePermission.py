from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class ApprovePermissionClass:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

        # Locators
        self.toggleIcon = (
            AppiumBy.XPATH,
            '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button'
        )

        self.approve_permission_button = (
            AppiumBy.XPATH,
            '//android.widget.Button[contains(@content-desc, "Approve Permission")]'
        )

        self.reason_input = (AppiumBy.XPATH, "//android.widget.EditText")
        self.submit_button = (AppiumBy.ACCESSIBILITY_ID, "Submit")
        self.filtericon = (AppiumBy.XPATH,
                           '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.Button')
        self.pending = (AppiumBy.ACCESSIBILITY_ID, "Pending\n19")
        self.approved = (AppiumBy.XPATH, '//android.widget.Button[@content-desc="Approved"]')
        self.Declined = (AppiumBy.XPATH, '//android.widget.Button[@content-desc="Declined"]')
        self.All = (AppiumBy.XPATH, '//android.widget.Button[@content-desc="All"]')
        self.clickondated = (AppiumBy.XPATH, '//android.view.View[@content-desc="dd-MM-yyyy"]')
        self.selectdata = (AppiumBy.ACCESSIBILITY_ID, 'Tuesday, July 1, 2025')
        self.clickokoncalender = (AppiumBy.ACCESSIBILITY_ID, "OK")
        self.checkonstatusandDatefield = (AppiumBy.ACCESSIBILITY_ID,
                                          r'Rejected\nName\n:\nNihaa\nEmp Id\n:\n917\nDate\n:\n01-07-2025\nLeave Date\n:\n30 minutes')

    def togglebar(self):
        print("☰ Toggling menu...")
        self.wait.until(EC.element_to_be_clickable(self.toggleIcon)).click()

    def click_approve_permission_menu(self):
        print("📂 Clicking 'Approve Permission'...")
        self.wait.until(EC.element_to_be_clickable(self.approve_permission_button)).click()

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
                        print("🟢 Approving permission request...")
                        self.wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Approve"))).click()

                        reason = self.wait.until(EC.element_to_be_clickable(self.reason_input))
                        reason.click()
                        time.sleep(0.5)
                        reason.send_keys("Permission approved")
                        print("✍️ Entered reason for approval.")

                        entered_text = reason.get_attribute("text")
                        if entered_text.strip():
                            self.wait.until(EC.element_to_be_clickable(self.submit_button)).click()
                            print("✅ Permission approved and submitted.")
                            approved = True
                        else:
                            print("❌ Reason field empty — approval not submitted.")

                    elif not declined:
                        print("🔴 Declining permission request...")
                        self.wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Decline"))).click()

                        reason = self.wait.until(EC.element_to_be_clickable(self.reason_input))
                        reason.click()
                        time.sleep(0.5)
                        reason.send_keys("Permission declined")
                        print("✍️ Entered reason for decline.")

                        entered_text = reason.get_attribute("text")
                        if entered_text.strip():
                            self.wait.until(EC.element_to_be_clickable(self.submit_button)).click()
                            print("✅ Permission declined and submitted.")
                            declined = True
                        else:
                            print("❌ Reason field empty — decline not submitted.")

                    if approved and declined:
                        break

            except Exception as e:
                print(f"⚠️ Error processing card: {e}")

        if not approved:
            print("❌ No pending permission to approve.")
        if not declined:
            print("❌ No pending permission to decline.")

    def safe_click(self, locator, label=""):
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            self.wait.until(EC.element_to_be_clickable(locator)).click()
            print(f"✅ Clicked {label or locator[1]}")
            time.sleep(0.5)
            return True
        except Exception as e:
            print(f"⚠️ Could not click {label or locator[1]} → {e}")
            return False

    def test_approve_one_request(self):
        print("🧪 Testing: Approving one request...")

        try:
            pending_cards = self.driver.find_elements(AppiumBy.XPATH,
                                                      "//android.view.View[contains(@content-desc, 'Emp Id') and contains(@content-desc, 'Pending')]")

            if not pending_cards:
                print("📋 List is empty - No pending requests to approve")
                return False

            pending_cards[0].click()
            time.sleep(1)

            self.wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Approve"))).click()

            reason = self.wait.until(EC.element_to_be_clickable(self.reason_input))
            reason.click()
            time.sleep(0.5)
            reason.send_keys("Test approval")

            entered_text = reason.get_attribute("text")
            if entered_text.strip():
                self.wait.until(EC.element_to_be_clickable(self.submit_button)).click()
                print("✅ Test approval completed successfully")
                return True
            else:
                print("❌ Test approval failed - reason field empty")
                return False

        except Exception as e:
            print(f"⚠️ Test approval failed: {e}")
            return False

    def test_decline_one_request(self):
        print("🧪 Testing: Declining one request...")

        try:
            pending_cards = self.driver.find_elements(AppiumBy.XPATH,
                                                      "//android.view.View[contains(@content-desc, 'Emp Id') and contains(@content-desc, 'Pending')]")

            if not pending_cards:
                print("📋 List is empty - No pending requests to decline")
                return False

            pending_cards[0].click()
            time.sleep(1)

            self.wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Decline"))).click()

            reason = self.wait.until(EC.element_to_be_clickable(self.reason_input))
            reason.click()
            time.sleep(0.5)
            reason.send_keys("Test decline")

            entered_text = reason.get_attribute("text")
            if entered_text.strip():
                self.wait.until(EC.element_to_be_clickable(self.submit_button)).click()
                print("✅ Test decline completed successfully")
                return True
            else:
                print("❌ Test decline failed - reason field empty")
                return False

        except Exception as e:
            print(f"⚠️ Test decline failed: {e}")
            return False

    def verify_filter_by_status_and_date(self):
        print("🔽 Filtering by status and date...")

        try:
            self.driver.find_element(*self.filtericon).click()
            print("🔁 Clicked Filter icon")
            time.sleep(1)
        except Exception as e:
            print(f"⚠️ Could not click Filter icon → {e}")
            return

        try:
            self.driver.find_element(*self.pending).click()
            print("✅ Clicked Pending filter")
            time.sleep(2)
            self.test_approve_one_request()
        except Exception as e:
            print(f"⚠️ Could not click Pending → {e}")

        try:
            self.driver.find_element(*self.filtericon).click()
            print("🔁 Clicked Filter icon again")
            time.sleep(1)
        except Exception as e:
            print(f"⚠️ Could not click Filter icon → {e}")

        try:
            self.driver.find_element(*self.approved).click()
            print("✅ Clicked Approved filter")
            time.sleep(2)

            approved_cards = self.driver.find_elements(AppiumBy.XPATH,
                                                       "//android.view.View[contains(@content-desc, 'Emp Id') and contains(@content-desc, 'Approved')]")

            if not approved_cards:
                print("📋 Approved list is empty")
            else:
                print(f"📋 Found {len(approved_cards)} approved requests")
        except Exception as e:
            print(f"⚠️ Could not click Approved → {e}")

        try:
            self.driver.find_element(*self.filtericon).click()
            print("🔁 Clicked Filter icon again")
            time.sleep(1)
        except Exception as e:
            print(f"⚠️ Could not click Filter icon → {e}")

        try:
            self.driver.find_element(*self.Declined).click()
            print("✅ Clicked Declined filter")
            time.sleep(2)

            declined_cards = self.driver.find_elements(AppiumBy.XPATH,
                                                       "//android.view.View[contains(@content-desc, 'Emp Id') and contains(@content-desc, 'Declined')]")

            if not declined_cards:
                print("📋 Declined list is empty")
                self.driver.find_element(*self.filtericon).click()
                time.sleep(1)
                try:
                    self.driver.find_element(*self.pending).click()
                    print("🔄 Switched back to Pending to test decline")
                    time.sleep(2)
                    self.test_decline_one_request()
                except:
                    print("⚠️ Could not switch back to Pending")
            else:
                print(f"📋 Found {len(declined_cards)} declined requests")
        except Exception as e:
            print(f"⚠️ Could not click Declined → {e}")

        try:
            self.driver.find_element(*self.filtericon).click()
            print("🔁 Clicked Filter icon again")
            time.sleep(1)
        except Exception as e:
            print(f"⚠️ Could not click Filter icon → {e}")

        try:
            self.driver.find_element(*self.All).click()
            print("✅ Clicked All filter")
            time.sleep(2)
        except Exception as e:
            print(f"⚠️ Could not click All → {e}")

        try:
            self.driver.find_element(*self.clickondated).click()
            print("📅 Clicked date field")
            time.sleep(2)

            try:
                date_1 = self.driver.find_element(AppiumBy.XPATH, '//android.view.View[@content-desc="1"]')
                date_1.click()
                print("📅 Selected date '1' from calendar")
                time.sleep(1)
            except Exception as e:
                print(f"⚠️ Could not select date '1' from calendar → {e}")
                try:
                    self.driver.find_element(*self.selectdata).click()
                    print("📅 Selected date using alternative locator")
                    time.sleep(1)
                except Exception as e2:
                    print(f"⚠️ Alternative date selection also failed → {e2}")

            try:
                self.driver.find_element(*self.clickokoncalender).click()
                print("✅ Clicked OK on calendar")
                time.sleep(2)
            except Exception as e:
                print(f"⚠️ Could not click OK on calendar → {e}")
        except Exception as e:
            print(f"⚠️ Failed to open date field: {e}")

        try:
            time.sleep(2)
            all_cards = self.driver.find_elements(AppiumBy.XPATH,
                                                  "//android.view.View[contains(@content-desc, 'Emp Id')]")

            if all_cards:
                print(f"📋 Found {len(all_cards)} records after date filter")

                for i, card in enumerate(all_cards[:3]):
                    try:
                        card_desc = card.get_attribute('content-desc')
                        print(f"📄 Card {i + 1}: {card_desc[:100]}..." if len(
                            card_desc) > 100 else f"📄 Card {i + 1}: {card_desc}")
                    except:
                        print(f"📄 Card {i + 1}: Could not read description")

                if len(all_cards) > 3:
                    print(f"📋 ... and {len(all_cards) - 3} more records")
            else:
                print("📋 No data visible after applying date filter")
        except Exception as e:
            print(f"⚠️ Error checking for visible data: {e}")

        try:
            result = self.driver.find_element(*self.checkonstatusandDatefield)
            print(f"✅ Specific filter result found: {result.get_attribute('content-desc')}")
        except:
            print("❌ Specific filter result not found.")

        print("🏁 Filter verification completed")
