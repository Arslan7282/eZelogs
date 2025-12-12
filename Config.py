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

    # -------------------------
    # TC-LI-002 Logout
    # -------------------------
    def test_logout(driver):
        menu = find(driver, (AppiumBy.XPATH, "//android.widget.Button[@content-desc='menu']"))
        menu.click()

        logout_btn = find(driver, (AppiumBy.XPATH, "//android.widget.TextView[@text='Logout']"))
        logout_btn.click()

        login_page = find(driver, (AppiumBy.XPATH, "//android.widget.Button[@content-desc='login']"))
        assert login_page.is_displayed()

    # -------------------------
    # TC-LI-003 Invalid email
    # -------------------------


def test_invalid_email(driver):
    email = find(driver, (AppiumBy.XPATH, "//android.widget.EditText[@content-desc='email']"))
    pwd = find(driver, (AppiumBy.XPATH, "//android.widget.EditText[@content-desc='password']"))
    login_btn = find(driver, (AppiumBy.XPATH, "//android.widget.Button[@content-desc='login']"))

    email.send_keys("nexone1122@gmail.com")
    pwd.send_keys("Nnexone@1122")
    login_btn.click()

    error = find(driver, (AppiumBy.XPATH, "//android.widget.TextView[contains(@text,'Invalid email')]"))
    assert error.is_displayed()

    # -------------------------
    # TC-LI-004 Invalid password
    # -------------------------


def test_invalid_password(driver):
    email = find(driver, (AppiumBy.XPATH, "//android.widget.EditText[@content-desc='email']"))
    pwd = find(driver, (AppiumBy.XPATH, "//android.widget.EditText[@content-desc='password']"))
    login_btn = find(driver, (AppiumBy.XPATH, "//android.widget.Button[@content-desc='login']"))

    email.send_keys("nexone1122@gmail.com")
    pwd.send_keys("Nnexone")
    login_btn.click()

    error = find(driver,(AppiumBy.XPATH, "//android.widget.TextView[contains(@text,'Incorrect password')]"))
    assert error.is_displayed()

    # -------------------------
    # TC-LI-005 Empty email
    # -------------------------
def test_empty_email(driver):
    pwd = find(driver, (AppiumBy.XPATH, "//android.widget.EditText[@content-desc='password']"))
    login_btn = find(driver, (AppiumBy.XPATH, "//android.widget.Button[@content-desc='login']"))

    pwd.send_keys("Nnexone@1122")
    login_btn.click()

    validation = find(driver,(AppiumBy.XPATH, "//android.widget.TextView[contains(@text,'enter email')]"))
    assert validation.is_displayed()

    # -------------------------
    # TC-LI-006 Empty password
    # -------------------------
def test_empty_password(driver):
    email = find(driver, (AppiumBy.XPATH, "//android.widget.EditText[@content-desc='email']"))
    login_btn = find(driver, (AppiumBy.XPATH, "//android.widget.Button[@content-desc='login']"))

    email.send_keys("nexone1122@gmail.com")
    login_btn.click()

    validation = find(driver,(AppiumBy.XPATH, "//android.widget.TextView[contains(@text,'enter password')]"))
    assert validation.is_displayed()

    # -------------------------
    # TC-LI-007 Both fields empty
    # -------------------------
def test_both_empty(driver):
    login_btn = find(driver, (AppiumBy.XPATH, "//android.widget.Button[@content-desc='login']"))
    login_btn.click()

    validation = find(driver, (AppiumBy.XPATH, "//android.widget.TextView"))
    assert validation.is_displayed()


# -------------------------
    # TC-LI-008 Password visibility toggle
    # -------------------------
    def test_password_visibility(driver):
        pwd = find(driver, (AppiumBy.XPATH, "//android.widget.EditText[@content-desc='password']"))
        eye_icon = find(driver, (AppiumBy.XPATH, "//android.widget.Button[@content-desc='toggle-password']"))

        pwd.send_keys("test1234")
        eye_icon.click()

        assert pwd.get_attribute("password") == "false"

    # -------------------------
    # TC-LI-009 Forgot Password navigation
    # -------------------------
    def test_forgot_password(driver):
        forgot_btn = find(driver, (AppiumBy.XPATH, "//android.widget.TextView[@text='Forgot Password?']"))
        forgot_btn.click()

        recovery = find(driver, (AppiumBy.XPATH, "//android.widget.TextView[contains(@text,'Recovery')]"))
        assert recovery.is_displayed()

    # -------------------------
    # TC-LI-010 Google login
    # -------------------------
    def test_google_login(driver):
        google_btn = find(driver, (AppiumBy.XPATH, "//android.widget.Button[@text='Continue with Google']"))
        google_btn.click()

        google_popup = find(driver, (AppiumBy.XPATH, "//android.widget.TextView[contains(@text,'Google')]"))
        assert google_popup.is_displayed()

    # -------------------------
    # TC-LI-012 Login button disabled
    # -------------------------


