class BasePageLocators():
    LOGIN_LINK = ("css selector", "#login_link")
    LOGIN_LINK_INVALID = ("css selector", "#login_link_inc")


class MainPageLocators():
    MAIN_PAGE_LINK = "http://selenium1py.pythonanywhere.com/en-gb/"
    LOGIN_LINK = ("css selector", "a[id='login_link']")


class LoginPageLocators():
    LOGIN_PAGE_LINK = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    SUBSTRING_LOGIN = "login"
    LOGIN_FORM = ("css selector", "div[class='col-sm-6 login_form']")
    REGISTER_FORM = ("css selector", "div[class='col-sm-6 register_form']")
    EMAIL_ADDR_INPUT = ("css selector", "label[for='id_registration-email']")
    PASSWORD1_INPUT = ("css selector", "label[for='id_registration-password2']")
    PASSWORD2_INPUT = ("css selector", "label[for='id_registration-password2']")
    REGISTER_BUTTON = ("css selector", "button[name='registration_submit']")
