from selenium.webdriver.common.by import By

from selenium_ui_api_tests.ui_tests.youtube.pages.base_page import BasePage


class MainPageLocators:
    LOCATOR_MAIN_PAGE_SHORTS_BUTTON = (By.XPATH, '(//a[contains(@title, "Shorts")])[1]')


class ShortsLocators:
    LOCATOR_SHORTS_PAGE_FIRST_SHORT = (By.XPATH, '//*[@id="shorts-inner-container"]/*[@id="0"]')


class Shorts(BasePage):

    def click_on_the_shorts_btn(self):
        self._click(MainPageLocators.LOCATOR_MAIN_PAGE_SHORTS_BUTTON)

    def check_shorts_btn_is_enabled(self):
        return self._find_element(MainPageLocators.LOCATOR_MAIN_PAGE_SHORTS_BUTTON).is_enabled()

    def first_short_is_visible(self):
        return self._find_element(ShortsLocators.LOCATOR_SHORTS_PAGE_FIRST_SHORT).is_displayed()