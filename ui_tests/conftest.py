import pytest
from selenium import webdriver


@pytest.fixture(scope='session')
def browser():
    capabilities = {
        # 'browserName': 'chrome',
        # 'browserVersion': '119.0',
        'selenoid:options': {
            'enableVNC': True,
            'enableVideo': True
        }
    }
    options = webdriver.ChromeOptions()
    options.capabilities.update(capabilities)

    driver = webdriver.Remote(command_executor='http://192.168.0.105:4444/wd/hub', options=options)
    driver.maximize_window()
    driver.implicitly_wait(15)

    yield driver
    driver.quit()






