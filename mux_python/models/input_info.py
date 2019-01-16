# coding: utf-8

"""
Mux Python - Copyright 2019 Mux Inc.

NOTE: This class is auto generated. Do not edit the class manually.
"""


import pprint
import re  # noqa: F401
import six

class InputInfo(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'settings': 'InputSettings',
        'file': 'InputFile'
    }

    attribute_map = {
        'settings': 'settings',
        'file': 'file'
    }

    def __init__(self, settings=None, file=None):  # noqa: E501
        """InputInfo - a model defined in OpenAPI"""  # noqa: E501

        self._settings = None
        self._file = None
        self.discriminator = None

        if settings is not None:
            self.settings = settings
        if file is not None:
            self.file = file

    @property
    def settings(self):
        """Gets the settings of this InputInfo.  # noqa: E501


        :return: The settings of this InputInfo.  # noqa: E501
        :rtype: InputSettings
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this InputInfo.


        :param settings: The settings of this InputInfo.  # noqa: E501
        :type: InputSettings
        """

        self._settings = settings

    @property
    def file(self):
        """Gets the file of this InputInfo.  # noqa: E501


        :return: The file of this InputInfo.  # noqa: E501
        :rtype: InputFile
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this InputInfo.


        :param file: The file of this InputInfo.  # noqa: E501
        :type: InputFile
        """

        self._file = file

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
        if not isinstance(other, InputInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
