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

class LiveStreamsApi(object):

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_live_stream(self, create_live_stream_request, **kwargs):  # noqa: E501
        """Create a live stream  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_live_stream(create_live_stream_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateLiveStreamRequest create_live_stream_request: (required)
        :return: LiveStreamResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_live_stream_with_http_info(create_live_stream_request, **kwargs)  # noqa: E501
        else:
            (data) = self.create_live_stream_with_http_info(create_live_stream_request, **kwargs)  # noqa: E501
            return data

    def create_live_stream_with_http_info(self, create_live_stream_request, **kwargs):  # noqa: E501
        """Create a live stream  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_live_stream_with_http_info(create_live_stream_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateLiveStreamRequest create_live_stream_request: (required)
        :return: LiveStreamResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['create_live_stream_request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_live_stream" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'create_live_stream_request' is set
        if ('create_live_stream_request' not in local_var_params or
                local_var_params['create_live_stream_request'] is None):
            raise ValueError("Missing the required parameter `create_live_stream_request` when calling `create_live_stream`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'create_live_stream_request' in local_var_params:
            body_params = local_var_params['create_live_stream_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['accessToken']  # noqa: E501

        return self.api_client.call_api(
            '/video/v1/live-streams', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LiveStreamResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_live_stream_playback_id(self, live_stream_id, create_playback_id_request, **kwargs):  # noqa: E501
        """Create a live stream playback ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_live_stream_playback_id(live_stream_id, create_playback_id_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str live_stream_id: The live stream ID (required)
        :param CreatePlaybackIDRequest create_playback_id_request: (required)
        :return: CreatePlaybackIDResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_live_stream_playback_id_with_http_info(live_stream_id, create_playback_id_request, **kwargs)  # noqa: E501
        else:
            (data) = self.create_live_stream_playback_id_with_http_info(live_stream_id, create_playback_id_request, **kwargs)  # noqa: E501
            return data

    def create_live_stream_playback_id_with_http_info(self, live_stream_id, create_playback_id_request, **kwargs):  # noqa: E501
        """Create a live stream playback ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_live_stream_playback_id_with_http_info(live_stream_id, create_playback_id_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str live_stream_id: The live stream ID (required)
        :param CreatePlaybackIDRequest create_playback_id_request: (required)
        :return: CreatePlaybackIDResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['live_stream_id', 'create_playback_id_request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_live_stream_playback_id" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'live_stream_id' is set
        if ('live_stream_id' not in local_var_params or
                local_var_params['live_stream_id'] is None):
            raise ValueError("Missing the required parameter `live_stream_id` when calling `create_live_stream_playback_id`")  # noqa: E501
        # verify the required parameter 'create_playback_id_request' is set
        if ('create_playback_id_request' not in local_var_params or
                local_var_params['create_playback_id_request'] is None):
            raise ValueError("Missing the required parameter `create_playback_id_request` when calling `create_live_stream_playback_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'live_stream_id' in local_var_params:
            path_params['LIVE_STREAM_ID'] = local_var_params['live_stream_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'create_playback_id_request' in local_var_params:
            body_params = local_var_params['create_playback_id_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['accessToken']  # noqa: E501

        return self.api_client.call_api(
            '/video/v1/live-streams/{LIVE_STREAM_ID}/playback-ids', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreatePlaybackIDResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_live_stream_simulcast_target(self, live_stream_id, create_simulcast_target_request, **kwargs):  # noqa: E501
        """Create a live stream simulcast target  # noqa: E501

        Create a simulcast target for the parent live stream. Simulcast target can only be created when the parent live stream is in idle state. Only one simulcast target can be created at a time with this API.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_live_stream_simulcast_target(live_stream_id, create_simulcast_target_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str live_stream_id: The live stream ID (required)
        :param CreateSimulcastTargetRequest create_simulcast_target_request: (required)
        :return: SimulcastTargetResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_live_stream_simulcast_target_with_http_info(live_stream_id, create_simulcast_target_request, **kwargs)  # noqa: E501
        else:
            (data) = self.create_live_stream_simulcast_target_with_http_info(live_stream_id, create_simulcast_target_request, **kwargs)  # noqa: E501
            return data

    def create_live_stream_simulcast_target_with_http_info(self, live_stream_id, create_simulcast_target_request, **kwargs):  # noqa: E501
        """Create a live stream simulcast target  # noqa: E501

        Create a simulcast target for the parent live stream. Simulcast target can only be created when the parent live stream is in idle state. Only one simulcast target can be created at a time with this API.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_live_stream_simulcast_target_with_http_info(live_stream_id, create_simulcast_target_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str live_stream_id: The live stream ID (required)
        :param CreateSimulcastTargetRequest create_simulcast_target_request: (required)
        :return: SimulcastTargetResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['live_stream_id', 'create_simulcast_target_request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_live_stream_simulcast_target" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'live_stream_id' is set
        if ('live_stream_id' not in local_var_params or
                local_var_params['live_stream_id'] is None):
            raise ValueError("Missing the required parameter `live_stream_id` when calling `create_live_stream_simulcast_target`")  # noqa: E501
        # verify the required parameter 'create_simulcast_target_request' is set
        if ('create_simulcast_target_request' not in local_var_params or
                local_var_params['create_simulcast_target_request'] is None):
            raise ValueError("Missing the required parameter `create_simulcast_target_request` when calling `create_live_stream_simulcast_target`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'live_stream_id' in local_var_params:
            path_params['LIVE_STREAM_ID'] = local_var_params['live_stream_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'create_simulcast_target_request' in local_var_params:
            body_params = local_var_params['create_simulcast_target_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['accessToken']  # noqa: E501

        return self.api_client.call_api(
            '/video/v1/live-streams/{LIVE_STREAM_ID}/simulcast-targets', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SimulcastTargetResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_live_stream(self, live_stream_id, **kwargs):  # noqa: E501
        """Delete a live stream  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_live_stream(live_stream_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str live_stream_id: The live stream ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_live_stream_with_http_info(live_stream_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_live_stream_with_http_info(live_stream_id, **kwargs)  # noqa: E501
            return data

    def delete_live_stream_with_http_info(self, live_stream_id, **kwargs):  # noqa: E501
        """Delete a live stream  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_live_stream_with_http_info(live_stream_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str live_stream_id: The live stream ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['live_stream_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_live_stream" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'live_stream_id' is set
        if ('live_stream_id' not in local_var_params or
                local_var_params['live_stream_id'] is None):
            raise ValueError("Missing the required parameter `live_stream_id` when calling `delete_live_stream`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'live_stream_id' in local_var_params:
            path_params['LIVE_STREAM_ID'] = local_var_params['live_stream_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['accessToken']  # noqa: E501

        return self.api_client.call_api(
            '/video/v1/live-streams/{LIVE_STREAM_ID}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_live_stream_playback_id(self, live_stream_id, playback_id, **kwargs):  # noqa: E501
        """Delete a live stream playback ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_live_stream_playback_id(live_stream_id, playback_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str live_stream_id: The live stream ID (required)
        :param str playback_id: The live stream's playback ID. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_live_stream_playback_id_with_http_info(live_stream_id, playback_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_live_stream_playback_id_with_http_info(live_stream_id, playback_id, **kwargs)  # noqa: E501
            return data

    def delete_live_stream_playback_id_with_http_info(self, live_stream_id, playback_id, **kwargs):  # noqa: E501
        """Delete a live stream playback ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_live_stream_playback_id_with_http_info(live_stream_id, playback_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str live_stream_id: The live stream ID (required)
        :param str playback_id: The live stream's playback ID. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['live_stream_id', 'playback_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_live_stream_playback_id" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'live_stream_id' is set
        if ('live_stream_id' not in local_var_params or
                local_var_params['live_stream_id'] is None):
            raise ValueError("Missing the required parameter `live_stream_id` when calling `delete_live_stream_playback_id`")  # noqa: E501
        # verify the required parameter 'playback_id' is set
        if ('playback_id' not in local_var_params or
                local_var_params['playback_id'] is None):
            raise ValueError("Missing the required parameter `playback_id` when calling `delete_live_stream_playback_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'live_stream_id' in local_var_params:
            path_params['LIVE_STREAM_ID'] = local_var_params['live_stream_id']  # noqa: E501
        if 'playback_id' in local_var_params:
            path_params['PLAYBACK_ID'] = local_var_params['playback_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['accessToken']  # noqa: E501

        return self.api_client.call_api(
            '/video/v1/live-streams/{LIVE_STREAM_ID}/playback-ids/{PLAYBACK_ID}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_live_stream_simulcast_target(self, live_stream_id, simulcast_target_id, **kwargs):  # noqa: E501
        """Delete a Live Stream Simulcast Target  # noqa: E501

        Delete the simulcast target using the simulcast target ID returned when creating the simulcast target. Simulcast Target can only be deleted when the parent live stream is in idle state.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_live_stream_simulcast_target(live_stream_id, simulcast_target_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str live_stream_id: The live stream ID (required)
        :param str simulcast_target_id: The ID of the simulcast target. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_live_stream_simulcast_target_with_http_info(live_stream_id, simulcast_target_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_live_stream_simulcast_target_with_http_info(live_stream_id, simulcast_target_id, **kwargs)  # noqa: E501
            return data

    def delete_live_stream_simulcast_target_with_http_info(self, live_stream_id, simulcast_target_id, **kwargs):  # noqa: E501
        """Delete a Live Stream Simulcast Target  # noqa: E501

        Delete the simulcast target using the simulcast target ID returned when creating the simulcast target. Simulcast Target can only be deleted when the parent live stream is in idle state.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_live_stream_simulcast_target_with_http_info(live_stream_id, simulcast_target_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str live_stream_id: The live stream ID (required)
        :param str simulcast_target_id: The ID of the simulcast target. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['live_stream_id', 'simulcast_target_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_live_stream_simulcast_target" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'live_stream_id' is set
        if ('live_stream_id' not in local_var_params or
                local_var_params['live_stream_id'] is None):
            raise ValueError("Missing the required parameter `live_stream_id` when calling `delete_live_stream_simulcast_target`")  # noqa: E501
        # verify the required parameter 'simulcast_target_id' is set
        if ('simulcast_target_id' not in local_var_params or
                local_var_params['simulcast_target_id'] is None):
            raise ValueError("Missing the required parameter `simulcast_target_id` when calling `delete_live_stream_simulcast_target`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'live_stream_id' in local_var_params:
            path_params['LIVE_STREAM_ID'] = local_var_params['live_stream_id']  # noqa: E501
        if 'simulcast_target_id' in local_var_params:
            path_params['SIMULCAST_TARGET_ID'] = local_var_params['simulcast_target_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['accessToken']  # noqa: E501

        return self.api_client.call_api(
            '/video/v1/live-streams/{LIVE_STREAM_ID}/simulcast-targets/{SIMULCAST_TARGET_ID}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_live_stream(self, live_stream_id, **kwargs):  # noqa: E501
        """Retrieve a live stream  # noqa: E501

        Retrieves the details of a live stream that has previously been created. Supply the unique live stream ID that was returned from your previous request, and Mux will return the corresponding live stream information. The same information is returned when creating a live stream.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_live_stream(live_stream_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str live_stream_id: The live stream ID (required)
        :return: LiveStreamResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_live_stream_with_http_info(live_stream_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_live_stream_with_http_info(live_stream_id, **kwargs)  # noqa: E501
            return data

    def get_live_stream_with_http_info(self, live_stream_id, **kwargs):  # noqa: E501
        """Retrieve a live stream  # noqa: E501

        Retrieves the details of a live stream that has previously been created. Supply the unique live stream ID that was returned from your previous request, and Mux will return the corresponding live stream information. The same information is returned when creating a live stream.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_live_stream_with_http_info(live_stream_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str live_stream_id: The live stream ID (required)
        :return: LiveStreamResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['live_stream_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_live_stream" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'live_stream_id' is set
        if ('live_stream_id' not in local_var_params or
                local_var_params['live_stream_id'] is None):
            raise ValueError("Missing the required parameter `live_stream_id` when calling `get_live_stream`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'live_stream_id' in local_var_params:
            path_params['LIVE_STREAM_ID'] = local_var_params['live_stream_id']  # noqa: E501

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
            '/video/v1/live-streams/{LIVE_STREAM_ID}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LiveStreamResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_live_stream_simulcast_target(self, live_stream_id, simulcast_target_id, **kwargs):  # noqa: E501
        """Retrieve a Live Stream Simulcast Target  # noqa: E501

        Retrieves the details of the simulcast target created for the parent live stream. Supply the unique live stream ID and simulcast target ID that was returned in the response of create simulcast target request, and Mux will return the corresponding information.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_live_stream_simulcast_target(live_stream_id, simulcast_target_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str live_stream_id: The live stream ID (required)
        :param str simulcast_target_id: The ID of the simulcast target. (required)
        :return: SimulcastTargetResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_live_stream_simulcast_target_with_http_info(live_stream_id, simulcast_target_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_live_stream_simulcast_target_with_http_info(live_stream_id, simulcast_target_id, **kwargs)  # noqa: E501
            return data

    def get_live_stream_simulcast_target_with_http_info(self, live_stream_id, simulcast_target_id, **kwargs):  # noqa: E501
        """Retrieve a Live Stream Simulcast Target  # noqa: E501

        Retrieves the details of the simulcast target created for the parent live stream. Supply the unique live stream ID and simulcast target ID that was returned in the response of create simulcast target request, and Mux will return the corresponding information.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_live_stream_simulcast_target_with_http_info(live_stream_id, simulcast_target_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str live_stream_id: The live stream ID (required)
        :param str simulcast_target_id: The ID of the simulcast target. (required)
        :return: SimulcastTargetResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['live_stream_id', 'simulcast_target_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_live_stream_simulcast_target" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'live_stream_id' is set
        if ('live_stream_id' not in local_var_params or
                local_var_params['live_stream_id'] is None):
            raise ValueError("Missing the required parameter `live_stream_id` when calling `get_live_stream_simulcast_target`")  # noqa: E501
        # verify the required parameter 'simulcast_target_id' is set
        if ('simulcast_target_id' not in local_var_params or
                local_var_params['simulcast_target_id'] is None):
            raise ValueError("Missing the required parameter `simulcast_target_id` when calling `get_live_stream_simulcast_target`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'live_stream_id' in local_var_params:
            path_params['LIVE_STREAM_ID'] = local_var_params['live_stream_id']  # noqa: E501
        if 'simulcast_target_id' in local_var_params:
            path_params['SIMULCAST_TARGET_ID'] = local_var_params['simulcast_target_id']  # noqa: E501

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
            '/video/v1/live-streams/{LIVE_STREAM_ID}/simulcast-targets/{SIMULCAST_TARGET_ID}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SimulcastTargetResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_live_streams(self, **kwargs):  # noqa: E501
        """List live streams  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_live_streams(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit: Number of items to include in the response
        :param int page: Offset by this many pages, of the size of `limit`
        :return: ListLiveStreamsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_live_streams_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_live_streams_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_live_streams_with_http_info(self, **kwargs):  # noqa: E501
        """List live streams  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_live_streams_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit: Number of items to include in the response
        :param int page: Offset by this many pages, of the size of `limit`
        :return: ListLiveStreamsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['limit', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_live_streams" % key
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
            '/video/v1/live-streams', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ListLiveStreamsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def reset_stream_key(self, live_stream_id, **kwargs):  # noqa: E501
        """Reset a live stream’s stream key  # noqa: E501

        Reset a live stream key if you want to immediately stop the current stream key from working and create a new stream key that can be used for future broadcasts.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.reset_stream_key(live_stream_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str live_stream_id: The live stream ID (required)
        :return: LiveStreamResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.reset_stream_key_with_http_info(live_stream_id, **kwargs)  # noqa: E501
        else:
            (data) = self.reset_stream_key_with_http_info(live_stream_id, **kwargs)  # noqa: E501
            return data

    def reset_stream_key_with_http_info(self, live_stream_id, **kwargs):  # noqa: E501
        """Reset a live stream’s stream key  # noqa: E501

        Reset a live stream key if you want to immediately stop the current stream key from working and create a new stream key that can be used for future broadcasts.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.reset_stream_key_with_http_info(live_stream_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str live_stream_id: The live stream ID (required)
        :return: LiveStreamResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['live_stream_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method reset_stream_key" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'live_stream_id' is set
        if ('live_stream_id' not in local_var_params or
                local_var_params['live_stream_id'] is None):
            raise ValueError("Missing the required parameter `live_stream_id` when calling `reset_stream_key`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'live_stream_id' in local_var_params:
            path_params['LIVE_STREAM_ID'] = local_var_params['live_stream_id']  # noqa: E501

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
            '/video/v1/live-streams/{LIVE_STREAM_ID}/reset-stream-key', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LiveStreamResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def signal_live_stream_complete(self, live_stream_id, **kwargs):  # noqa: E501
        """Signal a live stream is finished  # noqa: E501

        (Optional) Make the recorded asset available immediately instead of waiting for the reconnect_window.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.signal_live_stream_complete(live_stream_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str live_stream_id: The live stream ID (required)
        :return: SignalLiveStreamCompleteResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.signal_live_stream_complete_with_http_info(live_stream_id, **kwargs)  # noqa: E501
        else:
            (data) = self.signal_live_stream_complete_with_http_info(live_stream_id, **kwargs)  # noqa: E501
            return data

    def signal_live_stream_complete_with_http_info(self, live_stream_id, **kwargs):  # noqa: E501
        """Signal a live stream is finished  # noqa: E501

        (Optional) Make the recorded asset available immediately instead of waiting for the reconnect_window.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.signal_live_stream_complete_with_http_info(live_stream_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str live_stream_id: The live stream ID (required)
        :return: SignalLiveStreamCompleteResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['live_stream_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method signal_live_stream_complete" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'live_stream_id' is set
        if ('live_stream_id' not in local_var_params or
                local_var_params['live_stream_id'] is None):
            raise ValueError("Missing the required parameter `live_stream_id` when calling `signal_live_stream_complete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'live_stream_id' in local_var_params:
            path_params['LIVE_STREAM_ID'] = local_var_params['live_stream_id']  # noqa: E501

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
            '/video/v1/live-streams/{LIVE_STREAM_ID}/complete', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SignalLiveStreamCompleteResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
