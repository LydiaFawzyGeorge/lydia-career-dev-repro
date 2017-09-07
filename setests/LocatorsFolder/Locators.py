from selenium.webdriver.common.by import By


class UserRegisterLocator:
    _my_account = (By.LINK_TEXT,'MY ACCOUNT')
    _user_register = (By.XPATH,'//*[@id="login-form"]/div/div/div[2]/div/button')
    _first_name = (By.ID,'firstname')
    _last_name = (By.ID,'lastname')
    _email_address = (By.ID,'email_address')
    _customer_company_type = (By.ID,'customer_company_type')
    _customer_individual_role = (By.ID,'customer_individual_role')
    _screen_name = (By.ID,'screen_name')
    _password = (By.ID,'password')
    _confirm_password = (By.ID,'confirmation')
    _agreement = (By.ID,'agree_terms')
    _submit_data = (By.ID,'registerSubmit')


class UserLogout:
    _logout = (By.LINK_TEXT,'Log Out')


class UserLogin:
    _login_email = (By.ID,'email')
    _login_password = (By.ID,'pass')
    _login_submit = (By.ID,'send2')
