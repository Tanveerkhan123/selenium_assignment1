from .base_page import BasePage
from .dashboard_page import Dashboard

class RegisterPage(BasePage):

    def is_browser_on_the_page(self):
        self.wait_for_element_visibility('.action')
        return True


    def fill_form(self, user_email, user_fullname, user_pubname, user_password):
        email_elem = self.find_elem('#register-email')
        email_elem.send_keys(user_email)

        full_name = self.find_elem('#register-name')
        full_name.send_keys(user_fullname)

        pub_name = self.find_elem('#register-username')
        pub_name.send_keys(user_pubname)

        pass_elem = self.find_elem('#register-password')
        pass_elem.send_keys(user_password)

    def create_account(self):
        submit_elem = self.find_elem('.action')

        # Wait for the submit button until become click-able

        self.wait_for_element_to_be_clicked('.action')
        submit_elem.click()

        Dashboard(self.driver).wait_for_page()






