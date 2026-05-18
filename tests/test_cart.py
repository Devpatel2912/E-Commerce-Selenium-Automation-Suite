import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.cart_page import CartPage
from utils.config import Config

@pytest.mark.usefixtures("setup")
class TestCart:
    @pytest.fixture(autouse=True)
    def setup_pre_test(self, setup):
        login_page = LoginPage(self.driver)
        login_page.login(Config.USERNAME, Config.PASSWORD)
        
    def test_add_to_cart(self):
        home_page = HomePage(self.driver)
        home_page.add_product_to_cart("Sauce Labs Backpack")
        assert home_page.get_cart_item_count() == 1, "Cart badge count is not 1"
        
        home_page.go_to_cart()
        cart_page = CartPage(self.driver)
        cart_items = cart_page.get_cart_items()
        assert "Sauce Labs Backpack" in cart_items, "Product was not added to the cart"
        
    def test_remove_from_cart(self):
        home_page = HomePage(self.driver)
        home_page.add_product_to_cart("Sauce Labs Bike Light")
        home_page.add_product_to_cart("Sauce Labs Bolt T-Shirt")
        
        home_page.go_to_cart()
        cart_page = CartPage(self.driver)
        
        cart_items_before = cart_page.get_cart_items()
        assert len(cart_items_before) == 2, "Expected 2 items in cart"
        
        cart_page.remove_item("Sauce Labs Bike Light")
        
        cart_items_after = cart_page.get_cart_items()
        assert len(cart_items_after) == 1, "Item was not removed from cart"
        assert "Sauce Labs Bike Light" not in cart_items_after, "Removed item still in cart"
