from selenium.webdriver import Chrome, Firefox
from selenium.webdriver.chrome.options import Options
import pytest, sys
import os,pathlib


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        path = os.path.join(pathlib.Path(__file__).parent.absolute(), "drivers", "chromedriver.exe")
        # Initialize WebDriver
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument("--test-type")
        chrome_options.add_experimental_option("useAutomationExtension", False);
        chrome_options.add_experimental_option('prefs', {'credentials_enable_service': False, 'profile':
                                                {'password_manager_enabled': False}})
        # chrome_options.add_argument("--disable-dev-shm-usage")
        # chrome_options.add_argument("--disable-gpu")
        chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);
        driver = Chrome(options=chrome_options, executable_path=path)
    elif browser == 'firefox':
        driver = Firefox()
    else:
        sys.exit(0)
    # Wait implicitly for elements to be ready before attempting interactions
    driver.implicitly_wait(10)
    driver.maximize_window()
    # Return the driver object at the end of setup
    yield driver
    # For cleanup, quit the driver
    driver.quit()


def pytest_addoption(parser): #get value from CLI/hook
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser") #return browser value to setup

# This hook  Add environment info to the HTML report
def pytest_configure(config):
    config._metadata['Project Name'] = 'NOP Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'ManU'

#T his hook delete/modifies env info from HTML report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop('Plugins', None)