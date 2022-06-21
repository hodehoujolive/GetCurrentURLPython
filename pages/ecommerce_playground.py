from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class EcommercePlaygroundPage:

    #url
    url = 'https://ecommerce-playground.lambdatest.io/'

    #locators
    search_form = (By.NAME, "search")
    search_button = (By.CSS_SELECTOR, ".type-text")

    # Initializer
    def __init__(self, browser):
        self.browser = browser

    # Interaction methods
    def load(self):
        self.browser.get(self.url)

    def search(self , keyword):
        search_form = self.browser.find_element(*self.search_form)
        search_form.send_keys(keyword)
        search_button = self.browser.find_element(*self.search_button)
        search_button.click()
