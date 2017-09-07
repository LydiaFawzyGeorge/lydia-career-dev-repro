import unittest
import sys
from selenium import webdriver
# save time, then login again and make sure that data saved correctly
driver = webdriver.Chrome("C:/Users/LFawzy/Downloads/chromedriver_win32/chromedriver.exe")
driver.implicitly_wait(30)
driver.maximize_window()
    # navigate to the application home page driver.get("http://demo.magentocommerce.com/")
driver.get("http://timelive.integrantinc.com/")
#get user name element
user_name=driver.find_element_by_id("CtlLogin1_Login1_UserName")
user_name.send_keys("lfawzy@integrant.com")

def read_data_from_file():

    file=open("LoginData","r")
    data_file=file.read()
    file.close()
    new_file=str(data_file)
    return new_file

password=driver.find_element_by_id("CtlLogin1_Login1_Password")
password.send_keys(read_data_from_file())
btn_go=driver.find_element_by_id("CtlLogin1_Login1_LoginButton")
btn_go.click()

