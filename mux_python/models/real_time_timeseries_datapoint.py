# coding: utf-8

"""
Mux Python - Copyright 2019 Mux Inc.

NOTE: This class is auto generated. Do not edit the class manually.
"""


import pprint
import re  # noqa: F401
import six

class RealTimeTimeseriesDatapoint(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'value': 'float',
        'date': 'str',
        'concurent_viewers': 'int'
    }

    attribute_map = {
        'value': 'value',
        'date': 'date',
        'concurent_viewers': 'concurent_viewers'
    }

    def __init__(self, value=None, date=None, concurent_viewers=None):  # noqa: E501
        """RealTimeTimeseriesDatapoint - a model defined in OpenAPI"""  # noqa: E501

        self._value = None
        self._date = None
        self._concurent_viewers = None
        self.discriminator = None

        if value is not None:
            self.value = value
        if date is not None:
            self.date = date
        if concurent_viewers is not None:
            self.concurent_viewers = concurent_viewers

    @property
    def value(self):
        """Gets the value of this RealTimeTimeseriesDatapoint.  # noqa: E501


        :return: The value of this RealTimeTimeseriesDatapoint.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this RealTimeTimeseriesDatapoint.


        :param value: The value of this RealTimeTimeseriesDatapoint.  # noqa: E501
        :type: float
        """

        self._value = value

    @property
    def date(self):
        """Gets the date of this RealTimeTimeseriesDatapoint.  # noqa: E501


        :return: The date of this RealTimeTimeseriesDatapoint.  # noqa: E501
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this RealTimeTimeseriesDatapoint.


        :param date: The date of this RealTimeTimeseriesDatapoint.  # noqa: E501
        :type: str
        """

        self._date = date

    @property
    def concurent_viewers(self):
        """Gets the concurent_viewers of this RealTimeTimeseriesDatapoint.  # noqa: E501


        :return: The concurent_viewers of this RealTimeTimeseriesDatapoint.  # noqa: E501
        :rtype: int
        """
        return self._concurent_viewers

    @concurent_viewers.setter
    def concurent_viewers(self, concurent_viewers):
        """Sets the concurent_viewers of this RealTimeTimeseriesDatapoint.


        :param concurent_viewers: The concurent_viewers of this RealTimeTimeseriesDatapoint.  # noqa: E501
        :type: int
        """

        self._concurent_viewers = concurent_viewers

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
        if not isinstance(other, RealTimeTimeseriesDatapoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
