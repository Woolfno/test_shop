import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru', help='Choose language')
    parser.addoption('--browser_name', action='store', default='chrome', help='Choose browser: firefox, chrome')

@pytest.fixture(scope='function')
def browser(request):
    language = request.config.getoption('language')
    browser_name = request.config.getoption('browser_name')
    browser = None
    if browser_name.lower()=='firefox':
        profile = webdriver.FirefoxProfile()
        profile.set_preference('intl.accept_languages', language)
        browser = webdriver.Firefox(firefox_profile=profile)
    elif browser_name.lower()=='chrome':
        options = webdriver.chrome.options.Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError('--browser_name should be firefox or chrome')
    yield browser
    browser.quit()