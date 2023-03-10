# coding: utf-8

"""
    AP SSID配置管理

    AP SSID第三方接口。

    OpenAPI spec version: 1.4.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import cloudcampus
from cloudcampus.rest import ApiException
from cloudcampus.apis.apssid_cfg_northbound_api import ApssidCfgNorthboundApi


class TestApssidCfgNorthboundApi(unittest.TestCase):
    """ ApssidCfgNorthboundApi unit test stubs """

    def setUp(self):
        self.api = cloudcampus.apis.apssid_cfg_northbound_api.ApssidCfgNorthboundApi()

    def tearDown(self):
        pass

    def test_create_site_ssid_config(self):
        """
        Test case for create_site_ssid_config

        创建指定站点的SSID配置
        """
        pass

    def test_delete_site_ssid_config(self):
        """
        Test case for delete_site_ssid_config

        删除指定站点的SSID配置
        """
        pass

    def test_get_site_ssid_config(self):
        """
        Test case for get_site_ssid_config

        查询指定站点的SSID配置
        """
        pass

    def test_update_site_ssid_config(self):
        """
        Test case for update_site_ssid_config

        修改指定站点的SSID配置
        """
        pass


if __name__ == '__main__':
    unittest.main()