def test_login_disabled(driver):
    login_btn = find(driver, (AppiumBy.XPATH, "//android.widget.Button[@content-desc='login']"))
    assert login_btn.is_enabled() is False

    # -------------------------
    # TC-LI-013 Email format validation
    # -------------------------


def test_email_format(driver):
    email = find(driver, (AppiumBy.XPATH, "//android.widget.EditText[@content-desc='email']"))
    pwd = find(driver, (AppiumBy.XPATH, "//android.widget.EditText[@content-desc='password']"))
    login_btn = find(driver, (AppiumBy.XPATH, "//android.widget.Button[@content-desc='login']"))

    email.send_keys("Nnexone1122@")
    pwd.send_keys("Nnexone@1122")
    login_btn.click()

    validation = find(driver, (AppiumBy.XPATH, "//android.widget.TextView[contains(@text,'format')]"))
    assert validation.is_displayed()

    # -------------------------
    # TC-LI-014 Sign Up navigation
    # -------------------------


def test_sign_up_navigation(driver):
    signup_tab = find(driver, (AppiumBy.XPATH, "//android.widget.TextView[@text='Sign Up']"))
    signup_tab.click()

    signup_screen = find(driver, (AppiumBy.XPATH, "//android.widget.TextView[contains(@text,'Sign Up')]"))
    assert signup_screen.is_displayed()

    # -------------------------
    # Open Settings Popup (Required for all)
    # -------------------------
def test_open_settings(driver):
    settings_icon = find(driver, (AppiumBy.XPATH, "//android.widget.Button[@content-desc='settings']"))
    settings_icon.click()
    return find(driver, (AppiumBy.XPATH, "//android.widget.TextView[@text='Settings']"))


    # -------------------------
    # TC_SET_01 Verify Settings popup is displayed
    # -------------------------
def test_settings_popup_display(driver):
    popup = open_settings(driver)
    assert popup.is_displayed()


    # -------------------------
    # TC_SET_02 Verify Select All
    # -------------------------
def test_select_all(driver):
    open_settings(driver)
    select_all = find(driver, (AppiumBy.XPATH, "//android.widget.CheckBox[@content-desc='select_all']"))
    select_all.click()
    assert select_all.get_attribute("checked") == "true"


    # -------------------------
    # TC_SET_03 Verify Counter checkbox
    # -------------------------
def test_counter_toggle(driver):
    open_settings(driver)
    counter = find(driver, (AppiumBy.XPATH, "//android.widget.CheckBox[@content-desc='counter']"))
    counter.click()
    assert counter.get_attribute("checked") == "true"


    # -------------------------
    # TC_SET_04 Verify Quick Links toggle
    # -------------------------
def test_quick_links_toggle(driver):
    open_settings(driver)
    qlinks = find(driver, (AppiumBy.XPATH, "//android.widget.CheckBox[@content-desc='quick_links']"))
    qlinks.click()
    assert qlinks.get_attribute("checked") == "true"


    # -------------------------
    # TC_SET_05 Verify Vendor checkbox
    # -------------------------
def test_vendor_checkbox(driver):
    open_settings(driver)
    vendor = find(driver, (AppiumBy.XPATH, "//android.widget.CheckBox[@content-desc='vendor']"))
    vendor.click()
    assert vendor.get_attribute("checked") == "true"


    # -------------------------
    # TC_SET_06 Verify Gallery checkbox
    # -------------------------
