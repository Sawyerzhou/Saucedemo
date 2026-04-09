from selenium.webdriver.common.by import By
from .base_page import BasePage

class InventoryPage(BasePage):
    ADD_TO_CART_BTN = (By.ID, "add-to-cart-sauce-labs-backpack")
    SHOPPING_CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def add_backpack_to_cart(self):
        self.click(self.ADD_TO_CART_BTN)

    def get_cart_count(self):
        try:
            return int(self.get_text(self.SHOPPING_CART_BADGE))
        except:
            return 0