# coding: utf-8

"""
    控制器支持第三方系统通过API接口获取用户上下线信息

    控制器支持第三方系统通过API接口获取用户上下线信息 

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


class AuthenticationLogApi(object):
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

    def get_authentication_log_info_list(self, start_row_key, site_id, auth_result, lower_online_time, upper_online_time, **kwargs):
        """
        查询用户上下线日志信息
        ## 典型场景 ##  提供租户查询指定时间内用户上下线信息，按分页返回查询结果。例如：查询8月1日至8月7号这段时间哪些用户上线过。 ## 接口功能 ##  根据租户ID查询指定时间内用户上下线信息，每次最多返回101条数据，不足101条时表示当前数据已查询完；等于101条表示后续还有数据。下一页查询以上一次查询返回的endRowKey的值作为本次查询条件startRowKey的值。 ## 接口约束 ##  该接口支持北向管理员访问，必须在用户会话建立后使用。 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_authentication_log_info_list(start_row_key, site_id, auth_result, lower_online_time, upper_online_time, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str start_row_key: 起始rowkey（首次查询为空字符串，分页查询时取上一次查询结果endRowKey的值）。 (required)
        :param str site_id: 站点ID（使用站点查询接口获取站点ID），格式为UUID。 (required)
        :param str auth_result: 认证结果（0---成功，1---失败）。 (required)
        :param int lower_online_time: 用户上线起始时间（接口调用方格林威治时间戳）。 (required)
        :param int upper_online_time: 用户上线的结束时间（接口调用方格林威治时间戳）。查询时不允许查询时间跨度大于7天的数据。 (required)
        :param str user_name: 用户名（短信认证则为手机号码）。
        :param str terminal_mac: 接入终端MAC地址（格式：AA-BB-CC-DD-EE-FF）。
        :param str user_type: 用户类型（0---普通用户。1---短信注册用户。2---自注册用户。4---社交媒体用户。5---微信用户。6---Passcode用户。7---三方用户。20---普通访客。64---匿名用户）。
        :param str access_ssid: 接入SSID名称。
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_authentication_log_info_list_with_http_info(start_row_key, site_id, auth_result, lower_online_time, upper_online_time, **kwargs)
        else:
            (data) = self.get_authentication_log_info_list_with_http_info(start_row_key, site_id, auth_result, lower_online_time, upper_online_time, **kwargs)
            return data

    def get_authentication_log_info_list_with_http_info(self, start_row_key, site_id, auth_result, lower_online_time, upper_online_time, **kwargs):
        """
        查询用户上下线日志信息
        ## 典型场景 ##  提供租户查询指定时间内用户上下线信息，按分页返回查询结果。例如：查询8月1日至8月7号这段时间哪些用户上线过。 ## 接口功能 ##  根据租户ID查询指定时间内用户上下线信息，每次最多返回101条数据，不足101条时表示当前数据已查询完；等于101条表示后续还有数据。下一页查询以上一次查询返回的endRowKey的值作为本次查询条件startRowKey的值。 ## 接口约束 ##  该接口支持北向管理员访问，必须在用户会话建立后使用。 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_authentication_log_info_list_with_http_info(start_row_key, site_id, auth_result, lower_online_time, upper_online_time, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str start_row_key: 起始rowkey（首次查询为空字符串，分页查询时取上一次查询结果endRowKey的值）。 (required)
        :param str site_id: 站点ID（使用站点查询接口获取站点ID），格式为UUID。 (required)
        :param str auth_result: 认证结果（0---成功，1---失败）。 (required)
        :param int lower_online_time: 用户上线起始时间（接口调用方格林威治时间戳）。 (required)
        :param int upper_online_time: 用户上线的结束时间（接口调用方格林威治时间戳）。查询时不允许查询时间跨度大于7天的数据。 (required)
        :param str user_name: 用户名（短信认证则为手机号码）。
        :param str terminal_mac: 接入终端MAC地址（格式：AA-BB-CC-DD-EE-FF）。
        :param str user_type: 用户类型（0---普通用户。1---短信注册用户。2---自注册用户。4---社交媒体用户。5---微信用户。6---Passcode用户。7---三方用户。20---普通访客。64---匿名用户）。
        :param str access_ssid: 接入SSID名称。
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['start_row_key', 'site_id', 'auth_result', 'lower_online_time', 'upper_online_time', 'user_name', 'terminal_mac', 'user_type', 'access_ssid']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_authentication_log_info_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'start_row_key' is set
        if ('start_row_key' not in params) or (params['start_row_key'] is None):
            raise ValueError("Missing the required parameter `start_row_key` when calling `get_authentication_log_info_list`")
        # verify the required parameter 'site_id' is set
        if ('site_id' not in params) or (params['site_id'] is None):
            raise ValueError("Missing the required parameter `site_id` when calling `get_authentication_log_info_list`")
        # verify the required parameter 'auth_result' is set
        if ('auth_result' not in params) or (params['auth_result'] is None):
            raise ValueError("Missing the required parameter `auth_result` when calling `get_authentication_log_info_list`")
        # verify the required parameter 'lower_online_time' is set
        if ('lower_online_time' not in params) or (params['lower_online_time'] is None):
            raise ValueError("Missing the required parameter `lower_online_time` when calling `get_authentication_log_info_list`")
        # verify the required parameter 'upper_online_time' is set
        if ('upper_online_time' not in params) or (params['upper_online_time'] is None):
            raise ValueError("Missing the required parameter `upper_online_time` when calling `get_authentication_log_info_list`")

        if 'lower_online_time' in params and params['lower_online_time'] > 9999999999999:
            raise ValueError("Invalid value for parameter `lower_online_time` when calling `get_authentication_log_info_list`, must be a value less than or equal to `9999999999999`")
        if 'lower_online_time' in params and params['lower_online_time'] < 0:
            raise ValueError("Invalid value for parameter `lower_online_time` when calling `get_authentication_log_info_list`, must be a value greater than or equal to `0`")
        if 'upper_online_time' in params and params['upper_online_time'] > 9999999999999:
            raise ValueError("Invalid value for parameter `upper_online_time` when calling `get_authentication_log_info_list`, must be a value less than or equal to `9999999999999`")
        if 'upper_online_time' in params and params['upper_online_time'] < 0:
            raise ValueError("Invalid value for parameter `upper_online_time` when calling `get_authentication_log_info_list`, must be a value greater than or equal to `0`")
        if 'user_name' in params and len(params['user_name']) > 128:
            raise ValueError("Invalid value for parameter `user_name` when calling `get_authentication_log_info_list`, length must be less than or equal to `128`")
        if 'user_name' in params and len(params['user_name']) < 0:
            raise ValueError("Invalid value for parameter `user_name` when calling `get_authentication_log_info_list`, length must be greater than or equal to `0`")
        if 'terminal_mac' in params and len(params['terminal_mac']) > 32:
            raise ValueError("Invalid value for parameter `terminal_mac` when calling `get_authentication_log_info_list`, length must be less than or equal to `32`")
        if 'terminal_mac' in params and len(params['terminal_mac']) < 0:
            raise ValueError("Invalid value for parameter `terminal_mac` when calling `get_authentication_log_info_list`, length must be greater than or equal to `0`")
        if 'access_ssid' in params and len(params['access_ssid']) > 64:
            raise ValueError("Invalid value for parameter `access_ssid` when calling `get_authentication_log_info_list`, length must be less than or equal to `64`")
        if 'access_ssid' in params and len(params['access_ssid']) < 0:
            raise ValueError("Invalid value for parameter `access_ssid` when calling `get_authentication_log_info_list`, length must be greater than or equal to `0`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start_row_key' in params:
            query_params.append(('startRowKey', params['start_row_key']))
        if 'site_id' in params:
            query_params.append(('siteId', params['site_id']))
        if 'auth_result' in params:
            query_params.append(('authResult', params['auth_result']))
        if 'lower_online_time' in params:
            query_params.append(('lowerOnlineTime', params['lower_online_time']))
        if 'upper_online_time' in params:
            query_params.append(('upperOnlineTime', params['upper_online_time']))
        if 'user_name' in params:
            query_params.append(('userName', params['user_name']))
        if 'terminal_mac' in params:
            query_params.append(('terminalMac', params['terminal_mac']))
        if 'user_type' in params:
            query_params.append(('userType', params['user_type']))
        if 'access_ssid' in params:
            query_params.append(('accessSSID', params['access_ssid']))

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

        return self.api_client.call_api('/controller/campus/v1/accountservice/user/authenticationlog', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)