# coding: utf-8

"""
    站点模板管理

    站点模板第三方接口说明。 

    OpenAPI spec version: 1.2.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import cloudcampus
from cloudcampus.rest import ApiException
from cloudcampus.apis.site_template_northbound_api import SiteTemplateNorthboundApi


class TestSiteTemplateNorthboundApi(unittest.TestCase):
    """ SiteTemplateNorthboundApi unit test stubs """

    def setUp(self):
        self.api = cloudcampus.apis.site_template_northbound_api.SiteTemplateNorthboundApi()

    def tearDown(self):
        pass

    def test_add_site_template(self):
        """
        Test case for add_site_template

        创建站点模板
        """
        pass

    def test_bind_site_template(self):
        """
        Test case for bind_site_template

        绑定一个或多个站点到站点模板
        """
        pass

    def test_delete_site_templates(self):
        """
        Test case for delete_site_templates

        删除站点模板
        """
        pass

    def test_get_binding_site_list(self):
        """
        Test case for get_binding_site_list

        根据站点模板ID查询绑定的站点
        """
        pass

    def test_get_binding_site_template(self):
        """
        Test case for get_binding_site_template

        根据站点ID查询绑定的站点模板
        """
        pass

    def test_get_site_templates(self):
        """
        Test case for get_site_templates

        查询站点模板
        """
        pass

    def test_unbind_site_template(self):
        """
        Test case for unbind_site_template

        站点模板解绑定一个或多个站点
        """
        pass

    def test_update_site_template(self):
        """
        Test case for update_site_template

        修改站点模板
        """
        pass


if __name__ == '__main__':
    unittest.main()
