# coding: utf-8

"""
Mux Python - Copyright 2019 Mux Inc.

NOTE: This class is auto generated. Do not edit the class manually.
"""


import pprint
import re  # noqa: F401
import six

class FilterValue(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'value': 'str',
        'total_count': 'int'
    }

    attribute_map = {
        'value': 'value',
        'total_count': 'total_count'
    }

    def __init__(self, value=None, total_count=None):  # noqa: E501
        """FilterValue - a model defined in OpenAPI"""  # noqa: E501

        self._value = None
        self._total_count = None
        self.discriminator = None

        if value is not None:
            self.value = value
        if total_count is not None:
            self.total_count = total_count

    @property
    def value(self):
        """Gets the value of this FilterValue.  # noqa: E501


        :return: The value of this FilterValue.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this FilterValue.


        :param value: The value of this FilterValue.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def total_count(self):
        """Gets the total_count of this FilterValue.  # noqa: E501


        :return: The total_count of this FilterValue.  # noqa: E501
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this FilterValue.


        :param total_count: The total_count of this FilterValue.  # noqa: E501
        :type: int
        """

        self._total_count = total_count

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
        if not isinstance(other, FilterValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
