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

class AssetsApi(object):

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_asset(self, create_asset_request, **kwargs):  # noqa: E501
        """Create an asset  # noqa: E501

        Create a new Mux Video asset.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_asset(create_asset_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateAssetRequest create_asset_request: (required)
        :return: AssetResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_asset_with_http_info(create_asset_request, **kwargs)  # noqa: E501
        else:
            (data) = self.create_asset_with_http_info(create_asset_request, **kwargs)  # noqa: E501
            return data

    def create_asset_with_http_info(self, create_asset_request, **kwargs):  # noqa: E501
        """Create an asset  # noqa: E501

        Create a new Mux Video asset.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_asset_with_http_info(create_asset_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateAssetRequest create_asset_request: (required)
        :return: AssetResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['create_asset_request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_asset" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'create_asset_request' is set
        if ('create_asset_request' not in local_var_params or
                local_var_params['create_asset_request'] is None):
            raise ValueError("Missing the required parameter `create_asset_request` when calling `create_asset`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'create_asset_request' in local_var_params:
            body_params = local_var_params['create_asset_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['accessToken']  # noqa: E501

        return self.api_client.call_api(
            '/video/v1/assets', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AssetResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_asset_playback_id(self, asset_id, create_playback_id_request, **kwargs):  # noqa: E501
        """Create a playback ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_asset_playback_id(asset_id, create_playback_id_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str asset_id: The asset ID. (required)
        :param CreatePlaybackIDRequest create_playback_id_request: (required)
        :return: CreatePlaybackIDResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_asset_playback_id_with_http_info(asset_id, create_playback_id_request, **kwargs)  # noqa: E501
        else:
            (data) = self.create_asset_playback_id_with_http_info(asset_id, create_playback_id_request, **kwargs)  # noqa: E501
            return data

    def create_asset_playback_id_with_http_info(self, asset_id, create_playback_id_request, **kwargs):  # noqa: E501
        """Create a playback ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_asset_playback_id_with_http_info(asset_id, create_playback_id_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str asset_id: The asset ID. (required)
        :param CreatePlaybackIDRequest create_playback_id_request: (required)
        :return: CreatePlaybackIDResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['asset_id', 'create_playback_id_request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_asset_playback_id" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'asset_id' is set
        if ('asset_id' not in local_var_params or
                local_var_params['asset_id'] is None):
            raise ValueError("Missing the required parameter `asset_id` when calling `create_asset_playback_id`")  # noqa: E501
        # verify the required parameter 'create_playback_id_request' is set
        if ('create_playback_id_request' not in local_var_params or
                local_var_params['create_playback_id_request'] is None):
            raise ValueError("Missing the required parameter `create_playback_id_request` when calling `create_asset_playback_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'asset_id' in local_var_params:
            path_params['ASSET_ID'] = local_var_params['asset_id']  # noqa: E501

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
            '/video/v1/assets/{ASSET_ID}/playback-ids', 'POST',
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

    def create_asset_track(self, asset_id, create_track_request, **kwargs):  # noqa: E501
        """Create an asset track  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_asset_track(asset_id, create_track_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str asset_id: The asset ID. (required)
        :param CreateTrackRequest create_track_request: (required)
        :return: CreateTrackResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_asset_track_with_http_info(asset_id, create_track_request, **kwargs)  # noqa: E501
        else:
            (data) = self.create_asset_track_with_http_info(asset_id, create_track_request, **kwargs)  # noqa: E501
            return data

    def create_asset_track_with_http_info(self, asset_id, create_track_request, **kwargs):  # noqa: E501
        """Create an asset track  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_asset_track_with_http_info(asset_id, create_track_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str asset_id: The asset ID. (required)
        :param CreateTrackRequest create_track_request: (required)
        :return: CreateTrackResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['asset_id', 'create_track_request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_asset_track" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'asset_id' is set
        if ('asset_id' not in local_var_params or
                local_var_params['asset_id'] is None):
            raise ValueError("Missing the required parameter `asset_id` when calling `create_asset_track`")  # noqa: E501
        # verify the required parameter 'create_track_request' is set
        if ('create_track_request' not in local_var_params or
                local_var_params['create_track_request'] is None):
            raise ValueError("Missing the required parameter `create_track_request` when calling `create_asset_track`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'asset_id' in local_var_params:
            path_params['ASSET_ID'] = local_var_params['asset_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'create_track_request' in local_var_params:
            body_params = local_var_params['create_track_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['accessToken']  # noqa: E501

        return self.api_client.call_api(
            '/video/v1/assets/{ASSET_ID}/tracks', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreateTrackResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_asset(self, asset_id, **kwargs):  # noqa: E501
        """Delete an asset  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_asset(asset_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str asset_id: The asset ID. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_asset_with_http_info(asset_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_asset_with_http_info(asset_id, **kwargs)  # noqa: E501
            return data

    def delete_asset_with_http_info(self, asset_id, **kwargs):  # noqa: E501
        """Delete an asset  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_asset_with_http_info(asset_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str asset_id: The asset ID. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['asset_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_asset" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'asset_id' is set
        if ('asset_id' not in local_var_params or
                local_var_params['asset_id'] is None):
            raise ValueError("Missing the required parameter `asset_id` when calling `delete_asset`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'asset_id' in local_var_params:
            path_params['ASSET_ID'] = local_var_params['asset_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['accessToken']  # noqa: E501

        return self.api_client.call_api(
            '/video/v1/assets/{ASSET_ID}', 'DELETE',
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

    def delete_asset_playback_id(self, asset_id, playback_id, **kwargs):  # noqa: E501
        """Delete a playback ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_asset_playback_id(asset_id, playback_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str asset_id: The asset ID. (required)
        :param str playback_id: The live stream's playback ID. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_asset_playback_id_with_http_info(asset_id, playback_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_asset_playback_id_with_http_info(asset_id, playback_id, **kwargs)  # noqa: E501
            return data

    def delete_asset_playback_id_with_http_info(self, asset_id, playback_id, **kwargs):  # noqa: E501
        """Delete a playback ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_asset_playback_id_with_http_info(asset_id, playback_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str asset_id: The asset ID. (required)
        :param str playback_id: The live stream's playback ID. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['asset_id', 'playback_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_asset_playback_id" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'asset_id' is set
        if ('asset_id' not in local_var_params or
                local_var_params['asset_id'] is None):
            raise ValueError("Missing the required parameter `asset_id` when calling `delete_asset_playback_id`")  # noqa: E501
        # verify the required parameter 'playback_id' is set
        if ('playback_id' not in local_var_params or
                local_var_params['playback_id'] is None):
            raise ValueError("Missing the required parameter `playback_id` when calling `delete_asset_playback_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'asset_id' in local_var_params:
            path_params['ASSET_ID'] = local_var_params['asset_id']  # noqa: E501
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
            '/video/v1/assets/{ASSET_ID}/playback-ids/{PLAYBACK_ID}', 'DELETE',
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

    def delete_asset_track(self, asset_id, track_id, **kwargs):  # noqa: E501
        """Delete an asset track  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_asset_track(asset_id, track_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str asset_id: The asset ID. (required)
        :param str track_id: The track ID. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_asset_track_with_http_info(asset_id, track_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_asset_track_with_http_info(asset_id, track_id, **kwargs)  # noqa: E501
            return data

    def delete_asset_track_with_http_info(self, asset_id, track_id, **kwargs):  # noqa: E501
        """Delete an asset track  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_asset_track_with_http_info(asset_id, track_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str asset_id: The asset ID. (required)
        :param str track_id: The track ID. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['asset_id', 'track_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_asset_track" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'asset_id' is set
        if ('asset_id' not in local_var_params or
                local_var_params['asset_id'] is None):
            raise ValueError("Missing the required parameter `asset_id` when calling `delete_asset_track`")  # noqa: E501
        # verify the required parameter 'track_id' is set
        if ('track_id' not in local_var_params or
                local_var_params['track_id'] is None):
            raise ValueError("Missing the required parameter `track_id` when calling `delete_asset_track`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'asset_id' in local_var_params:
            path_params['ASSET_ID'] = local_var_params['asset_id']  # noqa: E501
        if 'track_id' in local_var_params:
            path_params['TRACK_ID'] = local_var_params['track_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['accessToken']  # noqa: E501

        return self.api_client.call_api(
            '/video/v1/assets/{ASSET_ID}/tracks/{TRACK_ID}', 'DELETE',
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

    def get_asset(self, asset_id, **kwargs):  # noqa: E501
        """Retrieve an asset  # noqa: E501

        Retrieves the details of an asset that has previously been created. Supply the unique asset ID that was returned from your previous request, and Mux will return the corresponding asset information. The same information is returned when creating an asset.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_asset(asset_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str asset_id: The asset ID. (required)
        :return: AssetResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_asset_with_http_info(asset_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_asset_with_http_info(asset_id, **kwargs)  # noqa: E501
            return data

    def get_asset_with_http_info(self, asset_id, **kwargs):  # noqa: E501
        """Retrieve an asset  # noqa: E501

        Retrieves the details of an asset that has previously been created. Supply the unique asset ID that was returned from your previous request, and Mux will return the corresponding asset information. The same information is returned when creating an asset.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_asset_with_http_info(asset_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str asset_id: The asset ID. (required)
        :return: AssetResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['asset_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_asset" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'asset_id' is set
        if ('asset_id' not in local_var_params or
                local_var_params['asset_id'] is None):
            raise ValueError("Missing the required parameter `asset_id` when calling `get_asset`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'asset_id' in local_var_params:
            path_params['ASSET_ID'] = local_var_params['asset_id']  # noqa: E501

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
            '/video/v1/assets/{ASSET_ID}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AssetResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_asset_input_info(self, asset_id, **kwargs):  # noqa: E501
        """Retrieve asset input info  # noqa: E501

        Returns a list of the input objects that were used to create the asset along with any settings that were applied to each input.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_asset_input_info(asset_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str asset_id: The asset ID. (required)
        :return: GetAssetInputInfoResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_asset_input_info_with_http_info(asset_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_asset_input_info_with_http_info(asset_id, **kwargs)  # noqa: E501
            return data

    def get_asset_input_info_with_http_info(self, asset_id, **kwargs):  # noqa: E501
        """Retrieve asset input info  # noqa: E501

        Returns a list of the input objects that were used to create the asset along with any settings that were applied to each input.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_asset_input_info_with_http_info(asset_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str asset_id: The asset ID. (required)
        :return: GetAssetInputInfoResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['asset_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_asset_input_info" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'asset_id' is set
        if ('asset_id' not in local_var_params or
                local_var_params['asset_id'] is None):
            raise ValueError("Missing the required parameter `asset_id` when calling `get_asset_input_info`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'asset_id' in local_var_params:
            path_params['ASSET_ID'] = local_var_params['asset_id']  # noqa: E501

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
            '/video/v1/assets/{ASSET_ID}/input-info', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetAssetInputInfoResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_asset_playback_id(self, asset_id, playback_id, **kwargs):  # noqa: E501
        """Retrieve a playback ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_asset_playback_id(asset_id, playback_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str asset_id: The asset ID. (required)
        :param str playback_id: The live stream's playback ID. (required)
        :return: GetAssetPlaybackIDResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_asset_playback_id_with_http_info(asset_id, playback_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_asset_playback_id_with_http_info(asset_id, playback_id, **kwargs)  # noqa: E501
            return data

    def get_asset_playback_id_with_http_info(self, asset_id, playback_id, **kwargs):  # noqa: E501
        """Retrieve a playback ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_asset_playback_id_with_http_info(asset_id, playback_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str asset_id: The asset ID. (required)
        :param str playback_id: The live stream's playback ID. (required)
        :return: GetAssetPlaybackIDResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['asset_id', 'playback_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_asset_playback_id" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'asset_id' is set
        if ('asset_id' not in local_var_params or
                local_var_params['asset_id'] is None):
            raise ValueError("Missing the required parameter `asset_id` when calling `get_asset_playback_id`")  # noqa: E501
        # verify the required parameter 'playback_id' is set
        if ('playback_id' not in local_var_params or
                local_var_params['playback_id'] is None):
            raise ValueError("Missing the required parameter `playback_id` when calling `get_asset_playback_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'asset_id' in local_var_params:
            path_params['ASSET_ID'] = local_var_params['asset_id']  # noqa: E501
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
            '/video/v1/assets/{ASSET_ID}/playback-ids/{PLAYBACK_ID}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetAssetPlaybackIDResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_assets(self, **kwargs):  # noqa: E501
        """List assets  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_assets(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit: Number of items to include in the response
        :param int page: Offset by this many pages, of the size of `limit`
        :return: ListAssetsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_assets_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_assets_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_assets_with_http_info(self, **kwargs):  # noqa: E501
        """List assets  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_assets_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit: Number of items to include in the response
        :param int page: Offset by this many pages, of the size of `limit`
        :return: ListAssetsResponse
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
                    " to method list_assets" % key
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
            '/video/v1/assets', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ListAssetsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_asset_mp4_support(self, asset_id, update_asset_mp4_support_request, **kwargs):  # noqa: E501
        """Update MP4 support  # noqa: E501

        Allows you add or remove mp4 support for assets that were created without it. Currently there are two values supported in this request, `standard` and `none`. `none` means that an asset *does not* have mp4 support, so submitting a request with `mp4_support` set to `none` will delete the mp4 assets from the asset in question.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_asset_mp4_support(asset_id, update_asset_mp4_support_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str asset_id: The asset ID. (required)
        :param UpdateAssetMP4SupportRequest update_asset_mp4_support_request: (required)
        :return: AssetResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_asset_mp4_support_with_http_info(asset_id, update_asset_mp4_support_request, **kwargs)  # noqa: E501
        else:
            (data) = self.update_asset_mp4_support_with_http_info(asset_id, update_asset_mp4_support_request, **kwargs)  # noqa: E501
            return data

    def update_asset_mp4_support_with_http_info(self, asset_id, update_asset_mp4_support_request, **kwargs):  # noqa: E501
        """Update MP4 support  # noqa: E501

        Allows you add or remove mp4 support for assets that were created without it. Currently there are two values supported in this request, `standard` and `none`. `none` means that an asset *does not* have mp4 support, so submitting a request with `mp4_support` set to `none` will delete the mp4 assets from the asset in question.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_asset_mp4_support_with_http_info(asset_id, update_asset_mp4_support_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str asset_id: The asset ID. (required)
        :param UpdateAssetMP4SupportRequest update_asset_mp4_support_request: (required)
        :return: AssetResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['asset_id', 'update_asset_mp4_support_request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_asset_mp4_support" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'asset_id' is set
        if ('asset_id' not in local_var_params or
                local_var_params['asset_id'] is None):
            raise ValueError("Missing the required parameter `asset_id` when calling `update_asset_mp4_support`")  # noqa: E501
        # verify the required parameter 'update_asset_mp4_support_request' is set
        if ('update_asset_mp4_support_request' not in local_var_params or
                local_var_params['update_asset_mp4_support_request'] is None):
            raise ValueError("Missing the required parameter `update_asset_mp4_support_request` when calling `update_asset_mp4_support`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'asset_id' in local_var_params:
            path_params['ASSET_ID'] = local_var_params['asset_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'update_asset_mp4_support_request' in local_var_params:
            body_params = local_var_params['update_asset_mp4_support_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['accessToken']  # noqa: E501

        return self.api_client.call_api(
            '/video/v1/assets/{ASSET_ID}/mp4-support', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AssetResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
