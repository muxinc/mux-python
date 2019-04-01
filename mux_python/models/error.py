# coding: utf-8

"""
Mux Python - Copyright 2019 Mux Inc.

NOTE: This class is auto generated. Do not edit the class manually.
"""


import pprint
import re  # noqa: F401
import six

class Error(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'id': 'int',
        'percentage': 'float',
        'notes': 'str',
        'message': 'str',
        'last_seen': 'str',
        'description': 'str',
        'count': 'int',
        'code': 'int'
    }

    attribute_map = {
        'id': 'id',
        'percentage': 'percentage',
        'notes': 'notes',
        'message': 'message',
        'last_seen': 'last_seen',
        'description': 'description',
        'count': 'count',
        'code': 'code'
    }

    def __init__(self, id=None, percentage=None, notes=None, message=None, last_seen=None, description=None, count=None, code=None):  # noqa: E501
        """Error - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._percentage = None
        self._notes = None
        self._message = None
        self._last_seen = None
        self._description = None
        self._count = None
        self._code = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if percentage is not None:
            self.percentage = percentage
        if notes is not None:
            self.notes = notes
        if message is not None:
            self.message = message
        if last_seen is not None:
            self.last_seen = last_seen
        if description is not None:
            self.description = description
        if count is not None:
            self.count = count
        if code is not None:
            self.code = code

    @property
    def id(self):
        """Gets the id of this Error.  # noqa: E501


        :return: The id of this Error.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Error.


        :param id: The id of this Error.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def percentage(self):
        """Gets the percentage of this Error.  # noqa: E501


        :return: The percentage of this Error.  # noqa: E501
        :rtype: float
        """
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        """Sets the percentage of this Error.


        :param percentage: The percentage of this Error.  # noqa: E501
        :type: float
        """

        self._percentage = percentage

    @property
    def notes(self):
        """Gets the notes of this Error.  # noqa: E501


        :return: The notes of this Error.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this Error.


        :param notes: The notes of this Error.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def message(self):
        """Gets the message of this Error.  # noqa: E501


        :return: The message of this Error.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this Error.


        :param message: The message of this Error.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def last_seen(self):
        """Gets the last_seen of this Error.  # noqa: E501


        :return: The last_seen of this Error.  # noqa: E501
        :rtype: str
        """
        return self._last_seen

    @last_seen.setter
    def last_seen(self, last_seen):
        """Sets the last_seen of this Error.


        :param last_seen: The last_seen of this Error.  # noqa: E501
        :type: str
        """

        self._last_seen = last_seen

    @property
    def description(self):
        """Gets the description of this Error.  # noqa: E501


        :return: The description of this Error.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Error.


        :param description: The description of this Error.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def count(self):
        """Gets the count of this Error.  # noqa: E501


        :return: The count of this Error.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this Error.


        :param count: The count of this Error.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def code(self):
        """Gets the code of this Error.  # noqa: E501


        :return: The code of this Error.  # noqa: E501
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this Error.


        :param code: The code of this Error.  # noqa: E501
        :type: int
        """

        self._code = code

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
        if not isinstance(other, Error):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
