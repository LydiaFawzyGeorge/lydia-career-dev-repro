from LocatorsFolder.Locators import UserRegisterLocator
from LocatorsFolder.Locators import UserLogout
from LocatorsFolder.Locators import UserLogin


class UserRegisterScript:

    def new_user_register(self,register_values):
        self.driver.find_element(*UserRegisterLocator.my_account).click()
        self.driver.find_element(*UserRegisterLocator.user_register).click()
        self.driver.find_element(*UserRegisterLocator.first_name).send_keys(register_values["FName"])
        self.driver.find_element(*UserRegisterLocator.last_name).send_keys(register_values["LName"])
        self.driver.find_element(*UserRegisterLocator.email_address).send_keys(register_values["Email"])
        self.driver.find_element(*UserRegisterLocator.customer_company_type).send_keys(register_values["Primarily"])
        self.driver.find_element(*UserRegisterLocator.customer_individual_role).send_keys(register_values["Role"])
        self.driver.find_element(*UserRegisterLocator.screen_name).send_keys(register_values["ScreenName"])
        self.driver.find_element(*UserRegisterLocator.password).send_keys(register_values["Password"])
        self.driver.find_element(*UserRegisterLocator.confirm_password).send_keys(register_values["Password"])
        self.driver.find_element(*UserRegisterLocator.agreement).click()
        print ('email: '+register_values["Email"]+', password: '+register_values["Password"])

    def submit_registeration(self):
        self.driver.find_element(*UserRegisterLocator.submit_data).click()

    def logout_user(self):
        self.driver.find_element(*UserLogout.logout).click()

    def login_user(self,register_values):
        self.driver.find_element(*UserLogin.login_email).send_keys(register_values["Email"])
        self.driver.find_element(*UserLogin.login_password).send_keys(register_values["Password"])
        print('email: ' + register_values["Email"] + ', password: ' + register_values["Password"])
        self.driver.find_element(*UserLogin.login_submit).click()

    def login_verify(self):
        self.displayed=self.driver.find_element(*UserLogout.logout).is_displayed()
        if (self.displayed):
            print("displayed")



