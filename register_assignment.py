from selenium import webdriver
import unittest
from pages.register_page import RegisterPage
from pages.dashboard_page import Dashboard
from pages.select_page import SelectPage

class EdxRegister(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.register = RegisterPage(self.driver)
        self.dashboard = Dashboard(self.driver)
        self.select = SelectPage(self.driver)

    def test_register(self):
        self.driver.get('https://courses.edx.org/register')
        self.assertTrue(self.register.is_browser_on_the_page())

        self.register.fill_form()

        self.select.select_country()

        self.register.create_account()

        self.dashboard.is_browser_on_the_page()







    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()