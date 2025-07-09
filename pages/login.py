import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

        # Define locators
        self.mobile_input = (AppiumBy.XPATH, '//android.widget.EditText[1]')
        self.password_input = (AppiumBy.XPATH, '//android.widget.EditText[2]')
        self.login_button = (AppiumBy.XPATH, '//android.widget.Button[@content-desc="LogIn"]')



    def wait_for_login_screen(self):
        self.wait.until(EC.presence_of_element_located(self.mobile_input))

    def enter_mobile(self, mobile):
        # Re-locate the element just before interaction to avoid stale reference
        self.wait.until(EC.presence_of_element_located(self.mobile_input))
        mobile_element = self.driver.find_element(*self.mobile_input)
        mobile_element.click()
        mobile_element.send_keys(mobile)

    def enter_password(self, password):
        self.wait.until(EC.presence_of_element_located(self.password_input))
        password_element = self.driver.find_element(*self.password_input)
        password_element.click()
        password_element.send_keys(password)
        self.driver.press_keycode(66)  # ENTER / Done

    def tap_login(self):
        self.driver.find_element(*self.login_button).click()
        time.sleep(5)







