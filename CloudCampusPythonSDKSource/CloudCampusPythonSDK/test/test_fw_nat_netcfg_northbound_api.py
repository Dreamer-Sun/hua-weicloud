# coding: utf-8

"""
    防火墙设备NAT配置

    防火墙设备NAT配置第三方接口。

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import cloudcampus
from cloudcampus.rest import ApiException
from cloudcampus.apis.fw_nat_netcfg_northbound_api import FwNatNetcfgNorthboundApi


class TestFwNatNetcfgNorthboundApi(unittest.TestCase):
    """ FwNatNetcfgNorthboundApi unit test stubs """

    def setUp(self):
        self.api = cloudcampus.apis.fw_nat_netcfg_northbound_api.FwNatNetcfgNorthboundApi()

    def tearDown(self):
        pass

    def test_create_device_fw_nat_config(self):
        """
        Test case for create_device_fw_nat_config

        创建防火墙设备NAT配置
        """
        pass

    def test_delete_device_fw_nat_config(self):
        """
        Test case for delete_device_fw_nat_config

        删除防火墙设备NAT配置
        """
        pass

    def test_get_device_fw_nat_config(self):
        """
        Test case for get_device_fw_nat_config

        查询防火墙设备NAT配置
        """
        pass

    def test_update_device_fw_nat_config(self):
        """
        Test case for update_device_fw_nat_config

        修改防火墙设备NAT配置
        """
        pass


if __name__ == '__main__':
    unittest.main()
