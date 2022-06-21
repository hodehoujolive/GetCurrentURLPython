import pytest
from pages.selenium_playground import SeleniumPlaygroundPage


def test_selenium_playground(browser):
    playground_page = SeleniumPlaygroundPage(browser)
    playground_page.load()
    playground_page.simple_form()

    # Get the current url of the page in a variable
    get_url = browser.current_url

    title = browser.title

    # Display the url in the console
    print("The current url is: "+str(get_url))

    # Save the url in a urls.txt file
    with open('urls.txt', 'a') as f:
        f.write(title + " : "+ get_url)
        f.write('\n')