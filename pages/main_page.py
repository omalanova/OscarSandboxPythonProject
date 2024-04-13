from locators.login_locators import LoginLocators
from locators.main_locators import MainLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    main_locators = MainLocators()
    login_locators = LoginLocators()

    def logout(self):
        self.click_to_element(self.main_locators.LOGOUT)