from selenium import webdriver

class DriverFactory:
    @staticmethod
    def get_driver(browser_name="chrome"):
        if browser_name.lower() == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("--start-maximized")
            
            # Disable password manager warning and automation info bar
            prefs = {
                "credentials_enable_service": False,
                "profile.password_manager_enabled": False
            }
            options.add_experimental_option("prefs", prefs)
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option("useAutomationExtension", False)
            
            driver = webdriver.Chrome(options=options)
        elif browser_name.lower() == "firefox":
            options = webdriver.FirefoxOptions()
            driver = webdriver.Firefox(options=options)
            driver.maximize_window()
        elif browser_name.lower() == "edge":
            options = webdriver.EdgeOptions()
            options.add_argument("--start-maximized")
            driver = webdriver.Edge(options=options)
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")
        return driver
