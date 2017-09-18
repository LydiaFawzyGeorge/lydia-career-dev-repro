from selenium import webdriver
import unittest
import xml.etree.ElementTree as ET

browser = {"Chrome": 'Chrome', "Firefox": 'Firefox'}


class BaseTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        tree = ET.parse('../DataSource/config.xml')
        root = tree.getroot()

        current_browser = browser["Chrome"]

        if (current_browser == 'Chrome'):
            for value in root.findall('Browser'):
                _browser = value.find('path').text
                print(_browser)
            # create new chrome session
            cls.driver = webdriver.Chrome(_browser)
            cls.driver.implicitly_wait(30)
            cls.driver.maximize_window()
        elif (current_browser == 'Firefox'):
            cls.driver = webdriver.Firefox()
            cls.driver.implicitly_wait(30)

        for value in root.findall('Application'):
            _url = value.find('Url').text
            print(_url)
        # navigate to application home page
        cls.driver.get(_url)
        cls.driver.title

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


