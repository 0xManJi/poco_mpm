# -*- coding: utf-8 -*-
# @Author  : Joy
# @FileName: test_home_page.py


from basepage.basepage import MainPage
from airtest.core.api import *

class TestHomePage():
    def setup_class(self):
        self.main_page = MainPage().Start_app()
    def test_home_page(self):
        pass

if __name__ == '__main__':
    TestHomePage().setup_class()