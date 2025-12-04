import pytest
from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="session")
def driver():
    cap = {
        'platformName': 'Android',
        "platformVersion": "12",
        "deviceName": "JFQO7PFEU44XBIIJ",
        "automationName": "UiAutomator2",
        "appium:noReset": True,
        "appium:fullReset": False,
        "newCommandTimeout": 300,
        "autoGrantPermissions": True,
    }

    url = "http://127.0.0.1:4723"

    driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
    driver.implicitly_wait(15)

    yield driver

    driver.quit()


# ---------------------------
# Test 001
# ---------------------------
def test_001_open_app(driver):
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "ezelogs, 0 notifications").click()


# ---------------------------
# Test 002
# ---------------------------
def test_002_get_started(driver):
    wait = WebDriverWait(driver, 30)
    get_started = wait.until(
        EC.presence_of_element_located(
            (AppiumBy.XPATH, "//android.widget.TextView[@text='Get Started']")
        )
    )
    get_started.click()


# ---------------------------
# Test 003
# ---------------------------
def test_003_open_signup_page(driver):
    wait = WebDriverWait(driver, 30)
    signup_btn = wait.until(
        EC.presence_of_element_located(
            (AppiumBy.XPATH, "//android.widget.TextView[@text='Sign Up']")
        )
    )
    signup_btn.click()


# ---------------------------
# Test 004
# ---------------------------
def test_004_fill_form(driver):
    wait = WebDriverWait(driver, 30)

    wait.until(EC.presence_of_element_located(
        (AppiumBy.XPATH, "//android.widget.EditText[@text='Your First Name']")
    )).send_keys("Abdullah")

    wait.until(EC.presence_of_element_located(
        (AppiumBy.XPATH, "//android.widget.EditText[@text='Your Last Name']")
    )).send_keys("Ahmad")

    wait.until(EC.presence_of_element_located(
        (AppiumBy.XPATH, "//android.widget.EditText[@text='Your Email Address']")
    )).send_keys("abdullah123@yopmail.com")

    wait.until(EC.presence_of_element_located(
        (AppiumBy.XPATH, "//android.widget.EditText[@text='your phone number']")
    )).send_keys("03028427278")

    wait.until(EC.presence_of_element_located(
        (AppiumBy.XPATH, "//android.widget.EditText[@text='Your Company Name']")
    )).send_keys("Preesoft")

    wait.until(EC.presence_of_element_located(
        (AppiumBy.XPATH, "//android.widget.EditText[@text='Your Work Title']")
    )).send_keys("CEO")

    wait.until(EC.presence_of_element_located(
        (AppiumBy.XPATH, "//android.widget.EditText[@text='Your Password']")
    )).send_keys("123456789")

    wait.until(EC.presence_of_element_located(
        (AppiumBy.XPATH, "//android.widget.EditText[@text='Confirm Password']")
    )).send_keys("123456789")


# ---------------------------
# Test 005
# ---------------------------
def test_005_submit_form(driver):
    wait = WebDriverWait(driver, 30)
    register_btn = wait.until(
        EC.presence_of_element_located(
            (AppiumBy.XPATH, "//android.widget.TextView[@text='Register']")
        )
    )
    register_btn.click()
