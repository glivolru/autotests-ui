import pytest
from playwright.sync_api import Page

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.courses_page import CoursesPage


@pytest.fixture
def login_page(chromium_page: Page) -> LoginPage:
    return LoginPage(page=chromium_page)


@pytest.fixture
def dashboard_page(chromium_page: Page) -> DashboardPage:
    return DashboardPage(page=chromium_page)


@pytest.fixture
def courses_list_page(chromium_page: Page) -> CoursesPage:
    return CoursesPage(page=chromium_page)
