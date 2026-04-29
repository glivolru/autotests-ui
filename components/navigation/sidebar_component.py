import re

from playwright.sync_api import Page

from components.base_components import BaseComponent
from components.navigation.sidebar_list_item_component import SidebarListComponent


class SidebarComponents(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.logout_list_item = SidebarListComponent(page, 'logout')
        self.courses_list_item = SidebarListComponent(page, 'courses')
        self.dashboard_list_item = SidebarListComponent(page, 'dashboard')

    def check_visible(self):
        self.logout_list_item.check_visible('Logout')
        self.courses_list_item.check_visible('Courses')
        self.dashboard_list_item.check_visible('Dashboard')

    def click_logout(self):
        self.logout_list_item.navigate_url(re.compile(r".*/#/auth/logout"))

    def click_courses(self):
        self.courses_list_item.navigate_url(re.compile(r".*/#/courses"))

    def click_dashboard(self):
        self.dashboard_list_item.navigate_url(re.compile(r".*/#/dashboard"))
