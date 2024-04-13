from pages.main_page import MainPage
from src.main_data import MainData
from src.urls import Urls



class TestMainPage:
    url = Urls()
    main_data = MainData()

    def test_logout(self, browser):
        page = MainPage()
        page.open()
        page.login()
        page.logout()
        assert browser.current_url == self.url.base_url

