import time

import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture
def setup(browser):
    if browser=='chrome':
        print("Launching Chrome")
        driver = webdriver.Chrome()

    elif browser=='firefox':
        print("Launching Firefox")
        driver = webdriver.Firefox()

    elif browser=='edge':
        print("Launching Edge")
        driver = webdriver.Edge()
    else:
        print("Launching Headless")
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    time.sleep(1)
    driver.get("https://www.worldometers.info/coronavirus/")
    yield driver
    driver.quit()
    return driver
