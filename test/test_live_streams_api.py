# coding: utf-8

"""
Mux Python - Copyright 2019 Mux Inc.

NOTE: This class is auto generated. Do not edit the class manually.
"""


from __future__ import absolute_import

import unittest

import mux_python
from mux_python.api.live_streams_api import LiveStreamsApi  # noqa: E501
from mux_python.rest import ApiException


class TestLiveStreamsApi(unittest.TestCase):
    """LiveStreamsApi unit test stubs"""

    def setUp(self):
        self.api = mux_python.api.live_streams_api.LiveStreamsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_live_stream(self):
        """Test case for create_live_stream

        Create a live stream  # noqa: E501
        """
        pass

    def test_create_live_stream_playback_id(self):
        """Test case for create_live_stream_playback_id

        Create a live stream playback ID  # noqa: E501
        """
        pass

    def test_create_live_stream_simulcast_target(self):
        """Test case for create_live_stream_simulcast_target

        Create a live stream simulcast target  # noqa: E501
        """
        pass

    def test_delete_live_stream(self):
        """Test case for delete_live_stream

        Delete a live stream  # noqa: E501
        """
        pass

    def test_delete_live_stream_playback_id(self):
        """Test case for delete_live_stream_playback_id

        Delete a live stream playback ID  # noqa: E501
        """
        pass

    def test_delete_live_stream_simulcast_target(self):
        """Test case for delete_live_stream_simulcast_target

        Delete a Live Stream Simulcast Target  # noqa: E501
        """
        pass

    def test_disable_live_stream(self):
        """Test case for disable_live_stream

        Disable a live stream  # noqa: E501
        """
        pass

    def test_enable_live_stream(self):
        """Test case for enable_live_stream

        Enable a live stream  # noqa: E501
        """
        pass

    def test_get_live_stream(self):
        """Test case for get_live_stream

        Retrieve a live stream  # noqa: E501
        """
        pass

    def test_get_live_stream_simulcast_target(self):
        """Test case for get_live_stream_simulcast_target

        Retrieve a Live Stream Simulcast Target  # noqa: E501
        """
        pass

    def test_list_live_streams(self):
        """Test case for list_live_streams

        List live streams  # noqa: E501
        """
        pass

    def test_reset_stream_key(self):
        """Test case for reset_stream_key

        Reset a live stream’s stream key  # noqa: E501
        """
        pass

    def test_signal_live_stream_complete(self):
        """Test case for signal_live_stream_complete

        Signal a live stream is finished  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
