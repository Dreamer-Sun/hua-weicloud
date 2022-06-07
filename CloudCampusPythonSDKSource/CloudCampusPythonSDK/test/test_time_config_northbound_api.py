# coding: utf-8

"""
    时间配置

    时间配置北向接口，主要特性： · 查询时区资源 · 查询时间配置信息（包括时区、夏令时和NTP） · 修改时间配置（包括时区、夏令时和NTP） . 查询站点模板时间配置信息（包括时区、夏令时和NTP） . 修改站点模板时间配置信息（包括时区、夏令时和NTP） 

    OpenAPI spec version: 1.1.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import cloudcampus
from cloudcampus.rest import ApiException
from cloudcampus.apis.time_config_northbound_api import TimeConfigNorthboundApi


class TestTimeConfigNorthboundApi(unittest.TestCase):
    """ TimeConfigNorthboundApi unit test stubs """

    def setUp(self):
        self.api = cloudcampus.apis.time_config_northbound_api.TimeConfigNorthboundApi()

    def tearDown(self):
        pass

    def test_config(self):
        """
        Test case for config

        修改站点内时间配置
        """
        pass

    def test_get_config(self):
        """
        Test case for get_config

        查询站点内时间配置
        """
        pass

    def test_get_site_template_time_config(self):
        """
        Test case for get_site_template_time_config

        查询站点模板时间配置
        """
        pass

    def test_site_template_time_config(self):
        """
        Test case for site_template_time_config

        修改站点模板时间配置
        """
        pass


if __name__ == '__main__':
    unittest.main()
