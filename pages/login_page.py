from selenium.webdriver.common.by import By
from utils.wait_utils import WaitUtils
from utils.config import Config

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait_utils = WaitUtils(driver)
        
    # Locators
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")
    
    # Actions
    def navigate_to_login(self):
        self.driver.get(Config.BASE_URL)
        
    def enter_username(self, username):
        self.wait_utils.send_text(self.USERNAME_INPUT, username)
        
    def enter_password(self, password):
        self.wait_utils.send_text(self.PASSWORD_INPUT, password)
        
    def click_login(self):
        self.wait_utils.click_element(self.LOGIN_BUTTON)
        
    def login(self, username, password):
        self.navigate_to_login()
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        
    def get_error_message(self):
        return self.wait_utils.get_text(self.ERROR_MESSAGE)
