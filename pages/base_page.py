from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout
        self.logger = logging.getLogger(__name__)

    def find_element(self, locator):
        """等待元素可见并返回"""
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def find_elements(self, locator):
        """等待至少一个元素出现并返回列表"""
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_all_elements_located(locator)
        )

    def click(self, locator):
        self.logger.info(f"Clicking element: {locator}")
        self.find_element(locator).click()

    def input_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.find_element(locator).text

    def is_element_visible(self, locator):
        """检查元素是否可见"""
        try:
            self.find_element(locator)
            return True
        except TimeoutException:
            return False