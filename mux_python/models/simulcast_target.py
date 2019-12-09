# coding: utf-8

"""
Mux Python - Copyright 2019 Mux Inc.

NOTE: This class is auto generated. Do not edit the class manually.
"""


import pprint
import re  # noqa: F401
import six

class SimulcastTarget(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'id': 'str',
        'passthrough': 'str',
        'status': 'str',
        'stream_key': 'str',
        'url': 'str'
    }

    attribute_map = {
        'id': 'id',
        'passthrough': 'passthrough',
        'status': 'status',
        'stream_key': 'stream_key',
        'url': 'url'
    }

    def __init__(self, id=None, passthrough=None, status=None, stream_key=None, url=None):  # noqa: E501
        """SimulcastTarget - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._passthrough = None
        self._status = None
        self._stream_key = None
        self._url = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if passthrough is not None:
            self.passthrough = passthrough
        if status is not None:
            self.status = status
        if stream_key is not None:
            self.stream_key = stream_key
        if url is not None:
            self.url = url

    @property
    def id(self):
        """Gets the id of this SimulcastTarget.  # noqa: E501

        ID of the Simulcast Target  # noqa: E501

        :return: The id of this SimulcastTarget.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SimulcastTarget.

        ID of the Simulcast Target  # noqa: E501

        :param id: The id of this SimulcastTarget.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def passthrough(self):
        """Gets the passthrough of this SimulcastTarget.  # noqa: E501

        Arbitrary Metadata set when creating a simulcast target.  # noqa: E501

        :return: The passthrough of this SimulcastTarget.  # noqa: E501
        :rtype: str
        """
        return self._passthrough

    @passthrough.setter
    def passthrough(self, passthrough):
        """Sets the passthrough of this SimulcastTarget.

        Arbitrary Metadata set when creating a simulcast target.  # noqa: E501

        :param passthrough: The passthrough of this SimulcastTarget.  # noqa: E501
        :type: str
        """

        self._passthrough = passthrough

    @property
    def status(self):
        """Gets the status of this SimulcastTarget.  # noqa: E501

        The current status of the simulcast target. See Statuses below for detailed description.   * `idle`: Default status. When the parent live stream is in disconnected status, simulcast targets will be idle state.   * `starting`: The simulcast target transitions into this state when the parent live stream transition into connected state.   * `broadcasting`: The simulcast target has successfully connected to the third party live streaming service and is pushing video to that service.   * `errored`: The simulcast target encountered an error either while attempting to connect to the third party live streaming service, or mid-broadcasting. Compared to other errored statuses in the Mux Video API, a simulcast may transition back into the broadcasting state if a connection with the service can be re-established.   # noqa: E501

        :return: The status of this SimulcastTarget.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SimulcastTarget.

        The current status of the simulcast target. See Statuses below for detailed description.   * `idle`: Default status. When the parent live stream is in disconnected status, simulcast targets will be idle state.   * `starting`: The simulcast target transitions into this state when the parent live stream transition into connected state.   * `broadcasting`: The simulcast target has successfully connected to the third party live streaming service and is pushing video to that service.   * `errored`: The simulcast target encountered an error either while attempting to connect to the third party live streaming service, or mid-broadcasting. Compared to other errored statuses in the Mux Video API, a simulcast may transition back into the broadcasting state if a connection with the service can be re-established.   # noqa: E501

        :param status: The status of this SimulcastTarget.  # noqa: E501
        :type: str
        """
        allowed_values = ["idle", "starting", "broadcasting", "errored"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def stream_key(self):
        """Gets the stream_key of this SimulcastTarget.  # noqa: E501

        Stream Key represents an stream identifier for the third party live streaming service to simulcast the parent live stream too.  # noqa: E501

        :return: The stream_key of this SimulcastTarget.  # noqa: E501
        :rtype: str
        """
        return self._stream_key

    @stream_key.setter
    def stream_key(self, stream_key):
        """Sets the stream_key of this SimulcastTarget.

        Stream Key represents an stream identifier for the third party live streaming service to simulcast the parent live stream too.  # noqa: E501

        :param stream_key: The stream_key of this SimulcastTarget.  # noqa: E501
        :type: str
        """

        self._stream_key = stream_key

    @property
    def url(self):
        """Gets the url of this SimulcastTarget.  # noqa: E501

        RTMP hostname including the application name for the third party live streaming service.  # noqa: E501

        :return: The url of this SimulcastTarget.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this SimulcastTarget.

        RTMP hostname including the application name for the third party live streaming service.  # noqa: E501

        :param url: The url of this SimulcastTarget.  # noqa: E501
        :type: str
        """

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
        if not isinstance(other, SimulcastTarget):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
