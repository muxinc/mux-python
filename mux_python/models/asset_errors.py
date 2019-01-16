# coding: utf-8

"""
Mux Python - Copyright 2019 Mux Inc.

NOTE: This class is auto generated. Do not edit the class manually.
"""


import pprint
import re  # noqa: F401
import six

class AssetErrors(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'type': 'str',
        'messages': 'list[str]'
    }

    attribute_map = {
        'type': 'type',
        'messages': 'messages'
    }

    def __init__(self, type=None, messages=None):  # noqa: E501
        """AssetErrors - a model defined in OpenAPI"""  # noqa: E501

        self._type = None
        self._messages = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if messages is not None:
            self.messages = messages

    @property
    def type(self):
        """Gets the type of this AssetErrors.  # noqa: E501


        :return: The type of this AssetErrors.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AssetErrors.


        :param type: The type of this AssetErrors.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def messages(self):
        """Gets the messages of this AssetErrors.  # noqa: E501


        :return: The messages of this AssetErrors.  # noqa: E501
        :rtype: list[str]
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        """Sets the messages of this AssetErrors.


        :param messages: The messages of this AssetErrors.  # noqa: E501
        :type: list[str]
        """

        self._messages = messages

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
        if not isinstance(other, AssetErrors):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
