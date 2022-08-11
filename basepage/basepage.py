# -*- coding: utf-8 -*-
# @Author  : Joy
# @FileName: basepage.py
from airtest.core.api import *

auto_setup(__file__, devices=["android://127.0.0.1:5037/127.0.0.1:7555"], logdir=True)

from poco.drivers.android.uiautomation import AndroidUiautomationPoco


class MainPage():
    poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

    def Start_app(self):
        auto_setup(__file__, devices=["android://127.0.0.1:5037/127.0.0.1:7555"], logdir=True)
        self.poco(text="微信").click()
        swipe((550, 250), (550, 1200))
        sleep(2.0)
        self.poco("com.tencent.mm:id/f1c").click()
