# coding: utf-8

"""
    室内地图信息查询

    室内地图第三方北向接口。 · 查询站点中所有楼栋基本信息 · 查询楼栋中所有楼层基本信息 · 查询楼栋中所有楼层详细信息 · 查询楼栋中楼层和设备布放信息 · 查询楼栋中楼层已布放设备详细信息 · 查询楼层已布放设备位置信息 

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import cloudcampus
from cloudcampus.rest import ApiException
from cloudcampus.models.floor_location_details import FloorLocationDetails


class TestFloorLocationDetails(unittest.TestCase):
    """ FloorLocationDetails unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testFloorLocationDetails(self):
        """
        Test FloorLocationDetails
        """
        # FIXME: construct object with mandatory attributes with example values
        #model = cloudcampus.models.floor_location_details.FloorLocationDetails()
        pass


if __name__ == '__main__':
    unittest.main()
