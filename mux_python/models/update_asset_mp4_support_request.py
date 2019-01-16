# coding: utf-8

"""
Mux Python - Copyright 2019 Mux Inc.

NOTE: This class is auto generated. Do not edit the class manually.
"""


import pprint
import re  # noqa: F401
import six

class UpdateAssetMP4SupportRequest(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'mp4_support': 'str'
    }

    attribute_map = {
        'mp4_support': 'mp4_support'
    }

    def __init__(self, mp4_support=None):  # noqa: E501
        """UpdateAssetMP4SupportRequest - a model defined in OpenAPI"""  # noqa: E501

        self._mp4_support = None
        self.discriminator = None

        if mp4_support is not None:
            self.mp4_support = mp4_support

    @property
    def mp4_support(self):
        """Gets the mp4_support of this UpdateAssetMP4SupportRequest.  # noqa: E501

        String value for the level of mp4 support  # noqa: E501

        :return: The mp4_support of this UpdateAssetMP4SupportRequest.  # noqa: E501
        :rtype: str
        """
        return self._mp4_support

    @mp4_support.setter
    def mp4_support(self, mp4_support):
        """Sets the mp4_support of this UpdateAssetMP4SupportRequest.

        String value for the level of mp4 support  # noqa: E501

        :param mp4_support: The mp4_support of this UpdateAssetMP4SupportRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["standard", "none"]  # noqa: E501
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
        if not isinstance(other, UpdateAssetMP4SupportRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
