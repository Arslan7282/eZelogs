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
el = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Get Started']")))
el.click()


# driver.quit()