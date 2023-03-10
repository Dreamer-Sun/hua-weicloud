# coding: utf-8

"""
    运维ping/trace探测

    ping/trace探测第三方接口。 · 创建ping探测任务 · 查询ping探测结果 · 创建trace探测任务 · 查询trace探测结果 

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


class TraceDiagnoseServiceApi(object):
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

    def create_trace_task(self, request, **kwargs):
        """
        创建Trace探测任务
        ## 典型场景 ##  创建Trace探测任务。 ## 接口功能 ##  创建Trace探测任务。 ## 接口约束 ##  只有租户管理员获取token并建立会话后才能调用该接口。 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_trace_task(request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param TraceDiagnoseDto request: 请求参数。 (required)
        :return: TraceTaskResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_trace_task_with_http_info(request, **kwargs)
        else:
            (data) = self.create_trace_task_with_http_info(request, **kwargs)
            return data

    def create_trace_task_with_http_info(self, request, **kwargs):
        """
        创建Trace探测任务
        ## 典型场景 ##  创建Trace探测任务。 ## 接口功能 ##  创建Trace探测任务。 ## 接口约束 ##  只有租户管理员获取token并建立会话后才能调用该接口。 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_trace_task_with_http_info(request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param TraceDiagnoseDto request: 请求参数。 (required)
        :return: TraceTaskResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['request']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_trace_task" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'request' is set
        if ('request' not in params) or (params['request'] is None):
            raise ValueError("Missing the required parameter `request` when calling `create_trace_task`")


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'request' in params:
            body_params = params['request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/controller/campus/v1/oamservice/trace', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='TraceTaskResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def query_trace_task_by_task_id(self, task_id, **kwargs):
        """
        查询Trace探测结果
        ## 典型场景 ##  根据taskId查询trace任务。 ## 接口功能 ##  查询Trace探测任务。 ## 接口约束 ##  只有租户管理员获取token并建立会话后才能调用该接口。 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.query_trace_task_by_task_id(task_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str task_id: Trace探测任务ID，格式UUID。 (required)
        :return: TraceReplyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.query_trace_task_by_task_id_with_http_info(task_id, **kwargs)
        else:
            (data) = self.query_trace_task_by_task_id_with_http_info(task_id, **kwargs)
            return data

    def query_trace_task_by_task_id_with_http_info(self, task_id, **kwargs):
        """
        查询Trace探测结果
        ## 典型场景 ##  根据taskId查询trace任务。 ## 接口功能 ##  查询Trace探测任务。 ## 接口约束 ##  只有租户管理员获取token并建立会话后才能调用该接口。 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.query_trace_task_by_task_id_with_http_info(task_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str task_id: Trace探测任务ID，格式UUID。 (required)
        :return: TraceReplyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['task_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method query_trace_task_by_task_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'task_id' is set
        if ('task_id' not in params) or (params['task_id'] is None):
            raise ValueError("Missing the required parameter `task_id` when calling `query_trace_task_by_task_id`")

        if 'task_id' in params and len(params['task_id']) > 36:
            raise ValueError("Invalid value for parameter `task_id` when calling `query_trace_task_by_task_id`, length must be less than or equal to `36`")
        if 'task_id' in params and len(params['task_id']) < 36:
            raise ValueError("Invalid value for parameter `task_id` when calling `query_trace_task_by_task_id`, length must be greater than or equal to `36`")

        collection_formats = {}

        path_params = {}
        if 'task_id' in params:
            path_params['taskId'] = params['task_id']

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

        return self.api_client.call_api('/controller/campus/v1/oamservice/trace/{taskId}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='TraceReplyResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
