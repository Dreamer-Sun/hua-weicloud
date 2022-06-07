# coding: utf-8

"""
    AP IOT配置

    AP IOT配置北向接口，主要特性： · 查询AP IOT配置信息 · 配置AP IOT信息 

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import cloudcampus
from cloudcampus.rest import ApiException
from cloudcampus.apis.ap_io_t_northbound_api import ApIoTNorthboundApi


class TestApIoTNorthboundApi(unittest.TestCase):
    """ ApIoTNorthboundApi unit test stubs """

    def setUp(self):
        self.api = cloudcampus.apis.ap_io_t_northbound_api.ApIoTNorthboundApi()

    def tearDown(self):
        pass

    def test_config(self):
        """
        Test case for config

        配置站点内AP的IOT配置
        """
        pass

    def test_get_config(self):
        """
        Test case for get_config

        查询站点内AP的IOT配置
        """
        pass


if __name__ == '__main__':
    unittest.main()
