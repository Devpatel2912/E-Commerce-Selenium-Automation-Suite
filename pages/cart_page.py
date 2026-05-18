from selenium.webdriver.common.by import By
from utils.wait_utils import WaitUtils

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait_utils = WaitUtils(driver)
        
    # Locators
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")
    CART_ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    
    def get_remove_button_locator(self, product_name):
        formatted_name = product_name.lower().replace(" ", "-")
        return (By.ID, f"remove-{formatted_name}")
        
    # Actions
    def get_cart_items(self):
        elements = self.driver.find_elements(*self.CART_ITEM_NAMES)
        return [el.text for el in elements]
        
    def remove_item(self, product_name):
        locator = self.get_remove_button_locator(product_name)
        self.wait_utils.click_element(locator)
        
    def click_checkout(self):
        self.wait_utils.click_element(self.CHECKOUT_BUTTON)
