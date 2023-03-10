# coding: utf-8

"""
    PPSK帐号配置

    PPSK帐号管理北向接口，主要包括： · 创建PPSK帐号 · 修改PPSK帐号 · 删除PPSK帐号 · 查询PPSK帐号 

    OpenAPI spec version: 1.1.1
    
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


class PPSKNorthboundApi(object):
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

    def create_ppsk_account(self, site_id, body, **kwargs):
        """
        新增PPSK帐号
        ## 典型场景 ##    在一个站点内，一次新增一个PPSK帐号。 ## 接口功能 ##    新增PPSK帐号。 ## 接口约束 ##    该接口支持北向操作管理员管理访问，必须在用户会话建立后使用。 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_ppsk_account(site_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str site_id: 站点ID，UUID格式。 (required)
        :param PPSKPostRequestDto body: PPSK帐号信息参数体。 (required)
        :return: PpskPostOrPutResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_ppsk_account_with_http_info(site_id, body, **kwargs)
        else:
            (data) = self.create_ppsk_account_with_http_info(site_id, body, **kwargs)
            return data

    def create_ppsk_account_with_http_info(self, site_id, body, **kwargs):
        """
        新增PPSK帐号
        ## 典型场景 ##    在一个站点内，一次新增一个PPSK帐号。 ## 接口功能 ##    新增PPSK帐号。 ## 接口约束 ##    该接口支持北向操作管理员管理访问，必须在用户会话建立后使用。 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_ppsk_account_with_http_info(site_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str site_id: 站点ID，UUID格式。 (required)
        :param PPSKPostRequestDto body: PPSK帐号信息参数体。 (required)
        :return: PpskPostOrPutResponseDto
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
                    " to method create_ppsk_account" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'site_id' is set
        if ('site_id' not in params) or (params['site_id'] is None):
            raise ValueError("Missing the required parameter `site_id` when calling `create_ppsk_account`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_ppsk_account`")


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

        return self.api_client.call_api('/controller/campus/v1/authconfigservice/accessconfig/{siteId}/ppsk', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='PpskPostOrPutResponseDto',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def delete_ppsk_account(self, site_id, account, **kwargs):
        """
        删除PPSK帐号
        ## 典型场景 ##    通过帐号名删除PPSK帐号信息。 ## 接口功能 ##    通过帐号名删除PPSK帐号信息。 ## 接口约束 ##    该接口支持北向操作管理员管理访问，必须在用户会话建立后使用。 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_ppsk_account(site_id, account, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str site_id: 站点ID，UUID格式。 (required)
        :param str account: PPSK帐号名称。 (required)
        :return: PpskDeleteResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_ppsk_account_with_http_info(site_id, account, **kwargs)
        else:
            (data) = self.delete_ppsk_account_with_http_info(site_id, account, **kwargs)
            return data

    def delete_ppsk_account_with_http_info(self, site_id, account, **kwargs):
        """
        删除PPSK帐号
        ## 典型场景 ##    通过帐号名删除PPSK帐号信息。 ## 接口功能 ##    通过帐号名删除PPSK帐号信息。 ## 接口约束 ##    该接口支持北向操作管理员管理访问，必须在用户会话建立后使用。 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_ppsk_account_with_http_info(site_id, account, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str site_id: 站点ID，UUID格式。 (required)
        :param str account: PPSK帐号名称。 (required)
        :return: PpskDeleteResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['site_id', 'account']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_ppsk_account" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'site_id' is set
        if ('site_id' not in params) or (params['site_id'] is None):
            raise ValueError("Missing the required parameter `site_id` when calling `delete_ppsk_account`")
        # verify the required parameter 'account' is set
        if ('account' not in params) or (params['account'] is None):
            raise ValueError("Missing the required parameter `account` when calling `delete_ppsk_account`")

        if 'account' in params and len(params['account']) > 64:
            raise ValueError("Invalid value for parameter `account` when calling `delete_ppsk_account`, length must be less than or equal to `64`")
        if 'account' in params and len(params['account']) < 1:
            raise ValueError("Invalid value for parameter `account` when calling `delete_ppsk_account`, length must be greater than or equal to `1`")

        collection_formats = {}

        path_params = {}
        if 'site_id' in params:
            path_params['siteId'] = params['site_id']
        if 'account' in params:
            path_params['account'] = params['account']

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

        return self.api_client.call_api('/controller/campus/v1/authconfigservice/accessconfig/{siteId}/ppsk/{account}', 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='PpskDeleteResponseDto',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_ppsk_account(self, site_id, **kwargs):
        """
        查询PPSK帐号
        ## 典型场景 ##    通过帐号名、VLAN ID查询PPSK帐号信息。 ## 接口功能 ##    通过帐号名、VLAN ID查询PPSK帐号信息。 ## 接口约束 ##    该接口支持北向操作管理员管理访问，必须在用户会话建立后使用。 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_ppsk_account(site_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str site_id: 站点ID，UUID格式。 (required)
        :param str account: 帐号名称。
        :param str ssid_name: SSID名称。
        :param int vlan: 帐号绑定的VLAN。
        :param int page_index: 页面索引。
        :param int page_size: 每页显示记录数。
        :return: PpskGetResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_ppsk_account_with_http_info(site_id, **kwargs)
        else:
            (data) = self.get_ppsk_account_with_http_info(site_id, **kwargs)
            return data

    def get_ppsk_account_with_http_info(self, site_id, **kwargs):
        """
        查询PPSK帐号
        ## 典型场景 ##    通过帐号名、VLAN ID查询PPSK帐号信息。 ## 接口功能 ##    通过帐号名、VLAN ID查询PPSK帐号信息。 ## 接口约束 ##    该接口支持北向操作管理员管理访问，必须在用户会话建立后使用。 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_ppsk_account_with_http_info(site_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str site_id: 站点ID，UUID格式。 (required)
        :param str account: 帐号名称。
        :param str ssid_name: SSID名称。
        :param int vlan: 帐号绑定的VLAN。
        :param int page_index: 页面索引。
        :param int page_size: 每页显示记录数。
        :return: PpskGetResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['site_id', 'account', 'ssid_name', 'vlan', 'page_index', 'page_size']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_ppsk_account" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'site_id' is set
        if ('site_id' not in params) or (params['site_id'] is None):
            raise ValueError("Missing the required parameter `site_id` when calling `get_ppsk_account`")


        collection_formats = {}

        path_params = {}
        if 'site_id' in params:
            path_params['siteId'] = params['site_id']

        query_params = []
        if 'account' in params:
            query_params.append(('account', params['account']))
        if 'ssid_name' in params:
            query_params.append(('ssidName', params['ssid_name']))
        if 'vlan' in params:
            query_params.append(('vlan', params['vlan']))
        if 'page_index' in params:
            query_params.append(('pageIndex', params['page_index']))
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))

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

        return self.api_client.call_api('/controller/campus/v1/authconfigservice/accessconfig/{siteId}/ppsk', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='PpskGetResponseDto',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update_ppsk_account(self, site_id, account, body, **kwargs):
        """
        修改PPSK帐号
        ## 典型场景 ##    修改PPSK帐号信息，包括PSK、VLAN ID和帐号描述信息。 ## 接口功能 ##    修改PPSK帐号信息。 ## 接口约束 ##    该接口支持北向操作管理员管理访问，必须在用户会话建立后使用。 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_ppsk_account(site_id, account, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str site_id: 站点ID，UUID格式。 (required)
        :param str account: PPSK帐号名称。 (required)
        :param PPSKPutRequestDto body: PPSK帐号信息参数体。 (required)
        :return: PpskPostOrPutResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_ppsk_account_with_http_info(site_id, account, body, **kwargs)
        else:
            (data) = self.update_ppsk_account_with_http_info(site_id, account, body, **kwargs)
            return data

    def update_ppsk_account_with_http_info(self, site_id, account, body, **kwargs):
        """
        修改PPSK帐号
        ## 典型场景 ##    修改PPSK帐号信息，包括PSK、VLAN ID和帐号描述信息。 ## 接口功能 ##    修改PPSK帐号信息。 ## 接口约束 ##    该接口支持北向操作管理员管理访问，必须在用户会话建立后使用。 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_ppsk_account_with_http_info(site_id, account, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str site_id: 站点ID，UUID格式。 (required)
        :param str account: PPSK帐号名称。 (required)
        :param PPSKPutRequestDto body: PPSK帐号信息参数体。 (required)
        :return: PpskPostOrPutResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['site_id', 'account', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_ppsk_account" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'site_id' is set
        if ('site_id' not in params) or (params['site_id'] is None):
            raise ValueError("Missing the required parameter `site_id` when calling `update_ppsk_account`")
        # verify the required parameter 'account' is set
        if ('account' not in params) or (params['account'] is None):
            raise ValueError("Missing the required parameter `account` when calling `update_ppsk_account`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_ppsk_account`")

        if 'account' in params and len(params['account']) > 64:
            raise ValueError("Invalid value for parameter `account` when calling `update_ppsk_account`, length must be less than or equal to `64`")
        if 'account' in params and len(params['account']) < 1:
            raise ValueError("Invalid value for parameter `account` when calling `update_ppsk_account`, length must be greater than or equal to `1`")

        collection_formats = {}

        path_params = {}
        if 'site_id' in params:
            path_params['siteId'] = params['site_id']
        if 'account' in params:
            path_params['account'] = params['account']

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

        return self.api_client.call_api('/controller/campus/v1/authconfigservice/accessconfig/{siteId}/ppsk/{account}', 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='PpskPostOrPutResponseDto',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
