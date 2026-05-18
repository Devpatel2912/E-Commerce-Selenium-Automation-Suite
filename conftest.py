import pytest
import os
from datetime import datetime
from utils.driver_factory import DriverFactory
from utils.screenshot import ScreenshotUtil

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests on")

@pytest.fixture(scope="function")
def setup(request):
    browser_name = request.config.getoption("browser")
    driver = DriverFactory.get_driver(browser_name)
    request.cls.driver = driver
    yield driver
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        try:
            if hasattr(item.cls, 'driver'):
                ScreenshotUtil.take_screenshot(item.cls.driver, item.name)
        except Exception as e:
            print(f"Failed to take screenshot: {e}")
