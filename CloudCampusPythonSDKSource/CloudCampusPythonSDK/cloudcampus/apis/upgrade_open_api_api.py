# coding: utf-8

"""
    设备升级

    · 查询设备文件 · 创建站点升级 · 查询站点升级 · 查询设备升级 · 取消设备升级 · 删除站点升级 · 重新升级设备 

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


class UpgradeOpenApiApi(object):
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

    def cancel_policy(self, policy_device_cancel_input_list, **kwargs):
        """
        取消设备升级
        ## 典型场景 ##    取消设备升级。 ## 接口功能 ##    取消设备升级。 ## 接口约束 ##    只有租户管理员获取token并建立会话后才能调用该接口。 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.cancel_policy(policy_device_cancel_input_list, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param PolicyDeviceCancelInputList policy_device_cancel_input_list: 取消设备升级入参。 (required)
        :return: CommonResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.cancel_policy_with_http_info(policy_device_cancel_input_list, **kwargs)
        else:
            (data) = self.cancel_policy_with_http_info(policy_device_cancel_input_list, **kwargs)
            return data

    def cancel_policy_with_http_info(self, policy_device_cancel_input_list, **kwargs):
        """
        取消设备升级
        ## 典型场景 ##    取消设备升级。 ## 接口功能 ##    取消设备升级。 ## 接口约束 ##    只有租户管理员获取token并建立会话后才能调用该接口。 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.cancel_policy_with_http_info(policy_device_cancel_input_list, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param PolicyDeviceCancelInputList policy_device_cancel_input_list: 取消设备升级入参。 (required)
        :return: CommonResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['policy_device_cancel_input_list']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cancel_policy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'policy_device_cancel_input_list' is set
        if ('policy_device_cancel_input_list' not in params) or (params['policy_device_cancel_input_list'] is None):
            raise ValueError("Missing the required parameter `policy_device_cancel_input_list` when calling `cancel_policy`")


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'policy_device_cancel_input_list' in params:
            body_params = params['policy_device_cancel_input_list']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/controller/campus/v1/oamservice/upgrade/policy/device/cancel', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='CommonResponseBody',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def cancel_site_policy(self, policy_site_cancel_input_list, **kwargs):
        """
        删除站点升级
        ## 典型场景 ##    删除多站点升级计划。 ## 接口功能 ##    删除多站点升级计划。 ## 接口约束 ##    只有租户管理员获取token并建立会话后才能调用该接口。    建议先取消所有站点下正在升级的设备。 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.cancel_site_policy(policy_site_cancel_input_list, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param PolicySiteCancelInputList policy_site_cancel_input_list: 删除多站点升级计划入参。 (required)
        :return: CommonResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.cancel_site_policy_with_http_info(policy_site_cancel_input_list, **kwargs)
        else:
            (data) = self.cancel_site_policy_with_http_info(policy_site_cancel_input_list, **kwargs)
            return data

    def cancel_site_policy_with_http_info(self, policy_site_cancel_input_list, **kwargs):
        """
        删除站点升级
        ## 典型场景 ##    删除多站点升级计划。 ## 接口功能 ##    删除多站点升级计划。 ## 接口约束 ##    只有租户管理员获取token并建立会话后才能调用该接口。    建议先取消所有站点下正在升级的设备。 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.cancel_site_policy_with_http_info(policy_site_cancel_input_list, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param PolicySiteCancelInputList policy_site_cancel_input_list: 删除多站点升级计划入参。 (required)
        :return: CommonResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['policy_site_cancel_input_list']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cancel_site_policy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'policy_site_cancel_input_list' is set
        if ('policy_site_cancel_input_list' not in params) or (params['policy_site_cancel_input_list'] is None):
            raise ValueError("Missing the required parameter `policy_site_cancel_input_list` when calling `cancel_site_policy`")


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'policy_site_cancel_input_list' in params:
            body_params = params['policy_site_cancel_input_list']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/controller/campus/v1/oamservice/upgrade/policy/site/cancel', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='CommonResponseBody',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def policy_configuration(self, policy_config, **kwargs):
        """
        创建站点升级
        ## 典型场景 ##    创建多站点升级计划。 ## 接口功能 ##    创建多站点升级计划。 ## 接口约束 ##    只有租户管理员获取token并建立会话后才能调用该接口。 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.policy_configuration(policy_config, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param PolicyConfig policy_config: 多站点升级计划。 (required)
        :return: PolicyConfigRes
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.policy_configuration_with_http_info(policy_config, **kwargs)
        else:
            (data) = self.policy_configuration_with_http_info(policy_config, **kwargs)
            return data

    def policy_configuration_with_http_info(self, policy_config, **kwargs):
        """
        创建站点升级
        ## 典型场景 ##    创建多站点升级计划。 ## 接口功能 ##    创建多站点升级计划。 ## 接口约束 ##    只有租户管理员获取token并建立会话后才能调用该接口。 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.policy_configuration_with_http_info(policy_config, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param PolicyConfig policy_config: 多站点升级计划。 (required)
        :return: PolicyConfigRes
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['policy_config']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method policy_configuration" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'policy_config' is set
        if ('policy_config' not in params) or (params['policy_config'] is None):
            raise ValueError("Missing the required parameter `policy_config` when calling `policy_configuration`")


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'policy_config' in params:
            body_params = params['policy_config']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/controller/campus/v1/oamservice/upgrade/policy', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='PolicyConfigRes',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def query_policy(self, site_id, **kwargs):
        """
        查询站点升级
        ## 典型场景 ##    查询站点升级计划概要。 ## 接口功能 ##    查询站点升级计划概要。 ## 接口约束 ##    只有租户管理员获取token并建立会话后才能调用该接口。 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.query_policy(site_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str site_id: 站点ID。 (required)
        :param str device_model: 设备款型。 如果不填就是站点下全量的数据。 如果填写了设备款型，就是该站点下该款型的升级计划。 
        :return: PolicyConfigRes
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.query_policy_with_http_info(site_id, **kwargs)
        else:
            (data) = self.query_policy_with_http_info(site_id, **kwargs)
            return data

    def query_policy_with_http_info(self, site_id, **kwargs):
        """
        查询站点升级
        ## 典型场景 ##    查询站点升级计划概要。 ## 接口功能 ##    查询站点升级计划概要。 ## 接口约束 ##    只有租户管理员获取token并建立会话后才能调用该接口。 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.query_policy_with_http_info(site_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str site_id: 站点ID。 (required)
        :param str device_model: 设备款型。 如果不填就是站点下全量的数据。 如果填写了设备款型，就是该站点下该款型的升级计划。 
        :return: PolicyConfigRes
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['site_id', 'device_model']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method query_policy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'site_id' is set
        if ('site_id' not in params) or (params['site_id'] is None):
            raise ValueError("Missing the required parameter `site_id` when calling `query_policy`")


        collection_formats = {}

        path_params = {}
        if 'site_id' in params:
            path_params['siteId'] = params['site_id']

        query_params = []
        if 'device_model' in params:
            query_params.append(('deviceModel', params['device_model']))

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

        return self.api_client.call_api('/controller/campus/v1/oamservice/upgrade/policy/{siteId}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='PolicyConfigRes',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def query_policy_detail(self, site_id, **kwargs):
        """
        查询设备升级
        ## 典型场景 ##    查询站点下具体设备的升级状态。 ## 接口功能 ##    查询站点下具体设备的升级状态。 ## 接口约束 ##    只有租户管理员获取token并建立会话后才能调用该接口。 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.query_policy_detail(site_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str site_id: 站点ID。 (required)
        :param str device_model: 设备款型。 如果不填就是站点下全量的数据。 如果填写了设备款型，就是该站点下该款型的升级状态。 
        :return: DeviceDetailListRes
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.query_policy_detail_with_http_info(site_id, **kwargs)
        else:
            (data) = self.query_policy_detail_with_http_info(site_id, **kwargs)
            return data

    def query_policy_detail_with_http_info(self, site_id, **kwargs):
        """
        查询设备升级
        ## 典型场景 ##    查询站点下具体设备的升级状态。 ## 接口功能 ##    查询站点下具体设备的升级状态。 ## 接口约束 ##    只有租户管理员获取token并建立会话后才能调用该接口。 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.query_policy_detail_with_http_info(site_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str site_id: 站点ID。 (required)
        :param str device_model: 设备款型。 如果不填就是站点下全量的数据。 如果填写了设备款型，就是该站点下该款型的升级状态。 
        :return: DeviceDetailListRes
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['site_id', 'device_model']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method query_policy_detail" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'site_id' is set
        if ('site_id' not in params) or (params['site_id'] is None):
            raise ValueError("Missing the required parameter `site_id` when calling `query_policy_detail`")


        collection_formats = {}

        path_params = {}
        if 'site_id' in params:
            path_params['siteId'] = params['site_id']

        query_params = []
        if 'device_model' in params:
            query_params.append(('deviceModel', params['device_model']))

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

        return self.api_client.call_api('/controller/campus/v1/oamservice/upgrade/policy-detail/{siteId}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='DeviceDetailListRes',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def query_version(self, device_model, **kwargs):
        """
        查询设备文件
        ## 典型场景 ##    根据设备款型查询可用文件列表。 ## 接口功能 ##    根据设备款型查询可用文件列表。 ## 接口约束 ##    只有租户管理员获取token并建立会话后才能调用该接口。 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.query_version(device_model, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str device_model: 设备款型。 (required)
        :return: AvailableVersion
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.query_version_with_http_info(device_model, **kwargs)
        else:
            (data) = self.query_version_with_http_info(device_model, **kwargs)
            return data

    def query_version_with_http_info(self, device_model, **kwargs):
        """
        查询设备文件
        ## 典型场景 ##    根据设备款型查询可用文件列表。 ## 接口功能 ##    根据设备款型查询可用文件列表。 ## 接口约束 ##    只有租户管理员获取token并建立会话后才能调用该接口。 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.query_version_with_http_info(device_model, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str device_model: 设备款型。 (required)
        :return: AvailableVersion
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['device_model']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method query_version" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'device_model' is set
        if ('device_model' not in params) or (params['device_model'] is None):
            raise ValueError("Missing the required parameter `device_model` when calling `query_version`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'device_model' in params:
            query_params.append(('deviceModel', params['device_model']))

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

        return self.api_client.call_api('/controller/campus/v1/oamservice/upgrade/version', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='AvailableVersion',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def re_upgrade(self, reupgrade_request_body, **kwargs):
        """
        重新升级设备
        ## 典型场景 ##    升级失败的设备重新升级。 ## 接口功能 ##    升级失败的设备重新升级。 ## 接口约束 ##    只有租户管理员获取token并建立会话后才能调用该接口。 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.re_upgrade(reupgrade_request_body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param ReupgradeRequestBody reupgrade_request_body: 重新升级入参。 (required)
        :return: CommonResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.re_upgrade_with_http_info(reupgrade_request_body, **kwargs)
        else:
            (data) = self.re_upgrade_with_http_info(reupgrade_request_body, **kwargs)
            return data

    def re_upgrade_with_http_info(self, reupgrade_request_body, **kwargs):
        """
        重新升级设备
        ## 典型场景 ##    升级失败的设备重新升级。 ## 接口功能 ##    升级失败的设备重新升级。 ## 接口约束 ##    只有租户管理员获取token并建立会话后才能调用该接口。 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.re_upgrade_with_http_info(reupgrade_request_body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param ReupgradeRequestBody reupgrade_request_body: 重新升级入参。 (required)
        :return: CommonResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['reupgrade_request_body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method re_upgrade" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'reupgrade_request_body' is set
        if ('reupgrade_request_body' not in params) or (params['reupgrade_request_body'] is None):
            raise ValueError("Missing the required parameter `reupgrade_request_body` when calling `re_upgrade`")


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'reupgrade_request_body' in params:
            body_params = params['reupgrade_request_body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/controller/campus/v1/oamservice/upgrade/reupgrade', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='CommonResponseBody',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
