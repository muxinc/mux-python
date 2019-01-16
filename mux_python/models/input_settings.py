# coding: utf-8

"""
Mux Python - Copyright 2019 Mux Inc.

NOTE: This class is auto generated. Do not edit the class manually.
"""


import pprint
import re  # noqa: F401
import six

class InputSettings(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'url': 'str',
        'language': 'str',
        'overlay_settings': 'InputSettingsOverlaySettings'
    }

    attribute_map = {
        'url': 'url',
        'language': 'language',
        'overlay_settings': 'overlay_settings'
    }

    def __init__(self, url=None, language=None, overlay_settings=None):  # noqa: E501
        """InputSettings - a model defined in OpenAPI"""  # noqa: E501

        self._url = None
        self._language = None
        self._overlay_settings = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if language is not None:
            self.language = language
        if overlay_settings is not None:
            self.overlay_settings = overlay_settings

    @property
    def url(self):
        """Gets the url of this InputSettings.  # noqa: E501


        :return: The url of this InputSettings.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this InputSettings.


        :param url: The url of this InputSettings.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def language(self):
        """Gets the language of this InputSettings.  # noqa: E501


        :return: The language of this InputSettings.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this InputSettings.


        :param language: The language of this InputSettings.  # noqa: E501
        :type: str
        """

        self._language = language

    @property
    def overlay_settings(self):
        """Gets the overlay_settings of this InputSettings.  # noqa: E501


        :return: The overlay_settings of this InputSettings.  # noqa: E501
        :rtype: InputSettingsOverlaySettings
        """
        return self._overlay_settings

    @overlay_settings.setter
    def overlay_settings(self, overlay_settings):
        """Sets the overlay_settings of this InputSettings.


        :param overlay_settings: The overlay_settings of this InputSettings.  # noqa: E501
        :type: InputSettingsOverlaySettings
        """

        self._overlay_settings = overlay_settings

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
        if not isinstance(other, InputSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
