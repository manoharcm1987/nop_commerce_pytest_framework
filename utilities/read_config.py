import configparser

config = configparser.RawConfigParser()
path = os.path.join(pathlib.Path(__file__).parent.parent.absolute(), "configurations", "config.ini")
#config.read("C://Old D drive//SeleniumWorkSpace//nop_commerce_pytest_framework//configurations//config.ini")
config.read(path)


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

    @staticmethod
    def get_test_data_file_path():
        path = pathlib.Path(__file__).parent.parent.absolute()
        return os.path.join(path, config.get('testdata', 'login_data_file_path'))

