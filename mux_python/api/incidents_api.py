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

class IncidentsApi(object):

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_incident(self, incident_id, **kwargs):  # noqa: E501
        """Get an Incident  # noqa: E501

        Returns the details of an incident   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_incident(incident_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str incident_id: ID of the Incident (required)
        :return: IncidentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_incident_with_http_info(incident_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_incident_with_http_info(incident_id, **kwargs)  # noqa: E501
            return data

    def get_incident_with_http_info(self, incident_id, **kwargs):  # noqa: E501
        """Get an Incident  # noqa: E501

        Returns the details of an incident   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_incident_with_http_info(incident_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str incident_id: ID of the Incident (required)
        :return: IncidentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['incident_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_incident" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'incident_id' is set
        if ('incident_id' not in local_var_params or
                local_var_params['incident_id'] is None):
            raise ValueError("Missing the required parameter `incident_id` when calling `get_incident`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'incident_id' in local_var_params:
            path_params['INCIDENT_ID'] = local_var_params['incident_id']  # noqa: E501

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
            '/data/v1/incidents/{INCIDENT_ID}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IncidentResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_incidents(self, **kwargs):  # noqa: E501
        """List Incidents  # noqa: E501

        Returns a list of incidents   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_incidents(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit: Number of items to include in the response
        :param int page: Offset by this many pages, of the size of `limit`
        :param str order_by: Value to order the results by
        :param str order_direction: Sort order.
        :param str status: Status to filter incidents by
        :param str severity: Severity to filter incidents by
        :return: ListIncidentsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_incidents_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_incidents_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_incidents_with_http_info(self, **kwargs):  # noqa: E501
        """List Incidents  # noqa: E501

        Returns a list of incidents   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_incidents_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit: Number of items to include in the response
        :param int page: Offset by this many pages, of the size of `limit`
        :param str order_by: Value to order the results by
        :param str order_direction: Sort order.
        :param str status: Status to filter incidents by
        :param str severity: Severity to filter incidents by
        :return: ListIncidentsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['limit', 'page', 'order_by', 'order_direction', 'status', 'severity']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_incidents" % key
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
        if 'order_by' in local_var_params:
            query_params.append(('order_by', local_var_params['order_by']))  # noqa: E501
        if 'order_direction' in local_var_params:
            query_params.append(('order_direction', local_var_params['order_direction']))  # noqa: E501
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))  # noqa: E501
        if 'severity' in local_var_params:
            query_params.append(('severity', local_var_params['severity']))  # noqa: E501

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
            '/data/v1/incidents', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ListIncidentsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_related_incidents(self, incident_id, **kwargs):  # noqa: E501
        """List Related Incidents  # noqa: E501

        Returns all the incidents that seem related to a specific incident   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_related_incidents(incident_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str incident_id: ID of the Incident (required)
        :param int limit: Number of items to include in the response
        :param int page: Offset by this many pages, of the size of `limit`
        :param str order_by: Value to order the results by
        :param str order_direction: Sort order.
        :return: ListRelatedIncidentsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_related_incidents_with_http_info(incident_id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_related_incidents_with_http_info(incident_id, **kwargs)  # noqa: E501
            return data

    def list_related_incidents_with_http_info(self, incident_id, **kwargs):  # noqa: E501
        """List Related Incidents  # noqa: E501

        Returns all the incidents that seem related to a specific incident   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_related_incidents_with_http_info(incident_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str incident_id: ID of the Incident (required)
        :param int limit: Number of items to include in the response
        :param int page: Offset by this many pages, of the size of `limit`
        :param str order_by: Value to order the results by
        :param str order_direction: Sort order.
        :return: ListRelatedIncidentsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['incident_id', 'limit', 'page', 'order_by', 'order_direction']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_related_incidents" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'incident_id' is set
        if ('incident_id' not in local_var_params or
                local_var_params['incident_id'] is None):
            raise ValueError("Missing the required parameter `incident_id` when calling `list_related_incidents`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'incident_id' in local_var_params:
            path_params['INCIDENT_ID'] = local_var_params['incident_id']  # noqa: E501

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))  # noqa: E501
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
            '/data/v1/incidents/{INCIDENT_ID}/related', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ListRelatedIncidentsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
