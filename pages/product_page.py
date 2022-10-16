from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        login_link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        login_link.click()

    def check_name(self):
        name = self.browser.find_element(*ProductPageLocators.NAME)
        name_text = name.text
        name_basket = self.browser.find_element(*ProductPageLocators.NAME_BASKET)
        name_basket_text = name_basket.text
        assert name_text == name_basket_text, "Name Error"

    def check_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE)
        price_text = price.text
        price_basket = self.browser.find_element(*ProductPageLocators.PRICE_BASKET)
        price_basket_text = price_basket.text
        assert price_text == price_basket_text, "Price Error"
