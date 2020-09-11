import pytest
from utilities.read_config import ConfigParser
from pageobjects.login_page import LoginPage
from utilities.logger import Logger


class Test001Login:

    logger = Logger.get_logger()

    @pytest.mark.skip()
    def test_home_page_title(self, setup):
        self.logger.info("**************" + Test001Login.__name__ + "*************")
        self.logger.info("************** Verify Home Page title *************")
        self.login_page = LoginPage(setup)
        title = self.login_page.get_login_page_title()
        if title == 'Your store. Login':
            self.logger.info("************** Verify Home Page title test passed*************")
            assert True
        else:
            self.login_page.take_screenshot("test_login")
            self.logger.error("************** Verify Home Page title test failed*************")
            assert False

    def test_login(self, setup):
        self.logger.info("**************" + Test001Login.__name__ + "*************")
        self.logger.info("************** Verify Login test *************")
        self.login_page = LoginPage(setup)
        self.login_page.set_username(ConfigParser.get_username())
        self.login_page.set_password(ConfigParser.get_password())
        self.login_page.click_login()
        title = self.login_page.get_login_page_title()
        if title == 'Dashboard / nopCommerce administration':
            self.logger.info("************** Verify Login test passed*************")
            assert True
        else:
            self.login_page.take_screenshot("test_login")
            self.logger.error("************** Verify Login test failed*************")
            assert False
