import random


class ShoppingCart:
    def __init__(self, driver):
        self.driver = driver

    def enter_text(self):
        element = self.driver.find_element("xpath", "//input[@id='product_attribute_12']")
        element.click()
        element.send_keys(random.randint(0, 9))

    def add_cart(self):
        self.driver.find_element("id", "add-to-cart-button-29").click()

    def shopping_cart(self):
        self.driver.find_element("xpath", "//span[@class= 'cart-label']").click()
