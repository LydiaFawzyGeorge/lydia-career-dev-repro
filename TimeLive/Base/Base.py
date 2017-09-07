import unittest
from selenium import webdriver
from DataSource.ReadFile import read_file



driver=webdriver.Chrome("C:/Users/LFawzy/Downloads/chromedriver_win32/chromedriver.exe")
driver.maximize_window()
driver.get("http://timelive.integrantinc.com/")
value_row=read_file.read_csv_file(1)


