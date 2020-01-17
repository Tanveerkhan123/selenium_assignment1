from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class is_document_ready(object):

    def __call__(self, driver):

        page_status = driver.execute_script("return document.readyState=='complete'")

        return page_status




class BasePage(object):

    def __init__(self, driver):

        self.driver = driver


    def find_elem(self, css_selector, timeout = 30):

        try:
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))

        except TimeoutException:
            raise  TimeoutException('{} not found'.format(css_selector))



    def wait_for_element_visibility(self, css_selector, timeout = 20):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, css_selector)))

        except TimeoutException:
            raise TimeoutException('{} is not visible'.format(css_selector))


    def wait_for_element_to_be_clicked(self, css_selector, timeout = 20):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector)))

        except TimeoutException:
            raise TimeoutException('{} is not clicked'.format(css_selector))


    def  wait_to_find_the_title(self, title_string, timeout = 10):

        try:
            return WebDriverWait(self.driver, timeout).until(EC.title_contains(title_string))
        except TimeoutException:
            raise TimeoutException('{} is not present in title'.format(title_string))


    def wait_for_page(self, timeout = 10):

        try:
            return WebDriverWait(self.driver, timeout).until(is_document_ready())
        except TimeoutException:

            raise TimeoutException('Page is not loaded completely: {}'.format(self))

        try:
            return WebDriverWait(self.driver, timeout).until(lambda x: (self.is_browser_on_page(), self))
        except TimeoutException:

            raise TimeoutException('Page is not loaded completely: {}'.format(self))
