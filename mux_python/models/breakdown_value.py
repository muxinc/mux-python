# coding: utf-8

"""
Mux Python - Copyright 2019 Mux Inc.

NOTE: This class is auto generated. Do not edit the class manually.
"""


import pprint
import re  # noqa: F401
import six

class BreakdownValue(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'views': 'int',
        'value': 'float',
        'total_watch_time': 'int',
        'negative_impact': 'int',
        'field': 'str'
    }

    attribute_map = {
        'views': 'views',
        'value': 'value',
        'total_watch_time': 'total_watch_time',
        'negative_impact': 'negative_impact',
        'field': 'field'
    }

    def __init__(self, views=None, value=None, total_watch_time=None, negative_impact=None, field=None):  # noqa: E501
        """BreakdownValue - a model defined in OpenAPI"""  # noqa: E501

        self._views = None
        self._value = None
        self._total_watch_time = None
        self._negative_impact = None
        self._field = None
        self.discriminator = None

        if views is not None:
            self.views = views
        if value is not None:
            self.value = value
        if total_watch_time is not None:
            self.total_watch_time = total_watch_time
        if negative_impact is not None:
            self.negative_impact = negative_impact
        if field is not None:
            self.field = field

    @property
    def views(self):
        """Gets the views of this BreakdownValue.  # noqa: E501


        :return: The views of this BreakdownValue.  # noqa: E501
        :rtype: int
        """
        return self._views

    @views.setter
    def views(self, views):
        """Sets the views of this BreakdownValue.


        :param views: The views of this BreakdownValue.  # noqa: E501
        :type: int
        """

        self._views = views

    @property
    def value(self):
        """Gets the value of this BreakdownValue.  # noqa: E501


        :return: The value of this BreakdownValue.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this BreakdownValue.


        :param value: The value of this BreakdownValue.  # noqa: E501
        :type: float
        """

        self._value = value

    @property
    def total_watch_time(self):
        """Gets the total_watch_time of this BreakdownValue.  # noqa: E501


        :return: The total_watch_time of this BreakdownValue.  # noqa: E501
        :rtype: int
        """
        return self._total_watch_time

    @total_watch_time.setter
    def total_watch_time(self, total_watch_time):
        """Sets the total_watch_time of this BreakdownValue.


        :param total_watch_time: The total_watch_time of this BreakdownValue.  # noqa: E501
        :type: int
        """

        self._total_watch_time = total_watch_time

    @property
    def negative_impact(self):
        """Gets the negative_impact of this BreakdownValue.  # noqa: E501


        :return: The negative_impact of this BreakdownValue.  # noqa: E501
        :rtype: int
        """
        return self._negative_impact

    @negative_impact.setter
    def negative_impact(self, negative_impact):
        """Sets the negative_impact of this BreakdownValue.


        :param negative_impact: The negative_impact of this BreakdownValue.  # noqa: E501
        :type: int
        """

        self._negative_impact = negative_impact

    @property
    def field(self):
        """Gets the field of this BreakdownValue.  # noqa: E501


        :return: The field of this BreakdownValue.  # noqa: E501
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field):
        """Sets the field of this BreakdownValue.


        :param field: The field of this BreakdownValue.  # noqa: E501
        :type: str
        """

        self._field = field

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
        if not isinstance(other, BreakdownValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
