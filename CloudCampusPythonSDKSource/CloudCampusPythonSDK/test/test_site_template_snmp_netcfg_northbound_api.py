# coding: utf-8

"""
    站点模板SNMP配置

    站点模板SNMP配置第三方接口说明。 

    OpenAPI spec version: 1.2.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import cloudcampus
from cloudcampus.rest import ApiException
from cloudcampus.apis.site_template_snmp_netcfg_northbound_api import SiteTemplateSnmpNetcfgNorthboundApi


class TestSiteTemplateSnmpNetcfgNorthboundApi(unittest.TestCase):
    """ SiteTemplateSnmpNetcfgNorthboundApi unit test stubs """

    def setUp(self):
        self.api = cloudcampus.apis.site_template_snmp_netcfg_northbound_api.SiteTemplateSnmpNetcfgNorthboundApi()

    def tearDown(self):
        pass

    def test_get_site_template_snmp(self):
        """
        Test case for get_site_template_snmp

        查询该站点模板SNMP配置信息
        """
        pass

    def test_update_site_template_snmp(self):
        """
        Test case for update_site_template_snmp

        修改该站点模板SNMP配置信息
        """
        pass


if __name__ == '__main__':
    unittest.main()
