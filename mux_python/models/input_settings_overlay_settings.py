# coding: utf-8

"""
Mux Python - Copyright 2019 Mux Inc.

NOTE: This class is auto generated. Do not edit the class manually.
"""


import pprint
import re  # noqa: F401
import six

class InputSettingsOverlaySettings(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'vertical_align': 'str',
        'vertical_margin': 'str',
        'horizontal_align': 'str',
        'horizontal_margin': 'str',
        'width': 'str',
        'height': 'str',
        'opacity': 'str'
    }

    attribute_map = {
        'vertical_align': 'vertical_align',
        'vertical_margin': 'vertical_margin',
        'horizontal_align': 'horizontal_align',
        'horizontal_margin': 'horizontal_margin',
        'width': 'width',
        'height': 'height',
        'opacity': 'opacity'
    }

    def __init__(self, vertical_align=None, vertical_margin=None, horizontal_align=None, horizontal_margin=None, width=None, height=None, opacity=None):  # noqa: E501
        """InputSettingsOverlaySettings - a model defined in OpenAPI"""  # noqa: E501

        self._vertical_align = None
        self._vertical_margin = None
        self._horizontal_align = None
        self._horizontal_margin = None
        self._width = None
        self._height = None
        self._opacity = None
        self.discriminator = None

        if vertical_align is not None:
            self.vertical_align = vertical_align
        if vertical_margin is not None:
            self.vertical_margin = vertical_margin
        if horizontal_align is not None:
            self.horizontal_align = horizontal_align
        if horizontal_margin is not None:
            self.horizontal_margin = horizontal_margin
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if opacity is not None:
            self.opacity = opacity

    @property
    def vertical_align(self):
        """Gets the vertical_align of this InputSettingsOverlaySettings.  # noqa: E501


        :return: The vertical_align of this InputSettingsOverlaySettings.  # noqa: E501
        :rtype: str
        """
        return self._vertical_align

    @vertical_align.setter
    def vertical_align(self, vertical_align):
        """Sets the vertical_align of this InputSettingsOverlaySettings.


        :param vertical_align: The vertical_align of this InputSettingsOverlaySettings.  # noqa: E501
        :type: str
        """

        self._vertical_align = vertical_align

    @property
    def vertical_margin(self):
        """Gets the vertical_margin of this InputSettingsOverlaySettings.  # noqa: E501


        :return: The vertical_margin of this InputSettingsOverlaySettings.  # noqa: E501
        :rtype: str
        """
        return self._vertical_margin

    @vertical_margin.setter
    def vertical_margin(self, vertical_margin):
        """Sets the vertical_margin of this InputSettingsOverlaySettings.


        :param vertical_margin: The vertical_margin of this InputSettingsOverlaySettings.  # noqa: E501
        :type: str
        """

        self._vertical_margin = vertical_margin

    @property
    def horizontal_align(self):
        """Gets the horizontal_align of this InputSettingsOverlaySettings.  # noqa: E501


        :return: The horizontal_align of this InputSettingsOverlaySettings.  # noqa: E501
        :rtype: str
        """
        return self._horizontal_align

    @horizontal_align.setter
    def horizontal_align(self, horizontal_align):
        """Sets the horizontal_align of this InputSettingsOverlaySettings.


        :param horizontal_align: The horizontal_align of this InputSettingsOverlaySettings.  # noqa: E501
        :type: str
        """

        self._horizontal_align = horizontal_align

    @property
    def horizontal_margin(self):
        """Gets the horizontal_margin of this InputSettingsOverlaySettings.  # noqa: E501


        :return: The horizontal_margin of this InputSettingsOverlaySettings.  # noqa: E501
        :rtype: str
        """
        return self._horizontal_margin

    @horizontal_margin.setter
    def horizontal_margin(self, horizontal_margin):
        """Sets the horizontal_margin of this InputSettingsOverlaySettings.


        :param horizontal_margin: The horizontal_margin of this InputSettingsOverlaySettings.  # noqa: E501
        :type: str
        """

        self._horizontal_margin = horizontal_margin

    @property
    def width(self):
        """Gets the width of this InputSettingsOverlaySettings.  # noqa: E501


        :return: The width of this InputSettingsOverlaySettings.  # noqa: E501
        :rtype: str
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this InputSettingsOverlaySettings.


        :param width: The width of this InputSettingsOverlaySettings.  # noqa: E501
        :type: str
        """

        self._width = width

    @property
    def height(self):
        """Gets the height of this InputSettingsOverlaySettings.  # noqa: E501


        :return: The height of this InputSettingsOverlaySettings.  # noqa: E501
        :rtype: str
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this InputSettingsOverlaySettings.


        :param height: The height of this InputSettingsOverlaySettings.  # noqa: E501
        :type: str
        """

        self._height = height

    @property
    def opacity(self):
        """Gets the opacity of this InputSettingsOverlaySettings.  # noqa: E501


        :return: The opacity of this InputSettingsOverlaySettings.  # noqa: E501
        :rtype: str
        """
        return self._opacity

    @opacity.setter
    def opacity(self, opacity):
        """Sets the opacity of this InputSettingsOverlaySettings.


        :param opacity: The opacity of this InputSettingsOverlaySettings.  # noqa: E501
        :type: str
        """

        self._opacity = opacity

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
        if not isinstance(other, InputSettingsOverlaySettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
