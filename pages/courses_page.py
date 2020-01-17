from .base_page import BasePage

class CoursePage(BasePage):

    def is_browser_on_the_page(self):
        return self.find_elem('.js-featured-results').is_displayed()