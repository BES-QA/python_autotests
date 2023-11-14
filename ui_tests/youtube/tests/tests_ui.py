from ui_tests.youtube.pages.shorts_page import ShortsPage
from ui_tests.conftest import browser


def test(browser):
    page = ShortsPage(browser)
    page.open()
    page.click_on_the_shorts_btn()
    active = page.check_shorts_btn_is_enabled()
    is_visible = page.first_short_is_visible()
    assert active is True
    assert is_visible is True

