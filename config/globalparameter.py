# coding:utf-8
__author__ = "helen"

'''
description:配置全局参数
'''
import time,os
# 获取当前项目的存放路径
project_path = os.path.abspath(os.path.join(os.path.dirname(os.path.split(os.path.realpath(__file__))[0]), '.'))
# 测试用例代码存放路径（拥有构建suite）
test_case_path_caigourukudan = project_path+"\\src\\test_case\\yidongkucun_case\\caigourukudan"
yidongxiaoshou_path = project_path+"\\src\\test_case\\yidongxiaoshou_case"
# 测试报告的存放路径，并以当前时间作为报告的前缀
report_path = project_path+"\\src\\report\\"
report_name = report_path+time.strftime('%Y-%m-%d_%H_%M_%S_',time.localtime())
# img存放路径
img_path = report_path+"\\img\\"
img_name = img_path+time.strftime('%Y-%m-%d_%H_%M_%S_',time.localtime())+".png"
