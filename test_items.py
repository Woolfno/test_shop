import pytest
from selenium.common.exceptions import NoSuchElementException
import time


def test_button_add_to_basket(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    button = None
    try:
        button = browser.find_element_by_class_name('btn-add-to-basket')
    except NoSuchElementException:
        pass
    assert button!=None, 'Should be button add to basket'