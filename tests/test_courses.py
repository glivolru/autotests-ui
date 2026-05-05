import pytest
from pages.courses_page import CoursesPage


@pytest.mark.regression
@pytest.mark.courses
def test_empty_courses_list(courses_list_page: CoursesPage):
    courses_list_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

    courses_list_page.check_visible_courses_title()
    courses_list_page.check_visible_create_course_button()
    courses_list_page.check_visible_empty_view()

    courses_list_page.navbar.check_visible('username')
    courses_list_page.sidebar.check_visible()
