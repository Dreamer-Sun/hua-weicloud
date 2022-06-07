# coding: utf-8

"""
    上网时长流量策略

    上网时长流量策略编辑查询开放API。 

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import cloudcampus
from cloudcampus.rest import ApiException
from cloudcampus.apis.time_flow_config_api import TimeFlowConfigApi


class TestTimeFlowConfigApi(unittest.TestCase):
    """ TimeFlowConfigApi unit test stubs """

    def setUp(self):
        self.api = cloudcampus.apis.time_flow_config_api.TimeFlowConfigApi()

    def tearDown(self):
        pass

    def test_add_time_flow_config(self):
        """
        Test case for add_time_flow_config

        新增计费策略
        """
        pass

    def test_del_time_flow_config(self):
        """
        Test case for del_time_flow_config

        删除计费策略
        """
        pass

    def test_get_time_flow_config(self):
        """
        Test case for get_time_flow_config

        查询计费策略
        """
        pass

    def test_modify_time_flow_config(self):
        """
        Test case for modify_time_flow_config

        修改计费策略
        """
        pass


if __name__ == '__main__':
    unittest.main()
