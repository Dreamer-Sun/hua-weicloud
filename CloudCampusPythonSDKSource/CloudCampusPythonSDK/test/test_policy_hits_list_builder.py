# coding: utf-8

"""
    CIS服务接口

    CIS操作接口说明： 1、创建CIS隔离 2、创建CIS阻断 3、撤销CIS阻断/隔离 4、阻断隔离应用状态查询 5、CIS策略命中率查询 

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import cloudcampus
from cloudcampus.rest import ApiException
from cloudcampus.models.policy_hits_list_builder import PolicyHitsListBuilder


class TestPolicyHitsListBuilder(unittest.TestCase):
    """ PolicyHitsListBuilder unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPolicyHitsListBuilder(self):
        """
        Test PolicyHitsListBuilder
        """
        # FIXME: construct object with mandatory attributes with example values
        #model = cloudcampus.models.policy_hits_list_builder.PolicyHitsListBuilder()
        pass


if __name__ == '__main__':
    unittest.main()
