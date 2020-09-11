from selenium.webdriver.common.by import By
from pageobjects.base_class import BaseClass


class LoginPage(BaseClass):

    textbox_email = (By.ID, "Email")
    textbox_password = (By.ID, "Password")
    button_login = (By.XPATH, "//input[@class='button-1 login-button']")
    button_logout = (By.LINK_TEXT, "Logout")

    def __init__(self, driver):
        super().__init__(driver)

    def set_username(self, username):
        self.clear_text_field(self.textbox_email)
        self.do_send_keys(self.textbox_email, username)

    def set_password(self, pwd):
        self.clear_text_field(self.textbox_password)
        self.do_send_keys(self.textbox_password, pwd)

    def click_login(self):
        self.do_click(self.button_login)

    def click_logout(self):
        self.do_click(self.button_logout)

    def get_login_page_title(self):
        return self.get_title()