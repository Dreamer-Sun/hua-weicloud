# coding: utf-8

"""
    AP页面推送策略

    AP页面推送策略开放API。 

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import cloudcampus
from cloudcampus.rest import ApiException
from cloudcampus.apis.portalpagerule_cfg_northbound_api import PortalpageruleCfgNorthboundApi


class TestPortalpageruleCfgNorthboundApi(unittest.TestCase):
    """ PortalpageruleCfgNorthboundApi unit test stubs """

    def setUp(self):
        self.api = cloudcampus.apis.portalpagerule_cfg_northbound_api.PortalpageruleCfgNorthboundApi()

    def tearDown(self):
        pass

    def test_add_portal_page_rule(self):
        """
        Test case for add_portal_page_rule

        创建页面推送策略
        """
        pass

    def test_delete_portal_page_rule(self):
        """
        Test case for delete_portal_page_rule

        删除页面推送策略
        """
        pass

    def test_get_portal_page_rule(self):
        """
        Test case for get_portal_page_rule

        查询页面推送策略
        """
        pass

    def test_update_portal_page_rule(self):
        """
        Test case for update_portal_page_rule

        修改页面推送策略
        """
        pass


if __name__ == '__main__':
    unittest.main()
