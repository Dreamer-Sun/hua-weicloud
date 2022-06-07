# coding: utf-8

"""
    终端应用流量信息查询

    终端TopN应用流量查询。 

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


class ApplicationOpenApiApi(object):
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

    def query_application_info(self, app_dimension, time_dimension, top, **kwargs):
        """
        查询终端TopN应用流量
        ## 典型场景 ##    提供查询终端TopN应用流量列表的接口。           ## 接口功能 ##    查询终端TopN应用流量列表。 ## 接口约束 ##    1、当前只支持Top5查询，后续扩展更多维度。    2、当前不支持自由选择时间段统计数据，只支持当前一天，当前一周或者当前一个月的数据查询。     
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.query_application_info(app_dimension, time_dimension, top, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str app_dimension: 查询维度，app---应用名称、apptype---应用类型。 (required)
        :param str time_dimension: 统计周期，day---天、week---周、month---月。 (required)
        :param int top: top流量数据个数，当前目前只支持范围5。 (required)
        :param str site_id: 站点ID，如果为空，代表租户维度。
        :return: ApplicationInfoResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.query_application_info_with_http_info(app_dimension, time_dimension, top, **kwargs)
        else:
            (data) = self.query_application_info_with_http_info(app_dimension, time_dimension, top, **kwargs)
            return data

    def query_application_info_with_http_info(self, app_dimension, time_dimension, top, **kwargs):
        """
        查询终端TopN应用流量
        ## 典型场景 ##    提供查询终端TopN应用流量列表的接口。           ## 接口功能 ##    查询终端TopN应用流量列表。 ## 接口约束 ##    1、当前只支持Top5查询，后续扩展更多维度。    2、当前不支持自由选择时间段统计数据，只支持当前一天，当前一周或者当前一个月的数据查询。     
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.query_application_info_with_http_info(app_dimension, time_dimension, top, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str app_dimension: 查询维度，app---应用名称、apptype---应用类型。 (required)
        :param str time_dimension: 统计周期，day---天、week---周、month---月。 (required)
        :param int top: top流量数据个数，当前目前只支持范围5。 (required)
        :param str site_id: 站点ID，如果为空，代表租户维度。
        :return: ApplicationInfoResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['app_dimension', 'time_dimension', 'top', 'site_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method query_application_info" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'app_dimension' is set
        if ('app_dimension' not in params) or (params['app_dimension'] is None):
            raise ValueError("Missing the required parameter `app_dimension` when calling `query_application_info`")
        # verify the required parameter 'time_dimension' is set
        if ('time_dimension' not in params) or (params['time_dimension'] is None):
            raise ValueError("Missing the required parameter `time_dimension` when calling `query_application_info`")
        # verify the required parameter 'top' is set
        if ('top' not in params) or (params['top'] is None):
            raise ValueError("Missing the required parameter `top` when calling `query_application_info`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'site_id' in params:
            query_params.append(('siteId', params['site_id']))
        if 'app_dimension' in params:
            query_params.append(('appDimension', params['app_dimension']))
        if 'time_dimension' in params:
            query_params.append(('timeDimension', params['time_dimension']))
        if 'top' in params:
            query_params.append(('top', params['top']))

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

        return self.api_client.call_api('/controller/campus/v1/performanceservice/application/apptraffic/topapp', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ApplicationInfoResp',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)