# coding: utf-8

"""
Mux Python - Copyright 2019 Mux Inc.

NOTE: This class is auto generated. Do not edit the class manually.
"""


import pprint
import re  # noqa: F401
import six

class CreateLiveStreamRequest(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'playback_policy': 'list[PlaybackPolicy]',
        'new_asset_settings': 'CreateAssetRequest',
        'reconnect_window': 'float',
        'passthrough': 'str',
        'reduced_latency': 'bool'
    }

    attribute_map = {
        'playback_policy': 'playback_policy',
        'new_asset_settings': 'new_asset_settings',
        'reconnect_window': 'reconnect_window',
        'passthrough': 'passthrough',
        'reduced_latency': 'reduced_latency'
    }

    def __init__(self, playback_policy=None, new_asset_settings=None, reconnect_window=None, passthrough=None, reduced_latency=None):  # noqa: E501
        """CreateLiveStreamRequest - a model defined in OpenAPI"""  # noqa: E501

        self._playback_policy = None
        self._new_asset_settings = None
        self._reconnect_window = None
        self._passthrough = None
        self._reduced_latency = None
        self.discriminator = None

        if playback_policy is not None:
            self.playback_policy = playback_policy
        if new_asset_settings is not None:
            self.new_asset_settings = new_asset_settings
        if reconnect_window is not None:
            self.reconnect_window = reconnect_window
        if passthrough is not None:
            self.passthrough = passthrough
        if reduced_latency is not None:
            self.reduced_latency = reduced_latency

    @property
    def playback_policy(self):
        """Gets the playback_policy of this CreateLiveStreamRequest.  # noqa: E501


        :return: The playback_policy of this CreateLiveStreamRequest.  # noqa: E501
        :rtype: list[PlaybackPolicy]
        """
        return self._playback_policy

    @playback_policy.setter
    def playback_policy(self, playback_policy):
        """Sets the playback_policy of this CreateLiveStreamRequest.


        :param playback_policy: The playback_policy of this CreateLiveStreamRequest.  # noqa: E501
        :type: list[PlaybackPolicy]
        """

        self._playback_policy = playback_policy

    @property
    def new_asset_settings(self):
        """Gets the new_asset_settings of this CreateLiveStreamRequest.  # noqa: E501


        :return: The new_asset_settings of this CreateLiveStreamRequest.  # noqa: E501
        :rtype: CreateAssetRequest
        """
        return self._new_asset_settings

    @new_asset_settings.setter
    def new_asset_settings(self, new_asset_settings):
        """Sets the new_asset_settings of this CreateLiveStreamRequest.


        :param new_asset_settings: The new_asset_settings of this CreateLiveStreamRequest.  # noqa: E501
        :type: CreateAssetRequest
        """

        self._new_asset_settings = new_asset_settings

    @property
    def reconnect_window(self):
        """Gets the reconnect_window of this CreateLiveStreamRequest.  # noqa: E501

        When live streaming software disconnects from Mux, either intentionally or due to a drop in the network, the Reconnect Window is the time in seconds that Mux should wait for the streaming software to reconnect before considering the live stream finished and completing the recorded asset. Defaults to 60 seconds on the API if not specified.  # noqa: E501

        :return: The reconnect_window of this CreateLiveStreamRequest.  # noqa: E501
        :rtype: float
        """
        return self._reconnect_window

    @reconnect_window.setter
    def reconnect_window(self, reconnect_window):
        """Sets the reconnect_window of this CreateLiveStreamRequest.

        When live streaming software disconnects from Mux, either intentionally or due to a drop in the network, the Reconnect Window is the time in seconds that Mux should wait for the streaming software to reconnect before considering the live stream finished and completing the recorded asset. Defaults to 60 seconds on the API if not specified.  # noqa: E501

        :param reconnect_window: The reconnect_window of this CreateLiveStreamRequest.  # noqa: E501
        :type: float
        """
        if reconnect_window is not None and reconnect_window > 300:  # noqa: E501
            raise ValueError("Invalid value for `reconnect_window`, must be a value less than or equal to `300`")  # noqa: E501
        if reconnect_window is not None and reconnect_window < 0.1:  # noqa: E501
            raise ValueError("Invalid value for `reconnect_window`, must be a value greater than or equal to `0.1`")  # noqa: E501

        self._reconnect_window = reconnect_window

    @property
    def passthrough(self):
        """Gets the passthrough of this CreateLiveStreamRequest.  # noqa: E501


        :return: The passthrough of this CreateLiveStreamRequest.  # noqa: E501
        :rtype: str
        """
        return self._passthrough

    @passthrough.setter
    def passthrough(self, passthrough):
        """Sets the passthrough of this CreateLiveStreamRequest.


        :param passthrough: The passthrough of this CreateLiveStreamRequest.  # noqa: E501
        :type: str
        """

        self._passthrough = passthrough

    @property
    def reduced_latency(self):
        """Gets the reduced_latency of this CreateLiveStreamRequest.  # noqa: E501

        Latency is the time from when the streamer does something in real life to when you see it happen in the player. Set this if you want lower latency for your live stream. Note: Reconnect windows are incompatible with Reduced Latency and will always be set to zero (0) seconds. Read more here: https://mux.com/blog/reduced-latency-for-mux-live-streaming-now-available/  # noqa: E501

        :return: The reduced_latency of this CreateLiveStreamRequest.  # noqa: E501
        :rtype: bool
        """
        return self._reduced_latency

    @reduced_latency.setter
    def reduced_latency(self, reduced_latency):
        """Sets the reduced_latency of this CreateLiveStreamRequest.

        Latency is the time from when the streamer does something in real life to when you see it happen in the player. Set this if you want lower latency for your live stream. Note: Reconnect windows are incompatible with Reduced Latency and will always be set to zero (0) seconds. Read more here: https://mux.com/blog/reduced-latency-for-mux-live-streaming-now-available/  # noqa: E501

        :param reduced_latency: The reduced_latency of this CreateLiveStreamRequest.  # noqa: E501
        :type: bool
        """

        self._reduced_latency = reduced_latency

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateLiveStreamRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
