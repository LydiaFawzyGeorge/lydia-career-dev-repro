from selenium import webdriver
import unittest


class UserRegister(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # create new chrome session
        cls.driver = webdriver.Chrome("C:/Users/LFawzy/Downloads/chromedriver_win32/chromedriver.exe")
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

        # navigate to application home page
        cls.driver.get("http://demo.magentocommerce.com/")
        cls.driver.title

    def test_a_user_register(self):
        # get the my account button
        self.my_account = self.driver.find_element_by_link_text("MY ACCOUNT")
        self.my_account.click()
        # get register button
        self.user_register = self.driver.find_element_by_xpath("//*[@id='login-form']/div/div/div[2]/div/button")
        self.user_register.click()

        # set personal info
        self.first_name = self.driver.find_element_by_id("firstname")
        self.first_name.send_keys("firstname8")
        self.last_name = self.driver.find_element_by_id("lastname")
        self.last_name.send_keys("lastname8")
        self.email_address = self.driver.find_element_by_id("email_address")
        self.email_address.send_keys("emailnew8@gmail.com")

        self.customer_company_type = self.driver.find_element_by_id("customer_company_type")
        self.customer_company_type.send_keys("Analyst/Media")

        self.customer_individual_role = self.driver.find_element_by_id("customer_individual_role")
        self.customer_individual_role.send_keys("Technical/developer")

        # set login information
        self.screen_name = self.driver.find_element_by_id("screen_name")
        self.screen_name.send_keys("screenname8")

        self.password = self.driver.find_element_by_id("password")
        self.password.send_keys("123@lolo.com")

        self.confirm_password = self.driver.find_element_by_id("confirmation")
        self.confirm_password.send_keys("123@lolo.com")

        # terms of service

        self.agreement = self.driver.find_element_by_id("agree_terms")
        self.agreement.click()
        self.submit_data = self.driver.find_element_by_id("registerSubmit")
        self.submit_data.click()

        # log out
    def test_b_user_logout(self):
        self.logout = self.driver.find_element_by_link_text("Log Out")
        self.logout.click()
        # login

    def test_c_user_login(self):
        self.login_email = self.driver.find_element_by_id("email")
        self.login_email.send_keys("emailnew8@gmail.com")
        self.login_password = self.driver.find_element_by_id("pass")
        self.login_password.send_keys("123@lolo.com")
        self.login_submit = self.driver.find_element_by_id("send2")
        self.login_submit.click()

        # if logout exists, so login was success
        self.logout = self.driver.find_element_by_link_text("Log Out")
        self.displayed = self.logout.is_displayed()
        if (self.displayed):
            print("displayed")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()