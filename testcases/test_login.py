import pytest
import allure
from pages.login_page import LoginPage
from utils.read_data import get_users


@allure.feature("登录模块")
@allure.story("用户登录")
@allure.severity(allure.severity_level.CRITICAL)
def test_standard_user_login(driver):
    users = get_users()
    username = users["standard_user"]["username"]
    password = users["standard_user"]["password"]

    login_page = LoginPage(driver)
    inventory_page = login_page.login(username, password)
    assert inventory_page.get_cart_count() == 0

def test_locked_out_user_login(driver):
    users = get_users()
    username = users["locked_out_user"]["username"]
    password = users["locked_out_user"]["password"]

    login_page = LoginPage(driver)
    login_page.login(username, password)
    error_msg = login_page.get_error_message()
    assert "locked out" in error_msg