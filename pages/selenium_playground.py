from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class SELENIUM_PLAYGROUND_PAGE:

    #url
    url = 'https://www.lambdatest.com/selenium-playground/'

    #locators
    SIMPLE_FORM = (By.XPATH, "//a[normalize-space()='Simple Form Demo']")

    # Initializer
    def __init__(self, browser):
        self.browser = browser


    # Interaction methods
    def load(self):
        self.browser.get(self.url)
        self.browser.implicitly_wait(30)
        

    def simple_form(self):
        simple_form = self.browser.find_element(*self.SIMPLE_FORM)
        simple_form.click()
