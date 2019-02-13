# coding: utf-8

"""
Mux Python - Copyright 2019 Mux Inc.

NOTE: This class is auto generated. Do not edit the class manually.
"""


import pprint
import re  # noqa: F401
import six

class CreateAssetRequest(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'input': 'list[InputSettings]',
        'playback_policy': 'list[PlaybackPolicy]',
        'demo': 'bool',
        'per_title_encode': 'bool',
        'passthrough': 'str',
        'mp4_support': 'str'
    }

    attribute_map = {
        'input': 'input',
        'playback_policy': 'playback_policy',
        'demo': 'demo',
        'per_title_encode': 'per_title_encode',
        'passthrough': 'passthrough',
        'mp4_support': 'mp4_support'
    }

    def __init__(self, input=None, playback_policy=None, demo=None, per_title_encode=None, passthrough=None, mp4_support=None):  # noqa: E501
        """CreateAssetRequest - a model defined in OpenAPI"""  # noqa: E501

        self._input = None
        self._playback_policy = None
        self._demo = None
        self._per_title_encode = None
        self._passthrough = None
        self._mp4_support = None
        self.discriminator = None

        if input is not None:
            self.input = input
        if playback_policy is not None:
            self.playback_policy = playback_policy
        if demo is not None:
            self.demo = demo
        if per_title_encode is not None:
            self.per_title_encode = per_title_encode
        if passthrough is not None:
            self.passthrough = passthrough
        if mp4_support is not None:
            self.mp4_support = mp4_support

    @property
    def input(self):
        """Gets the input of this CreateAssetRequest.  # noqa: E501


        :return: The input of this CreateAssetRequest.  # noqa: E501
        :rtype: list[InputSettings]
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this CreateAssetRequest.


        :param input: The input of this CreateAssetRequest.  # noqa: E501
        :type: list[InputSettings]
        """

        self._input = input

    @property
    def playback_policy(self):
        """Gets the playback_policy of this CreateAssetRequest.  # noqa: E501


        :return: The playback_policy of this CreateAssetRequest.  # noqa: E501
        :rtype: list[PlaybackPolicy]
        """
        return self._playback_policy

    @playback_policy.setter
    def playback_policy(self, playback_policy):
        """Sets the playback_policy of this CreateAssetRequest.


        :param playback_policy: The playback_policy of this CreateAssetRequest.  # noqa: E501
        :type: list[PlaybackPolicy]
        """

        self._playback_policy = playback_policy

    @property
    def demo(self):
        """Gets the demo of this CreateAssetRequest.  # noqa: E501


        :return: The demo of this CreateAssetRequest.  # noqa: E501
        :rtype: bool
        """
        return self._demo

    @demo.setter
    def demo(self, demo):
        """Sets the demo of this CreateAssetRequest.


        :param demo: The demo of this CreateAssetRequest.  # noqa: E501
        :type: bool
        """

        self._demo = demo

    @property
    def per_title_encode(self):
        """Gets the per_title_encode of this CreateAssetRequest.  # noqa: E501


        :return: The per_title_encode of this CreateAssetRequest.  # noqa: E501
        :rtype: bool
        """
        return self._per_title_encode

    @per_title_encode.setter
    def per_title_encode(self, per_title_encode):
        """Sets the per_title_encode of this CreateAssetRequest.


        :param per_title_encode: The per_title_encode of this CreateAssetRequest.  # noqa: E501
        :type: bool
        """

        self._per_title_encode = per_title_encode

    @property
    def passthrough(self):
        """Gets the passthrough of this CreateAssetRequest.  # noqa: E501


        :return: The passthrough of this CreateAssetRequest.  # noqa: E501
        :rtype: str
        """
        return self._passthrough

    @passthrough.setter
    def passthrough(self, passthrough):
        """Sets the passthrough of this CreateAssetRequest.


        :param passthrough: The passthrough of this CreateAssetRequest.  # noqa: E501
        :type: str
        """

        self._passthrough = passthrough

    @property
    def mp4_support(self):
        """Gets the mp4_support of this CreateAssetRequest.  # noqa: E501


        :return: The mp4_support of this CreateAssetRequest.  # noqa: E501
        :rtype: str
        """
        return self._mp4_support

    @mp4_support.setter
    def mp4_support(self, mp4_support):
        """Sets the mp4_support of this CreateAssetRequest.


        :param mp4_support: The mp4_support of this CreateAssetRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["none", "standard"]  # noqa: E501
        if mp4_support not in allowed_values:
            raise ValueError(
                "Invalid value for `mp4_support` ({0}), must be one of {1}"  # noqa: E501
                .format(mp4_support, allowed_values)
            )

        self._mp4_support = mp4_support

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
        if not isinstance(other, CreateAssetRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
