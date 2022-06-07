# coding: utf-8

"""
    租户管理

    租户管理第三方北向接口。 · 提供租户创建接口 · 提供租户删除接口 · 提供租户查询接口 

    OpenAPI spec version: 1.0.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import cloudcampus
from cloudcampus.rest import ApiException
from cloudcampus.apis.tenant_service_api import TenantServiceApi


class TestTenantServiceApi(unittest.TestCase):
    """ TenantServiceApi unit test stubs """

    def setUp(self):
        self.api = cloudcampus.apis.tenant_service_api.TenantServiceApi()

    def tearDown(self):
        pass

    def test_create_softcom_tenant(self):
        """
        Test case for create_softcom_tenant

        创建租户
        """
        pass

    def test_delete_softcom_tenant(self):
        """
        Test case for delete_softcom_tenant

        删除租户
        """
        pass

    def test_query_softcom_tenants(self):
        """
        Test case for query_softcom_tenants

        查询租户
        """
        pass


if __name__ == '__main__':
    unittest.main()
