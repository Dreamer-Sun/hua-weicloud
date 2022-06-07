# coding: utf-8

"""
    交换机STP保护配置

    主要特性： · 创建交换机STP保护配置 · 修改交换机STP保护配置 · 查询交换机STP保护配置 · 删除交换机STP保护配置 

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


class LSWStpProtectionNorthboundApi(object):
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

    def create_stp_protection(self, site_id, body, **kwargs):
        """
        创建交换机STP保护配置
        ## 典型场景 ##    提供配置参数的接口，创建交换机STP保护配置。 ## 接口功能 ##    创建交换机STP保护配置。 ## 接口约束 ##    该接口必须在租户内，存在交换机设备的站点内使用。 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_stp_protection(site_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str site_id: 站点ID。 (required)
        :param StpProtectionRequestDto body: 创建交换机STP保护配置信息。 (required)
        :return: StpProtectionResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_stp_protection_with_http_info(site_id, body, **kwargs)
        else:
            (data) = self.create_stp_protection_with_http_info(site_id, body, **kwargs)
            return data

    def create_stp_protection_with_http_info(self, site_id, body, **kwargs):
        """
        创建交换机STP保护配置
        ## 典型场景 ##    提供配置参数的接口，创建交换机STP保护配置。 ## 接口功能 ##    创建交换机STP保护配置。 ## 接口约束 ##    该接口必须在租户内，存在交换机设备的站点内使用。 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_stp_protection_with_http_info(site_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str site_id: 站点ID。 (required)
        :param StpProtectionRequestDto body: 创建交换机STP保护配置信息。 (required)
        :return: StpProtectionResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['site_id', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_stp_protection" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'site_id' is set
        if ('site_id' not in params) or (params['site_id'] is None):
            raise ValueError("Missing the required parameter `site_id` when calling `create_stp_protection`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_stp_protection`")


        collection_formats = {}

        path_params = {}
        if 'site_id' in params:
            path_params['siteId'] = params['site_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/controller/campus/v1/networkservice/networkconfig/net/lswstpprotection/sites/{siteId}/stpprotection', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='StpProtectionResponseDto',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def delete_stp_protection(self, site_id, body, **kwargs):
        """
        删除交换机STP保护配置
        ## 典型场景 ##    提供删除配置参数的接口，删除交换机STP保护配置。 ## 接口功能 ##    删除交换机STP保护配置。 ## 接口约束 ##    该接口必须在租户内，存在交换机设备的站点内使用。 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_stp_protection(site_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str site_id: 站点ID。 (required)
        :param DeleteStpProtectionRequestDto body: 删除交换机STP保护配置请求参数体。 (required)
        :return: DeleteStpProtectionResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_stp_protection_with_http_info(site_id, body, **kwargs)
        else:
            (data) = self.delete_stp_protection_with_http_info(site_id, body, **kwargs)
            return data

    def delete_stp_protection_with_http_info(self, site_id, body, **kwargs):
        """
        删除交换机STP保护配置
        ## 典型场景 ##    提供删除配置参数的接口，删除交换机STP保护配置。 ## 接口功能 ##    删除交换机STP保护配置。 ## 接口约束 ##    该接口必须在租户内，存在交换机设备的站点内使用。 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_stp_protection_with_http_info(site_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str site_id: 站点ID。 (required)
        :param DeleteStpProtectionRequestDto body: 删除交换机STP保护配置请求参数体。 (required)
        :return: DeleteStpProtectionResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['site_id', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_stp_protection" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'site_id' is set
        if ('site_id' not in params) or (params['site_id'] is None):
            raise ValueError("Missing the required parameter `site_id` when calling `delete_stp_protection`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `delete_stp_protection`")


        collection_formats = {}

        path_params = {}
        if 'site_id' in params:
            path_params['siteId'] = params['site_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/controller/campus/v1/networkservice/networkconfig/net/lswstpprotection/sites/{siteId}/stpprotection/batch-delete', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='DeleteStpProtectionResponseDto',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_stp_protection(self, site_id, **kwargs):
        """
        查询交换机STP保护配置
        ## 典型场景 ##    提供查询配置参数的接口，查询交换机STP保护配置信息。 ## 接口功能 ##    查询交换机STP保护配置信息。 ## 接口约束 ##    该接口必须在租户内，存在交换机设备的站点内使用。 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_stp_protection(site_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str site_id: 站点ID。 (required)
        :return: GetStpProtectionResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_stp_protection_with_http_info(site_id, **kwargs)
        else:
            (data) = self.get_stp_protection_with_http_info(site_id, **kwargs)
            return data

    def get_stp_protection_with_http_info(self, site_id, **kwargs):
        """
        查询交换机STP保护配置
        ## 典型场景 ##    提供查询配置参数的接口，查询交换机STP保护配置信息。 ## 接口功能 ##    查询交换机STP保护配置信息。 ## 接口约束 ##    该接口必须在租户内，存在交换机设备的站点内使用。 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_stp_protection_with_http_info(site_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str site_id: 站点ID。 (required)
        :return: GetStpProtectionResponseDto
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
                    " to method get_stp_protection" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'site_id' is set
        if ('site_id' not in params) or (params['site_id'] is None):
            raise ValueError("Missing the required parameter `site_id` when calling `get_stp_protection`")


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

        return self.api_client.call_api('/controller/campus/v1/networkservice/networkconfig/net/lswstpprotection/sites/{siteId}/stpprotection', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='GetStpProtectionResponseDto',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update_stp_protection(self, site_id, body, **kwargs):
        """
        修改交换机STP保护配置
        ## 典型场景 ##    提供配置参数的接口，修改交换机STP保护配置。 ## 接口功能 ##    修改交换机STP保护配置。 ## 接口约束 ##    该接口必须在租户内，存在交换机设备的站点内使用。 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_stp_protection(site_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str site_id: 站点ID。 (required)
        :param StpProtectionRequestDto body: 修改交换机STP保护配置参数体。 (required)
        :return: StpProtectionResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_stp_protection_with_http_info(site_id, body, **kwargs)
        else:
            (data) = self.update_stp_protection_with_http_info(site_id, body, **kwargs)
            return data

    def update_stp_protection_with_http_info(self, site_id, body, **kwargs):
        """
        修改交换机STP保护配置
        ## 典型场景 ##    提供配置参数的接口，修改交换机STP保护配置。 ## 接口功能 ##    修改交换机STP保护配置。 ## 接口约束 ##    该接口必须在租户内，存在交换机设备的站点内使用。 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_stp_protection_with_http_info(site_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str site_id: 站点ID。 (required)
        :param StpProtectionRequestDto body: 修改交换机STP保护配置参数体。 (required)
        :return: StpProtectionResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['site_id', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_stp_protection" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'site_id' is set
        if ('site_id' not in params) or (params['site_id'] is None):
            raise ValueError("Missing the required parameter `site_id` when calling `update_stp_protection`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_stp_protection`")


        collection_formats = {}

        path_params = {}
        if 'site_id' in params:
            path_params['siteId'] = params['site_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/controller/campus/v1/networkservice/networkconfig/net/lswstpprotection/sites/{siteId}/stpprotection', 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='StpProtectionResponseDto',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
