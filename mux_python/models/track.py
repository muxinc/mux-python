# coding: utf-8

"""
Mux Python - Copyright 2019 Mux Inc.

NOTE: This class is auto generated. Do not edit the class manually.
"""


import pprint
import re  # noqa: F401
import six

class Track(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'id': 'str',
        'type': 'str',
        'duration': 'float',
        'max_width': 'int',
        'max_height': 'int',
        'max_frame_rate': 'float',
        'max_channels': 'int',
        'max_channel_layout': 'str',
        'text_type': 'str',
        'language_code': 'str',
        'name': 'str',
        'closed_captions': 'bool',
        'passthrough': 'str'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'duration': 'duration',
        'max_width': 'max_width',
        'max_height': 'max_height',
        'max_frame_rate': 'max_frame_rate',
        'max_channels': 'max_channels',
        'max_channel_layout': 'max_channel_layout',
        'text_type': 'text_type',
        'language_code': 'language_code',
        'name': 'name',
        'closed_captions': 'closed_captions',
        'passthrough': 'passthrough'
    }

    def __init__(self, id=None, type=None, duration=None, max_width=None, max_height=None, max_frame_rate=None, max_channels=None, max_channel_layout=None, text_type=None, language_code=None, name=None, closed_captions=None, passthrough=None):  # noqa: E501
        """Track - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._type = None
        self._duration = None
        self._max_width = None
        self._max_height = None
        self._max_frame_rate = None
        self._max_channels = None
        self._max_channel_layout = None
        self._text_type = None
        self._language_code = None
        self._name = None
        self._closed_captions = None
        self._passthrough = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if duration is not None:
            self.duration = duration
        if max_width is not None:
            self.max_width = max_width
        if max_height is not None:
            self.max_height = max_height
        if max_frame_rate is not None:
            self.max_frame_rate = max_frame_rate
        if max_channels is not None:
            self.max_channels = max_channels
        if max_channel_layout is not None:
            self.max_channel_layout = max_channel_layout
        if text_type is not None:
            self.text_type = text_type
        if language_code is not None:
            self.language_code = language_code
        if name is not None:
            self.name = name
        if closed_captions is not None:
            self.closed_captions = closed_captions
        if passthrough is not None:
            self.passthrough = passthrough

    @property
    def id(self):
        """Gets the id of this Track.  # noqa: E501


        :return: The id of this Track.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Track.


        :param id: The id of this Track.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this Track.  # noqa: E501


        :return: The type of this Track.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Track.


        :param type: The type of this Track.  # noqa: E501
        :type: str
        """
        allowed_values = ["video", "audio", "text"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def duration(self):
        """Gets the duration of this Track.  # noqa: E501


        :return: The duration of this Track.  # noqa: E501
        :rtype: float
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this Track.


        :param duration: The duration of this Track.  # noqa: E501
        :type: float
        """

        self._duration = duration

    @property
    def max_width(self):
        """Gets the max_width of this Track.  # noqa: E501


        :return: The max_width of this Track.  # noqa: E501
        :rtype: int
        """
        return self._max_width

    @max_width.setter
    def max_width(self, max_width):
        """Sets the max_width of this Track.


        :param max_width: The max_width of this Track.  # noqa: E501
        :type: int
        """

        self._max_width = max_width

    @property
    def max_height(self):
        """Gets the max_height of this Track.  # noqa: E501


        :return: The max_height of this Track.  # noqa: E501
        :rtype: int
        """
        return self._max_height

    @max_height.setter
    def max_height(self, max_height):
        """Sets the max_height of this Track.


        :param max_height: The max_height of this Track.  # noqa: E501
        :type: int
        """

        self._max_height = max_height

    @property
    def max_frame_rate(self):
        """Gets the max_frame_rate of this Track.  # noqa: E501


        :return: The max_frame_rate of this Track.  # noqa: E501
        :rtype: float
        """
        return self._max_frame_rate

    @max_frame_rate.setter
    def max_frame_rate(self, max_frame_rate):
        """Sets the max_frame_rate of this Track.


        :param max_frame_rate: The max_frame_rate of this Track.  # noqa: E501
        :type: float
        """

        self._max_frame_rate = max_frame_rate

    @property
    def max_channels(self):
        """Gets the max_channels of this Track.  # noqa: E501


        :return: The max_channels of this Track.  # noqa: E501
        :rtype: int
        """
        return self._max_channels

    @max_channels.setter
    def max_channels(self, max_channels):
        """Sets the max_channels of this Track.


        :param max_channels: The max_channels of this Track.  # noqa: E501
        :type: int
        """

        self._max_channels = max_channels

    @property
    def max_channel_layout(self):
        """Gets the max_channel_layout of this Track.  # noqa: E501


        :return: The max_channel_layout of this Track.  # noqa: E501
        :rtype: str
        """
        return self._max_channel_layout

    @max_channel_layout.setter
    def max_channel_layout(self, max_channel_layout):
        """Sets the max_channel_layout of this Track.


        :param max_channel_layout: The max_channel_layout of this Track.  # noqa: E501
        :type: str
        """

        self._max_channel_layout = max_channel_layout

    @property
    def text_type(self):
        """Gets the text_type of this Track.  # noqa: E501


        :return: The text_type of this Track.  # noqa: E501
        :rtype: str
        """
        return self._text_type

    @text_type.setter
    def text_type(self, text_type):
        """Sets the text_type of this Track.


        :param text_type: The text_type of this Track.  # noqa: E501
        :type: str
        """
        allowed_values = ["subtitles"]  # noqa: E501
        if text_type not in allowed_values:
            raise ValueError(
                "Invalid value for `text_type` ({0}), must be one of {1}"  # noqa: E501
                .format(text_type, allowed_values)
            )

        self._text_type = text_type

    @property
    def language_code(self):
        """Gets the language_code of this Track.  # noqa: E501


        :return: The language_code of this Track.  # noqa: E501
        :rtype: str
        """
        return self._language_code

    @language_code.setter
    def language_code(self, language_code):
        """Sets the language_code of this Track.


        :param language_code: The language_code of this Track.  # noqa: E501
        :type: str
        """

        self._language_code = language_code

    @property
    def name(self):
        """Gets the name of this Track.  # noqa: E501


        :return: The name of this Track.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Track.


        :param name: The name of this Track.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def closed_captions(self):
        """Gets the closed_captions of this Track.  # noqa: E501


        :return: The closed_captions of this Track.  # noqa: E501
        :rtype: bool
        """
        return self._closed_captions

    @closed_captions.setter
    def closed_captions(self, closed_captions):
        """Sets the closed_captions of this Track.


        :param closed_captions: The closed_captions of this Track.  # noqa: E501
        :type: bool
        """

        self._closed_captions = closed_captions

    @property
    def passthrough(self):
        """Gets the passthrough of this Track.  # noqa: E501


        :return: The passthrough of this Track.  # noqa: E501
        :rtype: str
        """
        return self._passthrough

    @passthrough.setter
    def passthrough(self, passthrough):
        """Sets the passthrough of this Track.


        :param passthrough: The passthrough of this Track.  # noqa: E501
        :type: str
        """

        self._passthrough = passthrough

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
        if not isinstance(other, Track):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
