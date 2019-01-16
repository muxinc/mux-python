# coding: utf-8

"""
Mux Python - Copyright 2019 Mux Inc.

NOTE: This class is auto generated. Do not edit the class manually.
"""


import pprint
import re  # noqa: F401
import six

class InputFile(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'container_format': 'str',
        'tracks': 'list[InputTrack]'
    }

    attribute_map = {
        'container_format': 'container_format',
        'tracks': 'tracks'
    }

    def __init__(self, container_format=None, tracks=None):  # noqa: E501
        """InputFile - a model defined in OpenAPI"""  # noqa: E501

        self._container_format = None
        self._tracks = None
        self.discriminator = None

        if container_format is not None:
            self.container_format = container_format
        if tracks is not None:
            self.tracks = tracks

    @property
    def container_format(self):
        """Gets the container_format of this InputFile.  # noqa: E501


        :return: The container_format of this InputFile.  # noqa: E501
        :rtype: str
        """
        return self._container_format

    @container_format.setter
    def container_format(self, container_format):
        """Sets the container_format of this InputFile.


        :param container_format: The container_format of this InputFile.  # noqa: E501
        :type: str
        """

        self._container_format = container_format

    @property
    def tracks(self):
        """Gets the tracks of this InputFile.  # noqa: E501


        :return: The tracks of this InputFile.  # noqa: E501
        :rtype: list[InputTrack]
        """
        return self._tracks

    @tracks.setter
    def tracks(self, tracks):
        """Sets the tracks of this InputFile.


        :param tracks: The tracks of this InputFile.  # noqa: E501
        :type: list[InputTrack]
        """

        self._tracks = tracks

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
        if not isinstance(other, InputFile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
