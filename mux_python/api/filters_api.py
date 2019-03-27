# coding: utf-8

"""
Mux Python - Copyright 2019 Mux Inc.

NOTE: This class is auto generated. Do not edit the class manually.
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from mux_python.api_client import ApiClient

class FiltersApi(object):

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def list_filter_values(self, filter_id, **kwargs):  # noqa: E501
        """Lists values for a specific filter  # noqa: E501

        Lists the values for a filter along with a total count of related views   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_filter_values(filter_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str filter_id: ID of the Filter (required)
        :param int limit: Number of items to include in the response
        :param int page: Offset by this many pages, of the size of `limit`
        :param list[str] filters: Filter key:value pairs. Must be provided as an array query string parameter (e.g. filters[]=operating_system:windows&filters[]=country:US).  Possible filter names are the same as returned by the List Filters endpoint. 
        :param list[str] timeframe: Timeframe window to limit results by. Must be provided as an array query string parameter (e.g. timeframe[]=). Accepted formats are...   * array of epoch timestamps e.g. timeframe[]=1498867200&timeframe[]=1498953600    * duration string e.g. timeframe[]=24:hours or timeframe[]=7:days. 
        :return: ListFilterValuesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_filter_values_with_http_info(filter_id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_filter_values_with_http_info(filter_id, **kwargs)  # noqa: E501
            return data

    def list_filter_values_with_http_info(self, filter_id, **kwargs):  # noqa: E501
        """Lists values for a specific filter  # noqa: E501

        Lists the values for a filter along with a total count of related views   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_filter_values_with_http_info(filter_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str filter_id: ID of the Filter (required)
        :param int limit: Number of items to include in the response
        :param int page: Offset by this many pages, of the size of `limit`
        :param list[str] filters: Filter key:value pairs. Must be provided as an array query string parameter (e.g. filters[]=operating_system:windows&filters[]=country:US).  Possible filter names are the same as returned by the List Filters endpoint. 
        :param list[str] timeframe: Timeframe window to limit results by. Must be provided as an array query string parameter (e.g. timeframe[]=). Accepted formats are...   * array of epoch timestamps e.g. timeframe[]=1498867200&timeframe[]=1498953600    * duration string e.g. timeframe[]=24:hours or timeframe[]=7:days. 
        :return: ListFilterValuesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['filter_id', 'limit', 'page', 'filters', 'timeframe']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_filter_values" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'filter_id' is set
        if ('filter_id' not in local_var_params or
                local_var_params['filter_id'] is None):
            raise ValueError("Missing the required parameter `filter_id` when calling `list_filter_values`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'filter_id' in local_var_params:
            path_params['FILTER_ID'] = local_var_params['filter_id']  # noqa: E501

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))  # noqa: E501
        if 'filters' in local_var_params:
            query_params.append(('filters[]', local_var_params['filters']))  # noqa: E501
            collection_formats['filters[]'] = 'multi'  # noqa: E501
        if 'timeframe' in local_var_params:
            query_params.append(('timeframe[]', local_var_params['timeframe']))  # noqa: E501
            collection_formats['timeframe[]'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['accessToken']  # noqa: E501

        return self.api_client.call_api(
            '/data/v1/filters/{FILTER_ID}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ListFilterValuesResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_filters(self, **kwargs):  # noqa: E501
        """List Filters  # noqa: E501

        Lists all the filters broken out into basic and advanced   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_filters(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: ListFiltersResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_filters_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_filters_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_filters_with_http_info(self, **kwargs):  # noqa: E501
        """List Filters  # noqa: E501

        Lists all the filters broken out into basic and advanced   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_filters_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: ListFiltersResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_filters" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['accessToken']  # noqa: E501

        return self.api_client.call_api(
            '/data/v1/filters', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ListFiltersResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
