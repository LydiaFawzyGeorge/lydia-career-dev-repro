from Base.BaseTestCase import BaseTestCase

from DataSource.GenerateData import GenerateMyData
from TestScript.UserRegisterTestScript import UserRegisterScript
import unittest
from DataSource.DataSource_1 import JsonData



class UserRegister(BaseTestCase):

    _rows = []
    def test_a_register(self):
        data= JsonData.json_data(self)
        FName= data["FName"]
        LName= data["LName"]
        Email= data["Email"]
        ScreenName= data["ScreenName"]
        Password= data["Password"]
        Primarily= data["Primarily"]
        Role= data["Role"]
        global register_values
        register_values = GenerateMyData.my_generated_data_to_register(self,FName,LName,Email,ScreenName,Password,Primarily,Role)
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







