from appium import webdriver
import time
import pytest
from Pageop import BasePage

'''Desired Capability'''

desired_cap = {
  "platformName": "Android",
  "platformVersion": "10",
  "deviceName": "emulator-5554",
  "app": "/Users/warrenq/Downloads/Proxy_Id_Chinese_V2.apk",
  "appActivity": "co.proxy.ui.LauncherActivity",
  "appPackage": "co.proxy"
}

word = {
    "code1": '2222'
}

app = BasePage(webdriver).open("http://localhost:4723/wd/hub", desired_cap)
app.find_element_by_id('co.proxy:id/sign_in').click()

# print(app)
# <Pageop.BasePage object at 0x10def6210>
# appo = app.open(url="http://localhost:4723/wd/hub", des=desired_cap)
# print(appo)
# app.find_elm(path='co.proxy:id/sign_in')
# # Create the driver
# app = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)

# app.find_element_by_id('co.proxy:id/sign_in').click()
# app.wait_activity(1,timeout=3)
# app.find_element_by_id('co.proxy:id/input_email').send_keys('warren.qian@proxy.com')
# app.wait_activity(1,timeout=3)
# app.find_element_by_id('co.proxy:id/done').click()
# app.wait_activity(1,timeout=3)
# app.find_element_by_id('co.proxy:id/input_code').send_keys(*word['code1'])
# app.wait_activity(1,timeout=3)

#resend button
# # app.find_element_by_id('co.proxy:id/resend')

#done button
# app.find_element_by_id('co.proxy:id/done')

