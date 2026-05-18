import os
from datetime import datetime
from utils.logger import Logger

log = Logger.get_logger(__name__)

class ScreenshotUtil:
    @staticmethod
    def take_screenshot(driver, test_name):
        reports_dir = os.path.join(os.getcwd(), "screenshots")
        if not os.path.exists(reports_dir):
            os.makedirs(reports_dir)
            
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"{test_name}_{timestamp}.png"
        filepath = os.path.join(reports_dir, filename)
        
        try:
            driver.save_screenshot(filepath)
            log.info(f"Screenshot saved: {filepath}")
        except Exception as e:
            log.error(f"Failed to save screenshot: {e}")
