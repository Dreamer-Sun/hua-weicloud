# coding: utf-8

"""
    用户流量信息查询

    控制器支持查询指定时间内流量和时长发生变化的用户流量信息分页查询北向接口。 

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import cloudcampus
from cloudcampus.rest import ApiException
from cloudcampus.apis.time_flow_st_infos_api import TimeFlowStInfosApi


class TestTimeFlowStInfosApi(unittest.TestCase):
    """ TimeFlowStInfosApi unit test stubs """

    def setUp(self):
        self.api = cloudcampus.apis.time_flow_st_infos_api.TimeFlowStInfosApi()

    def tearDown(self):
        pass

    def test_get_time_flow_st_info_list(self):
        """
        Test case for get_time_flow_st_info_list

        查询用户流量信息
        """
        pass


if __name__ == '__main__':
    unittest.main()
