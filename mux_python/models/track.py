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
        'text_track_type': 'str',
        'language': 'str'
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
        'text_track_type': 'text_track_type',
        'language': 'language'
    }

    def __init__(self, id=None, type=None, duration=None, max_width=None, max_height=None, max_frame_rate=None, max_channels=None, max_channel_layout=None, text_track_type=None, language=None):  # noqa: E501
        """Track - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._type = None
        self._duration = None
        self._max_width = None
        self._max_height = None
        self._max_frame_rate = None
        self._max_channels = None
        self._max_channel_layout = None
        self._text_track_type = None
        self._language = None
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
        if text_track_type is not None:
            self.text_track_type = text_track_type
        if language is not None:
            self.language = language

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
    def text_track_type(self):
        """Gets the text_track_type of this Track.  # noqa: E501


        :return: The text_track_type of this Track.  # noqa: E501
        :rtype: str
        """
        return self._text_track_type

    @text_track_type.setter
    def text_track_type(self, text_track_type):
        """Sets the text_track_type of this Track.


        :param text_track_type: The text_track_type of this Track.  # noqa: E501
        :type: str
        """

        self._text_track_type = text_track_type

    @property
    def language(self):
        """Gets the language of this Track.  # noqa: E501


        :return: The language of this Track.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this Track.


        :param language: The language of this Track.  # noqa: E501
        :type: str
        """

        self._language = language

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
