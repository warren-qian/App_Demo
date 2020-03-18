from appium import webdriver
from appium.webdriver.common.mobileby import By


class BasePage(object):
   def __init__(self, driver):
       self.driver =driver

   def open(self, url, dec):
       return self.driver.Remote(url, dec)


   # def find_elm(self, path):
   #     self.driver.






