from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class ECOMMERCE_PLAYGROUND_PAGE:

    #url
    url = 'https://ecommerce-playground.lambdatest.io/'

    #locators
    SEARCH_FORM = (By.XPATH, "//div[@id='entry_217822']//input[@placeholder='Search For Products']")
    SEARCH_BUTTON = (By.XPATH, "//button[normalize-space()='Search']")

    # Initializer
    def __init__(self, browser):
        self.browser = browser


    # Interaction methods
    def load(self):
        self.browser.get(self.url)
        self.browser.implicitly_wait(30)
        

    def search(self , keyword):
        search_form = self.browser.find_element(*self.SEARCH_FORM)
        search_form.send_keys(keyword)
        search_button = self.browser.find_element(*self.SEARCH_BUTTON)
        search_button.click()
