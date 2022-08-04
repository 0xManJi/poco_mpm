# -*- coding: utf-8 -*-
# @Author  : Joy
# @FileName: air_case.py


# -*- encoding=utf8 -*-
__author__ = "ZHANG CHUN HE"

from airtest.core.api import *
from airtest.report.report import *
ST.FIND_TIMEOUT = 60
auto_setup(__file__,devices=["android://127.0.0.1:5037/HLRDU19807001907"],logdir="C:\\Users\Joy\Desktop\poco_mpm\log")

import os
print(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))


def buy_case():

    swipe(Template(r"../images/tpl1659532528881.png", record_pos=(-0.217, -0.8), resolution=(1080, 2340)), vector=[0.2263, 0.293])
    touch(Template(r"../images/tpl1659532550846.png", record_pos=(-0.34, -0.497), resolution=(1080, 2340)))
    touch(Template(r"../images/tpl1659532562928.png", record_pos=(-0.066, -0.812), resolution=(1080, 2340)))
    touch(Template(r"../images/tpl1659532619490.png", record_pos=(-0.084, -0.949), resolution=(1080, 2340)))
    sleep(1)
    text("饮料")
    touch(Template(r"../images/tpl1659532655386.png", record_pos=(-0.318, -0.342), resolution=(1080, 2340)))

    touch(Template(r"../images/tpl1659532667715.png", record_pos=(0.326, 0.981), resolution=(1080, 2340)))
    touch(Template(r"../images/tpl1659532674656.png", record_pos=(0.002, 0.981), resolution=(1080, 2340)))
    wait(Template(r"../images/tpl1659533785527.png", record_pos=(0.295, 0.994), resolution=(1080, 2340)))

    touch(Template(r"../images/tpl1659532691281.png", record_pos=(0.297, 0.994), resolution=(1080, 2340)))

    sleep(2)

    touch(Template(r"../images/tpl1659532723585.png", record_pos=(-0.429, -0.182), resolution=(1080, 2340)))
    sleep(2)
    touch(Template(r"../images/tpl1659532736225.png", record_pos=(-0.429, -0.923), resolution=(1080, 2340)))
    wait(Template(r"../images/tpl1659534014647.png", record_pos=(0.362, 1.007), resolution=(1080, 2340)))

    touch(Template(r"../images/tpl1659532745510.png", record_pos=(0.367, 1.005), resolution=(1080, 2340)))
    touch(Template(r"../images/tpl1659532752705.png", record_pos=(0.377, 0.094), resolution=(1080, 2340)))



if __name__ == '__main__':
    buy_case()

    simple_report(__file__, logpath="C:\\Users\Joy\Desktop\poco_mpm\log",output="C:\\Users\Joy\Desktop\poco_mpm\log\log.html")


