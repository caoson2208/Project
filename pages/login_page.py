from constants.config import config
from pages.base_page import BasePage
from locators.locators import LoginPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class LoginPage(BasePage):

    def __init__(self, driver, wait):
        self.url = config.BASE_URL
        self.locator = LoginPageLocators
        super().__init__(driver, wait)

    def go_to_login_page(self):
        self.go_to_page(self.url)

    def set_user_inputs(self, username, password):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "login_username")))
        self.driver.find_element(*LoginPageLocators.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

