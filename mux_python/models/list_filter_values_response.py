# coding: utf-8

"""
Mux Python - Copyright 2019 Mux Inc.

NOTE: This class is auto generated. Do not edit the class manually.
"""


import pprint
import re  # noqa: F401
import six

class ListFilterValuesResponse(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'data': 'list[FilterValue]',
        'total_row_count': 'int',
        'timeframe': 'list[int]'
    }

    attribute_map = {
        'data': 'data',
        'total_row_count': 'total_row_count',
        'timeframe': 'timeframe'
    }

    def __init__(self, data=None, total_row_count=None, timeframe=None):  # noqa: E501
        """ListFilterValuesResponse - a model defined in OpenAPI"""  # noqa: E501

        self._data = None
        self._total_row_count = None
        self._timeframe = None
        self.discriminator = None

        if data is not None:
            self.data = data
        if total_row_count is not None:
            self.total_row_count = total_row_count
        if timeframe is not None:
            self.timeframe = timeframe

    @property
    def data(self):
        """Gets the data of this ListFilterValuesResponse.  # noqa: E501


        :return: The data of this ListFilterValuesResponse.  # noqa: E501
        :rtype: list[FilterValue]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ListFilterValuesResponse.


        :param data: The data of this ListFilterValuesResponse.  # noqa: E501
        :type: list[FilterValue]
        """

        self._data = data

    @property
    def total_row_count(self):
        """Gets the total_row_count of this ListFilterValuesResponse.  # noqa: E501


        :return: The total_row_count of this ListFilterValuesResponse.  # noqa: E501
        :rtype: int
        """
        return self._total_row_count

    @total_row_count.setter
    def total_row_count(self, total_row_count):
        """Sets the total_row_count of this ListFilterValuesResponse.


        :param total_row_count: The total_row_count of this ListFilterValuesResponse.  # noqa: E501
        :type: int
        """

        self._total_row_count = total_row_count

    @property
    def timeframe(self):
        """Gets the timeframe of this ListFilterValuesResponse.  # noqa: E501


        :return: The timeframe of this ListFilterValuesResponse.  # noqa: E501
        :rtype: list[int]
        """
        return self._timeframe

    @timeframe.setter
    def timeframe(self, timeframe):
        """Sets the timeframe of this ListFilterValuesResponse.


        :param timeframe: The timeframe of this ListFilterValuesResponse.  # noqa: E501
        :type: list[int]
        """

        self._timeframe = timeframe

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
        if not isinstance(other, ListFilterValuesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
