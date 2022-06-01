import pytest
import time
from pages.ecommerce_playground import ECOMMERCE_PLAYGROUND_PAGE

keyword = "lambda"

def test_ecommerce_playground(browser):
    ecommerce_page = ECOMMERCE_PLAYGROUND_PAGE(browser)
    ecommerce_page.load()
    ecommerce_page.search(keyword)

    get_url = browser.current_url
    title = browser.title


    print("The current url is: "+str(get_url))
    assert "lambda" in get_url

    with open('urls.txt', 'a') as f:
        f.write(title + " : "+ get_url)
        f.write('\n')

    
