# -*- coding: utf-8 -*-
# @Author  : Joy
# @FileName: poco_case.py
__author__ = "ZHANG CHUN HE"

from airtest.core.api import *

auto_setup(__file__,devices=["android://127.0.0.1:5037/127.0.0.1:7555"],logdir=True)

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


poco(text="微信").click()
swipe((550,250),(550,1200))
sleep(2.0)
poco("com.tencent.mm:id/f1c").click()
sleep(2.0)
poco(text="搜索商品/运动/款号").click()

wait(Template(r"../images/tpl1659626999336.png", record_pos=(-0.091, -0.779), resolution=(900, 1600)))
text("饮料")