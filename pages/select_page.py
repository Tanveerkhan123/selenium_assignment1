from selenium.webdriver.support.ui import Select
from .base_page import BasePage

class SelectPage(BasePage):

    def select_country(self):
        country_elem = Select(self.find_elem('#register-country'))
        country_elem.select_by_visible_text('Pakistan')