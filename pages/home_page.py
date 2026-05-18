from selenium.webdriver.common.by import By
from utils.wait_utils import WaitUtils

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait_utils = WaitUtils(driver)
        
    # Locators
    TITLE = (By.CLASS_NAME, "title")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    
    def get_product_button_locator(self, product_name):
        formatted_name = product_name.lower().replace(" ", "-")
        return (By.ID, f"add-to-cart-{formatted_name}")
        
    def get_remove_button_locator(self, product_name):
        formatted_name = product_name.lower().replace(" ", "-")
        return (By.ID, f"remove-{formatted_name}")
    
    # Actions
    def is_on_home_page(self):
        try:
            title_text = self.wait_utils.get_text(self.TITLE)
            return title_text.lower() == "products"
        except:
            return False
            
    def add_product_to_cart(self, product_name):
        locator = self.get_product_button_locator(product_name)
        self.wait_utils.click_element(locator)
        
    def remove_product_from_cart(self, product_name):
        locator = self.get_remove_button_locator(product_name)
        self.wait_utils.click_element(locator)
        
    def get_cart_item_count(self):
        try:
            return int(self.wait_utils.get_text(self.CART_BADGE))
        except:
            return 0
            
    def go_to_cart(self):
        self.wait_utils.click_element(self.CART_ICON)
        
    def get_all_product_names(self):
        elements = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        return [el.text for el in elements]
