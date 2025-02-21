# coding: utf-8

"""
    Mux API

    Mux is how developers build online video. This API encompasses both Mux Video and Mux Data functionality to help you build your video-related projects better and faster than ever before.  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: devex@mux.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from mux_python.api_client import ApiClient
from mux_python.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class VideoViewsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_video_view(self, video_view_id, **kwargs):  # noqa: E501
        """Get a Video View  # noqa: E501

        Returns the details of a video view.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_video_view(video_view_id, async_req=True)
        >>> result = thread.get()

        :param video_view_id: ID of the Video View (required)
        :type video_view_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: VideoViewResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.get_video_view_with_http_info(video_view_id, **kwargs)  # noqa: E501

    def get_video_view_with_http_info(self, video_view_id, **kwargs):  # noqa: E501
        """Get a Video View  # noqa: E501

        Returns the details of a video view.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_video_view_with_http_info(video_view_id, async_req=True)
        >>> result = thread.get()

        :param video_view_id: ID of the Video View (required)
        :type video_view_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(VideoViewResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'video_view_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_video_view" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'video_view_id' is set
        if self.api_client.client_side_validation and ('video_view_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['video_view_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `video_view_id` when calling `get_video_view`")  # noqa: E501

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
        
        response_types_map = {
            200: "VideoViewResponse",
        }

        return self.api_client.call_api(
            '/data/v1/video-views/{VIDEO_VIEW_ID}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def list_video_views(self, **kwargs):  # noqa: E501
        """List Video Views  # noqa: E501

        Returns a list of video views which match the filters and have a `view_end` within the specified timeframe.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_video_views(async_req=True)
        >>> result = thread.get()

        :param limit: Number of items to include in the response
        :type limit: int
        :param page: Offset by this many pages, of the size of `limit`
        :type page: int
        :param viewer_id: Viewer ID to filter results by. This value may be provided by the integration, or may be created by Mux.
        :type viewer_id: str
        :param error_id: Filter video views by the provided error ID (as returned in the error_type_id field in the list video views endpoint). If you provide any as the error ID, this will filter the results to those with any error.
        :type error_id: int
        :param order_direction: Sort order.
        :type order_direction: str
        :param filters: Limit the results to rows that match conditions from provided key:value pairs. Must be provided as an array query string parameter.  To exclude rows that match a certain condition, prepend a `!` character to the dimension.  Possible filter names are the same as returned by the List Filters endpoint.  Example:    * `filters[]=operating_system:windows&filters[]=!country:US` 
        :type filters: list[str]
        :param metric_filters: Limit the results to rows that match inequality conditions from provided metric comparison clauses. Must be provided as an array query string parameter.  Possible filterable metrics are the same as the set of metric ids, with the exceptions of `exits_before_video_start`, `unique_viewers`, `video_startup_failure_percentage`, `view_dropped_percentage`, and `views`.  Example:    * `metric_filters[]=aggregate_startup_time>=1000` 
        :type metric_filters: list[str]
        :param timeframe: Timeframe window to limit results by. Must be provided as an array query string parameter (e.g. timeframe[]=).  Accepted formats are...    * array of epoch timestamps e.g. `timeframe[]=1498867200&timeframe[]=1498953600`   * duration string e.g. `timeframe[]=24:hours or timeframe[]=7:days` 
        :type timeframe: list[str]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ListVideoViewsResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.list_video_views_with_http_info(**kwargs)  # noqa: E501

    def list_video_views_with_http_info(self, **kwargs):  # noqa: E501
        """List Video Views  # noqa: E501

        Returns a list of video views which match the filters and have a `view_end` within the specified timeframe.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_video_views_with_http_info(async_req=True)
        >>> result = thread.get()

        :param limit: Number of items to include in the response
        :type limit: int
        :param page: Offset by this many pages, of the size of `limit`
        :type page: int
        :param viewer_id: Viewer ID to filter results by. This value may be provided by the integration, or may be created by Mux.
        :type viewer_id: str
        :param error_id: Filter video views by the provided error ID (as returned in the error_type_id field in the list video views endpoint). If you provide any as the error ID, this will filter the results to those with any error.
        :type error_id: int
        :param order_direction: Sort order.
        :type order_direction: str
        :param filters: Limit the results to rows that match conditions from provided key:value pairs. Must be provided as an array query string parameter.  To exclude rows that match a certain condition, prepend a `!` character to the dimension.  Possible filter names are the same as returned by the List Filters endpoint.  Example:    * `filters[]=operating_system:windows&filters[]=!country:US` 
        :type filters: list[str]
        :param metric_filters: Limit the results to rows that match inequality conditions from provided metric comparison clauses. Must be provided as an array query string parameter.  Possible filterable metrics are the same as the set of metric ids, with the exceptions of `exits_before_video_start`, `unique_viewers`, `video_startup_failure_percentage`, `view_dropped_percentage`, and `views`.  Example:    * `metric_filters[]=aggregate_startup_time>=1000` 
        :type metric_filters: list[str]
        :param timeframe: Timeframe window to limit results by. Must be provided as an array query string parameter (e.g. timeframe[]=).  Accepted formats are...    * array of epoch timestamps e.g. `timeframe[]=1498867200&timeframe[]=1498953600`   * duration string e.g. `timeframe[]=24:hours or timeframe[]=7:days` 
        :type timeframe: list[str]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ListVideoViewsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'limit',
            'page',
            'viewer_id',
            'error_id',
            'order_direction',
            'filters',
            'metric_filters',
            'timeframe'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_video_views" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'page' in local_var_params and local_var_params['page'] is not None:  # noqa: E501
            query_params.append(('page', local_var_params['page']))  # noqa: E501
        if 'viewer_id' in local_var_params and local_var_params['viewer_id'] is not None:  # noqa: E501
            query_params.append(('viewer_id', local_var_params['viewer_id']))  # noqa: E501
        if 'error_id' in local_var_params and local_var_params['error_id'] is not None:  # noqa: E501
            query_params.append(('error_id', local_var_params['error_id']))  # noqa: E501
        if 'order_direction' in local_var_params and local_var_params['order_direction'] is not None:  # noqa: E501
            query_params.append(('order_direction', local_var_params['order_direction']))  # noqa: E501
        if 'filters' in local_var_params and local_var_params['filters'] is not None:  # noqa: E501
            query_params.append(('filters[]', local_var_params['filters']))  # noqa: E501
            collection_formats['filters[]'] = 'multi'  # noqa: E501
        if 'metric_filters' in local_var_params and local_var_params['metric_filters'] is not None:  # noqa: E501
            query_params.append(('metric_filters[]', local_var_params['metric_filters']))  # noqa: E501
            collection_formats['metric_filters[]'] = 'multi'  # noqa: E501
        if 'timeframe' in local_var_params and local_var_params['timeframe'] is not None:  # noqa: E501
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
        
        response_types_map = {
            200: "ListVideoViewsResponse",
        }

        return self.api_client.call_api(
            '/data/v1/video-views', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))