def test_gallery_checkbox(driver):
    open_settings(driver)
    gallery = find(driver, (AppiumBy.XPATH, "//android.widget.CheckBox[@content-desc='gallery']"))
    gallery.click()
    assert gallery.get_attribute("checked") == "true"


    # -------------------------
    # TC_SET_07 Verify Employees checkbox
    # -------------------------
def test_employees_checkbox(driver):
    open_settings(driver)
    employees = find(driver, (AppiumBy.XPATH, "//android.widget.CheckBox[@content-desc='employees']"))
    employees.click()
    assert employees.get_attribute("checked") == "true"


    # -------------------------
    # TC_SET_08 Verify Customers checkbox
    # -------------------------
def test_customers_checkbox(driver):
    open_settings(driver)
    customers = find(driver, (AppiumBy.XPATH, "//android.widget.CheckBox[@content-desc='customers']"))
    customers.click()
    assert customers.get_attribute("checked") == "true"


    # -------------------------
    # TC_SET_09 Verify Recent Activities checkbox
    # -------------------------
def test_recent_activities_checkbox(driver):
    open_settings(driver)
    recent_act = find(driver,(AppiumBy.XPATH, "//android.widget.CheckBox[@content-desc='recent_activities']"))
    recent_act.click()
    assert recent_act.get_attribute("checked") == "true"


    # -------------------------
    # TC_SET_10 Verify Recent Projects checkbox
    # -------------------------
def test_recent_projects_checkbox(driver):
    open_settings(driver)
    recent_proj = find(driver,(AppiumBy.XPATH, "//android.widget.CheckBox[@content-desc='recent_projects']"))
    recent_proj.click()
    assert recent_proj.get_attribute("checked") == "true"


    # -------------------------
    # TC_SET_11 Verify Cancel button
    # -------------------------
def test_cancel_button(driver):
    open_settings(driver)
    cancel_btn = find(driver, (AppiumBy.XPATH, "//android.widget.Button[@text='Cancel']"))
    cancel_btn.click()

    dashboard = find(driver, (AppiumBy.XPATH, "//android.widget.TextView[@text='Dashboard']"))
    assert dashboard.is_displayed()


    # -------------------------
    # TC_SET_12 Verify Save button
    # -------------------------
def test_save_button(driver):
    open_settings(driver)

    options = [
        "//android.widget.CheckBox[@content-desc='counter']",
        "//android.widget.CheckBox[@content-desc='quick_links']",
        "//android.widget.CheckBox[@content-desc='vendor']"
    ]

    for opt in options:
        item = find(driver, (AppiumBy.XPATH, opt))
        item.click()

    save_btn = find(driver, (AppiumBy.XPATH, "//android.widget.Button[@text='Save']"))
    save_btn.click()

    dashboard = find(driver, (AppiumBy.XPATH, "//android.widget.TextView[@text='Dashboard']"))
    assert dashboard.is_displayed()


    # -------------------------
    # TC_MENU_02 My Account navigation
    # -------------------------
def test_my_account(driver):
    open_menu(driver)
    btn = find(driver, (AppiumBy.XPATH, "//android.widget.TextView[@text='My Account']"))
    btn.click()
    screen = find(driver, (AppiumBy.XPATH, "//android.widget.TextView[contains(@text,'Account')]"))
    assert screen.is_displayed()


    # -------------------------
    # TC_MENU_03 Invited Companies
    # -------------------------
def test_invited_companies(driver):
    open_menu(driver)
    btn = find(driver, (AppiumBy.XPATH, "//android.widget.TextView[@text='Invited Companies']"))
    btn.click()
    screen = find(driver, (AppiumBy.XPATH, "//android.widget.TextView[contains(@text,'Invited')]"))
    assert screen.is_displayed()


    # -------------------------
    # TC_MENU_04 Projects
    # -------------------------
def test_projects(driver):
    open_menu(driver)
    btn = find(driver, (AppiumBy.XPATH, "//android.widget.TextView[@text='Projects']"))
    btn.click()
    screen = find(driver, (AppiumBy.XPATH, "//android.widget.TextView[contains(@text,'Project')]"))
    assert screen.is_displayed()


    # -------------------------
    # TC_MENU_05 Resources Table
    # -------------------------
