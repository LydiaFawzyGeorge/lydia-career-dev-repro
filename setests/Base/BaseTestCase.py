from selenium import webdriver
import unittest


browser = {"Chrome": 'Chrome', "Firefox": 'Firefox'}


class BaseTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        current_browser = browser["Chrome"]

        if (current_browser == 'Chrome'):

            # create new chrome session
            cls.driver = webdriver.Chrome("../Resources/chromedriver.exe")
            cls.driver.implicitly_wait(30)
            cls.driver.maximize_window()
        elif (current_browser == 'Firefox'):
            cls.driver = webdriver.Firefox()
            cls.driver.implicitly_wait(30)




        # navigate to application home page
        cls.driver.get("http://demo.magentocommerce.com/")
        cls.driver.title

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


