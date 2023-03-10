# coding: utf-8

"""
    交换机管理VLAN配置

    LSW管理VLAN配置北向接口，主要特性：  · 查询交换机管理VLAN配置信息 · 修改交换机管理VLAN配置 

    OpenAPI spec version: 1.1.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import cloudcampus
from cloudcampus.rest import ApiException
from cloudcampus.apis.lsw_mgmt_vlan_northbound_api import LSWMgmtVlanNorthboundApi


class TestLSWMgmtVlanNorthboundApi(unittest.TestCase):
    """ LSWMgmtVlanNorthboundApi unit test stubs """

    def setUp(self):
        self.api = cloudcampus.apis.lsw_mgmt_vlan_northbound_api.LSWMgmtVlanNorthboundApi()

    def tearDown(self):
        pass

    def test_config(self):
        """
        Test case for config

        修改站点内交换机的管理VLAN配置
        """
        pass

    def test_get_config(self):
        """
        Test case for get_config

        获取站点内交换机的管理VLAN配置
        """
        pass


if __name__ == '__main__':
    unittest.main()
