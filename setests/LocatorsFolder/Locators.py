from selenium.webdriver.common.by import By


class UserRegisterLocator:
    my_account = (By.LINK_TEXT,'MY ACCOUNT')
    user_register = (By.XPATH,'//*[@id="login-form"]/div/div/div[2]/div/button')
    first_name = (By.ID,'firstname')
    last_name = (By.ID,'lastname')
    email_address = (By.ID,'email_address')
    customer_company_type = (By.ID,'customer_company_type')
    customer_individual_role = (By.ID,'customer_individual_role')
    screen_name = (By.ID,'screen_name')
    password = (By.ID,'password')
    confirm_password = (By.ID,'confirmation')
    agreement = (By.ID,'agree_terms')
    submit_data = (By.ID,'registerSubmit')


class UserLogout:
    logout = (By.LINK_TEXT,'Log Out')


class UserLogin:
    login_email = (By.ID,'email')
    login_password = (By.ID,'pass')
    login_submit = (By.ID,'send2')