def test_resources_table(driver):
    open_menu(driver)
    btn = find(driver, (AppiumBy.XPATH, "//android.widget.TextView[@text='Resources Table']"))
    btn.click()
    screen = find(driver, (AppiumBy.XPATH, "//android.widget.TextView[contains(@text,'Resources')]"))
    assert screen.is_displayed()


    # -------------------------
    # TC_MENU_06 Vendor
    # -------------------------
def test_vendor(driver):
    open_menu(driver)
    btn = find(driver, (AppiumBy.XPATH, "//android.widget.TextView[@text='Vendor']"))
    btn.click()
    screen = find(driver, (AppiumBy.XPATH, "//android.widget.TextView[contains(@text,'Vendor')]"))
    assert screen.is_displayed()


    # -------------------------
    # TC_MENU_07 Company Users
    # -------------------------
def test_company_users(driver):
    open_menu(driver)
    btn = find(driver, (AppiumBy.XPATH, "//android.widget.TextView[@text='Company Users']"))
    btn.click()
    screen = find(driver, (AppiumBy.XPATH, "//android.widget.TextView[contains(@text,'Users')]"))
    assert screen.is_displayed()


    # -------------------------
    # TC_MENU_08 Company Employees
    # -------------------------
def test_company_employees(driver):
    open_menu(driver)
    btn = find(driver, (AppiumBy.XPATH, "//android.widget.TextView[@text='Company Employees']"))
    btn.click()
    screen = find(driver, (AppiumBy.XPATH, "//android.widget.TextView[contains(@text,'Employee')]"))
    assert screen.is_displayed()


    # -------------------------
    # TC_MENU_09 Roles & Permissions
    # -------------------------
def test_roles_permissions(driver):
    open_menu(driver)
    btn = find(driver, (AppiumBy.XPATH, "//android.widget.TextView[@text='Roles & Permissions']"))
    btn.click()
    screen = find(driver, (AppiumBy.XPATH, "//android.widget.TextView[contains(@text,'Roles')]"))
    assert screen.is_displayed()


    # -------------------------
    # TC_MENU_10 Customers
    # -------------------------
def test_customers(driver):
    open_menu(driver)
    btn = find(driver, (AppiumBy.XPATH, "//android.widget.TextView[@text='Customers']"))
    btn.click()
    screen = find(driver, (AppiumBy.XPATH, "//android.widget.TextView[contains(@text,'Customers')]"))
    assert screen.is_displayed()


    # -------------------------
    # TC_MENU_11 Company Chat
    # -------------------------
def test_company_chat(driver):
    open_menu(driver)
    btn = find(driver, (AppiumBy.XPATH, "//android.widget.TextView[@text='Company Chat']"))
    btn.click()
    screen = find(driver, (AppiumBy.XPATH, "//android.widget.TextView[contains(@text,'Chat')]"))
    assert screen.is_displayed()


    # -------------------------
    # TC_MENU_12 Company Mail
    # -------------------------
def test_company_mail(driver):
    open_menu(driver)
    btn = find(driver, (AppiumBy.XPATH, "//android.widget.TextView[@text='Company Mail']"))
    btn.click()
    screen = find(driver, (AppiumBy.XPATH, "//android.widget.TextView[contains(@text,'Mail')]"))
    assert screen.is_displayed()


    # -------------------------
    # TC_MENU_13 Terms & Conditions
    # -------------------------
def test_terms_conditions(driver):
    open_menu(driver)
    btn = find(driver, (AppiumBy.XPATH, "//android.widget.TextView[@text='Term & Conditions']"))
    btn.click()
    screen = find(driver, (AppiumBy.XPATH, "//android.widget.TextView[contains(@text,'Terms')]"))
    assert screen.is_displayed()


    # -------------------------
    # TC_MENU_14 Settings
    # -------------------------
def test_settings(driver):
    open_menu(driver)
    btn = find(driver, (AppiumBy.XPATH, "//android.widget.TextView[@text='Settings']"))
    btn.click()
    screen = find(driver, (AppiumBy.XPATH, "//android.widget.TextView[contains(@text,'Settings')]"))
    assert screen.is_displayed()

    # -------------------------
    # TC_MENU_15 Logout
    # -------------------------


def test_logout(driver):
    open_menu(driver)
    btn = find(driver, (AppiumBy.XPATH, "//android.widget.TextView[@text='Logout']"))
    btn.click()

    login_screen = find(driver, (AppiumBy.XPATH, "//android.widget.Button[@content-desc='login']"))
    assert login_screen.is_displayed()

    # -------------------------
    # METHOD: Open Resources Table Page
    # -------------------------
