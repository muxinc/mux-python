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

class VideoViewsApi(object):

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_video_view(self, video_view_id, **kwargs):  # noqa: E501
        """Get a Video View  # noqa: E501

        Returns the details of a video view   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_video_view(video_view_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str video_view_id: ID of the Video View (required)
        :return: VideoViewResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_video_view_with_http_info(video_view_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_video_view_with_http_info(video_view_id, **kwargs)  # noqa: E501
            return data

    def get_video_view_with_http_info(self, video_view_id, **kwargs):  # noqa: E501
        """Get a Video View  # noqa: E501

        Returns the details of a video view   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_video_view_with_http_info(video_view_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str video_view_id: ID of the Video View (required)
        :return: VideoViewResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['video_view_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_video_view" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'video_view_id' is set
        if ('video_view_id' not in local_var_params or
                local_var_params['video_view_id'] is None):
            raise ValueError("Missing the required parameter `video_view_id` when calling `get_video_view`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'video_view_id' in local_var_params:
            path_params['VIDEO_VIEW_ID'] = local_var_params['video_view_id']  # noqa: E501

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
            '/data/v1/video-views/{VIDEO_VIEW_ID}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='VideoViewResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_video_views(self, **kwargs):  # noqa: E501
        """List Video Views  # noqa: E501

        Returns a list of video views   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_video_views(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit: Number of items to include in the response
        :param int page: Offset by this many pages, of the size of `limit`
        :param str viewer_id: Viewer ID to filter results by. This value may be provided by the integration, or may be created by Mux.
        :param int error_id: Filter video views by the provided error ID (as returned in the error_type_id field in the list video views endpoint). If you provide any as the error ID, this will filter the results to those with any error.
        :param str order_direction: Sort order.
        :param list[str] filters: Filter key:value pairs. Must be provided as an array query string parameter (e.g. filters[]=operating_system:windows&filters[]=country:US).  Possible filter names are the same as returned by the List Filters endpoint. 
        :param list[str] timeframe: Timeframe window to limit results by. Must be provided as an array query string parameter (e.g. timeframe[]=). Accepted formats are...   * array of epoch timestamps e.g. timeframe[]=1498867200&timeframe[]=1498953600    * duration string e.g. timeframe[]=24:hours or timeframe[]=7:days. 
        :return: ListVideoViewsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_video_views_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_video_views_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_video_views_with_http_info(self, **kwargs):  # noqa: E501
        """List Video Views  # noqa: E501

        Returns a list of video views   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_video_views_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit: Number of items to include in the response
        :param int page: Offset by this many pages, of the size of `limit`
        :param str viewer_id: Viewer ID to filter results by. This value may be provided by the integration, or may be created by Mux.
        :param int error_id: Filter video views by the provided error ID (as returned in the error_type_id field in the list video views endpoint). If you provide any as the error ID, this will filter the results to those with any error.
        :param str order_direction: Sort order.
        :param list[str] filters: Filter key:value pairs. Must be provided as an array query string parameter (e.g. filters[]=operating_system:windows&filters[]=country:US).  Possible filter names are the same as returned by the List Filters endpoint. 
        :param list[str] timeframe: Timeframe window to limit results by. Must be provided as an array query string parameter (e.g. timeframe[]=). Accepted formats are...   * array of epoch timestamps e.g. timeframe[]=1498867200&timeframe[]=1498953600    * duration string e.g. timeframe[]=24:hours or timeframe[]=7:days. 
        :return: ListVideoViewsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['limit', 'page', 'viewer_id', 'error_id', 'order_direction', 'filters', 'timeframe']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_video_views" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))  # noqa: E501
        if 'viewer_id' in local_var_params:
            query_params.append(('viewer_id', local_var_params['viewer_id']))  # noqa: E501
        if 'error_id' in local_var_params:
            query_params.append(('error_id', local_var_params['error_id']))  # noqa: E501
        if 'order_direction' in local_var_params:
            query_params.append(('order_direction', local_var_params['order_direction']))  # noqa: E501
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
            '/data/v1/video-views', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ListVideoViewsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
