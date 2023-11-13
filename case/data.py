# -*- coding: utf-8 -*-            
# @Author : ben
# @Time : 2023/11/9 12:06

import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


# 定义Android运行环境
desired_caps = {
    "deviceName": "127.0.0.1:16384",  # 启动的设备
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
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# help(webdriver.Remote)

# 1、使用ID定位（切换tab页）
driver.find_element(AppiumBy.ID,"com.orcbit.oladanceearphone:id/iv_account").click()
time.sleep(5)
# 2、使用ID定位（勾选同意用户协议）
driver.find_element(AppiumBy.ID,"com.orcbit.oladanceearphone:id/iv_agree").click()
time.sleep(5)
# 3、使用ID定位（切换到手机号码登录）
driver.find_element(AppiumBy.ID,"com.orcbit.oladanceearphone:id/tv_login_phone").click()
time.sleep(5)
# 4、使用ID定位（先清除输入栏信息）
driver.find_element(AppiumBy.ID,"com.orcbit.oladanceearphone:id/et_name").clear()
time.sleep(5)
# 5、使用ID定位（输入手机号码登录）
driver.find_element(AppiumBy.ID,"com.orcbit.oladanceearphone:id/et_name").send_keys("13570368266")
time.sleep(5)
# 6、使用ID定位（获取验证码）
driver.find_element(AppiumBy.ID,"com.orcbit.oladanceearphone:id/tv_next").click()
time.sleep(5)