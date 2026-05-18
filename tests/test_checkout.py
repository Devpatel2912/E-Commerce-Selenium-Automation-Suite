import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.config import Config

@pytest.mark.usefixtures("setup")
class TestCheckout:
    @pytest.fixture(autouse=True)
    def setup_pre_test(self, setup):
        login_page = LoginPage(self.driver)
        login_page.login(Config.USERNAME, Config.PASSWORD)
        
    def test_checkout_flow(self):
        home_page = HomePage(self.driver)
        home_page.add_product_to_cart("Sauce Labs Fleece Jacket")
        home_page.go_to_cart()
        
        cart_page = CartPage(self.driver)
        cart_page.click_checkout()
        
        checkout_page = CheckoutPage(self.driver)
        checkout_page.enter_checkout_info("John", "Doe", "12345")
        checkout_page.click_continue()
        
        # Verify step 2
        total = checkout_page.get_total_amount()
        assert "Total:" in total, "Total amount not displayed"
        
        checkout_page.click_finish()
        
        # Verify completion
        complete_msg = checkout_page.get_order_complete_message()
        assert "Thank you for your order!" in complete_msg, "Order not completed successfully"
        
    def test_checkout_missing_info(self):
        home_page = HomePage(self.driver)
        home_page.add_product_to_cart("Sauce Labs Onesie")
        home_page.go_to_cart()
        
        cart_page = CartPage(self.driver)
        cart_page.click_checkout()
        
        checkout_page = CheckoutPage(self.driver)
        checkout_page.enter_checkout_info("", "Doe", "12345")
        checkout_page.click_continue()
        
        error_msg = checkout_page.get_error_message()
        assert "Error: First Name is required" in error_msg, "Validation message not shown"
