# coding: utf-8

"""
    交换机管理VLAN配置

    LSW管理VLAN配置北向接口，主要特性：  · 查询交换机管理VLAN配置信息 · 修改交换机管理VLAN配置 

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


class LSWMgmtVlanNorthboundApi(object):
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

    def config(self, device_id, body, **kwargs):
        """
        修改站点内交换机的管理VLAN配置
        ## 典型场景 ##    提供配置参数的接口，修改交换机的管理VLAN配置。 ## 接口功能 ##    修改交换机管理VLAN配置。 ## 接口约束 ##    该接口必须在租户内，存在交换机设备的站点内使用。<br>    如果当前交换机设备的上行口为Access类型，则直接将defaultVLAN设置为当前管理VLAN。<br>    如果当前交换机设备的上行口为Trunk类型，则用户配置管理VLAN前需要同时放行旧管理VLAN和新管理VLAN。<br> 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.config(device_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str device_id: 设备ID，格式为uuid格式。 (required)
        :param MgmtVlanDto body: 站点内交换机的管理VLAN配置参数体。 (required)
        :return: MgmtVlanResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.config_with_http_info(device_id, body, **kwargs)
        else:
            (data) = self.config_with_http_info(device_id, body, **kwargs)
            return data

    def config_with_http_info(self, device_id, body, **kwargs):
        """
        修改站点内交换机的管理VLAN配置
        ## 典型场景 ##    提供配置参数的接口，修改交换机的管理VLAN配置。 ## 接口功能 ##    修改交换机管理VLAN配置。 ## 接口约束 ##    该接口必须在租户内，存在交换机设备的站点内使用。<br>    如果当前交换机设备的上行口为Access类型，则直接将defaultVLAN设置为当前管理VLAN。<br>    如果当前交换机设备的上行口为Trunk类型，则用户配置管理VLAN前需要同时放行旧管理VLAN和新管理VLAN。<br> 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.config_with_http_info(device_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str device_id: 设备ID，格式为uuid格式。 (required)
        :param MgmtVlanDto body: 站点内交换机的管理VLAN配置参数体。 (required)
        :return: MgmtVlanResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['device_id', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method config" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'device_id' is set
        if ('device_id' not in params) or (params['device_id'] is None):
            raise ValueError("Missing the required parameter `device_id` when calling `config`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `config`")


        collection_formats = {}

        path_params = {}
        if 'device_id' in params:
            path_params['deviceId'] = params['device_id']

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

        return self.api_client.call_api('/controller/campus/v1/networkservice/networkconfig/net/lswmgmtvlan/devices/{deviceId}/mgmtvlan', 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='MgmtVlanResponseDto',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_config(self, device_id, **kwargs):
        """
        获取站点内交换机的管理VLAN配置
        ## 典型场景 ##    提供查询配置参数的接口，查询LSW的管理VLAN配置信息。 ## 接口功能 ##    获取管理VLAN配置。 ## 接口约束 ##    该接口必须在租户内，存在交换机设备的站点内使用。 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_config(device_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str device_id: 设备ID。 (required)
        :return: MgmtVlanResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_config_with_http_info(device_id, **kwargs)
        else:
            (data) = self.get_config_with_http_info(device_id, **kwargs)
            return data

    def get_config_with_http_info(self, device_id, **kwargs):
        """
        获取站点内交换机的管理VLAN配置
        ## 典型场景 ##    提供查询配置参数的接口，查询LSW的管理VLAN配置信息。 ## 接口功能 ##    获取管理VLAN配置。 ## 接口约束 ##    该接口必须在租户内，存在交换机设备的站点内使用。 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_config_with_http_info(device_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str device_id: 设备ID。 (required)
        :return: MgmtVlanResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['device_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_config" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'device_id' is set
        if ('device_id' not in params) or (params['device_id'] is None):
            raise ValueError("Missing the required parameter `device_id` when calling `get_config`")


        collection_formats = {}

        path_params = {}
        if 'device_id' in params:
            path_params['deviceId'] = params['device_id']

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

        return self.api_client.call_api('/controller/campus/v1/networkservice/networkconfig/net/lswmgmtvlan/devices/{deviceId}/mgmtvlan', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='MgmtVlanResponseDto',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
