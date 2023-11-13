# -*- coding: utf-8 -*-            
# @Author : ben
# @Time : 2023/11/9 12:06

import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from case.verification_code import get_verification_code, b


# 定义Android运行环境
class App_config:
    def setup(self):
        desired_caps = {
            "deviceName": "4fb5de03",  # 启动的设备
            "automationName": "Appium",  # 使用的自动化引擎，如appium（默认）或Selendroid
            "platformName": "Android",  # 使用的移动平台，如Android或IOs
            # adb shell getprop ro.build.version.release，获取设备Android系统版本（即platformVersion）
            "platformVersion": "10",  # 指定的平台的系统版本，这里为安卓平台，12
            # dumpsys window | grep mCurrentFocus
            "appPackage": "com.orcbit.oladanceearphone",  # 被测试App的Package名
            "appActivity": ".ui.activity.MainActivity",  # 被测试App的Activity名
            "unicodeKeyboard": True,  # 设置中文键盘
            "resetKeyboard": True,  # 重置自动化时设置的键盘
        }

        # desired_caps={}
        # desired_caps['deviceName']:'NDPBB23129202538'
        # desired_caps['automationName']: 'Appium'
        # desired_caps['platformName']: 'Android'
        # desired_caps['platformVersion']: '10'
        # desired_caps['appPackage']: 'com.orcbit.oladanceearphone'
        # desired_caps['appActivity']: ".ui.activity.MainActivity"
        # desired_caps['unicodeKeyboard']: 'True'
        # desired_caps['resetKeyboard']: 'True'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    def teardown(self):
     # 回收session
       self.driver.quit()
    def test_api_demo(self):
       self.driver.implicitly_wait(5)
# 1、使用ID定位（切换tab页）
       self.driver.find_element(AppiumBy.ID,"com.orcbit.oladanceearphone:id/iv_account").click()

# 2、使用ID定位（勾选同意用户协议）
       self.driver.find_element(AppiumBy.ID,"com.orcbit.oladanceearphone:id/iv_agree").click()
# 3、使用ID定位（切换到手机号码登录）
       self.driver.find_element(AppiumBy.ID,"com.orcbit.oladanceearphone:id/tv_login_phone").click()

       time.sleep(5)

# 4、使用ID定位（先清除输入栏信息）
       self.driver.find_element(AppiumBy.ID,"com.orcbit.oladanceearphone:id/et_name").clear()

# 5、使用ID定位（输入手机号码登录）
       self.driver.find_element(AppiumBy.ID,"com.orcbit.oladanceearphone:id/et_name").send_keys("13570368266")

# 6、使用ID定位（获取验证码）
       self.driver.find_element(AppiumBy.ID,"com.orcbit.oladanceearphone:id/tv_next").click()
#
#        time.sleep(5)
# implicitly_wait()是由webdriver提供的隐式等待方法，它不是针对某一个元素，
# 而是针对当前session（即当前driver对象的生命周期）的全部元素，所以只需要在构造driver对象时设置一次即可。
# 隐式等待在定位元素时，需等待该页面全部元素加载完成，才会执行下一步操作（即下一条语句），如果超过设定时间未加载完成则抛出异常。
#        self.driver.find_element(AppiumBy.XPATH,
#        "//android.widget.LinearLayout[@resource-id='com.orcbit.oladanceearphone:id/vg_code']/android.widget.TextView[1]").click()
#        element = self.driver.find_element(AppiumBy.XPATH, "//android.widget.LinearLayout[@resource-id='com.orcbit.oladanceearphone:id/vg_code']/android.widget.TextView[1]")
#        if element.is_enabled():
#            element.click()
#            print('元素可点击')
#        else:
#            print("元素不可交互")
       # self.driver.find_element(AppiumBy.XPATH,
       # "//android.widget.LinearLayout[@resource-id='com.orcbit.oladanceearphone:id/vg_code']/android.widget.TextView[1]").\
       #     send_keys(b[0],b[1],b[2],b[3])







print("执行完毕")
