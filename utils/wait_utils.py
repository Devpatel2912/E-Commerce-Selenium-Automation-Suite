from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.config import Config
from utils.logger import Logger

log = Logger.get_logger(__name__)

class WaitUtils:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, Config.EXPLICIT_WAIT)

    def wait_for_element_visible(self, locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(locator))
        except Exception as e:
            log.error(f"Element {locator} not visible after {Config.EXPLICIT_WAIT} seconds")
            raise e

    def wait_for_element_clickable(self, locator):
        try:
            return self.wait.until(EC.element_to_be_clickable(locator))
        except Exception as e:
            log.error(f"Element {locator} not clickable after {Config.EXPLICIT_WAIT} seconds")
            raise e
            
    def click_element(self, locator):
        element = self.wait_for_element_clickable(locator)
        element.click()
        
    def send_text(self, locator, text):
        element = self.wait_for_element_visible(locator)
        element.clear()
        element.send_keys(text)
        
    def get_text(self, locator):
        element = self.wait_for_element_visible(locator)
        return element.text
