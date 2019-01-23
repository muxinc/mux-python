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
        'new_asset_settings': 'CreateAssetRequest'
    }

    attribute_map = {
        'playback_policy': 'playback_policy',
        'new_asset_settings': 'new_asset_settings'
    }

    def __init__(self, playback_policy=None, new_asset_settings=None):  # noqa: E501
        """CreateLiveStreamRequest - a model defined in OpenAPI"""  # noqa: E501

        self._playback_policy = None
        self._new_asset_settings = None
        self.discriminator = None

        if playback_policy is not None:
            self.playback_policy = playback_policy
        if new_asset_settings is not None:
            self.new_asset_settings = new_asset_settings

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
