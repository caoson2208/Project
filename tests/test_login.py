# coding=utf-8
import pytest
from pages.login_page import LoginPage
from tests.base_test import BaseTest



class TestLogin(BaseTest):

    @pytest.fixture
    def load_pages(self):
        self.page = LoginPage(self.driver, self.wait)
        self.page.go_to_login_page()

    def test_login(self, load_pages):
        self.page.set_user_inputs("soncao", "Son0799399003")

