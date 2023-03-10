# coding: utf-8

"""
    站点内AP设备Nat日志上报开关

    · 查询站点内AP设备Nat日志上报配置 · 配置站点内AP设备Nat日志上报信息 

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import cloudcampus
from cloudcampus.rest import ApiException
from cloudcampus.apis.nat_session_log_service_api import NatSessionLogServiceApi


class TestNatSessionLogServiceApi(unittest.TestCase):
    """ NatSessionLogServiceApi unit test stubs """

    def setUp(self):
        self.api = cloudcampus.apis.nat_session_log_service_api.NatSessionLogServiceApi()

    def tearDown(self):
        pass

    def test_configap_nat_session_log(self):
        """
        Test case for configap_nat_session_log

        配置站点内AP设备Nat日志上报信息
        """
        pass

    def test_get_ap_nat_session_log_config(self):
        """
        Test case for get_ap_nat_session_log_config

        查询站点内AP设备Nat日志上报配置
        """
        pass


if __name__ == '__main__':
    unittest.main()
