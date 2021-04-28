# coding: utf-8

"""
Mux Python - Copyright 2019 Mux Inc.

NOTE: This class is auto generated. Do not edit the class manually.
"""


import pprint
import re  # noqa: F401
import six

class GetAssetOrLiveStreamIdResponseDataObject(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'id': 'str',
        'type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type'
    }

    def __init__(self, id=None, type=None):  # noqa: E501
        """GetAssetOrLiveStreamIdResponseDataObject - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if type is not None:
            self.type = type

    @property
    def id(self):
        """Gets the id of this GetAssetOrLiveStreamIdResponseDataObject.  # noqa: E501

        The identifier of the object.  # noqa: E501

        :return: The id of this GetAssetOrLiveStreamIdResponseDataObject.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetAssetOrLiveStreamIdResponseDataObject.

        The identifier of the object.  # noqa: E501

        :param id: The id of this GetAssetOrLiveStreamIdResponseDataObject.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this GetAssetOrLiveStreamIdResponseDataObject.  # noqa: E501

        Identifies the object type associated with the playback ID.  # noqa: E501

        :return: The type of this GetAssetOrLiveStreamIdResponseDataObject.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GetAssetOrLiveStreamIdResponseDataObject.

        Identifies the object type associated with the playback ID.  # noqa: E501

        :param type: The type of this GetAssetOrLiveStreamIdResponseDataObject.  # noqa: E501
        :type: str
        """
        allowed_values = ["asset", "live_stream"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if not isinstance(other, GetAssetOrLiveStreamIdResponseDataObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other