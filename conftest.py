import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def browser():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--window-size=1440,1080")
    # service = Service(executable_path=ChromeDriverManager().install())
    browser = webdriver.Chrome(options=chrome_options)
    yield browser
    browser.quit()
