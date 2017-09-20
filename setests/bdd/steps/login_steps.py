from behave import *
import xml.etree.ElementTree as ET
from LocatorsFolder.Locators import UserLogin
from LocatorsFolder.Locators import UserLogout


@given('I am on login page')
def step_i_am_on_login_page(context):
    tree = ET.parse('../DataSource/config.xml')
    root = tree.getroot()
    for value in root.findall('Login'):
        _url = value.find('Url').text
    context.driver.get(_url)


@when ('I fill in user email {email}')
def step_i_fill_in_email(context,email):
    email_field=context.driver.find_element(*UserLogin.login_email)
    email_field.send_keys(email)


@when ('I fill in user password {password}')
def step_i_fill_in_password(context,password):
    password_field = context.driver.find_element(*UserLogin.login_password)
    password_field.send_keys(password)


@when ('I press "Login"')
def step_i_press_login(context):
    login_btn = context.driver.find_element(*UserLogin.login_submit)
    login_btn.click()


@then ('I should see "Log Out" button')
def step_i_should_see_logout_btn(context):
    logout_btn=context.driver.find_element(*UserLogout.logout)
    logout_btn.is_displayed()
