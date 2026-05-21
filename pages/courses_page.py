from components.course.course_view_component import CourseViewComponent
from pages.base_page import BasePage
from playwright.sync_api import Page, expect
from components.navigation.sidebar_component import SidebarComponents
from components.navigation.navbar_component import NavbarComponent
from components.views.empty_view_component import EmptyViewComponent


class CoursesPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.sidebar = SidebarComponents(page)
        self.navbar = NavbarComponent(page)
        self.empty_view = EmptyViewComponent(page, 'courses-list')
        self.course_view = CourseViewComponent(page)

        self.courses_title = page.get_by_test_id('courses-list-toolbar-title-text')
        self.create_course_button = page.get_by_test_id('courses-list-toolbar-create-course-button')

    def check_visible_courses_title(self):
        expect(self.courses_title).to_be_visible()
        expect(self.courses_title).to_have_text('Courses')

    def check_visible_empty_view(self):
        self.empty_view.check_visible(
            title='There is no results',
            description='Results from the load test pipeline will be displayed here'
        )

    def check_visible_create_course_button(self):
        expect(self.create_course_button).to_be_visible()

    def click_create_course_button(self):
        expect(self.create_course_button).to_be_visible()

    def check_visible_course_card(self, index: int, title: str, max_score: str, min_score: str, estimated_time: str):
        self.course_view.check_visible(
            index=index,
            title=title,
            max_score=max_score,
            min_score=min_score,
            estimated_time=estimated_time
        )