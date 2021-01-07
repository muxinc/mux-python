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

class RealTimeApi(object):

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_realtime_breakdown(self, realtime_metric_id, **kwargs):  # noqa: E501
        """Get Real-Time Breakdown  # noqa: E501

        Gets breakdown information for a specific dimension and metric along with the number of concurrent viewers and negative impact score.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_realtime_breakdown(realtime_metric_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str realtime_metric_id: ID of the Realtime Metric (required)
        :param str dimension: Dimension the specified value belongs to
        :param float timestamp: Timestamp to limit results by. This value must be provided as a unix timestamp. Defaults to the current unix timestamp.
        :param list[str] filters: Filter key:value pairs. Must be provided as an array query string parameter (e.g. filters[]=operating_system:windows&filters[]=country:US).  Possible filter names are the same as returned by the List Filters endpoint. 
        :param str order_by: Value to order the results by
        :param str order_direction: Sort order.
        :return: GetRealTimeBreakdownResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_realtime_breakdown_with_http_info(realtime_metric_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_realtime_breakdown_with_http_info(realtime_metric_id, **kwargs)  # noqa: E501
            return data

    def get_realtime_breakdown_with_http_info(self, realtime_metric_id, **kwargs):  # noqa: E501
        """Get Real-Time Breakdown  # noqa: E501

        Gets breakdown information for a specific dimension and metric along with the number of concurrent viewers and negative impact score.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_realtime_breakdown_with_http_info(realtime_metric_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str realtime_metric_id: ID of the Realtime Metric (required)
        :param str dimension: Dimension the specified value belongs to
        :param float timestamp: Timestamp to limit results by. This value must be provided as a unix timestamp. Defaults to the current unix timestamp.
        :param list[str] filters: Filter key:value pairs. Must be provided as an array query string parameter (e.g. filters[]=operating_system:windows&filters[]=country:US).  Possible filter names are the same as returned by the List Filters endpoint. 
        :param str order_by: Value to order the results by
        :param str order_direction: Sort order.
        :return: GetRealTimeBreakdownResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['realtime_metric_id', 'dimension', 'timestamp', 'filters', 'order_by', 'order_direction']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_realtime_breakdown" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'realtime_metric_id' is set
        if ('realtime_metric_id' not in local_var_params or
                local_var_params['realtime_metric_id'] is None):
            raise ValueError("Missing the required parameter `realtime_metric_id` when calling `get_realtime_breakdown`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'realtime_metric_id' in local_var_params:
            path_params['REALTIME_METRIC_ID'] = local_var_params['realtime_metric_id']  # noqa: E501

        query_params = []
        if 'dimension' in local_var_params:
            query_params.append(('dimension', local_var_params['dimension']))  # noqa: E501
        if 'timestamp' in local_var_params:
            query_params.append(('timestamp', local_var_params['timestamp']))  # noqa: E501
        if 'filters' in local_var_params:
            query_params.append(('filters[]', local_var_params['filters']))  # noqa: E501
            collection_formats['filters[]'] = 'multi'  # noqa: E501
        if 'order_by' in local_var_params:
            query_params.append(('order_by', local_var_params['order_by']))  # noqa: E501
        if 'order_direction' in local_var_params:
            query_params.append(('order_direction', local_var_params['order_direction']))  # noqa: E501

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
            '/data/v1/realtime/metrics/{REALTIME_METRIC_ID}/breakdown', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetRealTimeBreakdownResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_realtime_histogram_timeseries(self, realtime_metric_id, **kwargs):  # noqa: E501
        """Get Real-Time Histogram Timeseries  # noqa: E501

        Gets histogram timeseries information for a specific metric.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_realtime_histogram_timeseries(realtime_metric_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str realtime_metric_id: ID of the Realtime Metric (required)
        :param list[str] filters: Filter key:value pairs. Must be provided as an array query string parameter (e.g. filters[]=operating_system:windows&filters[]=country:US).  Possible filter names are the same as returned by the List Filters endpoint. 
        :return: GetRealTimeHistogramTimeseriesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_realtime_histogram_timeseries_with_http_info(realtime_metric_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_realtime_histogram_timeseries_with_http_info(realtime_metric_id, **kwargs)  # noqa: E501
            return data

    def get_realtime_histogram_timeseries_with_http_info(self, realtime_metric_id, **kwargs):  # noqa: E501
        """Get Real-Time Histogram Timeseries  # noqa: E501

        Gets histogram timeseries information for a specific metric.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_realtime_histogram_timeseries_with_http_info(realtime_metric_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str realtime_metric_id: ID of the Realtime Metric (required)
        :param list[str] filters: Filter key:value pairs. Must be provided as an array query string parameter (e.g. filters[]=operating_system:windows&filters[]=country:US).  Possible filter names are the same as returned by the List Filters endpoint. 
        :return: GetRealTimeHistogramTimeseriesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['realtime_metric_id', 'filters']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_realtime_histogram_timeseries" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'realtime_metric_id' is set
        if ('realtime_metric_id' not in local_var_params or
                local_var_params['realtime_metric_id'] is None):
            raise ValueError("Missing the required parameter `realtime_metric_id` when calling `get_realtime_histogram_timeseries`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'realtime_metric_id' in local_var_params:
            path_params['REALTIME_METRIC_ID'] = local_var_params['realtime_metric_id']  # noqa: E501

        query_params = []
        if 'filters' in local_var_params:
            query_params.append(('filters[]', local_var_params['filters']))  # noqa: E501
            collection_formats['filters[]'] = 'multi'  # noqa: E501

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
            '/data/v1/realtime/metrics/{REALTIME_METRIC_ID}/histogram-timeseries', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetRealTimeHistogramTimeseriesResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_realtime_timeseries(self, realtime_metric_id, **kwargs):  # noqa: E501
        """Get Real-Time Timeseries  # noqa: E501

        Gets Time series information for a specific metric along with the number of concurrent viewers.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_realtime_timeseries(realtime_metric_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str realtime_metric_id: ID of the Realtime Metric (required)
        :param list[str] filters: Filter key:value pairs. Must be provided as an array query string parameter (e.g. filters[]=operating_system:windows&filters[]=country:US).  Possible filter names are the same as returned by the List Filters endpoint. 
        :return: GetRealTimeTimeseriesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_realtime_timeseries_with_http_info(realtime_metric_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_realtime_timeseries_with_http_info(realtime_metric_id, **kwargs)  # noqa: E501
            return data

    def get_realtime_timeseries_with_http_info(self, realtime_metric_id, **kwargs):  # noqa: E501
        """Get Real-Time Timeseries  # noqa: E501

        Gets Time series information for a specific metric along with the number of concurrent viewers.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_realtime_timeseries_with_http_info(realtime_metric_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str realtime_metric_id: ID of the Realtime Metric (required)
        :param list[str] filters: Filter key:value pairs. Must be provided as an array query string parameter (e.g. filters[]=operating_system:windows&filters[]=country:US).  Possible filter names are the same as returned by the List Filters endpoint. 
        :return: GetRealTimeTimeseriesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['realtime_metric_id', 'filters']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_realtime_timeseries" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'realtime_metric_id' is set
        if ('realtime_metric_id' not in local_var_params or
                local_var_params['realtime_metric_id'] is None):
            raise ValueError("Missing the required parameter `realtime_metric_id` when calling `get_realtime_timeseries`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'realtime_metric_id' in local_var_params:
            path_params['REALTIME_METRIC_ID'] = local_var_params['realtime_metric_id']  # noqa: E501

        query_params = []
        if 'filters' in local_var_params:
            query_params.append(('filters[]', local_var_params['filters']))  # noqa: E501
            collection_formats['filters[]'] = 'multi'  # noqa: E501

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
            '/data/v1/realtime/metrics/{REALTIME_METRIC_ID}/timeseries', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetRealTimeTimeseriesResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_realtime_dimensions(self, **kwargs):  # noqa: E501
        """List Real-Time Dimensions  # noqa: E501

        Lists availiable real-time dimensions   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_realtime_dimensions(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: ListRealTimeDimensionsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_realtime_dimensions_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_realtime_dimensions_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_realtime_dimensions_with_http_info(self, **kwargs):  # noqa: E501
        """List Real-Time Dimensions  # noqa: E501

        Lists availiable real-time dimensions   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_realtime_dimensions_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: ListRealTimeDimensionsResponse
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
                    " to method list_realtime_dimensions" % key
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
            '/data/v1/realtime/dimensions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ListRealTimeDimensionsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_realtime_metrics(self, **kwargs):  # noqa: E501
        """List Real-Time Metrics  # noqa: E501

        Lists availiable real-time metrics.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_realtime_metrics(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: ListRealTimeMetricsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_realtime_metrics_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_realtime_metrics_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_realtime_metrics_with_http_info(self, **kwargs):  # noqa: E501
        """List Real-Time Metrics  # noqa: E501

        Lists availiable real-time metrics.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_realtime_metrics_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: ListRealTimeMetricsResponse
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
                    " to method list_realtime_metrics" % key
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
            '/data/v1/realtime/metrics', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ListRealTimeMetricsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
