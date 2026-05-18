from selenium.webdriver.common.by import By
from utils.wait_utils import WaitUtils

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait_utils = WaitUtils(driver)
        
    # Locators - Step 1
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")
    
    # Locators - Step 2
    FINISH_BUTTON = (By.ID, "finish")
    TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")
    
    # Locators - Complete
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")
    BACK_HOME_BUTTON = (By.ID, "back-to-products")
    
    # Actions
    def enter_checkout_info(self, first_name, last_name, postal_code):
        self.wait_utils.send_text(self.FIRST_NAME_INPUT, first_name)
        self.wait_utils.send_text(self.LAST_NAME_INPUT, last_name)
        self.wait_utils.send_text(self.POSTAL_CODE_INPUT, postal_code)
        
    def click_continue(self):
        self.wait_utils.click_element(self.CONTINUE_BUTTON)
        
    def get_error_message(self):
        return self.wait_utils.get_text(self.ERROR_MESSAGE)
        
    def click_finish(self):
        self.wait_utils.click_element(self.FINISH_BUTTON)
        
    def get_total_amount(self):
        return self.wait_utils.get_text(self.TOTAL_LABEL)
        
    def get_order_complete_message(self):
        return self.wait_utils.get_text(self.COMPLETE_HEADER)
