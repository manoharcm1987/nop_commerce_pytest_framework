
from utilities.read_config import ConfigParser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseClass:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(ConfigParser.get_application_url())

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located)
        return bool(element)

    def get_title(self):
        return self.driver.title

    def clear_text_field(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).clear()

    def take_screenshot(self, file_method_name):
        self.driver.save_screenshot("C://Old D drive//SeleniumWorkSpace//nop_commerce_pytest_framework//screenshots//"+file_method_name+".png")
