# coding: utf-8

"""
    终端客流量数据信息查询

    1、查询设备标签。 2、查询历史客户流量。 3、查询实时客户流量，返回最近5分钟内接入客户流量。 4、查询访客、路人、接入用户的历史趋势。 5、查询访客驻留时长的历史趋势。 6、查询回头客记录。 

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import cloudcampus
from cloudcampus.rest import ApiException
from cloudcampus.models.flow_distr_resp import FlowDistrResp


class TestFlowDistrResp(unittest.TestCase):
    """ FlowDistrResp unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testFlowDistrResp(self):
        """
        Test FlowDistrResp
        """
        # FIXME: construct object with mandatory attributes with example values
        #model = cloudcampus.models.flow_distr_resp.FlowDistrResp()
        pass


if __name__ == '__main__':
    unittest.main()
