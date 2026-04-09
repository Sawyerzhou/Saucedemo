from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    # 元素定位器
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")

    def login(self, username, password):
        """执行登录操作"""
        self.input_text(self.USERNAME_INPUT, username)
        self.input_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
        # 登录后返回商品列表页对象
        from .inventory_page import InventoryPage
        return InventoryPage(self.driver)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)