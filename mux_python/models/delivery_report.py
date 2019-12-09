# coding: utf-8

"""
Mux Python - Copyright 2019 Mux Inc.

NOTE: This class is auto generated. Do not edit the class manually.
"""


import pprint
import re  # noqa: F401
import six

class DeliveryReport(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'live_stream_id': 'str',
        'asset_id': 'str',
        'passthrough': 'str',
        'created_at': 'str',
        'asset_state': 'str',
        'asset_duration': 'float',
        'delivered_seconds': 'float'
    }

    attribute_map = {
        'live_stream_id': 'live_stream_id',
        'asset_id': 'asset_id',
        'passthrough': 'passthrough',
        'created_at': 'created_at',
        'asset_state': 'asset_state',
        'asset_duration': 'asset_duration',
        'delivered_seconds': 'delivered_seconds'
    }

    def __init__(self, live_stream_id=None, asset_id=None, passthrough=None, created_at=None, asset_state=None, asset_duration=None, delivered_seconds=None):  # noqa: E501
        """DeliveryReport - a model defined in OpenAPI"""  # noqa: E501

        self._live_stream_id = None
        self._asset_id = None
        self._passthrough = None
        self._created_at = None
        self._asset_state = None
        self._asset_duration = None
        self._delivered_seconds = None
        self.discriminator = None

        if live_stream_id is not None:
            self.live_stream_id = live_stream_id
        if asset_id is not None:
            self.asset_id = asset_id
        if passthrough is not None:
            self.passthrough = passthrough
        if created_at is not None:
            self.created_at = created_at
        if asset_state is not None:
            self.asset_state = asset_state
        if asset_duration is not None:
            self.asset_duration = asset_duration
        if delivered_seconds is not None:
            self.delivered_seconds = delivered_seconds

    @property
    def live_stream_id(self):
        """Gets the live_stream_id of this DeliveryReport.  # noqa: E501


        :return: The live_stream_id of this DeliveryReport.  # noqa: E501
        :rtype: str
        """
        return self._live_stream_id

    @live_stream_id.setter
    def live_stream_id(self, live_stream_id):
        """Sets the live_stream_id of this DeliveryReport.


        :param live_stream_id: The live_stream_id of this DeliveryReport.  # noqa: E501
        :type: str
        """

        self._live_stream_id = live_stream_id

    @property
    def asset_id(self):
        """Gets the asset_id of this DeliveryReport.  # noqa: E501


        :return: The asset_id of this DeliveryReport.  # noqa: E501
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        """Sets the asset_id of this DeliveryReport.


        :param asset_id: The asset_id of this DeliveryReport.  # noqa: E501
        :type: str
        """

        self._asset_id = asset_id

    @property
    def passthrough(self):
        """Gets the passthrough of this DeliveryReport.  # noqa: E501


        :return: The passthrough of this DeliveryReport.  # noqa: E501
        :rtype: str
        """
        return self._passthrough

    @passthrough.setter
    def passthrough(self, passthrough):
        """Sets the passthrough of this DeliveryReport.


        :param passthrough: The passthrough of this DeliveryReport.  # noqa: E501
        :type: str
        """

        self._passthrough = passthrough

    @property
    def created_at(self):
        """Gets the created_at of this DeliveryReport.  # noqa: E501


        :return: The created_at of this DeliveryReport.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this DeliveryReport.


        :param created_at: The created_at of this DeliveryReport.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def asset_state(self):
        """Gets the asset_state of this DeliveryReport.  # noqa: E501


        :return: The asset_state of this DeliveryReport.  # noqa: E501
        :rtype: str
        """
        return self._asset_state

    @asset_state.setter
    def asset_state(self, asset_state):
        """Sets the asset_state of this DeliveryReport.


        :param asset_state: The asset_state of this DeliveryReport.  # noqa: E501
        :type: str
        """

        self._asset_state = asset_state

    @property
    def asset_duration(self):
        """Gets the asset_duration of this DeliveryReport.  # noqa: E501


        :return: The asset_duration of this DeliveryReport.  # noqa: E501
        :rtype: float
        """
        return self._asset_duration

    @asset_duration.setter
    def asset_duration(self, asset_duration):
        """Sets the asset_duration of this DeliveryReport.


        :param asset_duration: The asset_duration of this DeliveryReport.  # noqa: E501
        :type: float
        """

        self._asset_duration = asset_duration

    @property
    def delivered_seconds(self):
        """Gets the delivered_seconds of this DeliveryReport.  # noqa: E501


        :return: The delivered_seconds of this DeliveryReport.  # noqa: E501
        :rtype: float
        """
        return self._delivered_seconds

    @delivered_seconds.setter
    def delivered_seconds(self, delivered_seconds):
        """Sets the delivered_seconds of this DeliveryReport.


        :param delivered_seconds: The delivered_seconds of this DeliveryReport.  # noqa: E501
        :type: float
        """

        self._delivered_seconds = delivered_seconds

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
        if not isinstance(other, DeliveryReport):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
