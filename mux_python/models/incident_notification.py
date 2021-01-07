# coding: utf-8

"""
Mux Python - Copyright 2019 Mux Inc.

NOTE: This class is auto generated. Do not edit the class manually.
"""


import pprint
import re  # noqa: F401
import six

class IncidentNotification(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'queued_at': 'str',
        'id': 'int',
        'attempted_at': 'str'
    }

    attribute_map = {
        'queued_at': 'queued_at',
        'id': 'id',
        'attempted_at': 'attempted_at'
    }

    def __init__(self, queued_at=None, id=None, attempted_at=None):  # noqa: E501
        """IncidentNotification - a model defined in OpenAPI"""  # noqa: E501

        self._queued_at = None
        self._id = None
        self._attempted_at = None
        self.discriminator = None

        if queued_at is not None:
            self.queued_at = queued_at
        if id is not None:
            self.id = id
        if attempted_at is not None:
            self.attempted_at = attempted_at

    @property
    def queued_at(self):
        """Gets the queued_at of this IncidentNotification.  # noqa: E501


        :return: The queued_at of this IncidentNotification.  # noqa: E501
        :rtype: str
        """
        return self._queued_at

    @queued_at.setter
    def queued_at(self, queued_at):
        """Sets the queued_at of this IncidentNotification.


        :param queued_at: The queued_at of this IncidentNotification.  # noqa: E501
        :type: str
        """

        self._queued_at = queued_at

    @property
    def id(self):
        """Gets the id of this IncidentNotification.  # noqa: E501


        :return: The id of this IncidentNotification.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IncidentNotification.


        :param id: The id of this IncidentNotification.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def attempted_at(self):
        """Gets the attempted_at of this IncidentNotification.  # noqa: E501


        :return: The attempted_at of this IncidentNotification.  # noqa: E501
        :rtype: str
        """
        return self._attempted_at

    @attempted_at.setter
    def attempted_at(self, attempted_at):
        """Sets the attempted_at of this IncidentNotification.


        :param attempted_at: The attempted_at of this IncidentNotification.  # noqa: E501
        :type: str
        """

        self._attempted_at = attempted_at

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
        if not isinstance(other, IncidentNotification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
