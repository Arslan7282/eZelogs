import time
from appium.webdriver.common.appiumby import AppiumBy

class AuthHelpers:

    @staticmethod
    def check_error_message(driver, expected_texts, timeout=5):

        for text in expected_texts:
            error_selectors = [
                (AppiumBy.XPATH, f"//*[contains(@text, '{text}')]"),
                (AppiumBy.XPATH,
                 f"//*[contains(translate(@text, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '{text.lower()}')]"),
            ]

            # if ElementHelpers.element_exists(driver, error_selectors, timeout=timeout):
            #     return True

        return False

