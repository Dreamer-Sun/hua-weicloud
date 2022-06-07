# coding: utf-8

"""
    License管理

    公有云license管理接口。 场景：对租户license操作的第三方接口。 

    OpenAPI spec version: 1.0.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import cloudcampus
from cloudcampus.rest import ApiException
from cloudcampus.apis.license_service_api import LicenseServiceApi


class TestLicenseServiceApi(unittest.TestCase):
    """ LicenseServiceApi unit test stubs """

    def setUp(self):
        self.api = cloudcampus.apis.license_service_api.LicenseServiceApi()

    def tearDown(self):
        pass

    def test_import_active_code(self):
        """
        Test case for import_active_code

        导入激活码
        """
        pass


if __name__ == '__main__':
    unittest.main()