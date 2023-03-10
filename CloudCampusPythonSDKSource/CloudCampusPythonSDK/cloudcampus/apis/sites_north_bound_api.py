# coding: utf-8

"""
    室内地图信息查询

    室内地图第三方北向接口。 · 查询站点中所有楼栋基本信息 · 查询楼栋中所有楼层基本信息 · 查询楼栋中所有楼层详细信息 · 查询楼栋中楼层和设备布放信息 · 查询楼栋中楼层已布放设备详细信息 · 查询楼层已布放设备位置信息 

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient
from .gettoken_api import GetTokenApi


class SitesNorthBoundApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        # config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            print('api_client cannot be None.')
            # if not config.api_client:
            #     config.api_client = ApiClient()
            # self.api_client = config.api_client

    def get_buildings_info(self, site_id, **kwargs):
        """
        查询站点中所有楼栋基本信息
        ## 典型场景 ##  查询站点中所有楼栋。 ## 接口功能 ##  查询站点中所有楼栋基本信息，包含楼栋ID，楼栋名称，楼层列表。 ## 接口约束 ##  只有租户管理员获取token并建立会话后才能调用该接口。 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_buildings_info(site_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str site_id: 站点标识，格式UUID。 (required)
        :return: QueryBuildingsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_buildings_info_with_http_info(site_id, **kwargs)
        else:
            (data) = self.get_buildings_info_with_http_info(site_id, **kwargs)
            return data

    def get_buildings_info_with_http_info(self, site_id, **kwargs):
        """
        查询站点中所有楼栋基本信息
        ## 典型场景 ##  查询站点中所有楼栋。 ## 接口功能 ##  查询站点中所有楼栋基本信息，包含楼栋ID，楼栋名称，楼层列表。 ## 接口约束 ##  只有租户管理员获取token并建立会话后才能调用该接口。 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_buildings_info_with_http_info(site_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str site_id: 站点标识，格式UUID。 (required)
        :return: QueryBuildingsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['site_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_buildings_info" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'site_id' is set
        if ('site_id' not in params) or (params['site_id'] is None):
            raise ValueError("Missing the required parameter `site_id` when calling `get_buildings_info`")

        if 'site_id' in params and len(params['site_id']) > 36:
            raise ValueError("Invalid value for parameter `site_id` when calling `get_buildings_info`, length must be less than or equal to `36`")
        if 'site_id' in params and len(params['site_id']) < 36:
            raise ValueError("Invalid value for parameter `site_id` when calling `get_buildings_info`, length must be greater than or equal to `36`")

        collection_formats = {}

        path_params = {}
        if 'site_id' in params:
            path_params['siteId'] = params['site_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/controller/campus/v1/indoormapservice/sites/{siteId}/buildings', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='QueryBuildingsResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
