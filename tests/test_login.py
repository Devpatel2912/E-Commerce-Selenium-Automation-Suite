import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from utils.config import Config

@pytest.mark.usefixtures("setup")
class TestLogin:
    def test_valid_login(self):
        login_page = LoginPage(self.driver)
        home_page = HomePage(self.driver)
        
        login_page.login(Config.USERNAME, Config.PASSWORD)
        assert home_page.is_on_home_page(), "Failed to login with valid credentials"

    @pytest.mark.parametrize("username, password, error_msg", [
        ("locked_out_user", "secret_sauce", "Sorry, this user has been locked out."),
        ("invalid_user", "secret_sauce", "Username and password do not match any user in this service"),
        ("", "secret_sauce", "Username is required"),
        ("standard_user", "", "Password is required")
    ])
    def test_invalid_login(self, username, password, error_msg):
        login_page = LoginPage(self.driver)
        
        login_page.login(username, password)
        actual_error = login_page.get_error_message()
        assert error_msg in actual_error, f"Expected error '{error_msg}' but got '{actual_error}'"
