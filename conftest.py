import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def chrome_options():
    options = Options()
    """For opening browser in full-screen"""
    options.add_argument("start-maximized")
    """For opening browser in particular size"""
    # options.add_argument('--window-size=100,100')
    """Runs without GUI (better performance)"""
    # options.add_argument('--headless=chrome')

    return options


@pytest.fixture(scope="function")
def driver(chrome_options):
    """ This fixture sets up a Chrome WebDriver instance before each test that uses it,
    and it ensures that the WebDriver is properly cleaned up after the test finishes."""
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()
