import time

import pytest
from utilities.read_config import ConfigParser
from pageobjects.login_page import LoginPage
from utilities.logger import Logger
from utilities import  excel_utility


class Test002LoginTestDDT:
    path = "./testdata/LoginData.xlsx"
    logger = Logger.get_logger()

    def test_login_ddt(self, setup):
        self.logger.info("**************" + Test002LoginTestDDT.__name__ + "*************")
        self.logger.info("************** Verify Home Page title *************")
        self.login_page = LoginPage(setup)

        row_count = excel_utility.get_row_count(self.path, "login_data_sheet")

        for row in range(2, row_count+1):
            user = excel_utility.read_cell_data(self.path, "login_data_sheet", row, 1)
            pwd= excel_utility.read_cell_data(self.path, "login_data_sheet", row, 2)
            expected = excel_utility.read_cell_data(self.path, "login_data_sheet", row, 3)
            self.logger.info(f"Username : {user}")
            self.logger.info(f"password : {pwd}")
            self.logger.info(f"expected : {expected}")
            status_list = list()
            self.login_page.set_username(user)
            self.login_page.set_password(pwd)
            self.login_page.click_login()
            time.sleep(5)
            title = self.login_page.get_login_page_title()
            exp_title = "Dashboard / nopCommerce administration"
            if title == exp_title:
                if expected == 'pass':
                    self.logger.info("*********passed***********")
                    self.login_page.click_logout()
                    status_list.append("pass")
                elif expected == 'fail':
                    self.logger.info("*******failed*********")
                    self.login_page.click_logout()
                    status_list.append("fail")
            elif title != exp_title:
                if expected == 'fail':
                    self.logger.info("*********passed***********")
                    status_list.append("pass")
                elif expected == 'pass':
                    self.logger.info("*********failed***********")
                    status_list.append("fail")
        if 'fail' not in status_list:
            self.logger.info("********* Login DDT is passed***********")
            assert True
        else:
            self.logger.info("********* Login DDT is failed***********")
            assert False


