import os
import warnings
from pathlib import Path

import pytest
import yaml

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service as ServiceChrome
from selenium.webdriver.firefox.service import Service as ServiceFirefox
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

os.environ['WDM_LOG_LEVEL'] = '0'

def load_config():
    path = Path(__file__).parent / "../config.yaml"
    with open(path) as config_file:
        return yaml.safe_load(config_file)

# Tải config một lần khi module được import
CONFIG = load_config()

class BaseTest:

    @pytest.fixture(autouse=True)
    def init_driver(self):
        warnings.simplefilter("ignore", ResourceWarning)
        if CONFIG['browser'] == 'chrome':
            options = webdriver.ChromeOptions()
            options.add_argument('--start-maximized')
            if CONFIG['headless']:
                options.add_argument('--headless')
                options.add_argument('--no-sandbox')
                options.add_argument('--disable-gpu')
            self.driver = webdriver.Chrome(service=ServiceChrome(ChromeDriverManager().install()), options=options)
        elif CONFIG['browser'] == 'firefox':
            options = webdriver.FirefoxOptions()
            options.add_argument('--start-maximized')
            if CONFIG['headless']:
                options.add_argument('--headless')
                options.add_argument('--no-sandbox')
                options.add_argument('--disable-gpu')
            self.driver = webdriver.Firefox(service=ServiceFirefox(GeckoDriverManager().install()), options=options)
        else:
            raise Exception("Incorrect Browser")

        # Không cần gọi maximize_window() nữa vì đã được set trong options
        self.wait = WebDriverWait(self.driver, CONFIG.get('timeout', 10))
        yield self.wait, self.driver

        if self.driver is not None:
            self.driver.quit()

# Các biến config có thể được truy cập trực tiếp nếu cần
BROWSER = CONFIG['browser']
HEADLESS = CONFIG['headless']
TIMEOUT = CONFIG.get('timeout', 10)