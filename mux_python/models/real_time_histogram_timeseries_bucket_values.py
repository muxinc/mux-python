# coding: utf-8

"""
Mux Python - Copyright 2019 Mux Inc.

NOTE: This class is auto generated. Do not edit the class manually.
"""


import pprint
import re  # noqa: F401
import six

class RealTimeHistogramTimeseriesBucketValues(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'percentage': 'float',
        'count': 'int'
    }

    attribute_map = {
        'percentage': 'percentage',
        'count': 'count'
    }

    def __init__(self, percentage=None, count=None):  # noqa: E501
        """RealTimeHistogramTimeseriesBucketValues - a model defined in OpenAPI"""  # noqa: E501

        self._percentage = None
        self._count = None
        self.discriminator = None

        if percentage is not None:
            self.percentage = percentage
        if count is not None:
            self.count = count

    @property
    def percentage(self):
        """Gets the percentage of this RealTimeHistogramTimeseriesBucketValues.  # noqa: E501


        :return: The percentage of this RealTimeHistogramTimeseriesBucketValues.  # noqa: E501
        :rtype: float
        """
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        """Sets the percentage of this RealTimeHistogramTimeseriesBucketValues.


        :param percentage: The percentage of this RealTimeHistogramTimeseriesBucketValues.  # noqa: E501
        :type: float
        """

        self._percentage = percentage

    @property
    def count(self):
        """Gets the count of this RealTimeHistogramTimeseriesBucketValues.  # noqa: E501


        :return: The count of this RealTimeHistogramTimeseriesBucketValues.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this RealTimeHistogramTimeseriesBucketValues.


        :param count: The count of this RealTimeHistogramTimeseriesBucketValues.  # noqa: E501
        :type: int
        """

        self._count = count

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
        if not isinstance(other, RealTimeHistogramTimeseriesBucketValues):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
