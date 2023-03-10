# coding: utf-8

"""
    Portal在线用户查询

    查询Portal在线用户第三方北向接口。提供了Portal在线用户的查询、强制下线接口。 

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


class PortalOnlineUsersMgrApi(object):
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

    def cut_portal_online_users(self, body, **kwargs):
        """
        管理员强制Portal在线用户下线
        ## 典型场景 ##  提供管理员强制Portal在线用户下线北向接口。 ## 接口功能 ##  管理员强制Portal在线用户下线 ## 接口约束 ##  只有租户管理员获取token并建立会话后才能调用该接口。 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.cut_portal_online_users(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CutPortalOnlineUserInputDto body: 管理员强制Portal在线用户下线参数。 (required)
        :return: CutPortalOnlineUserOutputDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.cut_portal_online_users_with_http_info(body, **kwargs)
        else:
            (data) = self.cut_portal_online_users_with_http_info(body, **kwargs)
            return data

    def cut_portal_online_users_with_http_info(self, body, **kwargs):
        """
        管理员强制Portal在线用户下线
        ## 典型场景 ##  提供管理员强制Portal在线用户下线北向接口。 ## 接口功能 ##  管理员强制Portal在线用户下线 ## 接口约束 ##  只有租户管理员获取token并建立会话后才能调用该接口。 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.cut_portal_online_users_with_http_info(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CutPortalOnlineUserInputDto body: 管理员强制Portal在线用户下线参数。 (required)
        :return: CutPortalOnlineUserOutputDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cut_portal_online_users" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `cut_portal_online_users`")


        collection_formats = {}

        path_params = {}

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

        return self.api_client.call_api('/controller/campus/v1/accountservice/onlineusers/batch-delete', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='CutPortalOnlineUserOutputDto',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def query_portal_online_user(self, **kwargs):
        """
        查询Portal在线用户
        ## 典型场景 ##  提供查询Portal在线用户北向接口。 ## 接口功能 ##  查询Portal在线用户列表。默认按照认证时间降序排列。 ## 接口约束 ##  只有租户管理员获取token并建立会话后才能调用该接口。 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.query_portal_online_user(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str user_type: 用户类型： 0---普通用户 1---短信注册用户 2---自注册用户 4---社交媒体用户 5---微信用户 6---Passcode用户 7---第三方用户 11---PPSK 20---普通访客 64---匿名用户 如果不填，查询所有类型。 
        :param str auth_mode: 认证方式： 1---Portal认证 2---Mac优先认证 3---第三方认证 4---PPSK 如果不填，查询所有类型。 
        :param int page_index: 起始页。
        :param int page_size: 分页大小。
        :param str user_name: 用户名。用户名使用模糊查询。
        :param int begin_time_long: 查询起始时间。
        :param int end_time_long: 查询结束时间。
        :param str access_policy: 认证策略名。
        :param str terminal_ip: 认证终端IP。
        :param str terminal_mac: 认证终端MAC。
        :param str ssid: SSID
        :param str user_group_id: 用户组ID。
        :param str site_id: 站点ID。
        :return: list[QueryPortalOnlineUserInfoOutputDto]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.query_portal_online_user_with_http_info(**kwargs)
        else:
            (data) = self.query_portal_online_user_with_http_info(**kwargs)
            return data

    def query_portal_online_user_with_http_info(self, **kwargs):
        """
        查询Portal在线用户
        ## 典型场景 ##  提供查询Portal在线用户北向接口。 ## 接口功能 ##  查询Portal在线用户列表。默认按照认证时间降序排列。 ## 接口约束 ##  只有租户管理员获取token并建立会话后才能调用该接口。 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.query_portal_online_user_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str user_type: 用户类型： 0---普通用户 1---短信注册用户 2---自注册用户 4---社交媒体用户 5---微信用户 6---Passcode用户 7---第三方用户 11---PPSK 20---普通访客 64---匿名用户 如果不填，查询所有类型。 
        :param str auth_mode: 认证方式： 1---Portal认证 2---Mac优先认证 3---第三方认证 4---PPSK 如果不填，查询所有类型。 
        :param int page_index: 起始页。
        :param int page_size: 分页大小。
        :param str user_name: 用户名。用户名使用模糊查询。
        :param int begin_time_long: 查询起始时间。
        :param int end_time_long: 查询结束时间。
        :param str access_policy: 认证策略名。
        :param str terminal_ip: 认证终端IP。
        :param str terminal_mac: 认证终端MAC。
        :param str ssid: SSID
        :param str user_group_id: 用户组ID。
        :param str site_id: 站点ID。
        :return: list[QueryPortalOnlineUserInfoOutputDto]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_type', 'auth_mode', 'page_index', 'page_size', 'user_name', 'begin_time_long', 'end_time_long', 'access_policy', 'terminal_ip', 'terminal_mac', 'ssid', 'user_group_id', 'site_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method query_portal_online_user" % key
                )
            params[key] = val
        del params['kwargs']

        if 'page_size' in params and params['page_size'] > 100:
            raise ValueError("Invalid value for parameter `page_size` when calling `query_portal_online_user`, must be a value less than or equal to `100`")
        if 'page_size' in params and params['page_size'] < 20:
            raise ValueError("Invalid value for parameter `page_size` when calling `query_portal_online_user`, must be a value greater than or equal to `20`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_type' in params:
            query_params.append(('userType', params['user_type']))
        if 'auth_mode' in params:
            query_params.append(('authMode', params['auth_mode']))
        if 'page_index' in params:
            query_params.append(('pageIndex', params['page_index']))
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))
        if 'user_name' in params:
            query_params.append(('userName', params['user_name']))
        if 'begin_time_long' in params:
            query_params.append(('beginTimeLong', params['begin_time_long']))
        if 'end_time_long' in params:
            query_params.append(('endTimeLong', params['end_time_long']))
        if 'access_policy' in params:
            query_params.append(('accessPolicy', params['access_policy']))
        if 'terminal_ip' in params:
            query_params.append(('terminalIp', params['terminal_ip']))
        if 'terminal_mac' in params:
            query_params.append(('terminalMac', params['terminal_mac']))
        if 'ssid' in params:
            query_params.append(('ssid', params['ssid']))
        if 'user_group_id' in params:
            query_params.append(('userGroupId', params['user_group_id']))
        if 'site_id' in params:
            query_params.append(('siteId', params['site_id']))

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

        return self.api_client.call_api('/controller/campus/v1/accountservice/onlineusers', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[QueryPortalOnlineUserInfoOutputDto]',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
