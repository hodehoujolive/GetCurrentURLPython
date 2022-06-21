from selenium.webdriver.common.by import By

class SeleniumPlaygroundPage:

    #url
    url = 'https://www.lambdatest.com/selenium-playground/'

    #locators
    simple_form_demo = (By.XPATH, "//a[normalize-space()='Simple Form Demo']")

    # Initializer
    def __init__(self, browser):
        self.browser = browser


    # Interaction methods
    def load(self):
        self.browser.get(self.url)
        

    def simple_form(self):
        simple_form = self.browser.find_element(*self.simple_form_demo)
        simple_form.click()