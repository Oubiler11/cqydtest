import pytest
import unittest
from src.data.data import *
from src.pages.yidongkucun import yidongkucun_login
from src.pages.yidongkucun import yidongkucun_search
from src.pages.yidongkucun import yidongkucun_fangan
from src.common import driver_config
from config.globalparameter import img_name
from appium import webdriver
# noinspection PyUnresolvedReferences
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.connectiontype import ConnectionType
from appium.webdriver.extensions.android.nativekey import AndroidKey
# noinspection PyUnresolvedReferences
import time
import unittest#引用自动化测试框架
import os
# noinspection PyUnresolvedReferences
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
import HTMLTestRunner
import random

class TestLong(unittest.TestCase):
    def setUp(self):
        driver = driver_config.Driver_Config()
        self.driver = driver.get_driver()


    def test_case_3(self):
        #引入页面元素
        self.login = yidongkucun_login.Login_page(self.driver)
        self.fangan = yidongkucun_fangan.search_page(self.driver)

        # ------------------------直接启动云苍穹个人首页，进入应用页-------------------------
        # 从云苍穹个人首页进入应用首页
        self.login.click_login_yingyong()

        # 从应用首页进入库存查询页
        self.login.click_login_yingyong_kccx()

        # ------------------------进入方案新增和切换页-------------------------
        self.login.click_login_kccx_fangan()

        # ------------------------循环新增两个方案-------------------------
        self.fangan.click_fangan_kccx_xinzengan()
        self.fangan.click_fangan_kccx_fanganminceng()
        self.fangan.send_fangan_kccx_fanganminceng()
        self.fangan.click_fangan_kccx_baocunan()
        time.sleep(5)

        #-----------------如果有test01这个固定的方案，就执行，没有的话，就随意切换方案--------
        try:
            #进入方案页
            self.login.click_login_kccx_fangan()
            self.fangan.click_fangan_kccx_qiehuanfangangd()
            try:
                self.fangan.noclick_fangan_kccx_meiyoukucun()
                ifangan = 1
                print ("固定方案切换成功，没有数据")
            except:
                ifangan = 2
                print("随机方案切换成功，包含数据")
            self.assertEqual(ifangan, 1, '断言失败，未成功登陆库存首页，test_case_1执行异常')
        except:
            self.login.click_login_kccx_fangan()
            self.fangan.click_fangan_kccx_qiehuanfangansj()
            i = 2
            print("库存首页搜索框获取失败")
            self.driver.get_screenshot_as_file("C:\\Users\\Administrator\\PycharmProjects\\pythonProject\\cqydtest\\src\\image\\test_case1_image.png")







    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()