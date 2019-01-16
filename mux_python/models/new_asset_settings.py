# coding: utf-8

"""
Mux Python - Copyright 2019 Mux Inc.

NOTE: This class is auto generated. Do not edit the class manually.
"""


import pprint
import re  # noqa: F401
import six

class NewAssetSettings(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'playback_policies': 'list[PlaybackPolicy]'
    }

    attribute_map = {
        'playback_policies': 'playback_policies'
    }

    def __init__(self, playback_policies=None):  # noqa: E501
        """NewAssetSettings - a model defined in OpenAPI"""  # noqa: E501

        self._playback_policies = None
        self.discriminator = None

        if playback_policies is not None:
            self.playback_policies = playback_policies

    @property
    def playback_policies(self):
        """Gets the playback_policies of this NewAssetSettings.  # noqa: E501


        :return: The playback_policies of this NewAssetSettings.  # noqa: E501
        :rtype: list[PlaybackPolicy]
        """
        return self._playback_policies

    @playback_policies.setter
    def playback_policies(self, playback_policies):
        """Sets the playback_policies of this NewAssetSettings.


        :param playback_policies: The playback_policies of this NewAssetSettings.  # noqa: E501
        :type: list[PlaybackPolicy]
        """

        self._playback_policies = playback_policies

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
        if not isinstance(other, NewAssetSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
