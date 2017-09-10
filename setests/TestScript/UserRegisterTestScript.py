from LocatorsFolder.Locators import UserRegisterLocator
from LocatorsFolder.Locators import UserLogout
from LocatorsFolder.Locators import UserLogin


class UserRegisterScript:

    def new_user_register(self,register_values):
        self.driver.find_element(*UserRegisterLocator._my_account).click()
        self.driver.find_element(*UserRegisterLocator._user_register).click()
        self.driver.find_element(*UserRegisterLocator._first_name).send_keys(register_values["FName"])
        self.driver.find_element(*UserRegisterLocator._last_name).send_keys(register_values["LName"])
        self.driver.find_element(*UserRegisterLocator._email_address).send_keys(register_values["Email"])
        self.driver.find_element(*UserRegisterLocator._customer_company_type).send_keys(register_values["Primarily"])
        self.driver.find_element(*UserRegisterLocator._customer_individual_role).send_keys(register_values["Role"])
        self.driver.find_element(*UserRegisterLocator._screen_name).send_keys(register_values["ScreenName"])
        self.driver.find_element(*UserRegisterLocator._password).send_keys(register_values["Password"])
        self.driver.find_element(*UserRegisterLocator._confirm_password).send_keys(register_values["Password"])
        self.driver.find_element(*UserRegisterLocator._agreement).click()
        print ('email: '+register_values["Email"]+', password: '+register_values["Password"])

    def submit_registeration(self):
        self.driver.find_element(*UserRegisterLocator._submit_data).click()

    def logout_user(self):
        self.driver.find_element(*UserLogout._logout).click()

    def login_user(self,register_values):
        self.driver.find_element(*UserLogin._login_email).send_keys(register_values["Email"])
        self.driver.find_element(*UserLogin._login_password).send_keys(register_values["Password"])
        print('email: ' + register_values["Email"] + ', password: ' + register_values["Password"])
        self.driver.find_element(*UserLogin._login_submit).click()

    def login_verify(self):
        self.displayed=self.driver.find_element(*UserLogout._logout).is_displayed()
        if (self.displayed):
            print("displayed")



