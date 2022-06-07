# coding: utf-8

"""
    WAC关联Fit AP管理

    WAC关联Fit AP第三方接口，主要特性：  · 根据指定的WAC设备ID查询关联的Fit AP列表 · 根据指定的WAC设备关联Fit AP列表 · 根据指定的WAC设备解除关联的Fit AP列表 

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import cloudcampus
from cloudcampus.rest import ApiException
from cloudcampus.apis.wac_fit_northbound_api import WACFitNorthboundApi


class TestWACFitNorthboundApi(unittest.TestCase):
    """ WACFitNorthboundApi unit test stubs """

    def setUp(self):
        self.api = cloudcampus.apis.wac_fit_northbound_api.WACFitNorthboundApi()

    def tearDown(self):
        pass

    def test_add_fit_aps(self):
        """
        Test case for add_fit_aps

        关联指定的WAC设备和Fit AP列表
        """
        pass

    def test_delete_fit_aps(self):
        """
        Test case for delete_fit_aps

        解除关联指定的WAC设备和Fit AP列表
        """
        pass

    def test_get_fit_aps(self):
        """
        Test case for get_fit_aps

        查询指定的WAC设备下关联的Fit AP列表
        """
        pass


if __name__ == '__main__':
    unittest.main()