def open_resources_table(driver):
    menu_btn = find(driver, (AppiumBy.XPATH, "//android.widget.Button[@content-desc='menu']"))
    menu_btn.click()

    resources_btn = find(driver, (AppiumBy.XPATH, "//android.widget.TextView[@text='Resources Table']"))
    resources_btn.click()

    return find(driver, (AppiumBy.XPATH, "//android.widget.TextView[@text='Resources']"))


    # -------------------------
    # TC_RT_01 Verify Resources Table page loads
    # -------------------------
def test_resources_page_load(driver):
    page = open_resources_table(driver)
    assert page.is_displayed()


    # -------------------------
    # TC_RT_02 Verify Trades option visible
    # -------------------------
def test_trades_option_visible(driver):
    open_resources_table(driver)
    trades = find(driver, (AppiumBy.XPATH, "//android.widget.TextView[@text='Trades']"))
    assert trades.is_displayed()


    # -------------------------
    # TC_RT_03 Verify navigation to Trades page
    # -------------------------
def test_trades_navigation(driver):
    open_resources_table(driver)
    trades = find(driver, (AppiumBy.XPATH, "//android.widget.TextView[@text='Trades']"))
    trades.click()

    trades_page = find(driver, (AppiumBy.XPATH, "//android.widget.TextView[contains(@text,'Trade')]"))
    assert trades_page.is_displayed()


    # -------------------------
    # TC_RT_04 Verify Trade / Worker Titles option visible
    # -------------------------
def test_trade_worker_titles_visible(driver):
    open_resources_table(driver)
    twt = find(driver, (AppiumBy.XPATH, "//android.widget.TextView[@text='Trade / Worker Titles']"))
    assert twt.is_displayed()


    # -------------------------
    # TC_RT_05 Verify navigation to Trade / Worker Titles page
    # -------------------------
def test_trade_worker_titles_navigation(driver):
    open_resources_table(driver)
    twt = find(driver, (AppiumBy.XPATH, "//android.widget.TextView[@text='Trade / Worker Titles']"))
    twt.click()

    twt_page = find(driver, (AppiumBy.XPATH, "//android.widget.TextView[contains(@text,'Worker')]"))
    assert twt_page.is_displayed()


    # -------------------------
    # TC_RT_06 Verify Cost Codes option visible
    # -------------------------
def test_cost_codes_option_visible(driver):
    open_resources_table(driver)
    cost_codes = find(driver, (AppiumBy.XPATH, "//android.widget.TextView[@text='Cost Codes']"))
    assert cost_codes.is_displayed()


    # -------------------------
    # TC_RT_07 Verify Materials option visible
    # -------------------------
def test_materials_option_visible(driver):
    open_resources_table(driver)
    materials = find(driver, (AppiumBy.XPATH, "//android.widget.TextView[@text='Materials']"))
    assert materials.is_displayed()


    # -------------------------
    # TC_RT_08 Verify Equipments option visible
    # -------------------------
def test_equipments_option_visible(driver):
    open_resources_table(driver)
    equipments = find(driver, (AppiumBy.XPATH, "//android.widget.TextView[@text='Equipments']"))
    assert equipments.is_displayed()


    # -------------------------
    # TC_RT_09 Verify Back button navigation
    # -------------------------
def test_back_button_navigation(driver):
    open_resources_table(driver)

    back_btn = find(driver, (AppiumBy.XPATH, "//android.widget.Button[@content-desc='back']"))
    back_btn.click()

    dashboard = find(driver, (AppiumBy.XPATH, "//android.widget.TextView[@text='Dashboard']"))
    assert dashboard.is_displayed()


    # -------------------------
    # TC_VEN_01 Verify Create Vendor page loads
    # -------------------------
def test_vendor_page_loads(driver):
    page = find(driver, (AppiumBy.XPATH, "//android.widget.TextView[@text='Create Vendor']"))
    assert page.is_displayed()


    # -------------------------
    # TC_VEN_02 Verify Basic Fields tab is default
    # -------------------------
