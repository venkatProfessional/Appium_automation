from appium import webdriver
from appium.options.android import UiAutomator2Options


def create_driver():
    options = UiAutomator2Options().load_capabilities({
        "platformName": "Android",
        "deviceName": "emulator-5554",  # Use `adb devices` to confirm this
        "automationName": "UiAutomator2",
        "app": r"C:\Users\JothiVenkatajalapath\Downloads\Hr Portal test 08.07.2025.apk",  # Absolute path to your APK
        "noReset": False
    })

    driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)
    driver.implicitly_wait(10)
    return driver
