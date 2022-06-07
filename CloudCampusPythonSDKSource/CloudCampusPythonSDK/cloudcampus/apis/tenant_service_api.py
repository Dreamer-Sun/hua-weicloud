# coding: utf-8

"""
    租户管理

    租户管理第三方北向接口。 · 提供租户创建接口 · 提供租户删除接口 · 提供租户查询接口 

    OpenAPI spec version: 1.0.2
    
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


class TenantServiceApi(object):
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

    def create_softcom_tenant(self, create_tenant_dto, **kwargs):
        """
        创建租户
        ## 典型场景 ##  创建租户。 ## 接口功能 ##  创建租户。 ## 接口约束 ##  支持MSP下面的北向管理员访问，该接口必须在用户会话建立后使用。 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_softcom_tenant(create_tenant_dto, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CreateTenantDto create_tenant_dto: 创建租户基本信息。 (required)
        :return: CreateTenantResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_softcom_tenant_with_http_info(create_tenant_dto, **kwargs)
        else:
            (data) = self.create_softcom_tenant_with_http_info(create_tenant_dto, **kwargs)
            return data

    def create_softcom_tenant_with_http_info(self, create_tenant_dto, **kwargs):
        """
        创建租户
        ## 典型场景 ##  创建租户。 ## 接口功能 ##  创建租户。 ## 接口约束 ##  支持MSP下面的北向管理员访问，该接口必须在用户会话建立后使用。 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_softcom_tenant_with_http_info(create_tenant_dto, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CreateTenantDto create_tenant_dto: 创建租户基本信息。 (required)
        :return: CreateTenantResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['create_tenant_dto']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_softcom_tenant" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'create_tenant_dto' is set
        if ('create_tenant_dto' not in params) or (params['create_tenant_dto'] is None):
            raise ValueError("Missing the required parameter `create_tenant_dto` when calling `create_softcom_tenant`")


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'create_tenant_dto' in params:
            body_params = params['create_tenant_dto']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/controller/campus/v1/baseservice/tenants/', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='CreateTenantResponseDto',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def delete_softcom_tenant(self, tenant_id, **kwargs):
        """
        删除租户
        ## 典型场景 ##  删除租户。 ## 接口功能 ##  通过租户标识删除租户。 ## 接口约束 ##  支持MSP下面的北向管理员访问，该接口必须在用户会话建立后使用。 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_softcom_tenant(tenant_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str tenant_id: 删除租户ID。 (required)
        :return: DeleteResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_softcom_tenant_with_http_info(tenant_id, **kwargs)
        else:
            (data) = self.delete_softcom_tenant_with_http_info(tenant_id, **kwargs)
            return data

    def delete_softcom_tenant_with_http_info(self, tenant_id, **kwargs):
        """
        删除租户
        ## 典型场景 ##  删除租户。 ## 接口功能 ##  通过租户标识删除租户。 ## 接口约束 ##  支持MSP下面的北向管理员访问，该接口必须在用户会话建立后使用。 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_softcom_tenant_with_http_info(tenant_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str tenant_id: 删除租户ID。 (required)
        :return: DeleteResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tenant_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_softcom_tenant" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tenant_id' is set
        if ('tenant_id' not in params) or (params['tenant_id'] is None):
            raise ValueError("Missing the required parameter `tenant_id` when calling `delete_softcom_tenant`")

        if 'tenant_id' in params and len(params['tenant_id']) > 36:
            raise ValueError("Invalid value for parameter `tenant_id` when calling `delete_softcom_tenant`, length must be less than or equal to `36`")
        if 'tenant_id' in params and len(params['tenant_id']) < 36:
            raise ValueError("Invalid value for parameter `tenant_id` when calling `delete_softcom_tenant`, length must be greater than or equal to `36`")

        collection_formats = {}

        path_params = {}
        if 'tenant_id' in params:
            path_params['tenantId'] = params['tenant_id']

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

        return self.api_client.call_api('/controller/campus/v1/baseservice/tenants/{tenantId}', 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='DeleteResponseDto',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def query_softcom_tenants(self, **kwargs):
        """
        查询租户
        ## 典型场景 ##  查询租户。 ## 接口功能 ##  提供分页查询租户列表功能。 ## 接口约束 ##  支持MSP下面的北向管理员访问，该接口必须在用户会话建立后使用，推荐使用分页查询，如果没有使用分页查询，可能会由于数据量多导致响应时间较长。 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.query_softcom_tenants(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page_index: 分页的序号。
        :param int page_size: 分页的大小。
        :return: TenantListDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.query_softcom_tenants_with_http_info(**kwargs)
        else:
            (data) = self.query_softcom_tenants_with_http_info(**kwargs)
            return data

    def query_softcom_tenants_with_http_info(self, **kwargs):
        """
        查询租户
        ## 典型场景 ##  查询租户。 ## 接口功能 ##  提供分页查询租户列表功能。 ## 接口约束 ##  支持MSP下面的北向管理员访问，该接口必须在用户会话建立后使用，推荐使用分页查询，如果没有使用分页查询，可能会由于数据量多导致响应时间较长。 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.query_softcom_tenants_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page_index: 分页的序号。
        :param int page_size: 分页的大小。
        :return: TenantListDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page_index', 'page_size']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method query_softcom_tenants" % key
                )
            params[key] = val
        del params['kwargs']

        if 'page_index' in params and params['page_index'] > 2147483647:
            raise ValueError("Invalid value for parameter `page_index` when calling `query_softcom_tenants`, must be a value less than or equal to `2147483647`")
        if 'page_index' in params and params['page_index'] < 0:
            raise ValueError("Invalid value for parameter `page_index` when calling `query_softcom_tenants`, must be a value greater than or equal to `0`")
        if 'page_size' in params and params['page_size'] > 1000:
            raise ValueError("Invalid value for parameter `page_size` when calling `query_softcom_tenants`, must be a value less than or equal to `1000`")
        if 'page_size' in params and params['page_size'] < 0:
            raise ValueError("Invalid value for parameter `page_size` when calling `query_softcom_tenants`, must be a value greater than or equal to `0`")

        collection_formats = {}

        path_params = {}

        query_params = []
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

        return self.api_client.call_api('/controller/campus/v1/baseservice/tenants/', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='TenantListDto',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)