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

class PlaybackIDApi(object):

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_asset_or_livestream_id(self, playback_id, **kwargs):  # noqa: E501
        """Retrieve an Asset or Live Stream ID  # noqa: E501

        Retrieves the Identifier of the Asset or Live Stream associated with the Playback ID.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_asset_or_livestream_id(playback_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str playback_id: The live stream's playback ID. (required)
        :return: GetAssetOrLiveStreamIdResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_asset_or_livestream_id_with_http_info(playback_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_asset_or_livestream_id_with_http_info(playback_id, **kwargs)  # noqa: E501
            return data

    def get_asset_or_livestream_id_with_http_info(self, playback_id, **kwargs):  # noqa: E501
        """Retrieve an Asset or Live Stream ID  # noqa: E501

        Retrieves the Identifier of the Asset or Live Stream associated with the Playback ID.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_asset_or_livestream_id_with_http_info(playback_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str playback_id: The live stream's playback ID. (required)
        :return: GetAssetOrLiveStreamIdResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['playback_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_asset_or_livestream_id" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'playback_id' is set
        if ('playback_id' not in local_var_params or
                local_var_params['playback_id'] is None):
            raise ValueError("Missing the required parameter `playback_id` when calling `get_asset_or_livestream_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'playback_id' in local_var_params:
            path_params['PLAYBACK_ID'] = local_var_params['playback_id']  # noqa: E501

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
            '/video/v1/playback-ids/{PLAYBACK_ID}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetAssetOrLiveStreamIdResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
