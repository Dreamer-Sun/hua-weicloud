# coding: utf-8

"""
    设备基础性能数据信息查询

    · 查询设备网络速率历史数据 · 查询站点维度TopN设备或者全部设备的上行流量、下行流量 · 查询站点维度设备连接终端数历史数据 · 查询单设备连接终端数历史数据 · 查询租户维度下设备状态历史数据 · 查询基于站点的站点健康度和设备健康度 · 查询站点下TOP N SSID流量和最近在线用户数 

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import cloudcampus
from cloudcampus.rest import ApiException
from cloudcampus.models.device_traffic_statistic_resp import DeviceTrafficStatisticResp


class TestDeviceTrafficStatisticResp(unittest.TestCase):
    """ DeviceTrafficStatisticResp unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDeviceTrafficStatisticResp(self):
        """
        Test DeviceTrafficStatisticResp
        """
        # FIXME: construct object with mandatory attributes with example values
        #model = cloudcampus.models.device_traffic_statistic_resp.DeviceTrafficStatisticResp()
        pass


if __name__ == '__main__':
    unittest.main()
