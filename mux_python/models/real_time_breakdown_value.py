# coding: utf-8

"""
Mux Python - Copyright 2019 Mux Inc.

NOTE: This class is auto generated. Do not edit the class manually.
"""


import pprint
import re  # noqa: F401
import six

class RealTimeBreakdownValue(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'value': 'str',
        'negative_impact': 'int',
        'metric_value': 'float',
        'display_value': 'str',
        'concurent_viewers': 'int'
    }

    attribute_map = {
        'value': 'value',
        'negative_impact': 'negative_impact',
        'metric_value': 'metric_value',
        'display_value': 'display_value',
        'concurent_viewers': 'concurent_viewers'
    }

    def __init__(self, value=None, negative_impact=None, metric_value=None, display_value=None, concurent_viewers=None):  # noqa: E501
        """RealTimeBreakdownValue - a model defined in OpenAPI"""  # noqa: E501

        self._value = None
        self._negative_impact = None
        self._metric_value = None
        self._display_value = None
        self._concurent_viewers = None
        self.discriminator = None

        if value is not None:
            self.value = value
        if negative_impact is not None:
            self.negative_impact = negative_impact
        if metric_value is not None:
            self.metric_value = metric_value
        if display_value is not None:
            self.display_value = display_value
        if concurent_viewers is not None:
            self.concurent_viewers = concurent_viewers

    @property
    def value(self):
        """Gets the value of this RealTimeBreakdownValue.  # noqa: E501


        :return: The value of this RealTimeBreakdownValue.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this RealTimeBreakdownValue.


        :param value: The value of this RealTimeBreakdownValue.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def negative_impact(self):
        """Gets the negative_impact of this RealTimeBreakdownValue.  # noqa: E501


        :return: The negative_impact of this RealTimeBreakdownValue.  # noqa: E501
        :rtype: int
        """
        return self._negative_impact

    @negative_impact.setter
    def negative_impact(self, negative_impact):
        """Sets the negative_impact of this RealTimeBreakdownValue.


        :param negative_impact: The negative_impact of this RealTimeBreakdownValue.  # noqa: E501
        :type: int
        """

        self._negative_impact = negative_impact

    @property
    def metric_value(self):
        """Gets the metric_value of this RealTimeBreakdownValue.  # noqa: E501


        :return: The metric_value of this RealTimeBreakdownValue.  # noqa: E501
        :rtype: float
        """
        return self._metric_value

    @metric_value.setter
    def metric_value(self, metric_value):
        """Sets the metric_value of this RealTimeBreakdownValue.


        :param metric_value: The metric_value of this RealTimeBreakdownValue.  # noqa: E501
        :type: float
        """

        self._metric_value = metric_value

    @property
    def display_value(self):
        """Gets the display_value of this RealTimeBreakdownValue.  # noqa: E501


        :return: The display_value of this RealTimeBreakdownValue.  # noqa: E501
        :rtype: str
        """
        return self._display_value

    @display_value.setter
    def display_value(self, display_value):
        """Sets the display_value of this RealTimeBreakdownValue.


        :param display_value: The display_value of this RealTimeBreakdownValue.  # noqa: E501
        :type: str
        """

        self._display_value = display_value

    @property
    def concurent_viewers(self):
        """Gets the concurent_viewers of this RealTimeBreakdownValue.  # noqa: E501


        :return: The concurent_viewers of this RealTimeBreakdownValue.  # noqa: E501
        :rtype: int
        """
        return self._concurent_viewers

    @concurent_viewers.setter
    def concurent_viewers(self, concurent_viewers):
        """Sets the concurent_viewers of this RealTimeBreakdownValue.


        :param concurent_viewers: The concurent_viewers of this RealTimeBreakdownValue.  # noqa: E501
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
        if not isinstance(other, RealTimeBreakdownValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
