from ui_tests.youtube.locators.main_page import LOCATOR_MAIN_PAGE_SHORTS_BUTTON
from ui_tests.youtube.pages.base_page import BasePage


class MainPage(BasePage):
    def click_on_the_shorts_btn(self):
        self._click(LOCATOR_MAIN_PAGE_SHORTS_BUTTON)
