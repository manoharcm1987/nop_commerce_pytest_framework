import pytest
from selenium.webdriver import Chrome
from pageobjects.login_page import LoginPage
from utilities.logger import Logger as log
class Test001Login:
    base_url = "https://admin-demo.nopcommerce.com/"
    username= "admin@yourstore.com"
    password = "admin"

    logger = log.get_logger()

    def test_home_page_title(self, setup):
        self.logger.info("**************" +Test001Login.__name__ + "*************")
        self.logger.info("************** Verify Home Page title *************")
        self.driver = setup
        self.driver.get(self.base_url)
        title = self.driver.title
        if title == 'Your store. Login':
            self.logger.info("************** Verify Home Page title test passed*************")
            assert True
        else:
            self.driver.save_screenshot(".//screenshots//"+self.test_home_page_title.__name__+".png")
            self.logger.error("************** Verify Home Page title test failed*************")
            assert False

    def test_login(self, setup):
        self.logger.info("**************" +Test001Login.__name__ + "*************")
        self.logger.info("************** Verify Login test *************")
        self.driver = setup
        self.driver.get(self.base_url)
        login_page = LoginPage(self.driver)
        login_page.set_username(self.username)
        login_page.set_password(self.password)
        login_page.click_login()
        title = self.driver.title
        #assert True if titles == "Dashboard / nopCommerce administration" else False
        if title == 'Dashboard / nopCommerce administration':
            self.logger.info("************** Verify Login test passed*************")
            assert True
        else:
            self.driver.save_screenshot(".//screenshots//"+self.test_login.__name__+".png")
            self.logger.info("************** Verify Login test failed*************")
            assert False