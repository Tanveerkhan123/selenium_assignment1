
class Dashboard(object):
    def __init__(self, driver):
        self.driver = driver


    def is_browser_on_the_page(self):

        assert 'Dashboard' in self.driver.title
