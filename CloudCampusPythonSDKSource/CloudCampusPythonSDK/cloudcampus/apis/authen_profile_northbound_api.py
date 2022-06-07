# coding: utf-8

"""
    认证模板管理

    认证模板北向接口定义 

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


class AuthenProfileNorthboundApi(object):
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

    def create_authen_profile(self, authen_profile_dto, **kwargs):
        """
        创建认证模板
        ## 典型场景 ##  提供创建认证模板的接口。<br> ## 接口功能 ##  提供创建认证模板的接口。 <br> ## 接口约束 ##  该接口支持租户管理员下北向接口管理访问，必须在用户会话建立后使用。 <br> 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_authen_profile(authen_profile_dto, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param AuthenProfileDto authen_profile_dto: 创建认证模板北向入参。 (required)
        :return: AuthenRespDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_authen_profile_with_http_info(authen_profile_dto, **kwargs)
        else:
            (data) = self.create_authen_profile_with_http_info(authen_profile_dto, **kwargs)
            return data

    def create_authen_profile_with_http_info(self, authen_profile_dto, **kwargs):
        """
        创建认证模板
        ## 典型场景 ##  提供创建认证模板的接口。<br> ## 接口功能 ##  提供创建认证模板的接口。 <br> ## 接口约束 ##  该接口支持租户管理员下北向接口管理访问，必须在用户会话建立后使用。 <br> 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_authen_profile_with_http_info(authen_profile_dto, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param AuthenProfileDto authen_profile_dto: 创建认证模板北向入参。 (required)
        :return: AuthenRespDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authen_profile_dto']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_authen_profile" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authen_profile_dto' is set
        if ('authen_profile_dto' not in params) or (params['authen_profile_dto'] is None):
            raise ValueError("Missing the required parameter `authen_profile_dto` when calling `create_authen_profile`")


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'authen_profile_dto' in params:
            body_params = params['authen_profile_dto']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/controller/campus/v3/networkconfig/openprofile/authenprofile', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='AuthenRespDto',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def delete_authen_profile(self, authen_profile_delete_dto, **kwargs):
        """
        删除认证模板
        ## 典型场景 ##  提供批量删除认证模板的接口。<br> ## 接口功能 ##  提供批量删除认证模板的接口。 <br> ## 接口约束 ##  该接口支持租户管理员下北向接口管理访问，必须在用户会话建立后使用。 <br> 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_authen_profile(authen_profile_delete_dto, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param AuthenProfileDeleteDto authen_profile_delete_dto: 删除认证模板北向入参。 (required)
        :return: AuthenProfileDeleteRespDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_authen_profile_with_http_info(authen_profile_delete_dto, **kwargs)
        else:
            (data) = self.delete_authen_profile_with_http_info(authen_profile_delete_dto, **kwargs)
            return data

    def delete_authen_profile_with_http_info(self, authen_profile_delete_dto, **kwargs):
        """
        删除认证模板
        ## 典型场景 ##  提供批量删除认证模板的接口。<br> ## 接口功能 ##  提供批量删除认证模板的接口。 <br> ## 接口约束 ##  该接口支持租户管理员下北向接口管理访问，必须在用户会话建立后使用。 <br> 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_authen_profile_with_http_info(authen_profile_delete_dto, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param AuthenProfileDeleteDto authen_profile_delete_dto: 删除认证模板北向入参。 (required)
        :return: AuthenProfileDeleteRespDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authen_profile_delete_dto']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_authen_profile" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authen_profile_delete_dto' is set
        if ('authen_profile_delete_dto' not in params) or (params['authen_profile_delete_dto'] is None):
            raise ValueError("Missing the required parameter `authen_profile_delete_dto` when calling `delete_authen_profile`")


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'authen_profile_delete_dto' in params:
            body_params = params['authen_profile_delete_dto']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/controller/campus/v3/networkconfig/openprofile/authenprofile/batch-delete', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='AuthenProfileDeleteRespDto',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_authen_profile(self, **kwargs):
        """
        查询认证模板
        ## 典型场景 ##  提供查询认证模板的接口。<br> ## 接口功能 ##  提供查询认证模板的接口。 <br> ## 接口约束 ##  该接口支持租户管理员下北向接口管理访问，必须在用户会话建立后使用。 <br> 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_authen_profile(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page_num: 页码。
        :param int page_size: 分页尺寸。
        :param str query_value: 认证模板名称模糊查询，支持精确和模糊匹配，不支持正则。
        :return: AuthenProfileQueryResultDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_authen_profile_with_http_info(**kwargs)
        else:
            (data) = self.get_authen_profile_with_http_info(**kwargs)
            return data

    def get_authen_profile_with_http_info(self, **kwargs):
        """
        查询认证模板
        ## 典型场景 ##  提供查询认证模板的接口。<br> ## 接口功能 ##  提供查询认证模板的接口。 <br> ## 接口约束 ##  该接口支持租户管理员下北向接口管理访问，必须在用户会话建立后使用。 <br> 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_authen_profile_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page_num: 页码。
        :param int page_size: 分页尺寸。
        :param str query_value: 认证模板名称模糊查询，支持精确和模糊匹配，不支持正则。
        :return: AuthenProfileQueryResultDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page_num', 'page_size', 'query_value']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_authen_profile" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page_num' in params:
            query_params.append(('pageNum', params['page_num']))
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))
        if 'query_value' in params:
            query_params.append(('queryValue', params['query_value']))

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

        return self.api_client.call_api('/controller/campus/v3/networkconfig/openprofile/authenprofile', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='AuthenProfileQueryResultDto',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_authen_profile_by_id(self, id, **kwargs):
        """
        根据ID查询认证模板
        ## 典型场景 ##  提供根据ID查询认证模板的接口。<br> ## 接口功能 ##  提供根据ID查询认证模板的接口。 <br> ## 接口约束 ##  该接口支持租户管理员下北向接口管理访问，必须在用户会话建立后使用。 <br> 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_authen_profile_by_id(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: 认证模板ID。 (required)
        :return: AuthenRespDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_authen_profile_by_id_with_http_info(id, **kwargs)
        else:
            (data) = self.get_authen_profile_by_id_with_http_info(id, **kwargs)
            return data

    def get_authen_profile_by_id_with_http_info(self, id, **kwargs):
        """
        根据ID查询认证模板
        ## 典型场景 ##  提供根据ID查询认证模板的接口。<br> ## 接口功能 ##  提供根据ID查询认证模板的接口。 <br> ## 接口约束 ##  该接口支持租户管理员下北向接口管理访问，必须在用户会话建立后使用。 <br> 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_authen_profile_by_id_with_http_info(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: 认证模板ID。 (required)
        :return: AuthenRespDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_authen_profile_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_authen_profile_by_id`")


        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

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

        return self.api_client.call_api('/controller/campus/v3/networkconfig/openprofile/authenprofile/{id}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='AuthenRespDto',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update_authen_profile(self, id, authen_profile_dto, **kwargs):
        """
        更新认证模板
        ## 典型场景 ##  提供更新认证模板的接口。<br> ## 接口功能 ##  提供更新认证模板的接口。 <br> ## 接口约束 ##  该接口支持租户管理员下北向接口管理访问，必须在用户会话建立后使用。 <br> 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_authen_profile(id, authen_profile_dto, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: 认证模板ID。 (required)
        :param AuthenProfileDto authen_profile_dto: 更新认证模板北向入参。 (required)
        :return: AuthenRespDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_authen_profile_with_http_info(id, authen_profile_dto, **kwargs)
        else:
            (data) = self.update_authen_profile_with_http_info(id, authen_profile_dto, **kwargs)
            return data

    def update_authen_profile_with_http_info(self, id, authen_profile_dto, **kwargs):
        """
        更新认证模板
        ## 典型场景 ##  提供更新认证模板的接口。<br> ## 接口功能 ##  提供更新认证模板的接口。 <br> ## 接口约束 ##  该接口支持租户管理员下北向接口管理访问，必须在用户会话建立后使用。 <br> 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_authen_profile_with_http_info(id, authen_profile_dto, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: 认证模板ID。 (required)
        :param AuthenProfileDto authen_profile_dto: 更新认证模板北向入参。 (required)
        :return: AuthenRespDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'authen_profile_dto']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_authen_profile" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_authen_profile`")
        # verify the required parameter 'authen_profile_dto' is set
        if ('authen_profile_dto' not in params) or (params['authen_profile_dto'] is None):
            raise ValueError("Missing the required parameter `authen_profile_dto` when calling `update_authen_profile`")


        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'authen_profile_dto' in params:
            body_params = params['authen_profile_dto']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/controller/campus/v3/networkconfig/openprofile/authenprofile/{id}', 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='AuthenRespDto',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)