from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    URL = 'https://www.youtube.com/'

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def _find_element(self, locator, time=10) -> WebElement:
        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator),
                                                      message=f'Не удалось найти элемент {locator}')

    def _find_elements(self, locator, time=10) -> WebElement:
        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator),
                                                      message=f'Не удалось найти элементы {locator}')

    def _click(self, element):
        (ActionChains(self.driver)
         .move_to_element(self._find_element(element))
         .click()
         .perform())
