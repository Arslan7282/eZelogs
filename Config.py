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
def test_001_open_app(driver):
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "ezelogs, 0 notifications").click()


# ---------------------------
# TC-SU-001 – Get Started Opens Next Screen
# ---------------------------
def test_002_get_started(driver):
    try:
        btn = find(driver, "//android.widget.TextView[@text='Get Started']")
        btn.click()
    except:
        assert False, "Get Started button not found"


# ---------------------------
# TC-SU-003 – Fill Invalid Data
# ---------------------------
def test_003_fill_valid_data(driver):
    try:
        find(driver, "//android.widget.EditText[@text='Your Email Address']").send_keys("ezelogtest112233@yopmail.com")
        find(driver, "//android.widget.EditText[@text='Your Password']").send_keys("Ezelogtest123@")
        # btn = find(driver, "//android.widget.TextView[@text='Register']")
        # btn.click()
        # errors = AuthHelpers.assert_error_message(driver)

        assert errors, "No validation errors displayed for invalid input"
    except:
        return False, "Failed to fill invalid data"


def test_004_submit_registration(driver):
    # Click the Register button
    btn = find(driver, "(//android.widget.TextView[@text='Login'])[2]")
    btn.click()


# ---------------------------
# TC-DASH-001 – Verify Company Dashboard Loads
# ---------------------------
def test_005_verify_dashboard_loads(driver):
    try:
        dashboard = find(driver, "//android.widget.TextView[@text='Suffa Tech IT Solution Company']")
        assert dashboard.is_displayed(), "Dashboard not loaded"
    except:
        assert False, "Company Dashboard failed to load"

# ---------------------------
# TC-DASH-005 – Navigate to Projects Page
# ---------------------------
def test_006_navigate_to_projects(driver):
    try:
        projects = find(driver, "//android.widget.TextView[@text='Projects']")
        projects.click()
    except:
        assert False, "Projects navigation failed"


# ---------------------------
# TC-DASH-002 – Verify All Projects Count Visible
# ---------------------------
def test_007_verify_all_projects_count(driver):
    try:
        count = find(driver, "//android.widget.TextView[contains(@text,'All Projects')]")
        assert count.is_displayed(), "All Projects count not visible"
    except:
        assert False, "All Projects count not found"


# ---------------------------
# TC-DASH-003 – Verify Pending Projects Count
# ---------------------------
def test_007_verify_pending_projects_count(driver):
    try:
        pending = find(driver, "//android.widget.TextView[contains(@text,'Pending')]")
        assert pending.is_displayed(), "Pending Projects not visible"
    except:
        assert False, "Pending Projects count not found"


# ---------------------------
# TC-DASH-004 – Verify Quick Links Visibility
# ---------------------------
def test_008_verify_quick_links(driver):
    try:
        quick_links = find(driver, "//android.widget.TextView[@text='Quick Links']")
        assert quick_links.is_displayed(), "Quick Links not visible"
    except:
        assert False, "Quick Links section missing"


# ---------------------------
# TC-PROJ-006 – Verify Projects Screen Loads
# ---------------------------
def test_010_verify_projects_screen(driver):
    try:
        header = find(driver, "//android.widget.TextView[@text='Projects']")
        assert header.is_displayed(), "Projects screen not loaded"
    except:
        assert False, "Projects screen failed to load"


# ---------------------------
# TC-PROJ-007 – Verify Search Field
# ---------------------------
def test_011_verify_search_field(driver):
    try:
        search = find(driver, "//android.widget.EditText[contains(@text,'Search...')]")
        search.click()
        search.send_keys("Vhgh")
    except:
        assert False, "Search field not working"


# ---------------------------
# TC-PROJ-008 – Verify Project List Visibility
# ---------------------------
def test_012_verify_project_list(driver):
    try:
        project_list = driver.find_elements(
            AppiumBy.XPATH,
            "//android.widget.TextView[contains(@resource-id,'project')]"
        )
        assert len(project_list) > 0, "Project list is empty"
    except:
        assert False, "Project list not visible"


# ---------------------------
# TC-PROJ-009 – Verify Show More Button
# ---------------------------
def test_013_verify_show_more_button(driver):
    try:
        show_more = find(driver, "//android.widget.TextView[@text='Show More']")
        show_more.click()
    except:
        assert False, "Show More button not working"


# ---------------------------
# TC-PROJ-010 – Verify Add Project (+) Button
# ---------------------------
def test_014_verify_add_project_button(driver):
    try:
        add_btn = find(driver, "//android.widget.TextView[@text='']")
        add_btn.click()
    except:
        assert False, "Add Project (+) button not found"


# ---------------------------
# TC-PROJ-011 – Verify Create Project Page Loads
# ---------------------------
def test_015_verify_create_project_page(driver):
    try:
        title = find(driver, "//android.widget.TextView[@text='Create Project']")
        assert title.is_displayed(), "Create Project page not loaded"
    except:
        assert False, "Create Project page failed to load"


# ---------------------------
# TC-PROJ-012 – Verify Mandatory Field Validation
# ---------------------------
def test_016_verify_mandatory_fields(driver):
    try:
        save_btn = find(driver, "//android.widget.TextView[@text='Submit']")
        save_btn.click()

        errors = driver.find_elements(
            AppiumBy.XPATH,
            "//android.widget.TextView[contains(@text,'required')]"
        )

        assert len(errors) > 0, "No validation errors shown"
    except:
        assert False, "Mandatory validation failed"

# ---------------------------
# TC-PROJ-015 – Verify ZIP Code Input
# ---------------------------
def test_019_verify_zip_code_field(driver):
    try:
        zip_code = find(driver, "//android.widget.EditText[contains(@text,'Zip Code*')]")
        zip_code.click()
        zip_code.send_keys("54000")
    except:
        assert False, "ZIP code field not working"


# ---------------------------
# TC-PROJ-013 – Verify Country Dropdown
# ---------------------------
def test_017_verify_country_dropdown(driver):
    try:
        country = find(driver, "//android.widget.TextView[contains(@text,'Select Country')]")
        country.click()
    except:
        assert False, "Country dropdown not clickable"


# ---------------------------
# TC-PROJ-014 – Verify State Field after Country Selection
# ---------------------------
def test_018_verify_state_field(driver):
    try:
        state = find(driver, "//android.widget.EditText[contains(@text,'Select country first')]")
        state.click()
        state.send_keys("Punjab")
    except:
        assert False, "State field not working"


# ---------------------------
# TC-PROJ-016 – Submit Form with Valid Data
# ---------------------------
def test_020_submit_valid_project_form(driver):
    try:
        # Fill other required fields (adjust XPaths if needed)
        find(driver, "//android.widget.EditText[contains(@text,'Project Name')]").send_keys("Automation Project")
        find(driver, "//android.widget.EditText[contains(@text,'Address')]").send_keys("Lahore, Pakistan")

        submit = find(driver, "//android.widget.TextView[@text='Submit']")
        submit.click()
    except:
        assert False, "Project form submission failed"
