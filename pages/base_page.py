from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

from locators.login_locators import LoginLocators
from src.user_data import UserData
class BasePage:
    timeout = 10
    locators = LoginLocators()
    user = UserData()

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def login(self):
        self.element_is_visible(self.locators.USER_NAME).send_keys(self.user.user)
        self.element_is_visible(self.locators.PASSWORD).send_keys(self.user.password)
        self.element_is_clickable(self.locators.LOGIN).click()

    def open(self):
        self.browser.get(self.url)

    def get_text(self, locator):
        return self.element_is_visible(locator).text

    def element_is_visible(self, locator, timeout=timeout):
        return wait(self.browser, timeout).until(EC.visibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=timeout):
        return wait(self.browser, timeout).until(EC.element_to_be_clickable(locator))