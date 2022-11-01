from selenium.webdriver.common.by import By


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    PRICE_BASKET = (By.CSS_SELECTOR, ".alertinner p > strong")
    NAME_BASKET = (By.CSS_SELECTOR, ".alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link")