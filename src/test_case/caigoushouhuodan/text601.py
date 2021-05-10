from src.pages.yidongkucun.caigoushouhuodan import yidongkucun_cgshd_a1_login
from src.common import driver_config
# noinspection PyUnresolvedReferences
from appium.webdriver.common.touch_action import TouchAction
# noinspection PyUnresolvedReferences
import time
import unittest#引用自动化测试框架
# noinspection PyUnresolvedReferences
from appium.webdriver.webdriver import WebDriver


class TestLong1(unittest.TestCase):
    def setUp(self):
        driver = driver_config.Driver_Config()
        self.driver = driver.get_driver()



    def test_case_1(self):
        #引入页面元素
        self.login = yidongkucun_cgshd_a1_login.Login_page(self.driver)

        #点击采购收货，如果不是应用首页，说明环境有问题
        try:
            # 点击应用图标
            self.login.click_cq_yunzhijia_yidongkucun ()
            self.assertEqual (self.login.dy_cq_yunzhijia_yidongkucun, 1, '断言失败，进入移动库存失败')


        except:
            print("请确认环境正确或账号登陆成功")

        #进入采购收单页面
        self.login.click_cgshd_yingyong_tubiao()
        self.assertEqual(self.login.dy_cgshd_yingyong_tubiao, 1, '断言失败，采购收货单点击失败')





    def tearDown(self):
        self.driver.quit()




if __name__ == '__main__':
    unittest.main()