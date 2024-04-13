from src.urls import Urls
from pages.login_page import LoginPage
from locators.main_locators import MainLocators


class TestLogin:
    url = Urls()
    main_locators = MainLocators()

    def test_login(self, browser):

        page = LoginPage(browser, self.url.base_url)
        page.open()
        page.login()
        actual_text = page.get_text(self.main_locators.START_MESSAGE)
        expected_text = "Рады видеть вас снова"
        assert actual_text == expected_text, \
            f"Unexpected text, expected text: {expected_text}, actual text: {actual_text}"
