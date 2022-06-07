# coding: utf-8

"""
    运维ping/trace探测

    ping/trace探测第三方接口。 · 创建ping探测任务 · 查询ping探测结果 · 创建trace探测任务 · 查询trace探测结果 

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import cloudcampus
from cloudcampus.rest import ApiException
from cloudcampus.apis.ping_diagnose_service_api import PingDiagnoseServiceApi


class TestPingDiagnoseServiceApi(unittest.TestCase):
    """ PingDiagnoseServiceApi unit test stubs """

    def setUp(self):
        self.api = cloudcampus.apis.ping_diagnose_service_api.PingDiagnoseServiceApi()

    def tearDown(self):
        pass

    def test_create_ping_task(self):
        """
        Test case for create_ping_task

        创建ping探测任务
        """
        pass

    def test_query_ping_task_by_task_id(self):
        """
        Test case for query_ping_task_by_task_id

        查询ping探测结果
        """
        pass


if __name__ == '__main__':
    unittest.main()
