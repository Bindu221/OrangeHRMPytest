# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
# class Basepage:
#     def __init__(self, driver):
#         self.driver = driver
#
#     def hrm_send_keys(self, locators, text):
#         WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(locators))
#
#     def hrm_btn_click(self, locators):
#         WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(locators)).click()
#
#     def hrm_get_title(self, title):
#         WebDriverWait(self.driver, 30).until(EC.title_is(title))
#         return self.driver.title
#
#     def hrm_click_link(self, locator):
#         WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(locator)).click()
#
####################################################
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException
#
# class BasePage:
#     def __init__(self, driver):
#         self.driver = driver
#
#     def find_element(self, by, locator, timeout=10):
#         """Find an element with an explicit wait."""
#         try:
#             element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((by, locator)))
#             return element
#         except TimeoutException:
#             raise Exception(f"Element with locator ({by}, {locator}) not found.")
#
#     def click_element(self, by, locator, timeout=10):
#         """Click an element."""
#         element = self.find_element(by, locator, timeout)
#         element.click()
#
#     def enter_text(self, by, locator, text, timeout=10):
#         """Enter text into an input field."""
#         element = self.find_element(by, locator, timeout)
#         element.clear()
#         element.send_keys(text)
###############################################
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Basepage:
    def __init__(self, driver):
        self.driver = driver

    def hrm_send_keys(self, locators, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locators)).send_keys(text)

    def hrm_btn_click(self, locators):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locators)).click()

    def hrm_get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    def hrm_click_link(self, locators):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locators)).click()
