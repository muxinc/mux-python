# coding: utf-8

"""
Mux Python - Copyright 2019 Mux Inc.

NOTE: This class is auto generated. Do not edit the class manually.
"""


import pprint
import re  # noqa: F401
import six

class PlaybackID(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'id': 'str',
        'policy': 'PlaybackPolicy'
    }

    attribute_map = {
        'id': 'id',
        'policy': 'policy'
    }

    def __init__(self, id=None, policy=None):  # noqa: E501
        """PlaybackID - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._policy = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if policy is not None:
            self.policy = policy

    @property
    def id(self):
        """Gets the id of this PlaybackID.  # noqa: E501


        :return: The id of this PlaybackID.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PlaybackID.


        :param id: The id of this PlaybackID.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def policy(self):
        """Gets the policy of this PlaybackID.  # noqa: E501


        :return: The policy of this PlaybackID.  # noqa: E501
        :rtype: PlaybackPolicy
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """Sets the policy of this PlaybackID.


        :param policy: The policy of this PlaybackID.  # noqa: E501
        :type: PlaybackPolicy
        """

        self._policy = policy

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
        if not isinstance(other, PlaybackID):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
