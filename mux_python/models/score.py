# coding: utf-8

"""
Mux Python - Copyright 2019 Mux Inc.

NOTE: This class is auto generated. Do not edit the class manually.
"""


import pprint
import re  # noqa: F401
import six

class Score(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'watch_time': 'int',
        'view_count': 'int',
        'name': 'str',
        'value': 'float',
        'metric': 'str',
        'items': 'list[Metric]'
    }

    attribute_map = {
        'watch_time': 'watch_time',
        'view_count': 'view_count',
        'name': 'name',
        'value': 'value',
        'metric': 'metric',
        'items': 'items'
    }

    def __init__(self, watch_time=None, view_count=None, name=None, value=None, metric=None, items=None):  # noqa: E501
        """Score - a model defined in OpenAPI"""  # noqa: E501

        self._watch_time = None
        self._view_count = None
        self._name = None
        self._value = None
        self._metric = None
        self._items = None
        self.discriminator = None

        if watch_time is not None:
            self.watch_time = watch_time
        if view_count is not None:
            self.view_count = view_count
        if name is not None:
            self.name = name
        if value is not None:
            self.value = value
        if metric is not None:
            self.metric = metric
        if items is not None:
            self.items = items

    @property
    def watch_time(self):
        """Gets the watch_time of this Score.  # noqa: E501


        :return: The watch_time of this Score.  # noqa: E501
        :rtype: int
        """
        return self._watch_time

    @watch_time.setter
    def watch_time(self, watch_time):
        """Sets the watch_time of this Score.


        :param watch_time: The watch_time of this Score.  # noqa: E501
        :type: int
        """

        self._watch_time = watch_time

    @property
    def view_count(self):
        """Gets the view_count of this Score.  # noqa: E501


        :return: The view_count of this Score.  # noqa: E501
        :rtype: int
        """
        return self._view_count

    @view_count.setter
    def view_count(self, view_count):
        """Sets the view_count of this Score.


        :param view_count: The view_count of this Score.  # noqa: E501
        :type: int
        """

        self._view_count = view_count

    @property
    def name(self):
        """Gets the name of this Score.  # noqa: E501


        :return: The name of this Score.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Score.


        :param name: The name of this Score.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def value(self):
        """Gets the value of this Score.  # noqa: E501


        :return: The value of this Score.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Score.


        :param value: The value of this Score.  # noqa: E501
        :type: float
        """

        self._value = value

    @property
    def metric(self):
        """Gets the metric of this Score.  # noqa: E501


        :return: The metric of this Score.  # noqa: E501
        :rtype: str
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """Sets the metric of this Score.


        :param metric: The metric of this Score.  # noqa: E501
        :type: str
        """

        self._metric = metric

    @property
    def items(self):
        """Gets the items of this Score.  # noqa: E501


        :return: The items of this Score.  # noqa: E501
        :rtype: list[Metric]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this Score.


        :param items: The items of this Score.  # noqa: E501
        :type: list[Metric]
        """

        self._items = items

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
        if not isinstance(other, Score):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
