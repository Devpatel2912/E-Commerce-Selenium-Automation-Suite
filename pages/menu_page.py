from selenium.webdriver.common.by import By
from utils.wait_utils import WaitUtils

class MenuPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait_utils = WaitUtils(driver)
        
    # Locators
    BURGER_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")
    ALL_ITEMS_LINK = (By.ID, "inventory_sidebar_link")
    RESET_STATE_LINK = (By.ID, "reset_sidebar_link")
    
    # Actions
    def open_menu(self):
        self.wait_utils.click_element(self.BURGER_BUTTON)
        
    def click_logout(self):
        self.wait_utils.click_element(self.LOGOUT_LINK)
        
    def logout(self):
        self.open_menu()
        self.click_logout()
