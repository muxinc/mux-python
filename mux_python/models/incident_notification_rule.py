# coding: utf-8

"""
Mux Python - Copyright 2019 Mux Inc.

NOTE: This class is auto generated. Do not edit the class manually.
"""


import pprint
import re  # noqa: F401
import six

class IncidentNotificationRule(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'status': 'str',
        'rules': 'list[NotificationRule]',
        'property_id': 'str',
        'id': 'str',
        'action': 'str'
    }

    attribute_map = {
        'status': 'status',
        'rules': 'rules',
        'property_id': 'property_id',
        'id': 'id',
        'action': 'action'
    }

    def __init__(self, status=None, rules=None, property_id=None, id=None, action=None):  # noqa: E501
        """IncidentNotificationRule - a model defined in OpenAPI"""  # noqa: E501

        self._status = None
        self._rules = None
        self._property_id = None
        self._id = None
        self._action = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if rules is not None:
            self.rules = rules
        if property_id is not None:
            self.property_id = property_id
        if id is not None:
            self.id = id
        if action is not None:
            self.action = action

    @property
    def status(self):
        """Gets the status of this IncidentNotificationRule.  # noqa: E501


        :return: The status of this IncidentNotificationRule.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this IncidentNotificationRule.


        :param status: The status of this IncidentNotificationRule.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def rules(self):
        """Gets the rules of this IncidentNotificationRule.  # noqa: E501


        :return: The rules of this IncidentNotificationRule.  # noqa: E501
        :rtype: list[NotificationRule]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this IncidentNotificationRule.


        :param rules: The rules of this IncidentNotificationRule.  # noqa: E501
        :type: list[NotificationRule]
        """

        self._rules = rules

    @property
    def property_id(self):
        """Gets the property_id of this IncidentNotificationRule.  # noqa: E501


        :return: The property_id of this IncidentNotificationRule.  # noqa: E501
        :rtype: str
        """
        return self._property_id

    @property_id.setter
    def property_id(self, property_id):
        """Sets the property_id of this IncidentNotificationRule.


        :param property_id: The property_id of this IncidentNotificationRule.  # noqa: E501
        :type: str
        """

        self._property_id = property_id

    @property
    def id(self):
        """Gets the id of this IncidentNotificationRule.  # noqa: E501


        :return: The id of this IncidentNotificationRule.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IncidentNotificationRule.


        :param id: The id of this IncidentNotificationRule.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def action(self):
        """Gets the action of this IncidentNotificationRule.  # noqa: E501


        :return: The action of this IncidentNotificationRule.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this IncidentNotificationRule.


        :param action: The action of this IncidentNotificationRule.  # noqa: E501
        :type: str
        """

        self._action = action

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
        if not isinstance(other, IncidentNotificationRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