def test_basic_fields_tab_default(driver):
    tab = find(driver, (AppiumBy.XPATH, "//android.widget.TextView[@text='Basic Fields']"))
    assert tab.get_attribute("selected") == "true"


    # -------------------------
    # TC_VEN_03 Verify More Details tab switch
    # -------------------------
def test_more_details_tab_switch(driver):
    tab = find(driver, (AppiumBy.XPATH, "//android.widget.TextView[@text='More Details']"))
    tab.click()
    assert tab.get_attribute("selected") == "true"


    # -------------------------
    # TC_VEN_04 Verify Type of Vendor dropdown
    # -------------------------
def test_type_of_vendor_dropdown(driver):
    dropdown = find(driver, (AppiumBy.XPATH, "//android.widget.Spinner[@content-desc='type_of_vendor']"))
    dropdown.click()
    option = find(driver, (AppiumBy.XPATH, "//android.widget.CheckedTextView[@text='Contractor']"))
    assert option.is_displayed()


    # -------------------------
    # TC_VEN_05 First Name field
    # -------------------------
def test_first_name_field(driver):
    first_name = find(driver, (AppiumBy.XPATH, "//android.widget.EditText[@content-desc='first_name']"))
    first_name.send_keys("Ali")
    assert first_name.text == "Ali"


    # -------------------------
    # TC_VEN_06 Last Name field
    # -------------------------
def test_last_name_field(driver):
    last_name = find(driver, (AppiumBy.XPATH, "//android.widget.EditText[@content-desc='last_name']"))
    last_name.send_keys("Khan")
    assert last_name.text == "Khan"


    # -------------------------
    # TC_VEN_07 Title field
    # -------------------------
def test_title_field(driver):
    title = find(driver, (AppiumBy.XPATH, "//android.widget.EditText[@content-desc='title']"))
    title.send_keys("Site Manager")
    assert title.text == "Site Manager"


    # -------------------------
    # TC_VEN_08 Trade / Specialty
    # -------------------------
def test_trade_field( driver):
    trade = find(driver, (AppiumBy.XPATH, "//android.widget.EditText[@content-desc='trade']"))
    trade.send_keys("Electrical")
    assert trade.text == "Electrical"


    # -------------------------
    # TC_VEN_09 Company Name field
    # -------------------------
def test_company_name_field(driver):
    company = find(driver, (AppiumBy.XPATH, "//android.widget.EditText[@content-desc='company_name']"))
    company.send_keys("ABC Constructions")
    assert company.text == "ABC Constructions"


    # -------------------------
    # TC_VEN_10 Email field validation
    # -------------------------
def test_email_field(driver):
    email = find(driver, (AppiumBy.XPATH, "//android.widget.EditText[@content-desc='email']"))
    email.send_keys("test@abc.com")
    assert email.text == "test@abc.com"


    # -------------------------
    # TC_VEN_11 File upload
    # -------------------------
def test_file_upload(driver):
    upload_btn = find(driver, (AppiumBy.XPATH, "//android.widget.Button[@text='Choose File']"))
    upload_btn.click()
    # Note: File picker interaction may vary by device/emulator; assume file selected
    file_attached = find(driver,
                                       (AppiumBy.XPATH, "//android.widget.TextView[contains(@text,'vendor_doc.jpg')]"))
    assert file_attached.is_displayed()


    # -------------------------
    # TC_VEN_12 Save Basic Fields
    # -------------------------
def test_save_basic_fields(driver):
    save_btn = find(driver, (AppiumBy.XPATH, "//android.widget.Button[@text='Save Basic Fields']"))
    save_btn.click()
    success_msg = find(driver, (AppiumBy.XPATH,"//android.widget.TextView[contains(@text,'Vendor saved successfully')]"))
    assert success_msg.is_displayed()


    # -------------------------
    # TC_VEN_13 Mandatory field validation
    # -------------------------
def test_mandatory_field_validation(driver):
    # Clear required fields
    first_name = find(driver, (AppiumBy.XPATH, "//android.widget.EditText[@content-desc='first_name']"))
    first_name.clear()
    save_btn = find(driver, (AppiumBy.XPATH, "//android.widget.Button[@text='Save Basic Fields']"))
    save_btn.click()
    validation = find(driver, (AppiumBy.XPATH, "//android.widget.TextView[contains(@text,'required')]"))
    assert validation.is_displayed()













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


