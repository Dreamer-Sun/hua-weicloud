# coding: utf-8

"""
    交换机STP配置

    LSW STP配置北向接口，主要特性： · 查询交换STP配置信息 · 修改交换机STP配置 · 删除交换机STP配置 

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import cloudcampus
from cloudcampus.rest import ApiException
from cloudcampus.apis.lsw_stp_northbound_api import LSWStpNorthboundApi


class TestLSWStpNorthboundApi(unittest.TestCase):
    """ LSWStpNorthboundApi unit test stubs """

    def setUp(self):
        self.api = cloudcampus.apis.lsw_stp_northbound_api.LSWStpNorthboundApi()

    def tearDown(self):
        pass

    def test_config(self):
        """
        Test case for config

        全量修改站点内交换机的STP配置
        """
        pass

    def test_delete(self):
        """
        Test case for delete

        删除站点内交换机的STP配置
        """
        pass

    def test_get_config(self):
        """
        Test case for get_config

        查询站点内交换机的STP配置
        """
        pass

    def test_incre_config(self):
        """
        Test case for incre_config

        增量修改站点内交换机的STP配置
        """
        pass


if __name__ == '__main__':
    unittest.main()
