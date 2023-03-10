# coding: utf-8

"""
    交换机端口配置

    LSW端口配置北向接口，主要特性： · 查询交换机所有接口信息 · 修改交换机以太接口配置 · 创建交换机Eth-Trunk接口 · 修改交换机Eth-Trunk接口 · 删除交换机Eth-Trunk接口 

    OpenAPI spec version: 1.4.2
    
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


class LSWPortNorthboundApi(object):
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
        修改交换机端口配置
        ## 典型场景 ##    提供配置参数的接口，修改交换机以太端口配置。 ## 接口功能 ##    修改交换机以太端口配置，支持同时配置多个端口。 ## 接口约束 ##    该接口必须在租户内，存在交换机设备的站点内使用。 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.config(device_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str device_id: 设备ID。 (required)
        :param list[LSWEthPortDto] body: 交换机以太端口配置参数体。 (required)
        :return: PutResponseDto
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
        修改交换机端口配置
        ## 典型场景 ##    提供配置参数的接口，修改交换机以太端口配置。 ## 接口功能 ##    修改交换机以太端口配置，支持同时配置多个端口。 ## 接口约束 ##    该接口必须在租户内，存在交换机设备的站点内使用。 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.config_with_http_info(device_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str device_id: 设备ID。 (required)
        :param list[LSWEthPortDto] body: 交换机以太端口配置参数体。 (required)
        :return: PutResponseDto
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

        return self.api_client.call_api('/controller/campus/v1/networkservice/networkconfig/net/lswport/devices/{deviceId}/ethernet-ports', 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='PutResponseDto',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def create_eth_trunk(self, device_id, body, **kwargs):
        """
        创建交换机EthTrunk端口
        ## 典型场景 ##    提供配置参数的接口，创建交换机EthTrunk端口。 ## 接口功能 ##    创建交换机EthTrunk端口，可以同时配置此EthTrunk端口参数。 ## 接口约束 ##    该接口必须在租户内，存在交换机设备的站点内使用。 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_eth_trunk(device_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str device_id: 设备ID。 (required)
        :param LSWEthTrunkPortDto body: 创建交换机EthTrunk端口参数体。 (required)
        :return: EthTrunkResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_eth_trunk_with_http_info(device_id, body, **kwargs)
        else:
            (data) = self.create_eth_trunk_with_http_info(device_id, body, **kwargs)
            return data

    def create_eth_trunk_with_http_info(self, device_id, body, **kwargs):
        """
        创建交换机EthTrunk端口
        ## 典型场景 ##    提供配置参数的接口，创建交换机EthTrunk端口。 ## 接口功能 ##    创建交换机EthTrunk端口，可以同时配置此EthTrunk端口参数。 ## 接口约束 ##    该接口必须在租户内，存在交换机设备的站点内使用。 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_eth_trunk_with_http_info(device_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str device_id: 设备ID。 (required)
        :param LSWEthTrunkPortDto body: 创建交换机EthTrunk端口参数体。 (required)
        :return: EthTrunkResponseDto
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
                    " to method create_eth_trunk" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'device_id' is set
        if ('device_id' not in params) or (params['device_id'] is None):
            raise ValueError("Missing the required parameter `device_id` when calling `create_eth_trunk`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_eth_trunk`")


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

        return self.api_client.call_api('/controller/campus/v1/networkservice/networkconfig/net/lswport/devices/{deviceId}/ethtrunk-ports', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='EthTrunkResponseDto',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def delete_eth_trunk(self, device_id, name, **kwargs):
        """
        删除交换机EthTrunk端口
        ## 典型场景 ##    提供配置参数的接口，删除交换机EthTrunk端口。 ## 接口功能 ##    删除交换机EthTrunk端口。 ## 接口约束 ##    该接口必须在租户内，存在交换机设备的站点内使用。 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_eth_trunk(device_id, name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str device_id: 设备ID。 (required)
        :param str name: EthTrunk端口名称，必须是Eth-Trunk[数字]的格式，数字最大63。 (required)
        :return: ResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_eth_trunk_with_http_info(device_id, name, **kwargs)
        else:
            (data) = self.delete_eth_trunk_with_http_info(device_id, name, **kwargs)
            return data

    def delete_eth_trunk_with_http_info(self, device_id, name, **kwargs):
        """
        删除交换机EthTrunk端口
        ## 典型场景 ##    提供配置参数的接口，删除交换机EthTrunk端口。 ## 接口功能 ##    删除交换机EthTrunk端口。 ## 接口约束 ##    该接口必须在租户内，存在交换机设备的站点内使用。 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_eth_trunk_with_http_info(device_id, name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str device_id: 设备ID。 (required)
        :param str name: EthTrunk端口名称，必须是Eth-Trunk[数字]的格式，数字最大63。 (required)
        :return: ResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['device_id', 'name']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_eth_trunk" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'device_id' is set
        if ('device_id' not in params) or (params['device_id'] is None):
            raise ValueError("Missing the required parameter `device_id` when calling `delete_eth_trunk`")
        # verify the required parameter 'name' is set
        if ('name' not in params) or (params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `delete_eth_trunk`")

        if 'name' in params and len(params['name']) > 11:
            raise ValueError("Invalid value for parameter `name` when calling `delete_eth_trunk`, length must be less than or equal to `11`")
        if 'name' in params and len(params['name']) < 10:
            raise ValueError("Invalid value for parameter `name` when calling `delete_eth_trunk`, length must be greater than or equal to `10`")

        collection_formats = {}

        path_params = {}
        if 'device_id' in params:
            path_params['deviceId'] = params['device_id']
        if 'name' in params:
            path_params['name'] = params['name']

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

        return self.api_client.call_api('/controller/campus/v1/networkservice/networkconfig/net/lswport/devices/{deviceId}/ethtrunk-ports/{name}', 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ResponseDto',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_config(self, device_id, **kwargs):
        """
        查询交换机端口配置
        ## 典型场景 ##    提供查询配置参数的接口，查询交换机端口配置。 ## 接口功能 ##    查询交换机端口配置（包括以太口和EthTrunk口）。 ## 接口约束 ##    该接口必须在租户内，存在交换机设备的站点内使用。 
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
        :return: GetResponseDto
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
        查询交换机端口配置
        ## 典型场景 ##    提供查询配置参数的接口，查询交换机端口配置。 ## 接口功能 ##    查询交换机端口配置（包括以太口和EthTrunk口）。 ## 接口约束 ##    该接口必须在租户内，存在交换机设备的站点内使用。 
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
        :return: GetResponseDto
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

        return self.api_client.call_api('/controller/campus/v1/networkservice/networkconfig/net/lswport/devices/{deviceId}/ports', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='GetResponseDto',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update_eth_trunk(self, device_id, name, body, **kwargs):
        """
        修改交换机EthTrunk端口
        ## 典型场景 ##    提供配置参数的接口，修改交换机EthTrunk端口。 ## 接口功能 ##    修改交换机EthTrunk端口，可以同时配置此EthTrunk端口参数。 ## 接口约束 ##    该接口必须在租户内，存在交换机设备的站点内使用。 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_eth_trunk(device_id, name, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str device_id: 设备ID。 (required)
        :param str name: EthTrunk端口名称，必须是Eth-Trunk[数字]的格式，数字最大63。 (required)
        :param LSWEthTrunkPortDto body: 修改交换机EthTrunk端口参数体。 (required)
        :return: EthTrunkResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_eth_trunk_with_http_info(device_id, name, body, **kwargs)
        else:
            (data) = self.update_eth_trunk_with_http_info(device_id, name, body, **kwargs)
            return data

    def update_eth_trunk_with_http_info(self, device_id, name, body, **kwargs):
        """
        修改交换机EthTrunk端口
        ## 典型场景 ##    提供配置参数的接口，修改交换机EthTrunk端口。 ## 接口功能 ##    修改交换机EthTrunk端口，可以同时配置此EthTrunk端口参数。 ## 接口约束 ##    该接口必须在租户内，存在交换机设备的站点内使用。 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_eth_trunk_with_http_info(device_id, name, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str device_id: 设备ID。 (required)
        :param str name: EthTrunk端口名称，必须是Eth-Trunk[数字]的格式，数字最大63。 (required)
        :param LSWEthTrunkPortDto body: 修改交换机EthTrunk端口参数体。 (required)
        :return: EthTrunkResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['device_id', 'name', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_eth_trunk" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'device_id' is set
        if ('device_id' not in params) or (params['device_id'] is None):
            raise ValueError("Missing the required parameter `device_id` when calling `update_eth_trunk`")
        # verify the required parameter 'name' is set
        if ('name' not in params) or (params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `update_eth_trunk`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_eth_trunk`")

        if 'name' in params and len(params['name']) > 11:
            raise ValueError("Invalid value for parameter `name` when calling `update_eth_trunk`, length must be less than or equal to `11`")
        if 'name' in params and len(params['name']) < 10:
            raise ValueError("Invalid value for parameter `name` when calling `update_eth_trunk`, length must be greater than or equal to `10`")

        collection_formats = {}

        path_params = {}
        if 'device_id' in params:
            path_params['deviceId'] = params['device_id']
        if 'name' in params:
            path_params['name'] = params['name']

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

        return self.api_client.call_api('/controller/campus/v1/networkservice/networkconfig/net/lswport/devices/{deviceId}/ethtrunk-ports/{name}', 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='EthTrunkResponseDto',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
