from selenium import webdriver
import xml.etree.ElementTree as ET

browser = {"Chrome": 'Chrome', "Firefox": 'Firefox'}


def before_all(context):
    current_browser = browser["Chrome"]
    tree = ET.parse('../DataSource/config.xml')
    root = tree.getroot()

    if (current_browser == 'Chrome'):
        for value in root.findall('Browser'):
            _browser = value.find('path').text
            print(_browser)
        # create new chrome session
        context.driver = webdriver.Chrome(_browser)
        context.driver.implicitly_wait(30)
        context.driver.maximize_window()

def after_all(context):
    context.driver.quit()
