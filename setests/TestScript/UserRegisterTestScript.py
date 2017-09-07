from LocatorsFolder.Locators import UserRegisterLocator
from LocatorsFolder.Locators import UserLogout
from LocatorsFolder.Locators import UserLogin


class UserRegisterScript:

    def new_user_register(self,rows):
        self.driver.find_element(*UserRegisterLocator._my_account).click()
        self.driver.find_element(*UserRegisterLocator._user_register).click()
        self.driver.find_element(*UserRegisterLocator._first_name).send_keys(rows[0])
        self.driver.find_element(*UserRegisterLocator._last_name).send_keys(rows[1])
        self.driver.find_element(*UserRegisterLocator._email_address).send_keys(rows[2])
        self.driver.find_element(*UserRegisterLocator._customer_company_type).send_keys(rows[5])
        self.driver.find_element(*UserRegisterLocator._customer_individual_role).send_keys(rows[6])
        self.driver.find_element(*UserRegisterLocator._screen_name).send_keys(rows[3])
        self.driver.find_element(*UserRegisterLocator._password).send_keys(rows[4])
        self.driver.find_element(*UserRegisterLocator._confirm_password).send_keys(rows[4])
        self.driver.find_element(*UserRegisterLocator._agreement).click()
        print ('email: '+rows[2]+', password: '+rows[4])

    def submit_registeration(self):
        self.driver.find_element(*UserRegisterLocator._submit_data).click()

    def logout_user(self):
        self.driver.find_element(*UserLogout._logout).click()

    def login_user(self,rows):
        self.driver.find_element(*UserLogin._login_email).send_keys(rows[2])
        self.driver.find_element(*UserLogin._login_password).send_keys(rows[4])
        print('email: ' + rows[2] + ', password: ' + rows[4])
        self.driver.find_element(*UserLogin._login_submit).click()

    def login_verify(self):
        self.displayed=self.driver.find_element(*UserLogout._logout).is_displayed()
        if (self.displayed):
            print("displayed")



