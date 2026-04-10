from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    reg_button = page.get_by_test_id("registration-page-registration-button")
    expect(reg_button).to_be_disabled()

    reg_email = page.get_by_test_id("registration-form-email-input").locator("input")
    reg_email.fill("user.name@gmail.com")

    reg_username = page.get_by_test_id("registration-form-username-input").locator("input")
    reg_username.fill("username")

    reg_password = page.get_by_test_id("registration-form-password-input").locator("input")
    reg_password.fill("password")

    reg_button = page.get_by_test_id("registration-page-registration-button")
    expect(reg_button).not_to_be_disabled()

    page.wait_for_timeout(5000)

