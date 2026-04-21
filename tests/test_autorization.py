from playwright.sync_api import expect, Page
import pytest
from pages.login_page import LoginPage

creds = {
    ("user.name@gmail.com", "password"): "Invalid data",
    ("user.name@gmail.com", " "): "Invalid pass",
    (" ", "password"): "Invalid email"
}


@pytest.mark.parametrize('email, password',
                         creds.keys(),
                         ids=creds.values())
@pytest.mark.regression
@pytest.mark.registration
def test_wrong_email_or_password_authorization(login_page: LoginPage, email: str, password: str):
    login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
    login_page.fill_login_form(email=email, password=password)
    login_page.click_login_button()
    login_page.check_visible_wrong_email_or_password_alert()