# ---------------------------
# TC-SET-001 – Verify Settings Popup Displayed
# ---------------------------
def test_001_verify_settings_btn(driver):
    try:
        setting_btn = find(driver, "//android.widget.TextView[@text='Settings']")
        setting_btn.click()
    except:
        assert False, "Settings popup not found"


# ---------------------------
# TC-SET-001 – Verify Settings Popup Displayed
# ---------------------------
def test_001_verify_settings_popup(driver):
    try:
        popup = find(driver, "//android.widget.TextView[@text='Settings']")
        assert popup.is_displayed(), "Settings popup not displayed"
    except:
        assert False, "Settings popup not found"


# ---------------------------
# TC-SET-002 – Verify Select All Checkbox
# ---------------------------
def test_002_verify_select_all_checkbox(driver):
    try:
        select_all = find(driver, "//android.widget.TextView[contains(@text,'Select All')]")
        select_all.click()
    except:
        assert False, "Select All checkbox not working"


# ---------------------------
# TC-SET-003 – Verify Counter Toggle
# ---------------------------
def test_003_verify_counter_toggle(driver):
    try:
        counter = find(driver, "//android.widget.TextView[@text='Counter']")
        counter.click()
    except:
        assert False, "Counter toggle not clickable"


# ---------------------------
# TC-SET-004 – Verify Quick Links Toggle
# ---------------------------
def test_004_verify_quick_links_toggle(driver):
    try:
        quick_links = find(driver, "//android.widget.TextView[@text='Quick Links']")
        quick_links.click()
    except:
        assert False, "Quick Links toggle not clickable"


# ---------------------------
# TC-SET-005 – Verify Vendor Checkbox
# ---------------------------
def test_005_verify_vendor_checkbox(driver):
    try:
        vendor = find(driver, "//android.widget.TextView[@text='Vendor']")
        vendor.click()
    except:
        assert False, "Vendor checkbox not clickable"


# ---------------------------
# TC-SET-006 – Verify Gallery Checkbox
# ---------------------------
def test_006_verify_gallery_checkbox(driver):
    try:
        gallery = find(driver, "//android.widget.TextView[@text='Gallery']")
        gallery.click()
    except:
        assert False, "Gallery checkbox not clickable"


# ---------------------------
# TC-SET-007 – Verify Employees Checkbox
# ---------------------------
def test_007_verify_employees_checkbox(driver):
    try:
        employees = find(driver, "//android.widget.TextView[@text='Employees']")
        employees.click()
    except:
        assert False, "Employees checkbox not clickable"


# ---------------------------
# TC-SET-008 – Verify Customers Checkbox
# ---------------------------
def test_008_verify_customers_checkbox(driver):
    try:
        customers = find(driver, "//android.widget.TextView[@text='Customers']")
        customers.click()
    except:
        assert False, "Customers checkbox not clickable"


# ---------------------------
# TC-SET-009 – Verify Recent Activities Checkbox
# ---------------------------
def test_009_verify_recent_activities_checkbox(driver):
    try:
        activities = find(driver, "//android.widget.TextView[@text='Recent Activities']")
        activities.click()
    except:
        assert False, "Recent Activities checkbox not clickable"


# ---------------------------
# TC-SET-010 – Verify Recent Projects Checkbox
# ---------------------------
def test_010_verify_recent_projects_checkbox(driver):
    try:
        projects = find(driver, "//android.widget.TextView[@text='Recent Projects']")
        projects.click()
    except:
        assert False, "Recent Projects checkbox not clickable"


# ---------------------------
# TC-SET-011 – Verify Cancel Button
# ---------------------------
def test_011_verify_cancel_button(driver):
    try:
        cancel = find(driver, "//android.widget.TextView[@text='Cancel']")
        cancel.click()
    except:
        assert False, "Cancel button not working"


# ---------------------------
# TC-SET-012 – Verify Save Button
# ---------------------------
def test_012_verify_save_button(driver):
    try:
        # Re-open settings if cancel closed it (optional)
        settings = find(driver, "//android.widget.TextView[@text='Settings']")
        settings.click()

        save = find(driver, "//android.widget.TextView[@text='Save']")
        save.click()
    except:
        assert False, "Save button not working"
