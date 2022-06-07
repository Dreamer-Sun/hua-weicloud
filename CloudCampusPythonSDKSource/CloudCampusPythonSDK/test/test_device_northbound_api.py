# coding: utf-8

"""
    设备基本信息管理

    设备相关操作接口。 场景：对设备增删改查操作的第三方接口。

    OpenAPI spec version: 1.6.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import cloudcampus
from cloudcampus.rest import ApiException
from cloudcampus.apis.device_northbound_api import DeviceNorthboundApi


class TestDeviceNorthboundApi(unittest.TestCase):
    """ DeviceNorthboundApi unit test stubs """

    def setUp(self):
        self.api = cloudcampus.apis.device_northbound_api.DeviceNorthboundApi()

    def tearDown(self):
        pass

    def test_batch_modify_devices(self):
        """
        Test case for batch_modify_devices

        批量修改设备
        """
        pass

    def test_create_devices(self):
        """
        Test case for create_devices

        创建设备
        """
        pass

    def test_delete_devices(self):
        """
        Test case for delete_devices

        删除设备
        """
        pass

    def test_get_device_models(self):
        """
        Test case for get_device_models

        查询设备款型
        """
        pass

    def test_get_site_device(self):
        """
        Test case for get_site_device

        查询设备
        """
        pass

    def test_modify_devices(self):
        """
        Test case for modify_devices

        修改设备
        """
        pass

    def test_replace_device(self):
        """
        Test case for replace_device

        替换设备
        """
        pass

    def test_replace_original_device(self):
        """
        Test case for replace_original_device

        替换设备款型
        """
        pass


if __name__ == '__main__':
    unittest.main()
