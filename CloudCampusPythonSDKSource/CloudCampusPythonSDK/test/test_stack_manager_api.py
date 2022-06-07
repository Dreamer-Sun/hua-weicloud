# coding: utf-8

"""
    堆叠管理

    堆叠管理第三方接口。 场景：创建堆叠操作的第三方接口。

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import cloudcampus
from cloudcampus.rest import ApiException
from cloudcampus.apis.stack_manager_api import StackManagerApi


class TestStackManagerApi(unittest.TestCase):
    """ StackManagerApi unit test stubs """

    def setUp(self):
        self.api = cloudcampus.apis.stack_manager_api.StackManagerApi()

    def tearDown(self):
        pass

    def test_create_stack(self):
        """
        Test case for create_stack

        添加指定ESN设备到指定堆叠
        """
        pass


if __name__ == '__main__':
    unittest.main()
