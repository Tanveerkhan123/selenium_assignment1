from.base_page import BasePage
from .courses_page import CoursePage

class Dashboard(BasePage):

    def is_browser_on_the_page(self):
        return self.find_elem('.btn-neutral').is_displayed()


    def go_to_course_page(self):

        self.find_elem('.btn-neutral').click()
        CoursePage(self.driver).wait_for_page()



