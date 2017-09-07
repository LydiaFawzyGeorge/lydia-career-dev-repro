from Base.BaseTestCase import BaseTestCase
from DataSource.ExcelLib import Data
from ddt import ddt, data, unpack
from DataSource.GenerateData import GenerateMyData
from TestScript.UserRegisterTestScript import UserRegisterScript
import unittest


@ddt
class UserRegister(BaseTestCase):

    _rows = []

    @data(*Data.get_data("../DataSource/DataSource.xlsx"))
    @unpack
    def test_a_register(self,FName,LName,Email,ScreenName,Password,Primarily,Role):

        global _rows
        _rows = GenerateMyData.my_generated_data_to_register(self,FName,LName,Email,ScreenName,Password,Primarily,Role)
        UserRegisterScript.new_user_register(self,_rows)

    def test_b_sumbit_register(self):
        UserRegisterScript.submit_registeration(self)

    def test_c_user_logout(self):
        UserRegisterScript.logout_user(self)

    def test_d_user_login(self):
        UserRegisterScript.login_user(self,_rows)
        UserRegisterScript.login_verify(self)


if __name__ == '__main__':
    unittest.main()







