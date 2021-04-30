from src.pages.yidongkucun.caigourukudan import yidongkucun_a3_sousuo_yishenhe, yidongkucun_a2_search, \
    yidongkucun_a1_login,yidongkucun_cgrkd_a4_shouye_neirong
from src.common import driver_config
# noinspection PyUnresolvedReferences
from appium.webdriver.common.touch_action import TouchAction
# noinspection PyUnresolvedReferences
import time
import unittest#引用自动化测试框架
# noinspection PyUnresolvedReferences
from appium.webdriver.webdriver import WebDriver


class TestLong4(unittest.TestCase):
    def setUp(self):
        driver = driver_config.Driver_Config()
        self.driver = driver.get_driver()


    def test_case_4(self):
        #引入页面元素
        self.login = yidongkucun_a1_login.Login_page(self.driver)

        #------------------------搜狗浏览器，进入库存查询页-------------------------
        #点击移动库存，如果不是应用首页，说明环境有问题
        try:
            # 再次点击搜狗浏览器的二次栏
            self.login.click_cq_yunzhijia_yidongkucun ()
            self.assertEqual(self.login.dy_cq_yunzhijia_yidongkucun, 1, '断言失败，进入移动库存失败')


        except:
            print("请确认环境正确或账号登陆成功")

        #输入采购入库单页面
        self.login.click_cq_yunzhijia_caigouruku()
        self.assertEqual(self.login.dy_cq_yunzhijia_caigouruku, 1, '断言失败，采购入库点击失败')


        #引入search的页面元素
        self.search = yidongkucun_a2_search.search_page(self.driver)
        self.buxian = yidongkucun_a3_sousuo_yishenhe.buxian_page(self.driver)

        #点击业务日期
        self.buxian.click_cgrk_shouye_yewuriqi()
        self.assertEqual(self.buxian.dy_cgrk_shouye_yewuriqi, 1, '断言失败，不限下拉菜单点击失败')

        #点击业务日期下拉菜单的不限
        self.buxian.click_cgrk_shouye_yewuriqi_buxian()
        self.assertEqual(self.buxian.dy_cgrk_shouye_yewuriqi_buxian, 1, '断言失败，不限下拉菜单点击失败')

        #引入a4内容页
        self.neirong = yidongkucun_cgrkd_a4_shouye_neirong.neirong_page(self.driver)

        #点击订单内容
        self.neirong.click_cgrk_shouye_dingdan_neirong()
        self.assertEqual(self.neirong.dy_cgrk_shouye_dingdan_neirong,1, '断言失败，订单内容点击失败')


        #---------判断用例是否成功---------#
        #查找暂存按钮
        self.login.noclick_cgrk_yingyong_zancuntubiao()
        #如果查找成功，判断为成功
        if self.login.dy_no_cgrk_yingyong_zancuntubiao == 1:
            print("test_case4:pass")
        #如果查询不成功，判断为失败
        else:
            self.assertEqual(self.login.dy_no_cgrk_yingyong_zancuntubiao, 1, '断言失败，test_case_4执行失败！')


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()