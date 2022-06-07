# coding: utf-8

"""
    防火墙特征库升级

    防火墙特征库升级接口 

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import cloudcampus
from cloudcampus.rest import ApiException
from cloudcampus.apis.fw_config_upgrade_policy_api import FwConfigUpgradePolicyApi


class TestFwConfigUpgradePolicyApi(unittest.TestCase):
    """ FwConfigUpgradePolicyApi unit test stubs """

    def setUp(self):
        self.api = cloudcampus.apis.fw_config_upgrade_policy_api.FwConfigUpgradePolicyApi()

    def tearDown(self):
        pass

    def test_config_upgrade_policy(self):
        """
        Test case for config_upgrade_policy

        配置防火墙站点特征库升级策略
        """
        pass

    def test_get_upgrade_policy(self):
        """
        Test case for get_upgrade_policy

        查询防火墙站点特征库升级策略
        """
        pass


if __name__ == '__main__':
    unittest.main()