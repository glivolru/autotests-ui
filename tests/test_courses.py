import pytest
from playwright.sync_api import sync_playwright, expect


@pytest.mark.regression
@pytest.mark.courses
def test_empty_courses_list(chromium_page, chromium_page_with_state):

    chromium_page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

    courses_title = chromium_page.get_by_test_id("courses-list-toolbar-title-text")
    expect(courses_title).to_be_visible()

    folder_icon = chromium_page.get_by_test_id("courses-list-empty-view-icon")
    expect(folder_icon).to_be_visible()

    empty_result_text = chromium_page.get_by_test_id("courses-list-empty-view-title-text")
    expect(empty_result_text).to_be_visible()

    empty_result_description = chromium_page.get_by_test_id("courses-list-empty-view-description-text")
    expect(empty_result_description).to_be_visible()
