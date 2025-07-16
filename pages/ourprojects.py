from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class listprojects:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

        self.searchbar = (AppiumBy.XPATH, '//android.widget.EditText')
        self.first_result = (AppiumBy.XPATH, '//android.view.View[contains(@content-desc, "smiligence")]')
        self.save_button = (AppiumBy.ACCESSIBILITY_ID, "Save")
        self.fetch_location_button = (AppiumBy.XPATH, '//android.widget.Button[@content-desc="Fetch Location"]')
        self.allow_popup_button = (AppiumBy.XPATH,
                                   '//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_allow_foreground_only_button"]')
        self.location_display = (AppiumBy.XPATH,
                                 '//android.view.View[@content-desc="Google Building 43, Mountain View, California, United States, 94043"]')
        self.save_button_after_fetched = (AppiumBy.XPATH, '//android.widget.Button[@content-desc="Save"]')
        self.toast_message = (
            AppiumBy.XPATH,
            ".//android.widget.Toast[contains(@text, 'Updated Location Address')]"
        )

        self.clickonwidgetabtn = (AppiumBy.XPATH,'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.Button')
        self.clickoninactive=(AppiumBy.XPATH,'//android.widget.Button[@content-desc="Inactive"]')
        self.clickonactive =(AppiumBy.XPATH,'//android.widget.Button[@content-desc="Active"]')
        self.clickonAll = (AppiumBy.XPATH,'//android.widget.Button[@content-desc="All"]')

    def wait_for_projects_page(self):
        self.wait.until(EC.presence_of_element_located(self.searchbar))

    def search(self, value):
        search_element = self.wait.until(EC.element_to_be_clickable(self.searchbar))
        search_element.click()
        search_element.clear()
        search_element.send_keys(value)

    def click_first_result(self):
        first = self.wait.until(EC.element_to_be_clickable(self.first_result))
        first.click()

    def click_save_button(self):
        try:
            fetch = self.wait.until(EC.element_to_be_clickable(self.save_button))
            fetch.click()
            print("✅ Clicked Save button")
        except Exception as e:
            print(f"❌ Could not click Save: {e}")

    def click_fetch_location(self):
        fetch = self.wait.until(EC.element_to_be_clickable(self.fetch_location_button))
        fetch.click()

    def allow_location_popup(self):
        allow = self.wait.until(EC.element_to_be_clickable(self.allow_popup_button))
        allow.click()

    def click_save_after_fetched(self):
        savebtn = self.wait.until(EC.element_to_be_clickable(self.save_button_after_fetched))
        savebtn.click()

    def wait_for_save_button(self):
        self.wait.until(EC.element_to_be_clickable(self.save_button))  # Make sure this locator is defined

    def is_location_displayed(self):
        try:
            self.wait.until(EC.presence_of_element_located(self.location_display))
            return True
        except:
            return False

    def is_project_saved(self):
        try:
            toast = self.wait.until(EC.presence_of_element_located(self.toast_message))
            print("✅ Toast found:", toast.text)
            return True
        except:
            print("❌ Toast not found: Project may not be saved.")
            return False

    def wait_for_location_and_click_save(self):
        try:
            # ✅ Wait until the location text is visible (replace with actual accessibility ID if needed)
            self.wait.until(
                EC.presence_of_element_located(
                    (AppiumBy.ACCESSIBILITY_ID, "Google Building 43, Mountain View, California, United States, 94043")
                )
            )
            print("📍 Location fetched and visible.")

            # ✅ Now wait and click the Save button
            save_button = self.wait.until(
                EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Save"))
            )
            save_button.click()
            print("✅ Save button clicked after location fetched.")

        except Exception as e:
            print(f"❌ Error waiting for location or clicking Save: {e}")

    from appium.webdriver.common.appiumby import AppiumBy
    from selenium.common.exceptions import TimeoutException, NoSuchElementException

    from appium.webdriver.common.appiumby import AppiumBy
    from selenium.common.exceptions import TimeoutException

    def clickoninactiveactive(self):
        print("Started: Inactive and Active flow")

        # Click on Widget tab
        widget = self.wait.until(EC.element_to_be_clickable(self.clickonwidgetabtn))
        widget.click()
        print("Clicked on Widget tab")

        # Click on Active
        active = self.wait.until(EC.element_to_be_clickable(self.clickonactive))
        active.click()
        print("Clicked on Active")

        # Click on Widget tab again
        widget = self.wait.until(EC.element_to_be_clickable(self.clickonwidgetabtn))
        widget.click()
        print("Clicked on Widget tab again after Active")

        # Try finding Inactive by XPath, fallback to Accessibility ID
        try:
            inactive = self.wait.until(EC.element_to_be_clickable(
                (AppiumBy.XPATH, '//android.widget.Button[@content-desc="Inactive"]')
            ))
            print("Found Inactive using XPath")
        except TimeoutException:
            print("Inactive not found by XPath, trying Accessibility ID")
            try:
                inactive = self.wait.until(EC.element_to_be_clickable(
                    (AppiumBy.ACCESSIBILITY_ID, 'Inactive')
                ))
                print("Found Inactive using Accessibility ID")
            except TimeoutException:
                print("Inactive not found using XPath or Accessibility ID")
                return

        # Click on Inactive
        inactive.click()
        print("Clicked on Inactive")

        # Click on Widget tab again
        widget = self.wait.until(EC.element_to_be_clickable(self.clickonwidgetabtn))
        widget.click()
        print("Clicked on Widget tab again after Inactive")
        ALL = self.wait.until(EC.element_to_be_clickable(self.clickonAll))
        ALL.click()
        print("All the widjet clicked")



