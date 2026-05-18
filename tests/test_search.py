import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from utils.config import Config

@pytest.mark.usefixtures("setup")
class TestProductValidation:
    @pytest.fixture(autouse=True)
    def setup_pre_test(self, setup):
        login_page = LoginPage(self.driver)
        login_page.login(Config.USERNAME, Config.PASSWORD)
        
    def test_products_displayed(self):
        home_page = HomePage(self.driver)
        products = home_page.get_all_product_names()
        assert len(products) > 0, "No products displayed on the page"
        assert "Sauce Labs Backpack" in products, "Expected product not found in the list"
