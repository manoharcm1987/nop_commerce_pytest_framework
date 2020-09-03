from selenium.webdriver.common.by import By


class LoginPage:

    textbox_email = (By.ID, "Email")
    textbox_password = (By.ID, "Password")
    button_login = (By.XPATH, "//input[@class='button-1 login-button']")
    button_logout = (By.LINK_TEXT, "Logout")

    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username):
        email = self.driver.find_element(*self.textbox_email)
        email.clear()
        email.send_keys(username)

    def set_password(self, pwd):
        password = self.driver.find_element(*self.textbox_password)
        password.clear()
        password.send_keys(pwd)

    def click_login(self):
        self.driver.find_element(*self.button_login).click()

    def click_logout(self):
        self.driver.find_element(*self.button_logout).click()