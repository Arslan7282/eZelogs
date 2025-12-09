import pytest
from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Auth_Helpers import AuthHelpers


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


def find(driver, xpath, timeout=20):
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((AppiumBy.XPATH, xpath))
    )


# ---------------------------
# Test 001 – Open App
# ---------------------------
def test_000_open_app(driver):
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "ezelogs, 0 notifications").click()


# ---------------------------
# TC-SU-001 – Get Started Opens Next Screen
# ---------------------------
def test_001_get_started(driver):
    try:
        btn = find(driver, "//android.widget.TextView[@text='Get Started']")
        btn.click()
    except:
        assert False, "Get Started button not found"


# ---------------------------
# TC-SU-002 – Open Sign Up Page
# ---------------------------
def test_002_open_signup_page(driver):
    try:
        btn = find(driver, "//android.widget.TextView[@text='Sign Up']")
        btn.click()
    except:
        assert False, "Sign Up button not found"


# ---------------------------
# TC-SU-003 – Fill Invalid Data
# ---------------------------
def test_003_fill_invalid_data(driver):
    try:
        find(driver, "//android.widget.EditText[@text='Your Email Address']").send_keys("nexone1122@")
        find(driver, "//android.widget.EditText[@text='your phone number']").send_keys("03366@")
        find(driver, "//android.widget.EditText[@text='Your Password']").send_keys("Nnexone@1122")
        find(driver, "//android.widget.EditText[@text='Confirm Password']").send_keys("Nnexone1122")
        btn = find(driver, "//android.widget.TextView[@text='Register']")
        btn.click()
        errors = AuthHelpers.assert_error_message(driver)

        assert errors, "No validation errors displayed for invalid input"
    except:
        return False, "Failed to fill invalid data"


# ---------------------------
# TC-SU-004 – Submit Form & Print Errors
# ---------------------------
def test_004_submit_registration_errors(driver):
    try:
        # Click the Register button
        btn = find(driver, "//android.widget.TextView[@text='Register']")
        btn.click()

        # Capture error messages
        errors = driver.find_elements(
            AppiumBy.XPATH,
            "//android.widget.TextView[contains(@text,'invalid') or contains(@text,'required') or contains(@text,'mismatch')]"
        )

        if errors:
            print("\n=== Error Messages ===")
            for e in errors:
                print(e.text)
            print("====================\n")
        else:
            print("No error messages found.")

    except Exception as e:
        return False, f"Exception while submitting form: {str(e)}"


# ---------------------------
# TC-SU-010 – Show/Hide Password
# ---------------------------
def test_005_show_hide_password(driver):
    try:
        eye = find(driver, "(//android.widget.TextView[@text=''])[1]")
        eye.click()
    except:
        assert False, "Password toggle not found"


# ---------------------------
# TC-SU-011 – WhatsApp Checkbox
# ---------------------------
def test_006_whatsapp_checkbox(driver):
    try:
        cb = find(driver, "//android.widget.TextView[@text='']")
        cb.click()
    except:
        assert False, "WhatsApp checkbox not found"


# ---------------------------
# TC-SU-012 – Country Code Selection
# ---------------------------
def test_007_country_code(driver):
    try:
        code = find(driver, "//android.widget.TextView[@text='+92']")
        code.click()
    except:
        assert False, "Country code +92 not found"


# ---------------------------
# TC-SU-014 – Password Min Length
# ---------------------------
def test_008_password_min_length(driver):
    try:
        pwd = find(driver, "//android.widget.EditText[@text='Your Password']")
        pwd.send_keys("123")
    except:
        assert False, "Password field not found"


# ---------------------------
# TC-SU-015 – Google Sign Up
# ---------------------------
def test_009_google_signup(driver):
    try:
        btn = find(driver, "//android.widget.TextView[@text='Continue with Google']")
        btn.click()
    except:
        assert False, "Google sign up button not found"


