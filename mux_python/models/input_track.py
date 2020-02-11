# coding: utf-8

"""
Mux Python - Copyright 2019 Mux Inc.

NOTE: This class is auto generated. Do not edit the class manually.
"""


import pprint
import re  # noqa: F401
import six

class InputTrack(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'type': 'str',
        'duration': 'float',
        'encoding': 'str',
        'width': 'int',
        'height': 'int',
        'frame_rate': 'float',
        'sample_rate': 'int',
        'sample_size': 'int',
        'channels': 'int'
    }

    attribute_map = {
        'type': 'type',
        'duration': 'duration',
        'encoding': 'encoding',
        'width': 'width',
        'height': 'height',
        'frame_rate': 'frame_rate',
        'sample_rate': 'sample_rate',
        'sample_size': 'sample_size',
        'channels': 'channels'
    }

    def __init__(self, type=None, duration=None, encoding=None, width=None, height=None, frame_rate=None, sample_rate=None, sample_size=None, channels=None):  # noqa: E501
        """InputTrack - a model defined in OpenAPI"""  # noqa: E501

        self._type = None
        self._duration = None
        self._encoding = None
        self._width = None
        self._height = None
        self._frame_rate = None
        self._sample_rate = None
        self._sample_size = None
        self._channels = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if duration is not None:
            self.duration = duration
        if encoding is not None:
            self.encoding = encoding
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if frame_rate is not None:
            self.frame_rate = frame_rate
        if sample_rate is not None:
            self.sample_rate = sample_rate
        if sample_size is not None:
            self.sample_size = sample_size
        if channels is not None:
            self.channels = channels

    @property
    def type(self):
        """Gets the type of this InputTrack.  # noqa: E501


        :return: The type of this InputTrack.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InputTrack.


        :param type: The type of this InputTrack.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def duration(self):
        """Gets the duration of this InputTrack.  # noqa: E501


        :return: The duration of this InputTrack.  # noqa: E501
        :rtype: float
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this InputTrack.


        :param duration: The duration of this InputTrack.  # noqa: E501
        :type: float
        """

        self._duration = duration

    @property
    def encoding(self):
        """Gets the encoding of this InputTrack.  # noqa: E501


        :return: The encoding of this InputTrack.  # noqa: E501
        :rtype: str
        """
        return self._encoding

    @encoding.setter
    def encoding(self, encoding):
        """Sets the encoding of this InputTrack.


        :param encoding: The encoding of this InputTrack.  # noqa: E501
        :type: str
        """

        self._encoding = encoding

    @property
    def width(self):
        """Gets the width of this InputTrack.  # noqa: E501


        :return: The width of this InputTrack.  # noqa: E501
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this InputTrack.


        :param width: The width of this InputTrack.  # noqa: E501
        :type: int
        """

        self._width = width

    @property
    def height(self):
        """Gets the height of this InputTrack.  # noqa: E501


        :return: The height of this InputTrack.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this InputTrack.


        :param height: The height of this InputTrack.  # noqa: E501
        :type: int
        """

        self._height = height

    @property
    def frame_rate(self):
        """Gets the frame_rate of this InputTrack.  # noqa: E501


        :return: The frame_rate of this InputTrack.  # noqa: E501
        :rtype: float
        """
        return self._frame_rate

    @frame_rate.setter
    def frame_rate(self, frame_rate):
        """Sets the frame_rate of this InputTrack.


        :param frame_rate: The frame_rate of this InputTrack.  # noqa: E501
        :type: float
        """

        self._frame_rate = frame_rate

    @property
    def sample_rate(self):
        """Gets the sample_rate of this InputTrack.  # noqa: E501


        :return: The sample_rate of this InputTrack.  # noqa: E501
        :rtype: int
        """
        return self._sample_rate

    @sample_rate.setter
    def sample_rate(self, sample_rate):
        """Sets the sample_rate of this InputTrack.


        :param sample_rate: The sample_rate of this InputTrack.  # noqa: E501
        :type: int
        """

        self._sample_rate = sample_rate

    @property
    def sample_size(self):
        """Gets the sample_size of this InputTrack.  # noqa: E501


        :return: The sample_size of this InputTrack.  # noqa: E501
        :rtype: int
        """
        return self._sample_size

    @sample_size.setter
    def sample_size(self, sample_size):
        """Sets the sample_size of this InputTrack.


        :param sample_size: The sample_size of this InputTrack.  # noqa: E501
        :type: int
        """

        self._sample_size = sample_size

    @property
    def channels(self):
        """Gets the channels of this InputTrack.  # noqa: E501


        :return: The channels of this InputTrack.  # noqa: E501
        :rtype: int
        """
        return self._channels

    @channels.setter
    def channels(self, channels):
        """Sets the channels of this InputTrack.


        :param channels: The channels of this InputTrack.  # noqa: E501
        :type: int
        """

        self._channels = channels

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
        if not isinstance(other, InputTrack):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
