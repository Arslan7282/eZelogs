import time
from appium.webdriver.common.appiumby import AppiumBy

class AuthHelpers:

    @staticmethod
    def get_error_messages(driver, timeout=5):
        """Find visible error messages and return them as a list."""
        time.sleep(timeout)

        # Common selectors for error text
        selectors = [
            (AppiumBy.XPATH, "//*[contains(@text,'error')]"),
            (AppiumBy.XPATH, "//android.widget.TextView"),
        ]

        found_messages = []

        for by, value in selectors:
            try:
                elements = driver.find_elements(by, value)
                for el in elements:
                    text = el.text.strip()
                    if text and len(text) < 150:  # filter layout junk
                        if any(word in text.lower() for word in ["error", "invalid", "required"]):
                            found_messages.append(text)
            except:
                pass

        return found_messages

    @staticmethod
    def assert_error_message(driver):
        """Print errors + fail test if no error is found."""
        errors = AuthHelpers.get_error_messages(driver)

        print("\n--- ERROR MESSAGES FOUND ---")
        if errors:
            for e in errors:
                print(f"❌ {e}")
            print("------------------------------\n")
            return errors

        print("❌ No error message shown!")
        raise AssertionError("No error message was displayed!")
