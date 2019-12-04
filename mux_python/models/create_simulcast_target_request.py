# coding: utf-8

"""
Mux Python - Copyright 2019 Mux Inc.

NOTE: This class is auto generated. Do not edit the class manually.
"""


import pprint
import re  # noqa: F401
import six

class CreateSimulcastTargetRequest(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'passthrough': 'str',
        'stream_key': 'str',
        'url': 'str'
    }

    attribute_map = {
        'passthrough': 'passthrough',
        'stream_key': 'stream_key',
        'url': 'url'
    }

    def __init__(self, passthrough=None, stream_key=None, url=None):  # noqa: E501
        """CreateSimulcastTargetRequest - a model defined in OpenAPI"""  # noqa: E501

        self._passthrough = None
        self._stream_key = None
        self._url = None
        self.discriminator = None

        if passthrough is not None:
            self.passthrough = passthrough
        if stream_key is not None:
            self.stream_key = stream_key
        self.url = url

    @property
    def passthrough(self):
        """Gets the passthrough of this CreateSimulcastTargetRequest.  # noqa: E501

        Arbitrary metadata set by you when creating a simulcast target.  # noqa: E501

        :return: The passthrough of this CreateSimulcastTargetRequest.  # noqa: E501
        :rtype: str
        """
        return self._passthrough

    @passthrough.setter
    def passthrough(self, passthrough):
        """Sets the passthrough of this CreateSimulcastTargetRequest.

        Arbitrary metadata set by you when creating a simulcast target.  # noqa: E501

        :param passthrough: The passthrough of this CreateSimulcastTargetRequest.  # noqa: E501
        :type: str
        """

        self._passthrough = passthrough

    @property
    def stream_key(self):
        """Gets the stream_key of this CreateSimulcastTargetRequest.  # noqa: E501

        Stream Key represents a stream identifier on the third party live streaming service to send the parent live stream to.  # noqa: E501

        :return: The stream_key of this CreateSimulcastTargetRequest.  # noqa: E501
        :rtype: str
        """
        return self._stream_key

    @stream_key.setter
    def stream_key(self, stream_key):
        """Sets the stream_key of this CreateSimulcastTargetRequest.

        Stream Key represents a stream identifier on the third party live streaming service to send the parent live stream to.  # noqa: E501

        :param stream_key: The stream_key of this CreateSimulcastTargetRequest.  # noqa: E501
        :type: str
        """

        self._stream_key = stream_key

    @property
    def url(self):
        """Gets the url of this CreateSimulcastTargetRequest.  # noqa: E501

        RTMP hostname including application name for the third party live streaming service. Example: 'rtmp://live.example.com/app'.  # noqa: E501

        :return: The url of this CreateSimulcastTargetRequest.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this CreateSimulcastTargetRequest.

        RTMP hostname including application name for the third party live streaming service. Example: 'rtmp://live.example.com/app'.  # noqa: E501

        :param url: The url of this CreateSimulcastTargetRequest.  # noqa: E501
        :type: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

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
        if not isinstance(other, CreateSimulcastTargetRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
