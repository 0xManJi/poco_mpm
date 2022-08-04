# -*- coding: utf-8 -*-
# @Author  : Joy
# @FileName: poco_case.py
__author__ = "ZHANG CHUN HE"

from airtest.core.api import *

auto_setup(__file__,devices=["android://127.0.0.1:5037/HLRDU19807001907"],logdir=True)

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


start_app("com.tencent.mm")
swipe((550,250),(550,1200))
sleep(2.0)
poco("com.tencent.mm:id/f15").click()

poco(text="搜索商品/运动/款号").click()
