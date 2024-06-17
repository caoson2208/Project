from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Constants
LOGIN_URL = "https://be.hurav.com/#/login"
EXPECTED_URL = "https://divui.com/dashboard"
USERNAME = "soncao"
PASSWORD = "Son0799399003"

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = driver.find_element(by=By.ID, value="login_username")
        self.password_input = driver.find_element(by=By.ID, value="login_password_fake")
        self.login_button = driver.find_element(By.CSS_SELECTOR, "button[ng-click*='doLogin()']")

    def enter_username(self, username):
        self.username_input.send_keys(username)

    def enter_password(self, password):
        self.password_input.send_keys(password)

    def click_login(self):
        self.login_button.click()


def test_login(driver, login_url, username, password, expected_url):
    driver.get(login_url)
    driver.implicitly_wait(5)

    login_page = LoginPage(driver)
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()

    wait = WebDriverWait(driver, 5)
    wait.until(lambda d: d.current_url == expected_url)

    current_url = driver.current_url
    assert current_url == expected_url, f"URL không đúng, hiện tại là: {current_url}"


def create_driver() -> webdriver.Chrome:
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver


if __name__ == "__main__":
    with create_driver() as driver:
        test_login(driver, LOGIN_URL, USERNAME, PASSWORD, EXPECTED_URL)