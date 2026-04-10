from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    reg_email = page.get_by_test_id("registration-form-email-input").locator("input")
    reg_email.fill("user.name@gmail.com")

    reg_username = page.get_by_test_id("registration-form-username-input").locator("input")
    reg_username.fill("username")

    reg_password = page.get_by_test_id("registration-form-password-input").locator("input")
    reg_password.fill("password")

    reg_button = page.get_by_test_id("registration-page-registration-button")
    reg_button.click()

    context.storage_state(path='browser-state.json')


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='browser-state.json')
    page = context.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

    courses_title = page.get_by_test_id("courses-list-toolbar-title-text")
    expect(courses_title).to_be_visible()

    folder_icon = page.get_by_test_id("courses-list-empty-view-icon")
    expect(folder_icon).to_be_visible()

    empty_result_text = page.get_by_test_id("courses-list-empty-view-title-text")
    expect(empty_result_text).to_be_visible()

    empty_result_description = page.get_by_test_id("courses-list-empty-view-description-text")
    expect(empty_result_description).to_be_visible()

    page.wait_for_timeout(5000)
