import pytest
from pages.login_page import LoginPage
from pages.menu_page import MenuPage
from utils.config import Config
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup")
class TestLogout:
    def test_logout(self):
        login_page = LoginPage(self.driver)
        login_page.login(Config.USERNAME, Config.PASSWORD)
        
        menu_page = MenuPage(self.driver)
        menu_page.logout()
        
        # Verify logout by checking if login button is displayed
        login_btn = self.driver.find_elements(By.ID, "login-button")
        assert len(login_btn) > 0, "Failed to logout, login button not found"
