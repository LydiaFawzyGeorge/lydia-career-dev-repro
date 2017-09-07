from Base import Base

class Login(Base.BaseTestCase):



    def UserLogin(self,UserName,Password):
        user_name = self.find_element_by_id("CtlLogin1_Login1_UserName")
        user_name.send_keys("lfawzy@integrant.com")
        password = self.find_element_by_id("CtlLogin1_Login1_Password")
       # password.send_keys(read_data_from_file())
        btn_go = self.find_element_by_id("CtlLogin1_Login1_LoginButton")
        btn_go.click()

