# coding: utf-8

"""
    单板管理

    单板管理第三方接口。

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import cloudcampus
from cloudcampus.rest import ApiException
from cloudcampus.apis.board_netcfg_northbound_api import BoardNetcfgNorthboundApi


class TestBoardNetcfgNorthboundApi(unittest.TestCase):
    """ BoardNetcfgNorthboundApi unit test stubs """

    def setUp(self):
        self.api = cloudcampus.apis.board_netcfg_northbound_api.BoardNetcfgNorthboundApi()

    def tearDown(self):
        pass

    def test_create_device_board_config(self):
        """
        Test case for create_device_board_config

        添加单板配置
        """
        pass

    def test_delete_device_board_config(self):
        """
        Test case for delete_device_board_config

        删除单板配置
        """
        pass

    def test_get_device_board_config(self):
        """
        Test case for get_device_board_config

        查询单板配置
        """
        pass


if __name__ == '__main__':
    unittest.main()