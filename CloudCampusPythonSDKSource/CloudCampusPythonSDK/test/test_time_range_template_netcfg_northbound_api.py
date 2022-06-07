# coding: utf-8

"""
    时间模板管理

    时间模板第三方接口说明。 

    OpenAPI spec version: 1.2.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import cloudcampus
from cloudcampus.rest import ApiException
from cloudcampus.apis.time_range_template_netcfg_northbound_api import TimeRangeTemplateNetcfgNorthboundApi


class TestTimeRangeTemplateNetcfgNorthboundApi(unittest.TestCase):
    """ TimeRangeTemplateNetcfgNorthboundApi unit test stubs """

    def setUp(self):
        self.api = cloudcampus.apis.time_range_template_netcfg_northbound_api.TimeRangeTemplateNetcfgNorthboundApi()

    def tearDown(self):
        pass

    def test_get_time_range_template(self):
        """
        Test case for get_time_range_template

        查询时间段模板
        """
        pass

    def test_modify_time_range_template(self):
        """
        Test case for modify_time_range_template

        修改时间段模板
        """
        pass

    def test_time_rangetemplate_post(self):
        """
        Test case for time_rangetemplate_post

        新增时间段模板
        """
        pass


if __name__ == '__main__':
    unittest.main()
