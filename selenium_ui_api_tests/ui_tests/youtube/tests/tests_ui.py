from selenium_ui_api_tests.ui_tests.youtube.pages.youtube import Shorts
from selenium_ui_api_tests.ui_tests.conftest import browser


def test(browser):
    page = Shorts(browser)
    page.open()
    page.click_on_the_shorts_btn()
    active = page.check_shorts_btn_is_enabled()
    is_visible = page.first_short_is_visible()
    assert active is True
    assert is_visible is True

