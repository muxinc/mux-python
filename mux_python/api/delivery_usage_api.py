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

class DeliveryUsageApi(object):

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def list_delivery_usage(self, **kwargs):  # noqa: E501
        """List Usage  # noqa: E501

        Returns a list of delivery usage records and their associated Asset IDs or Live Stream IDs.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_delivery_usage(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: Offset by this many pages, of the size of `limit`
        :param int limit: Number of items to include in the response
        :param str asset_id: Filter response to return delivery usage for this asset only.
        :param list[str] timeframe: Time window to get delivery usage information. timeframe[0] indicates the start time, timeframe[1] indicates the end time in seconds since the Unix epoch. Default time window is 1 hour representing usage from 13th to 12th hour from when the request is made. 
        :return: ListDeliveryUsageResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_delivery_usage_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_delivery_usage_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_delivery_usage_with_http_info(self, **kwargs):  # noqa: E501
        """List Usage  # noqa: E501

        Returns a list of delivery usage records and their associated Asset IDs or Live Stream IDs.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_delivery_usage_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: Offset by this many pages, of the size of `limit`
        :param int limit: Number of items to include in the response
        :param str asset_id: Filter response to return delivery usage for this asset only.
        :param list[str] timeframe: Time window to get delivery usage information. timeframe[0] indicates the start time, timeframe[1] indicates the end time in seconds since the Unix epoch. Default time window is 1 hour representing usage from 13th to 12th hour from when the request is made. 
        :return: ListDeliveryUsageResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['page', 'limit', 'asset_id', 'timeframe']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_delivery_usage" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))  # noqa: E501
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'asset_id' in local_var_params:
            query_params.append(('asset_id', local_var_params['asset_id']))  # noqa: E501
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
            '/video/v1/delivery-usage', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ListDeliveryUsageResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
