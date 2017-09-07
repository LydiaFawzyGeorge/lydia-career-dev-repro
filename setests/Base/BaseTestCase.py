from selenium import webdriver
import unittest


class BaseTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # create new chrome session
        cls.driver = webdriver.Chrome("C:/Users/LFawzy/Downloads/chromedriver_win32/chromedriver.exe")
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

        # navigate to application home page
        cls.driver.get("http://demo.magentocommerce.com/")
        cls.driver.title

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


