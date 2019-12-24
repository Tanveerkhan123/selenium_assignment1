from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


class RegisterPage(object):

    def __init__(self, driver):
        self.driver = driver

    def is_browser_on_the_page(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'.action')))
        return True


    def fill_form(self):
        email_elem = self.driver.find_element_by_css_selector('#register-email')
        email_elem.send_keys('dumy123')

        full_name = self.driver.find_element_by_css_selector('#register-name')
        full_name.send_keys('test 123')

        pub_name = self.driver.find_element_by_css_selector('#register-username')
        pub_name.send_keys('Tan321r')

        pass_elem = self.driver.find_element_by_css_selector('#register-password')
        pass_elem.send_keys('dummy123')

    def create_account(self):
        submit_elem = self.driver.find_element_by_css_selector('.action')
        submit_elem.click()

        time.sleep(10)





