import configparser

config = configparser.RawConfigParser()
config.read("C://Old D drive//SeleniumWorkSpace//nop_commerce_pytest_framework//configurations//config.ini")


class ConfigParser:
    @staticmethod
    def get_application_url():
        return config.get('login info', 'base_url')

    @staticmethod
    def get_username():
        return config.get('login info', 'username')

    @staticmethod
    def get_password():
        return config.get('login info', 'password')


