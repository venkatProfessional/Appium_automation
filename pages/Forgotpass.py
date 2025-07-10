from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class forgotpasswordclass:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.login_screen_field = (AppiumBy.XPATH, '//android.widget.EditText[1]')
        self.forgot_password_button = (AppiumBy.XPATH, '//android.widget.Button[@content-desc="Forgot Password?"]')
        self.email_input = (AppiumBy.XPATH, '//android.widget.EditText')
        self.reset_button = (AppiumBy.XPATH, '//android.widget.Button[@content-desc="RESET PASSWORD"]')
        self.back_to_login_button = (AppiumBy.XPATH, '//android.widget.Button[@content-desc="Back to Login"]')

    def is_on_login_screen(self):
        try:
            self.wait.until(EC.presence_of_element_located(self.login_screen_field))
            print("✅ Login screen is visible.")
            return True
        except:
            print("❌ Login screen is NOT visible.")
            return False

    def click_forgot_password(self):
        if self.is_on_login_screen():
            print("🔐 Clicking on 'Forgot Password?' button...")
            self.wait.until(EC.element_to_be_clickable(self.forgot_password_button)).click()
            self.wait_for_forgot_password_screen()

            # Click the email field right after navigation
            email_field = self.wait.until(EC.presence_of_element_located(self.email_input))
            email_field.click()
            print("🖱️ Clicked into email input field.")
        else:
            raise Exception("❌ Cannot click 'Forgot Password?' — not on login screen.")

    def wait_for_forgot_password_screen(self):
        print("⏳ Waiting for Forgot Password screen...")
        self.wait.until(EC.presence_of_element_located(self.email_input))
        self.wait.until(EC.presence_of_element_located(self.reset_button))
        print("✅ Forgot Password screen loaded.")

    def enter_email_and_submit(self, email):
        print(f"✍️ Typing email: '{email}'")
        email_field = self.wait.until(EC.presence_of_element_located(self.email_input))
        email_field.clear()
        email_field.send_keys(email)

        print("🔘 Clicking 'RESET PASSWORD' button...")
        self.wait.until(EC.element_to_be_clickable(self.reset_button)).click()
        time.sleep(1)

        # Re-enter email after submission
        try:
            print("🔁 Re-entering email after reset...")
            email_field = self.wait.until(EC.presence_of_element_located(self.email_input))
            email_field.clear()
            email_field.send_keys(email)
        except Exception as e:
            print(f"⚠️ Unable to re-enter email: {e}")

    def test_negative_emails(self):
        print("\n🚫 Running negative test cases...")
        invalid_emails = ["", "abc", "abc@", "abc.com", "abc@.com", "user@com", "@example.com"]

        for email in invalid_emails:
            try:
                self.enter_email_and_submit(email)
                print(f"❌ Invalid email accepted: '{email}'")
            except Exception as e:
                print(f"✅ show a validation to the user '{email}' — {str(e)}")

    def test_positive_email(self):
        print("\n✅ Running positive test case...")
        try:
            self.enter_email_and_submit("user@example.com")  # Use a valid test email
            print("✅ Valid email submitted successfully.")
        except Exception as e:
            print(f"❌ Valid email failed — {str(e)}")

    def return_to_login_screen(self):
        print("🔙 Clicking 'Back to Login' button...")
        try:
            self.wait.until(EC.element_to_be_clickable(self.back_to_login_button)).click()
            self.wait.until(EC.presence_of_element_located(self.login_screen_field))
            print("✅ Returned to login screen.")
        except Exception as e:
            print(f"❌ Failed to return to login screen: {e}")

    def run_forgot_password_flow(self):
        self.click_forgot_password()
        self.test_negative_emails()
        self.test_positive_email()
        self.return_to_login_screen()
