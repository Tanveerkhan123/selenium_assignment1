from selenium import webdriver
import unittest

class Github(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Firefox()

    def test_login(self):
        self.driver.get('https://www.github.com/login')
        self.assertIn('GitHub', self.driver.title)

        email_elem = self.driver.find_element_by_css_selector('#login_field')
        email_elem.send_keys('trainingdummy123@gmail.com')

        pwd_elem = self.driver.find_element_by_css_selector('#password')
        pwd_elem.send_keys('trainingdummy123')

        submit_elem = self.driver.find_element_by_css_selector('.btn')
        submit_elem.click()


        self.assertIn('GitHub', self.driver.title)

    def tearDown(self):

        self.driver.close()


if __name__ == "__main__":
    unittest.main()

