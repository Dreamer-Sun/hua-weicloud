# coding: utf-8

"""
    AP站点射频配置

    AP站点射频配置第三方接口说明。 

    OpenAPI spec version: 1.1.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import cloudcampus
from cloudcampus.rest import ApiException
from cloudcampus.apis.groupradio_cfg_northbound_api import GroupradioCfgNorthboundApi


class TestGroupradioCfgNorthboundApi(unittest.TestCase):
    """ GroupradioCfgNorthboundApi unit test stubs """

    def setUp(self):
        self.api = cloudcampus.apis.groupradio_cfg_northbound_api.GroupradioCfgNorthboundApi()

    def tearDown(self):
        pass

    def test_get_all_device_radio_config(self):
        """
        Test case for get_all_device_radio_config

        查询站点下所有AP设备射频配置信息
        """
        pass

    def test_get_group_radio_config(self):
        """
        Test case for get_group_radio_config

        查询AP站点射频配置信息
        """
        pass

    def test_update_group_radio_config(self):
        """
        Test case for update_group_radio_config

        修改AP站点射频配置信息
        """
        pass


if __name__ == '__main__':
    unittest.main()
