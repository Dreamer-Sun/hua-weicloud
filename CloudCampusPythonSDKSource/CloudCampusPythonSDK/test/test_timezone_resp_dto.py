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
from cloudcampus.models.timezone_resp_dto import TimezoneRespDto


class TestTimezoneRespDto(unittest.TestCase):
    """ TimezoneRespDto unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTimezoneRespDto(self):
        """
        Test TimezoneRespDto
        """
        # FIXME: construct object with mandatory attributes with example values
        #model = cloudcampus.models.timezone_resp_dto.TimezoneRespDto()
        pass


if __name__ == '__main__':
    unittest.main()
