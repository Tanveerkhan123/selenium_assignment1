from selenium.webdriver.support.ui import Select

class SelectPage(object):
    def __init__(self, driver):
        self.driver = driver

    def select_country(self):
        country_elem = Select(self.driver.find_element_by_css_selector('#register-country'))
        country_elem.select_by_visible_text('Pakistan')