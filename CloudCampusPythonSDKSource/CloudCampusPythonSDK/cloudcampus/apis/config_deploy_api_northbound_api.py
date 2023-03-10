# coding: utf-8

"""
    失败重下发配置

    失败重下发

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


class ConfigDeployApiNorthboundApi(object):
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

    def deploy_all_config(self, device_id, **kwargs):
        """
        全量下发配置
        ## 典型场景 ##    提供配置参数的接口，重新下发设备所有配置。 ## 接口功能 ##    重新下发设备所有配置。 ## 接口约束 ##    只有租户管理员获取token并建立会话后才能调用该接口。 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.deploy_all_config(device_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str device_id: 设备ID，UUID格式。 (required)
        :return: CommonDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.deploy_all_config_with_http_info(device_id, **kwargs)
        else:
            (data) = self.deploy_all_config_with_http_info(device_id, **kwargs)
            return data

    def deploy_all_config_with_http_info(self, device_id, **kwargs):
        """
        全量下发配置
        ## 典型场景 ##    提供配置参数的接口，重新下发设备所有配置。 ## 接口功能 ##    重新下发设备所有配置。 ## 接口约束 ##    只有租户管理员获取token并建立会话后才能调用该接口。 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.deploy_all_config_with_http_info(device_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str device_id: 设备ID，UUID格式。 (required)
        :return: CommonDto
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
                    " to method deploy_all_config" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'device_id' is set
        if ('device_id' not in params) or (params['device_id'] is None):
            raise ValueError("Missing the required parameter `device_id` when calling `deploy_all_config`")


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

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/controller/campus/v1/networkconfigservice/deploy/devices/{deviceId}/alldeploy', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='CommonDto',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def redeploy_fail_config(self, device_id, **kwargs):
        """
        重下发失败配置
        ## 典型场景 ##    提供配置参数的接口，重新下发配置结果为失败的配置。 ## 接口功能 ##    重新下发配置结果不为成功的配置。 ## 接口约束 ##    只有租户管理员获取token并建立会话后才能调用该接口。 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.redeploy_fail_config(device_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str device_id: 设备ID，UUID格式。 (required)
        :return: CommonDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.redeploy_fail_config_with_http_info(device_id, **kwargs)
        else:
            (data) = self.redeploy_fail_config_with_http_info(device_id, **kwargs)
            return data

    def redeploy_fail_config_with_http_info(self, device_id, **kwargs):
        """
        重下发失败配置
        ## 典型场景 ##    提供配置参数的接口，重新下发配置结果为失败的配置。 ## 接口功能 ##    重新下发配置结果不为成功的配置。 ## 接口约束 ##    只有租户管理员获取token并建立会话后才能调用该接口。 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.redeploy_fail_config_with_http_info(device_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str device_id: 设备ID，UUID格式。 (required)
        :return: CommonDto
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
                    " to method redeploy_fail_config" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'device_id' is set
        if ('device_id' not in params) or (params['device_id'] is None):
            raise ValueError("Missing the required parameter `device_id` when calling `redeploy_fail_config`")


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

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/controller/campus/v1/networkconfigservice/deploy/devices/{deviceId}/redeploy', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='CommonDto',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
