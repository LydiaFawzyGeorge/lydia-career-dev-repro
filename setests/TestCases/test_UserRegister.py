from Base.BaseTestCase import BaseTestCase

from DataSource.GenerateData import GenerateMyData
from TestScript.UserRegisterTestScript import UserRegisterScript
import unittest
from DataSource.DataSource_1 import JsonData



class UserRegister(BaseTestCase):

    _rows = []
    def test_a_register(self):
        data= JsonData.json_data(self)
        first_name= data["FName"]
        last_name= data["LName"]
        email= data["Email"]
        screen_name= data["ScreenName"]
        password= data["Password"]
        primarily= data["Primarily"]
        role= data["Role"]
        global register_values
        register_values = GenerateMyData.my_generated_data_to_register(self,first_name,last_name,email,screen_name,password,primarily,role)
        UserRegisterScript.new_user_register(self,register_values)

    def test_b_sumbit_register(self):
        UserRegisterScript.submit_registeration(self)

    def test_c_user_logout(self):
        UserRegisterScript.logout_user(self)

    def test_d_user_login(self):
        UserRegisterScript.login_user(self,register_values)
        UserRegisterScript.login_verify(self)


if __name__ == '__main__':
    unittest.main()







