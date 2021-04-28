# coding: utf-8

"""
Mux Python - Copyright 2019 Mux Inc.

NOTE: This class is auto generated. Do not edit the class manually.
"""


import pprint
import re  # noqa: F401
import six

class RealTimeHistogramTimeseriesDatapoint(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'timestamp': 'str',
        'sum': 'int',
        'p95': 'float',
        'median': 'float',
        'max_percentage': 'float',
        'bucket_values': 'list[RealTimeHistogramTimeseriesBucketValues]',
        'average': 'float'
    }

    attribute_map = {
        'timestamp': 'timestamp',
        'sum': 'sum',
        'p95': 'p95',
        'median': 'median',
        'max_percentage': 'max_percentage',
        'bucket_values': 'bucket_values',
        'average': 'average'
    }

    def __init__(self, timestamp=None, sum=None, p95=None, median=None, max_percentage=None, bucket_values=None, average=None):  # noqa: E501
        """RealTimeHistogramTimeseriesDatapoint - a model defined in OpenAPI"""  # noqa: E501

        self._timestamp = None
        self._sum = None
        self._p95 = None
        self._median = None
        self._max_percentage = None
        self._bucket_values = None
        self._average = None
        self.discriminator = None

        if timestamp is not None:
            self.timestamp = timestamp
        if sum is not None:
            self.sum = sum
        if p95 is not None:
            self.p95 = p95
        if median is not None:
            self.median = median
        if max_percentage is not None:
            self.max_percentage = max_percentage
        if bucket_values is not None:
            self.bucket_values = bucket_values
        if average is not None:
            self.average = average

    @property
    def timestamp(self):
        """Gets the timestamp of this RealTimeHistogramTimeseriesDatapoint.  # noqa: E501


        :return: The timestamp of this RealTimeHistogramTimeseriesDatapoint.  # noqa: E501
        :rtype: str
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this RealTimeHistogramTimeseriesDatapoint.


        :param timestamp: The timestamp of this RealTimeHistogramTimeseriesDatapoint.  # noqa: E501
        :type: str
        """

        self._timestamp = timestamp

    @property
    def sum(self):
        """Gets the sum of this RealTimeHistogramTimeseriesDatapoint.  # noqa: E501


        :return: The sum of this RealTimeHistogramTimeseriesDatapoint.  # noqa: E501
        :rtype: int
        """
        return self._sum

    @sum.setter
    def sum(self, sum):
        """Sets the sum of this RealTimeHistogramTimeseriesDatapoint.


        :param sum: The sum of this RealTimeHistogramTimeseriesDatapoint.  # noqa: E501
        :type: int
        """

        self._sum = sum

    @property
    def p95(self):
        """Gets the p95 of this RealTimeHistogramTimeseriesDatapoint.  # noqa: E501


        :return: The p95 of this RealTimeHistogramTimeseriesDatapoint.  # noqa: E501
        :rtype: float
        """
        return self._p95

    @p95.setter
    def p95(self, p95):
        """Sets the p95 of this RealTimeHistogramTimeseriesDatapoint.


        :param p95: The p95 of this RealTimeHistogramTimeseriesDatapoint.  # noqa: E501
        :type: float
        """

        self._p95 = p95

    @property
    def median(self):
        """Gets the median of this RealTimeHistogramTimeseriesDatapoint.  # noqa: E501


        :return: The median of this RealTimeHistogramTimeseriesDatapoint.  # noqa: E501
        :rtype: float
        """
        return self._median

    @median.setter
    def median(self, median):
        """Sets the median of this RealTimeHistogramTimeseriesDatapoint.


        :param median: The median of this RealTimeHistogramTimeseriesDatapoint.  # noqa: E501
        :type: float
        """

        self._median = median

    @property
    def max_percentage(self):
        """Gets the max_percentage of this RealTimeHistogramTimeseriesDatapoint.  # noqa: E501


        :return: The max_percentage of this RealTimeHistogramTimeseriesDatapoint.  # noqa: E501
        :rtype: float
        """
        return self._max_percentage

    @max_percentage.setter
    def max_percentage(self, max_percentage):
        """Sets the max_percentage of this RealTimeHistogramTimeseriesDatapoint.


        :param max_percentage: The max_percentage of this RealTimeHistogramTimeseriesDatapoint.  # noqa: E501
        :type: float
        """

        self._max_percentage = max_percentage

    @property
    def bucket_values(self):
        """Gets the bucket_values of this RealTimeHistogramTimeseriesDatapoint.  # noqa: E501


        :return: The bucket_values of this RealTimeHistogramTimeseriesDatapoint.  # noqa: E501
        :rtype: list[RealTimeHistogramTimeseriesBucketValues]
        """
        return self._bucket_values

    @bucket_values.setter
    def bucket_values(self, bucket_values):
        """Sets the bucket_values of this RealTimeHistogramTimeseriesDatapoint.


        :param bucket_values: The bucket_values of this RealTimeHistogramTimeseriesDatapoint.  # noqa: E501
        :type: list[RealTimeHistogramTimeseriesBucketValues]
        """

        self._bucket_values = bucket_values

    @property
    def average(self):
        """Gets the average of this RealTimeHistogramTimeseriesDatapoint.  # noqa: E501


        :return: The average of this RealTimeHistogramTimeseriesDatapoint.  # noqa: E501
        :rtype: float
        """
        return self._average

    @average.setter
    def average(self, average):
        """Sets the average of this RealTimeHistogramTimeseriesDatapoint.


        :param average: The average of this RealTimeHistogramTimeseriesDatapoint.  # noqa: E501
        :type: float
        """

        self._average = average

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
        if not isinstance(other, RealTimeHistogramTimeseriesDatapoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other