import pytest
from playwright.sync_api import Page, Playwright


@pytest.fixture
def chromium_page(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    yield browser.new_page()
    browser.close()


@pytest.fixture
def initialize_browser_state(chromium_page) -> None:
    chromium_page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    reg_email = chromium_page.get_by_test_id("registration-form-email-input").locator("input")
    reg_email.fill("user.name@gmail.com")

    reg_username = chromium_page.get_by_test_id("registration-form-username-input").locator("input")
    reg_username.fill("username")

    reg_password = chromium_page.get_by_test_id("registration-form-password-input").locator("input")
    reg_password.fill("password")

    reg_button = chromium_page.get_by_test_id("registration-page-registration-button")
    reg_button.click()

    chromium_page.context.storage_state(path='browser-state.json')


@pytest.fixture(scope='function')
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='browser-state.json')
    page = context.new_page()
    yield page
    browser.close()
