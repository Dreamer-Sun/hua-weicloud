# coding: utf-8

"""
    交换机全局VLAN配置

    配置交换机全局VLAN 

    OpenAPI spec version: 1.0.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import cloudcampus
from cloudcampus.rest import ApiException
from cloudcampus.apis.lsw_global_vlan_northbound_api import LSWGlobalVlanNorthboundApi


class TestLSWGlobalVlanNorthboundApi(unittest.TestCase):
    """ LSWGlobalVlanNorthboundApi unit test stubs """

    def setUp(self):
        self.api = cloudcampus.apis.lsw_global_vlan_northbound_api.LSWGlobalVlanNorthboundApi()

    def tearDown(self):
        pass

    def test_create_lsw_global_vlan_info(self):
        """
        Test case for create_lsw_global_vlan_info

        创建交换机的全局VLAN配置
        """
        pass

    def test_delete_lsw_global_vlan_info(self):
        """
        Test case for delete_lsw_global_vlan_info

        删除交换机的全局VLAN配置
        """
        pass

    def test_get_lsw_global_vlan_infos(self):
        """
        Test case for get_lsw_global_vlan_infos

        查询交换机的全局VLAN配置
        """
        pass

    def test_update_lsw_global_vlan_info(self):
        """
        Test case for update_lsw_global_vlan_info

        修改交换机的全局VLAN配置
        """
        pass


if __name__ == '__main__':
    unittest.main()
