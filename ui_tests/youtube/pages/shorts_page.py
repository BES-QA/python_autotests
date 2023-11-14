from ui_tests.youtube.locators import main_page
from ui_tests.youtube.locators import shorts_page
from ui_tests.youtube.pages.main_page import MainPage


class ShortsPage(MainPage):
    def check_shorts_btn_is_enabled(self):
        return self._find_element(main_page.LOCATOR_MAIN_PAGE_SHORTS_BUTTON).is_enabled()


    def first_short_is_visible(self):
        return self._find_element(shorts_page.LOCATOR_SHORTS_PAGE_FIRST_SHORT).is_displayed()
