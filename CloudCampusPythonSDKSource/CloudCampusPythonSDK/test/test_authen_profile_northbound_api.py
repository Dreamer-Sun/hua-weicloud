# coding: utf-8

"""
    认证模板管理

    认证模板北向接口定义 

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import cloudcampus
from cloudcampus.rest import ApiException
from cloudcampus.apis.authen_profile_northbound_api import AuthenProfileNorthboundApi


class TestAuthenProfileNorthboundApi(unittest.TestCase):
    """ AuthenProfileNorthboundApi unit test stubs """

    def setUp(self):
        self.api = cloudcampus.apis.authen_profile_northbound_api.AuthenProfileNorthboundApi()

    def tearDown(self):
        pass

    def test_create_authen_profile(self):
        """
        Test case for create_authen_profile

        创建认证模板
        """
        pass

    def test_delete_authen_profile(self):
        """
        Test case for delete_authen_profile

        删除认证模板
        """
        pass

    def test_get_authen_profile(self):
        """
        Test case for get_authen_profile

        查询认证模板
        """
        pass

    def test_get_authen_profile_by_id(self):
        """
        Test case for get_authen_profile_by_id

        根据ID查询认证模板
        """
        pass

    def test_update_authen_profile(self):
        """
        Test case for update_authen_profile

        更新认证模板
        """
        pass


if __name__ == '__main__':
    unittest.main()