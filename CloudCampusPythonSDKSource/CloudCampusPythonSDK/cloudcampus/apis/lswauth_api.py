# coding: utf-8

"""
    交换机有线认证模板配置

    交换机有线认证模板，主要包括： · 创建站点下交换机有线认证模板配置 · 查询站点下交换机有线认证模板配置 · 修改站点下交换机有线认证模板配置 · 删除站点下交换机有线认证模板配置 · 修改站点交换机有线认证部分模板配置 · 增量绑站点交换机有线认证模板配置定 

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


class LswauthApi(object):
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

    def create_lsw_auth(self, lsw_auth_config_core, site_id, **kwargs):
        """
        创建站点下交换机有线认证模板配置
        ## 典型场景 ##  创建站点下交换机有线认证模板配置。<br> ## 接口功能 ##  创建站点下交换机有线认证模板配置。 <br> ## 接口约束 ##  该接口支持租户下北向接口管理员访问，必须在用户会话建立后使用。 <br> 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_lsw_auth(lsw_auth_config_core, site_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param LswAuthConfigCore lsw_auth_config_core: 交换机认证模板配置信息。 (required)
        :param str site_id: 站点标识，UUID格式。 (required)
        :return: LswAuthConfigResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_lsw_auth_with_http_info(lsw_auth_config_core, site_id, **kwargs)
        else:
            (data) = self.create_lsw_auth_with_http_info(lsw_auth_config_core, site_id, **kwargs)
            return data

    def create_lsw_auth_with_http_info(self, lsw_auth_config_core, site_id, **kwargs):
        """
        创建站点下交换机有线认证模板配置
        ## 典型场景 ##  创建站点下交换机有线认证模板配置。<br> ## 接口功能 ##  创建站点下交换机有线认证模板配置。 <br> ## 接口约束 ##  该接口支持租户下北向接口管理员访问，必须在用户会话建立后使用。 <br> 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_lsw_auth_with_http_info(lsw_auth_config_core, site_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param LswAuthConfigCore lsw_auth_config_core: 交换机认证模板配置信息。 (required)
        :param str site_id: 站点标识，UUID格式。 (required)
        :return: LswAuthConfigResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['lsw_auth_config_core', 'site_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_lsw_auth" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'lsw_auth_config_core' is set
        if ('lsw_auth_config_core' not in params) or (params['lsw_auth_config_core'] is None):
            raise ValueError("Missing the required parameter `lsw_auth_config_core` when calling `create_lsw_auth`")
        # verify the required parameter 'site_id' is set
        if ('site_id' not in params) or (params['site_id'] is None):
            raise ValueError("Missing the required parameter `site_id` when calling `create_lsw_auth`")

        if 'site_id' in params and len(params['site_id']) > 36:
            raise ValueError("Invalid value for parameter `site_id` when calling `create_lsw_auth`, length must be less than or equal to `36`")
        if 'site_id' in params and len(params['site_id']) < 36:
            raise ValueError("Invalid value for parameter `site_id` when calling `create_lsw_auth`, length must be greater than or equal to `36`")

        collection_formats = {}

        path_params = {}
        if 'site_id' in params:
            path_params['siteId'] = params['site_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'lsw_auth_config_core' in params:
            body_params = params['lsw_auth_config_core']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/controller/campus/v1/authconfigservice/accessconfig/lswauth/{siteId}/profiles', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='LswAuthConfigResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def delete_lsw_auth(self, site_id, ids, **kwargs):
        """
        删除站点下交换机有线认证模板配置
        ## 典型场景 ##  批量删除站点下交换机有线认证模板。<br> ## 接口功能 ##  批量删除站点下交换机有线认证模板。 <br> ## 接口约束 ##  该接口支持租户下北向接口管理员访问，必须在用户会话建立后使用。 <br> 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_lsw_auth(site_id, ids, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str site_id: 站点标识，UUID格式。 (required)
        :param LswAuthDeleteDto ids: 待删除的有线认证模板。 (required)
        :return: DeleteAuthResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_lsw_auth_with_http_info(site_id, ids, **kwargs)
        else:
            (data) = self.delete_lsw_auth_with_http_info(site_id, ids, **kwargs)
            return data

    def delete_lsw_auth_with_http_info(self, site_id, ids, **kwargs):
        """
        删除站点下交换机有线认证模板配置
        ## 典型场景 ##  批量删除站点下交换机有线认证模板。<br> ## 接口功能 ##  批量删除站点下交换机有线认证模板。 <br> ## 接口约束 ##  该接口支持租户下北向接口管理员访问，必须在用户会话建立后使用。 <br> 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_lsw_auth_with_http_info(site_id, ids, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str site_id: 站点标识，UUID格式。 (required)
        :param LswAuthDeleteDto ids: 待删除的有线认证模板。 (required)
        :return: DeleteAuthResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['site_id', 'ids']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_lsw_auth" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'site_id' is set
        if ('site_id' not in params) or (params['site_id'] is None):
            raise ValueError("Missing the required parameter `site_id` when calling `delete_lsw_auth`")
        # verify the required parameter 'ids' is set
        if ('ids' not in params) or (params['ids'] is None):
            raise ValueError("Missing the required parameter `ids` when calling `delete_lsw_auth`")

        if 'site_id' in params and len(params['site_id']) > 36:
            raise ValueError("Invalid value for parameter `site_id` when calling `delete_lsw_auth`, length must be less than or equal to `36`")
        if 'site_id' in params and len(params['site_id']) < 36:
            raise ValueError("Invalid value for parameter `site_id` when calling `delete_lsw_auth`, length must be greater than or equal to `36`")

        collection_formats = {}

        path_params = {}
        if 'site_id' in params:
            path_params['siteId'] = params['site_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'ids' in params:
            body_params = params['ids']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/controller/campus/v1/authconfigservice/accessconfig/lswauth/{siteId}/profiles/batch-delete', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='DeleteAuthResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_lsw_auth(self, site_id, **kwargs):
        """
        查询站点下交换机有线认证模板配置
        ## 典型场景 ##  查询指定站点内交换机有线认证模板列表。<br> ## 接口功能 ##  查询站点下交换机有线认证模板列表。 <br> ## 接口约束 ##  该接口支持租户下北向接口管理员访问，必须在用户会话建立后使用。 <br> 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_lsw_auth(site_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str site_id: 站点标识，UUID格式。 (required)
        :param str profile_name: 认证模板名称，支持模糊查询。
        :param str policy_id: 认证模板ID，UUID格式。
        :return: LswAuthConfigResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_lsw_auth_with_http_info(site_id, **kwargs)
        else:
            (data) = self.get_lsw_auth_with_http_info(site_id, **kwargs)
            return data

    def get_lsw_auth_with_http_info(self, site_id, **kwargs):
        """
        查询站点下交换机有线认证模板配置
        ## 典型场景 ##  查询指定站点内交换机有线认证模板列表。<br> ## 接口功能 ##  查询站点下交换机有线认证模板列表。 <br> ## 接口约束 ##  该接口支持租户下北向接口管理员访问，必须在用户会话建立后使用。 <br> 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_lsw_auth_with_http_info(site_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str site_id: 站点标识，UUID格式。 (required)
        :param str profile_name: 认证模板名称，支持模糊查询。
        :param str policy_id: 认证模板ID，UUID格式。
        :return: LswAuthConfigResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['site_id', 'profile_name', 'policy_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_lsw_auth" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'site_id' is set
        if ('site_id' not in params) or (params['site_id'] is None):
            raise ValueError("Missing the required parameter `site_id` when calling `get_lsw_auth`")

        if 'site_id' in params and len(params['site_id']) > 36:
            raise ValueError("Invalid value for parameter `site_id` when calling `get_lsw_auth`, length must be less than or equal to `36`")
        if 'site_id' in params and len(params['site_id']) < 36:
            raise ValueError("Invalid value for parameter `site_id` when calling `get_lsw_auth`, length must be greater than or equal to `36`")
        if 'profile_name' in params and len(params['profile_name']) > 128:
            raise ValueError("Invalid value for parameter `profile_name` when calling `get_lsw_auth`, length must be less than or equal to `128`")
        if 'profile_name' in params and len(params['profile_name']) < 1:
            raise ValueError("Invalid value for parameter `profile_name` when calling `get_lsw_auth`, length must be greater than or equal to `1`")
        if 'policy_id' in params and len(params['policy_id']) > 36:
            raise ValueError("Invalid value for parameter `policy_id` when calling `get_lsw_auth`, length must be less than or equal to `36`")
        if 'policy_id' in params and len(params['policy_id']) < 36:
            raise ValueError("Invalid value for parameter `policy_id` when calling `get_lsw_auth`, length must be greater than or equal to `36`")

        collection_formats = {}

        path_params = {}
        if 'site_id' in params:
            path_params['siteId'] = params['site_id']

        query_params = []
        if 'profile_name' in params:
            query_params.append(('profileName', params['profile_name']))
        if 'policy_id' in params:
            query_params.append(('policyId', params['policy_id']))

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

        return self.api_client.call_api('/controller/campus/v1/authconfigservice/accessconfig/lswauth/{siteId}/profiles', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='LswAuthConfigResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update_lsw_auth(self, site_id, profile_id, lsw_auth_config, **kwargs):
        """
        修改站点下交换机有线认证模板配置
        ## 典型场景 ##  修改站点下交换机有线认证模板。<br> ## 接口功能 ##  修改站点下交换机有线认证模板。 <br> ## 接口约束 ##  该接口支持租户下北向接口管理员访问，必须在用户会话建立后使用。 <br> 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_lsw_auth(site_id, profile_id, lsw_auth_config, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str site_id: 站点标识，UUID格式。 (required)
        :param str profile_id: 认证模板ID，UUID格式。 (required)
        :param LswAuthConfig lsw_auth_config: 有线认证配置。 (required)
        :return: LswAuthConfigResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_lsw_auth_with_http_info(site_id, profile_id, lsw_auth_config, **kwargs)
        else:
            (data) = self.update_lsw_auth_with_http_info(site_id, profile_id, lsw_auth_config, **kwargs)
            return data

    def update_lsw_auth_with_http_info(self, site_id, profile_id, lsw_auth_config, **kwargs):
        """
        修改站点下交换机有线认证模板配置
        ## 典型场景 ##  修改站点下交换机有线认证模板。<br> ## 接口功能 ##  修改站点下交换机有线认证模板。 <br> ## 接口约束 ##  该接口支持租户下北向接口管理员访问，必须在用户会话建立后使用。 <br> 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_lsw_auth_with_http_info(site_id, profile_id, lsw_auth_config, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str site_id: 站点标识，UUID格式。 (required)
        :param str profile_id: 认证模板ID，UUID格式。 (required)
        :param LswAuthConfig lsw_auth_config: 有线认证配置。 (required)
        :return: LswAuthConfigResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['site_id', 'profile_id', 'lsw_auth_config']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_lsw_auth" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'site_id' is set
        if ('site_id' not in params) or (params['site_id'] is None):
            raise ValueError("Missing the required parameter `site_id` when calling `update_lsw_auth`")
        # verify the required parameter 'profile_id' is set
        if ('profile_id' not in params) or (params['profile_id'] is None):
            raise ValueError("Missing the required parameter `profile_id` when calling `update_lsw_auth`")
        # verify the required parameter 'lsw_auth_config' is set
        if ('lsw_auth_config' not in params) or (params['lsw_auth_config'] is None):
            raise ValueError("Missing the required parameter `lsw_auth_config` when calling `update_lsw_auth`")

        if 'site_id' in params and len(params['site_id']) > 36:
            raise ValueError("Invalid value for parameter `site_id` when calling `update_lsw_auth`, length must be less than or equal to `36`")
        if 'site_id' in params and len(params['site_id']) < 36:
            raise ValueError("Invalid value for parameter `site_id` when calling `update_lsw_auth`, length must be greater than or equal to `36`")
        if 'profile_id' in params and len(params['profile_id']) > 36:
            raise ValueError("Invalid value for parameter `profile_id` when calling `update_lsw_auth`, length must be less than or equal to `36`")
        if 'profile_id' in params and len(params['profile_id']) < 36:
            raise ValueError("Invalid value for parameter `profile_id` when calling `update_lsw_auth`, length must be greater than or equal to `36`")

        collection_formats = {}

        path_params = {}
        if 'site_id' in params:
            path_params['siteId'] = params['site_id']
        if 'profile_id' in params:
            path_params['profileId'] = params['profile_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'lsw_auth_config' in params:
            body_params = params['lsw_auth_config']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/controller/campus/v1/authconfigservice/accessconfig/lswauth/{siteId}/profiles/{profileId}', 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='LswAuthConfigResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update_lsw_auth_inc(self, site_id, profile_id, lsw_device_info, **kwargs):
        """
        增量绑定交换机无线认证模板配置
        ## 典型场景 ##  交换机无线认证配置增量绑定设备。<br> ## 接口功能 ##  交换机无线认证配置增量绑定设备。 <br> ## 接口约束 ##  该接口支持租户下北向接口管理员访问，必须在用户会话建立后使用。 <br> 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_lsw_auth_inc(site_id, profile_id, lsw_device_info, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str site_id: 站点标识，UUID格式。 (required)
        :param str profile_id: 认证模板ID，UUID格式。 (required)
        :param LswDeviceInfo lsw_device_info: 设备接口列表。 (required)
        :return: LswAuthConfigResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_lsw_auth_inc_with_http_info(site_id, profile_id, lsw_device_info, **kwargs)
        else:
            (data) = self.update_lsw_auth_inc_with_http_info(site_id, profile_id, lsw_device_info, **kwargs)
            return data

    def update_lsw_auth_inc_with_http_info(self, site_id, profile_id, lsw_device_info, **kwargs):
        """
        增量绑定交换机无线认证模板配置
        ## 典型场景 ##  交换机无线认证配置增量绑定设备。<br> ## 接口功能 ##  交换机无线认证配置增量绑定设备。 <br> ## 接口约束 ##  该接口支持租户下北向接口管理员访问，必须在用户会话建立后使用。 <br> 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_lsw_auth_inc_with_http_info(site_id, profile_id, lsw_device_info, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str site_id: 站点标识，UUID格式。 (required)
        :param str profile_id: 认证模板ID，UUID格式。 (required)
        :param LswDeviceInfo lsw_device_info: 设备接口列表。 (required)
        :return: LswAuthConfigResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['site_id', 'profile_id', 'lsw_device_info']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_lsw_auth_inc" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'site_id' is set
        if ('site_id' not in params) or (params['site_id'] is None):
            raise ValueError("Missing the required parameter `site_id` when calling `update_lsw_auth_inc`")
        # verify the required parameter 'profile_id' is set
        if ('profile_id' not in params) or (params['profile_id'] is None):
            raise ValueError("Missing the required parameter `profile_id` when calling `update_lsw_auth_inc`")
        # verify the required parameter 'lsw_device_info' is set
        if ('lsw_device_info' not in params) or (params['lsw_device_info'] is None):
            raise ValueError("Missing the required parameter `lsw_device_info` when calling `update_lsw_auth_inc`")

        if 'site_id' in params and len(params['site_id']) > 36:
            raise ValueError("Invalid value for parameter `site_id` when calling `update_lsw_auth_inc`, length must be less than or equal to `36`")
        if 'site_id' in params and len(params['site_id']) < 36:
            raise ValueError("Invalid value for parameter `site_id` when calling `update_lsw_auth_inc`, length must be greater than or equal to `36`")
        if 'profile_id' in params and len(params['profile_id']) > 36:
            raise ValueError("Invalid value for parameter `profile_id` when calling `update_lsw_auth_inc`, length must be less than or equal to `36`")
        if 'profile_id' in params and len(params['profile_id']) < 36:
            raise ValueError("Invalid value for parameter `profile_id` when calling `update_lsw_auth_inc`, length must be greater than or equal to `36`")

        collection_formats = {}

        path_params = {}
        if 'site_id' in params:
            path_params['siteId'] = params['site_id']
        if 'profile_id' in params:
            path_params['profileId'] = params['profile_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'lsw_device_info' in params:
            body_params = params['lsw_device_info']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/controller/campus/v1/authconfigservice/accessconfig/lswauth/{siteId}/profiles/{profileId}/devices', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='LswAuthConfigResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update_lsw_auth_pro_inc(self, site_id, profile_id, lsw_auth_config_profile, **kwargs):
        """
        修改站点交换机有线认证部分模板配置
        ## 典型场景 ##  修改站点交换机有线认证部分模板配置。<br> ## 接口功能 ##  修改站点交换机有线认证部分模板配置。 <br> ## 接口约束 ##  该接口支持租户下北向接口管理员访问，必须在用户会话建立后使用。 <br> 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_lsw_auth_pro_inc(site_id, profile_id, lsw_auth_config_profile, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str site_id: 站点标识，UUID格式。 (required)
        :param str profile_id: 认证模板ID，UUID格式。 (required)
        :param LswAuthConfigProfile lsw_auth_config_profile: 有线认证配置。 (required)
        :return: LswAuthConfigResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_lsw_auth_pro_inc_with_http_info(site_id, profile_id, lsw_auth_config_profile, **kwargs)
        else:
            (data) = self.update_lsw_auth_pro_inc_with_http_info(site_id, profile_id, lsw_auth_config_profile, **kwargs)
            return data

    def update_lsw_auth_pro_inc_with_http_info(self, site_id, profile_id, lsw_auth_config_profile, **kwargs):
        """
        修改站点交换机有线认证部分模板配置
        ## 典型场景 ##  修改站点交换机有线认证部分模板配置。<br> ## 接口功能 ##  修改站点交换机有线认证部分模板配置。 <br> ## 接口约束 ##  该接口支持租户下北向接口管理员访问，必须在用户会话建立后使用。 <br> 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_lsw_auth_pro_inc_with_http_info(site_id, profile_id, lsw_auth_config_profile, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str site_id: 站点标识，UUID格式。 (required)
        :param str profile_id: 认证模板ID，UUID格式。 (required)
        :param LswAuthConfigProfile lsw_auth_config_profile: 有线认证配置。 (required)
        :return: LswAuthConfigResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['site_id', 'profile_id', 'lsw_auth_config_profile']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_lsw_auth_pro_inc" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'site_id' is set
        if ('site_id' not in params) or (params['site_id'] is None):
            raise ValueError("Missing the required parameter `site_id` when calling `update_lsw_auth_pro_inc`")
        # verify the required parameter 'profile_id' is set
        if ('profile_id' not in params) or (params['profile_id'] is None):
            raise ValueError("Missing the required parameter `profile_id` when calling `update_lsw_auth_pro_inc`")
        # verify the required parameter 'lsw_auth_config_profile' is set
        if ('lsw_auth_config_profile' not in params) or (params['lsw_auth_config_profile'] is None):
            raise ValueError("Missing the required parameter `lsw_auth_config_profile` when calling `update_lsw_auth_pro_inc`")

        if 'site_id' in params and len(params['site_id']) > 36:
            raise ValueError("Invalid value for parameter `site_id` when calling `update_lsw_auth_pro_inc`, length must be less than or equal to `36`")
        if 'site_id' in params and len(params['site_id']) < 36:
            raise ValueError("Invalid value for parameter `site_id` when calling `update_lsw_auth_pro_inc`, length must be greater than or equal to `36`")
        if 'profile_id' in params and len(params['profile_id']) > 36:
            raise ValueError("Invalid value for parameter `profile_id` when calling `update_lsw_auth_pro_inc`, length must be less than or equal to `36`")
        if 'profile_id' in params and len(params['profile_id']) < 36:
            raise ValueError("Invalid value for parameter `profile_id` when calling `update_lsw_auth_pro_inc`, length must be greater than or equal to `36`")

        collection_formats = {}

        path_params = {}
        if 'site_id' in params:
            path_params['siteId'] = params['site_id']
        if 'profile_id' in params:
            path_params['profileId'] = params['profile_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'lsw_auth_config_profile' in params:
            body_params = params['lsw_auth_config_profile']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/controller/campus/v1/authconfigservice/accessconfig/lswauth/{siteId}/profileInfos/{profileId}', 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='LswAuthConfigResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
