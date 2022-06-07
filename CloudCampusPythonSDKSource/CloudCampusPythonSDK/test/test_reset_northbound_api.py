# coding: utf-8

"""
    设备出厂设置恢复

    设备恢复出厂设置第三方接口。

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import cloudcampus
from cloudcampus.rest import ApiException
from cloudcampus.apis.reset_northbound_api import ResetNorthboundApi


class TestResetNorthboundApi(unittest.TestCase):
    """ ResetNorthboundApi unit test stubs """

    def setUp(self):
        self.api = cloudcampus.apis.reset_northbound_api.ResetNorthboundApi()

    def tearDown(self):
        pass

    def test_reset_device(self):
        """
        Test case for reset_device

        批量恢复设备出厂设置
        """
        pass


if __name__ == '__main__':
    unittest.main()