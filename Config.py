from appium.webdriver.common.appiumby import AppiumBy
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException

cap: Dict[str, Any] = {
    'platformName': 'Android',
    "platformVersion": "12",
    "deviceName": "JFQO7PFEU44XBIIJ",
    "automationName": "UiAutomator2",
    #if we want to open an specific app then we have no need to add these lines
#dumpsys window windows | grep -E 'mTopActivityComponent' this command is used to find out the package name
    # "appPackage": "com.bbk.launcher2",
    # "appActivity": "com.eZelogs.app.MainActivity",
    "appium:noReset": True,
    "appium:fullReset": False,
    "newCommandTimeout": 300,
    "autoGrantPermissions": True,
}

url = 'http://127.0.0.1:4723'

driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
# implicitly wait until the app is completely load then it perfom other actions we use it because the time.sleep(5) comman some times work as axpected and some times it not work as expected
driver.implicitly_wait(15)

driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='ezelogs, 0 notifications').click()

wait = WebDriverWait(driver, 30)
get_started_ele = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Get Started']")))
get_started_ele.click()

signup_btn_ele = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Sign Up']")))
signup_btn_ele.click()

first_name_ele = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.EditText[@text='Your First Name']")))
first_name_ele.send_keys("Abdullah")

last_name_ele = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.EditText[@text='Your Last Name']")))
last_name_ele.send_keys("Ahmad")

email_ele = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.EditText[@text='Your Email Address']")))
email_ele.send_keys("abdullah123@yopmail.com")

phone_ele = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.EditText[@text='your phone number']")))
phone_ele.send_keys("03028427278")

check_box_ele = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='']")))
check_box_ele.click()

company_name_ele = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.EditText[@text='Your Company Name']")))
compoany_name_ele.send_keys("Preesoft")

work_title_ele = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.EditText[@text='Your Work Title']")))
work_title_ele.send_keys("CEO")

password_ele = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.EditText[@text='Your Password']")))
password_ele.send_keys("123456789")

confirm_password_ele = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.EditText[@text='Confirm Password']")))
confirm_password_ele.send_keys("123456789")

register_btn_ele = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.EditText[@text='Register']")))
register_btn_ele.click()

# driver.quit()