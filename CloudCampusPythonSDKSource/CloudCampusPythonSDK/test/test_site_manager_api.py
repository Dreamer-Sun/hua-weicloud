# coding: utf-8

"""
    站点管理

    站点管理第三方接口。 场景：对站点增删改查操作的第三方接口。

    OpenAPI spec version: 1.3.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import cloudcampus
from cloudcampus.rest import ApiException
from cloudcampus.apis.site_manager_api import SiteManagerApi


class TestSiteManagerApi(unittest.TestCase):
    """ SiteManagerApi unit test stubs """

    def setUp(self):
        self.api = cloudcampus.apis.site_manager_api.SiteManagerApi()

    def tearDown(self):
        pass

    def test_create_sites(self):
        """
        Test case for create_sites

        创建站点
        """
        pass

    def test_delete_sites(self):
        """
        Test case for delete_sites

        删除站点
        """
        pass

    def test_query_sites(self):
        """
        Test case for query_sites

        查询站点
        """
        pass

    def test_update_site(self):
        """
        Test case for update_site

        修改站点
        """
        pass


if __name__ == '__main__':
    unittest.main()