# ---------------------------
# TC-SU-003b – Fill Valid Data (Optional)
# ---------------------------
def test_010_fill_valid_data(driver):
    try:
        find(driver, "//android.widget.EditText[@text='Your First Name']").send_keys("Abdullah")
        find(driver, "//android.widget.EditText[@text='Your Last Name']").send_keys("Ahmad")
        find(driver, "//android.widget.EditText[@text='Your Email Address']").send_keys("abdullah123@yopmail.com")
        find(driver, "//android.widget.EditText[@text='your phone number']").send_keys("03028427278")
        find(driver, "//android.widget.EditText[@text='Your Company Name']").send_keys("Preesoft")
        find(driver, "//android.widget.EditText[@text='Your Work Title']").send_keys("CEO")
        find(driver, "//android.widget.EditText[@text='Your Password']").send_keys("Test@1234")
        find(driver, "//android.widget.EditText[@text='Confirm Password']").send_keys("Test@1234")
    except:
        return False, "Failed to fill valid data"


def test_011_submit_registration(driver):
    # Click the Register button
    btn = find(driver, "//android.widget.TextView[@text='Register']")
    btn.click()

# # ---------------------------
# # Test 001
# # ---------------------------
# def test_001_open_app(driver):
#     driver.find_element(AppiumBy.ACCESSIBILITY_ID, "ezelogs, 0 notifications").click()
#
#
# # ---------------------------
# # Test 002
# # ---------------------------
# def test_002_get_started(driver):
#     wait = WebDriverWait(driver, 30)
#     get_started = wait.until(
#         EC.presence_of_element_located(
#             (AppiumBy.XPATH, "//android.widget.TextView[@text='Get Started']")
#         )
#     )
#     get_started.click()
#
#
# # ---------------------------
# # Test 003
# # ---------------------------
# def test_003_open_signup_page(driver):
#     wait = WebDriverWait(driver, 30)
#     signup_btn = wait.until(
#         EC.presence_of_element_located(
#             (AppiumBy.XPATH, "//android.widget.TextView[@text='Sign Up']")
#         )
#     )
#     signup_btn.click()
#
#
# # ---------------------------
# # Test 004
# # ---------------------------
# def test_004_fill_form(driver):
#     wait = WebDriverWait(driver, 30)
#
#     wait.until(EC.presence_of_element_located(
#         (AppiumBy.XPATH, "//android.widget.EditText[@text='Your First Name']")
#     )).send_keys("Abdullah")
#
#     wait.until(EC.presence_of_element_located(
#         (AppiumBy.XPATH, "//android.widget.EditText[@text='Your Last Name']")
#     )).send_keys("Ahmad")
#
#     wait.until(EC.presence_of_element_located(
#         (AppiumBy.XPATH, "//android.widget.EditText[@text='Your Email Address']")
#     )).send_keys("abdullah123@yopmail.com")
#
#     wait.until(EC.presence_of_element_located(
#         (AppiumBy.XPATH, "//android.widget.EditText[@text='your phone number']")
#     )).send_keys("03028427278")
#
#     wait.until(EC.presence_of_element_located(
#         (AppiumBy.XPATH, "//android.widget.EditText[@text='Your Company Name']")
#     )).send_keys("Preesoft")
#
#     wait.until(EC.presence_of_element_located(
#         (AppiumBy.XPATH, "//android.widget.EditText[@text='Your Work Title']")
#     )).send_keys("CEO")
#
#     wait.until(EC.presence_of_element_located(
#         (AppiumBy.XPATH, "//android.widget.EditText[@text='Your Password']")
#     )).send_keys("Test@1234")
#
#     wait.until(EC.presence_of_element_located(
#         (AppiumBy.XPATH, "//android.widget.EditText[@text='Confirm Password']")
#     )).send_keys("Test@1234")
#
#
# # ---------------------------
# # Test 005
# # ---------------------------
# def test_005_submit_form(driver):
#     wait = WebDriverWait(driver, 30)
#     register_btn = wait.until(
#         EC.presence_of_element_located(
#             (AppiumBy.XPATH, "//android.widget.TextView[@text='Register']")
#         )
#     )
#     register_btn.click()
