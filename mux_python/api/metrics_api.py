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

class MetricsApi(object):

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_metric_timeseries_data(self, metric_id, **kwargs):  # noqa: E501
        """Get metric timeseries data  # noqa: E501

        Returns timeseries data for a specific metric   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_metric_timeseries_data(metric_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str metric_id: ID of the Metric (required)
        :param list[str] timeframe: Timeframe window to limit results by. Must be provided as an array query string parameter (e.g. timeframe[]=). Accepted formats are...   * array of epoch timestamps e.g. timeframe[]=1498867200&timeframe[]=1498953600    * duration string e.g. timeframe[]=24:hours or timeframe[]=7:days. 
        :param list[str] filters: Filter key:value pairs. Must be provided as an array query string parameter (e.g. filters[]=operating_system:windows&filters[]=country:US).  Possible filter names are the same as returned by the List Filters endpoint. 
        :param str measurement: Measurement for the provided metric. If omitted, the deafult for the metric will be used.
        :param str order_direction: Sort order.
        :param str group_by: Time granularity to group results by. If this value is omitted, a default granularity is chosen based on the supplied timeframe.
        :return: GetMetricTimeseriesDataResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_metric_timeseries_data_with_http_info(metric_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_metric_timeseries_data_with_http_info(metric_id, **kwargs)  # noqa: E501
            return data

    def get_metric_timeseries_data_with_http_info(self, metric_id, **kwargs):  # noqa: E501
        """Get metric timeseries data  # noqa: E501

        Returns timeseries data for a specific metric   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_metric_timeseries_data_with_http_info(metric_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str metric_id: ID of the Metric (required)
        :param list[str] timeframe: Timeframe window to limit results by. Must be provided as an array query string parameter (e.g. timeframe[]=). Accepted formats are...   * array of epoch timestamps e.g. timeframe[]=1498867200&timeframe[]=1498953600    * duration string e.g. timeframe[]=24:hours or timeframe[]=7:days. 
        :param list[str] filters: Filter key:value pairs. Must be provided as an array query string parameter (e.g. filters[]=operating_system:windows&filters[]=country:US).  Possible filter names are the same as returned by the List Filters endpoint. 
        :param str measurement: Measurement for the provided metric. If omitted, the deafult for the metric will be used.
        :param str order_direction: Sort order.
        :param str group_by: Time granularity to group results by. If this value is omitted, a default granularity is chosen based on the supplied timeframe.
        :return: GetMetricTimeseriesDataResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['metric_id', 'timeframe', 'filters', 'measurement', 'order_direction', 'group_by']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_metric_timeseries_data" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'metric_id' is set
        if ('metric_id' not in local_var_params or
                local_var_params['metric_id'] is None):
            raise ValueError("Missing the required parameter `metric_id` when calling `get_metric_timeseries_data`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'metric_id' in local_var_params:
            path_params['METRIC_ID'] = local_var_params['metric_id']  # noqa: E501

        query_params = []
        if 'timeframe' in local_var_params:
            query_params.append(('timeframe[]', local_var_params['timeframe']))  # noqa: E501
            collection_formats['timeframe[]'] = 'multi'  # noqa: E501
        if 'filters' in local_var_params:
            query_params.append(('filters[]', local_var_params['filters']))  # noqa: E501
            collection_formats['filters[]'] = 'multi'  # noqa: E501
        if 'measurement' in local_var_params:
            query_params.append(('measurement', local_var_params['measurement']))  # noqa: E501
        if 'order_direction' in local_var_params:
            query_params.append(('order_direction', local_var_params['order_direction']))  # noqa: E501
        if 'group_by' in local_var_params:
            query_params.append(('group_by', local_var_params['group_by']))  # noqa: E501

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
            '/data/v1/metrics/{METRIC_ID}/timeseries', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetMetricTimeseriesDataResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_overall_values(self, metric_id, **kwargs):  # noqa: E501
        """Get Overall values  # noqa: E501

        Returns the overall value for a specific metric, as well as the total view count, watch time, and the Mux Global metric value for the metric.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_overall_values(metric_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str metric_id: ID of the Metric (required)
        :param list[str] timeframe: Timeframe window to limit results by. Must be provided as an array query string parameter (e.g. timeframe[]=). Accepted formats are...   * array of epoch timestamps e.g. timeframe[]=1498867200&timeframe[]=1498953600    * duration string e.g. timeframe[]=24:hours or timeframe[]=7:days. 
        :param list[str] filters: Filter key:value pairs. Must be provided as an array query string parameter (e.g. filters[]=operating_system:windows&filters[]=country:US).  Possible filter names are the same as returned by the List Filters endpoint. 
        :param str measurement: Measurement for the provided metric. If omitted, the deafult for the metric will be used.
        :return: GetOverallValuesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_overall_values_with_http_info(metric_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_overall_values_with_http_info(metric_id, **kwargs)  # noqa: E501
            return data

    def get_overall_values_with_http_info(self, metric_id, **kwargs):  # noqa: E501
        """Get Overall values  # noqa: E501

        Returns the overall value for a specific metric, as well as the total view count, watch time, and the Mux Global metric value for the metric.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_overall_values_with_http_info(metric_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str metric_id: ID of the Metric (required)
        :param list[str] timeframe: Timeframe window to limit results by. Must be provided as an array query string parameter (e.g. timeframe[]=). Accepted formats are...   * array of epoch timestamps e.g. timeframe[]=1498867200&timeframe[]=1498953600    * duration string e.g. timeframe[]=24:hours or timeframe[]=7:days. 
        :param list[str] filters: Filter key:value pairs. Must be provided as an array query string parameter (e.g. filters[]=operating_system:windows&filters[]=country:US).  Possible filter names are the same as returned by the List Filters endpoint. 
        :param str measurement: Measurement for the provided metric. If omitted, the deafult for the metric will be used.
        :return: GetOverallValuesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['metric_id', 'timeframe', 'filters', 'measurement']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_overall_values" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'metric_id' is set
        if ('metric_id' not in local_var_params or
                local_var_params['metric_id'] is None):
            raise ValueError("Missing the required parameter `metric_id` when calling `get_overall_values`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'metric_id' in local_var_params:
            path_params['METRIC_ID'] = local_var_params['metric_id']  # noqa: E501

        query_params = []
        if 'timeframe' in local_var_params:
            query_params.append(('timeframe[]', local_var_params['timeframe']))  # noqa: E501
            collection_formats['timeframe[]'] = 'multi'  # noqa: E501
        if 'filters' in local_var_params:
            query_params.append(('filters[]', local_var_params['filters']))  # noqa: E501
            collection_formats['filters[]'] = 'multi'  # noqa: E501
        if 'measurement' in local_var_params:
            query_params.append(('measurement', local_var_params['measurement']))  # noqa: E501

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
            '/data/v1/metrics/{METRIC_ID}/overall', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetOverallValuesResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_all_metric_values(self, **kwargs):  # noqa: E501
        """List all metric values  # noqa: E501

        List all of the values across every breakdown for a specific metric   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_all_metric_values(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] timeframe: Timeframe window to limit results by. Must be provided as an array query string parameter (e.g. timeframe[]=). Accepted formats are...   * array of epoch timestamps e.g. timeframe[]=1498867200&timeframe[]=1498953600    * duration string e.g. timeframe[]=24:hours or timeframe[]=7:days. 
        :param list[str] filters: Filter key:value pairs. Must be provided as an array query string parameter (e.g. filters[]=operating_system:windows&filters[]=country:US).  Possible filter names are the same as returned by the List Filters endpoint. 
        :param str dimension: Dimension the specified value belongs to
        :param str value: Value to show all available metrics for
        :return: ListAllMetricValuesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_all_metric_values_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_all_metric_values_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_all_metric_values_with_http_info(self, **kwargs):  # noqa: E501
        """List all metric values  # noqa: E501

        List all of the values across every breakdown for a specific metric   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_all_metric_values_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] timeframe: Timeframe window to limit results by. Must be provided as an array query string parameter (e.g. timeframe[]=). Accepted formats are...   * array of epoch timestamps e.g. timeframe[]=1498867200&timeframe[]=1498953600    * duration string e.g. timeframe[]=24:hours or timeframe[]=7:days. 
        :param list[str] filters: Filter key:value pairs. Must be provided as an array query string parameter (e.g. filters[]=operating_system:windows&filters[]=country:US).  Possible filter names are the same as returned by the List Filters endpoint. 
        :param str dimension: Dimension the specified value belongs to
        :param str value: Value to show all available metrics for
        :return: ListAllMetricValuesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['timeframe', 'filters', 'dimension', 'value']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_all_metric_values" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'timeframe' in local_var_params:
            query_params.append(('timeframe[]', local_var_params['timeframe']))  # noqa: E501
            collection_formats['timeframe[]'] = 'multi'  # noqa: E501
        if 'filters' in local_var_params:
            query_params.append(('filters[]', local_var_params['filters']))  # noqa: E501
            collection_formats['filters[]'] = 'multi'  # noqa: E501
        if 'dimension' in local_var_params:
            query_params.append(('dimension', local_var_params['dimension']))  # noqa: E501
        if 'value' in local_var_params:
            query_params.append(('value', local_var_params['value']))  # noqa: E501

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
            '/data/v1/metrics/comparison', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ListAllMetricValuesResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_breakdown_values(self, metric_id, **kwargs):  # noqa: E501
        """List breakdown values  # noqa: E501

        List the breakdown values for a specific metric   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_breakdown_values(metric_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str metric_id: ID of the Metric (required)
        :param str group_by: Breakdown value to group the results by
        :param str measurement: Measurement for the provided metric. If omitted, the deafult for the metric will be used.
        :param list[str] filters: Filter key:value pairs. Must be provided as an array query string parameter (e.g. filters[]=operating_system:windows&filters[]=country:US).  Possible filter names are the same as returned by the List Filters endpoint. 
        :param int limit: Number of items to include in the response
        :param int page: Offset by this many pages, of the size of `limit`
        :param str order_by: Value to order the results by
        :param str order_direction: Sort order.
        :param list[str] timeframe: Timeframe window to limit results by. Must be provided as an array query string parameter (e.g. timeframe[]=). Accepted formats are...   * array of epoch timestamps e.g. timeframe[]=1498867200&timeframe[]=1498953600    * duration string e.g. timeframe[]=24:hours or timeframe[]=7:days. 
        :return: ListBreakdownValuesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_breakdown_values_with_http_info(metric_id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_breakdown_values_with_http_info(metric_id, **kwargs)  # noqa: E501
            return data

    def list_breakdown_values_with_http_info(self, metric_id, **kwargs):  # noqa: E501
        """List breakdown values  # noqa: E501

        List the breakdown values for a specific metric   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_breakdown_values_with_http_info(metric_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str metric_id: ID of the Metric (required)
        :param str group_by: Breakdown value to group the results by
        :param str measurement: Measurement for the provided metric. If omitted, the deafult for the metric will be used.
        :param list[str] filters: Filter key:value pairs. Must be provided as an array query string parameter (e.g. filters[]=operating_system:windows&filters[]=country:US).  Possible filter names are the same as returned by the List Filters endpoint. 
        :param int limit: Number of items to include in the response
        :param int page: Offset by this many pages, of the size of `limit`
        :param str order_by: Value to order the results by
        :param str order_direction: Sort order.
        :param list[str] timeframe: Timeframe window to limit results by. Must be provided as an array query string parameter (e.g. timeframe[]=). Accepted formats are...   * array of epoch timestamps e.g. timeframe[]=1498867200&timeframe[]=1498953600    * duration string e.g. timeframe[]=24:hours or timeframe[]=7:days. 
        :return: ListBreakdownValuesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['metric_id', 'group_by', 'measurement', 'filters', 'limit', 'page', 'order_by', 'order_direction', 'timeframe']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_breakdown_values" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'metric_id' is set
        if ('metric_id' not in local_var_params or
                local_var_params['metric_id'] is None):
            raise ValueError("Missing the required parameter `metric_id` when calling `list_breakdown_values`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'metric_id' in local_var_params:
            path_params['METRIC_ID'] = local_var_params['metric_id']  # noqa: E501

        query_params = []
        if 'group_by' in local_var_params:
            query_params.append(('group_by', local_var_params['group_by']))  # noqa: E501
        if 'measurement' in local_var_params:
            query_params.append(('measurement', local_var_params['measurement']))  # noqa: E501
        if 'filters' in local_var_params:
            query_params.append(('filters[]', local_var_params['filters']))  # noqa: E501
            collection_formats['filters[]'] = 'multi'  # noqa: E501
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))  # noqa: E501
        if 'order_by' in local_var_params:
            query_params.append(('order_by', local_var_params['order_by']))  # noqa: E501
        if 'order_direction' in local_var_params:
            query_params.append(('order_direction', local_var_params['order_direction']))  # noqa: E501
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
            '/data/v1/metrics/{METRIC_ID}/breakdown', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ListBreakdownValuesResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_insights(self, metric_id, **kwargs):  # noqa: E501
        """List Insights  # noqa: E501

        Returns a list of insights for a metric. These are the worst performing values across all breakdowns sorted by how much they negatively impact a specific metric.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_insights(metric_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str metric_id: ID of the Metric (required)
        :param str measurement: Measurement for the provided metric. If omitted, the deafult for the metric will be used.
        :param str order_direction: Sort order.
        :param list[str] timeframe: Timeframe window to limit results by. Must be provided as an array query string parameter (e.g. timeframe[]=). Accepted formats are...   * array of epoch timestamps e.g. timeframe[]=1498867200&timeframe[]=1498953600    * duration string e.g. timeframe[]=24:hours or timeframe[]=7:days. 
        :return: ListInsightsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_insights_with_http_info(metric_id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_insights_with_http_info(metric_id, **kwargs)  # noqa: E501
            return data

    def list_insights_with_http_info(self, metric_id, **kwargs):  # noqa: E501
        """List Insights  # noqa: E501

        Returns a list of insights for a metric. These are the worst performing values across all breakdowns sorted by how much they negatively impact a specific metric.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_insights_with_http_info(metric_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str metric_id: ID of the Metric (required)
        :param str measurement: Measurement for the provided metric. If omitted, the deafult for the metric will be used.
        :param str order_direction: Sort order.
        :param list[str] timeframe: Timeframe window to limit results by. Must be provided as an array query string parameter (e.g. timeframe[]=). Accepted formats are...   * array of epoch timestamps e.g. timeframe[]=1498867200&timeframe[]=1498953600    * duration string e.g. timeframe[]=24:hours or timeframe[]=7:days. 
        :return: ListInsightsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['metric_id', 'measurement', 'order_direction', 'timeframe']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_insights" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'metric_id' is set
        if ('metric_id' not in local_var_params or
                local_var_params['metric_id'] is None):
            raise ValueError("Missing the required parameter `metric_id` when calling `list_insights`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'metric_id' in local_var_params:
            path_params['METRIC_ID'] = local_var_params['metric_id']  # noqa: E501

        query_params = []
        if 'measurement' in local_var_params:
            query_params.append(('measurement', local_var_params['measurement']))  # noqa: E501
        if 'order_direction' in local_var_params:
            query_params.append(('order_direction', local_var_params['order_direction']))  # noqa: E501
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
            '/data/v1/metrics/{METRIC_ID}/insights', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ListInsightsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
