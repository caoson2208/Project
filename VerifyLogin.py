import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Constants
LOGIN_URL = "https://be.hurav.com/#/login"
EXPECTED_URL = "https://be.hurav.com/#/dashboard"
USERNAME = "soncao"
PASSWORD = "Son0799399003"


def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    return webdriver.Chrome(options=options)


def login(driver, username, password):
    driver.get(LOGIN_URL)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "login_username")))

    driver.find_element(By.ID, "login_username").send_keys(username)
    driver.find_element(By.ID, "login_password_fake").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "button[ng-click*='doLogin()']").click()


def verify_login(driver):
    WebDriverWait(driver, 10).until(EC.url_to_be(EXPECTED_URL))
    assert driver.current_url == EXPECTED_URL, f"URL không đúng, hiện tại là: {driver.current_url}"
    time.sleep(5)


def test_login():
    driver = setup_driver()
    try:
        login(driver, USERNAME, PASSWORD)
        verify_login(driver)
        print("Đăng nhập thành công!")
    except Exception as e:
        print(f"Đăng nhập thất bại: {str(e)}")
    finally:
        driver.quit()


if __name__ == "__main__":
    test_login()