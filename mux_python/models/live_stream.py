# coding: utf-8

"""
Mux Python - Copyright 2019 Mux Inc.

NOTE: This class is auto generated. Do not edit the class manually.
"""


import pprint
import re  # noqa: F401
import six

class LiveStream(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'id': 'str',
        'created_at': 'str',
        'stream_key': 'str',
        'active_asset_id': 'str',
        'recent_asset_ids': 'list[str]',
        'status': 'str',
        'playback_ids': 'list[PlaybackID]',
        'new_asset_settings': 'Asset',
        'passthrough': 'str',
        'reconnect_window': 'float',
        'reduced_latency': 'bool',
        'simulcast_targets': 'list[SimulcastTarget]'
    }

    attribute_map = {
        'id': 'id',
        'created_at': 'created_at',
        'stream_key': 'stream_key',
        'active_asset_id': 'active_asset_id',
        'recent_asset_ids': 'recent_asset_ids',
        'status': 'status',
        'playback_ids': 'playback_ids',
        'new_asset_settings': 'new_asset_settings',
        'passthrough': 'passthrough',
        'reconnect_window': 'reconnect_window',
        'reduced_latency': 'reduced_latency',
        'simulcast_targets': 'simulcast_targets'
    }

    def __init__(self, id=None, created_at=None, stream_key=None, active_asset_id=None, recent_asset_ids=None, status=None, playback_ids=None, new_asset_settings=None, passthrough=None, reconnect_window=None, reduced_latency=None, simulcast_targets=None):  # noqa: E501
        """LiveStream - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._created_at = None
        self._stream_key = None
        self._active_asset_id = None
        self._recent_asset_ids = None
        self._status = None
        self._playback_ids = None
        self._new_asset_settings = None
        self._passthrough = None
        self._reconnect_window = None
        self._reduced_latency = None
        self._simulcast_targets = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if created_at is not None:
            self.created_at = created_at
        if stream_key is not None:
            self.stream_key = stream_key
        if active_asset_id is not None:
            self.active_asset_id = active_asset_id
        if recent_asset_ids is not None:
            self.recent_asset_ids = recent_asset_ids
        if status is not None:
            self.status = status
        if playback_ids is not None:
            self.playback_ids = playback_ids
        if new_asset_settings is not None:
            self.new_asset_settings = new_asset_settings
        if passthrough is not None:
            self.passthrough = passthrough
        if reconnect_window is not None:
            self.reconnect_window = reconnect_window
        if reduced_latency is not None:
            self.reduced_latency = reduced_latency
        if simulcast_targets is not None:
            self.simulcast_targets = simulcast_targets

    @property
    def id(self):
        """Gets the id of this LiveStream.  # noqa: E501


        :return: The id of this LiveStream.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LiveStream.


        :param id: The id of this LiveStream.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def created_at(self):
        """Gets the created_at of this LiveStream.  # noqa: E501


        :return: The created_at of this LiveStream.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this LiveStream.


        :param created_at: The created_at of this LiveStream.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def stream_key(self):
        """Gets the stream_key of this LiveStream.  # noqa: E501


        :return: The stream_key of this LiveStream.  # noqa: E501
        :rtype: str
        """
        return self._stream_key

    @stream_key.setter
    def stream_key(self, stream_key):
        """Sets the stream_key of this LiveStream.


        :param stream_key: The stream_key of this LiveStream.  # noqa: E501
        :type: str
        """

        self._stream_key = stream_key

    @property
    def active_asset_id(self):
        """Gets the active_asset_id of this LiveStream.  # noqa: E501


        :return: The active_asset_id of this LiveStream.  # noqa: E501
        :rtype: str
        """
        return self._active_asset_id

    @active_asset_id.setter
    def active_asset_id(self, active_asset_id):
        """Sets the active_asset_id of this LiveStream.


        :param active_asset_id: The active_asset_id of this LiveStream.  # noqa: E501
        :type: str
        """

        self._active_asset_id = active_asset_id

    @property
    def recent_asset_ids(self):
        """Gets the recent_asset_ids of this LiveStream.  # noqa: E501


        :return: The recent_asset_ids of this LiveStream.  # noqa: E501
        :rtype: list[str]
        """
        return self._recent_asset_ids

    @recent_asset_ids.setter
    def recent_asset_ids(self, recent_asset_ids):
        """Sets the recent_asset_ids of this LiveStream.


        :param recent_asset_ids: The recent_asset_ids of this LiveStream.  # noqa: E501
        :type: list[str]
        """

        self._recent_asset_ids = recent_asset_ids

    @property
    def status(self):
        """Gets the status of this LiveStream.  # noqa: E501


        :return: The status of this LiveStream.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this LiveStream.


        :param status: The status of this LiveStream.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def playback_ids(self):
        """Gets the playback_ids of this LiveStream.  # noqa: E501


        :return: The playback_ids of this LiveStream.  # noqa: E501
        :rtype: list[PlaybackID]
        """
        return self._playback_ids

    @playback_ids.setter
    def playback_ids(self, playback_ids):
        """Sets the playback_ids of this LiveStream.


        :param playback_ids: The playback_ids of this LiveStream.  # noqa: E501
        :type: list[PlaybackID]
        """

        self._playback_ids = playback_ids

    @property
    def new_asset_settings(self):
        """Gets the new_asset_settings of this LiveStream.  # noqa: E501


        :return: The new_asset_settings of this LiveStream.  # noqa: E501
        :rtype: Asset
        """
        return self._new_asset_settings

    @new_asset_settings.setter
    def new_asset_settings(self, new_asset_settings):
        """Sets the new_asset_settings of this LiveStream.


        :param new_asset_settings: The new_asset_settings of this LiveStream.  # noqa: E501
        :type: Asset
        """

        self._new_asset_settings = new_asset_settings

    @property
    def passthrough(self):
        """Gets the passthrough of this LiveStream.  # noqa: E501


        :return: The passthrough of this LiveStream.  # noqa: E501
        :rtype: str
        """
        return self._passthrough

    @passthrough.setter
    def passthrough(self, passthrough):
        """Sets the passthrough of this LiveStream.


        :param passthrough: The passthrough of this LiveStream.  # noqa: E501
        :type: str
        """

        self._passthrough = passthrough

    @property
    def reconnect_window(self):
        """Gets the reconnect_window of this LiveStream.  # noqa: E501


        :return: The reconnect_window of this LiveStream.  # noqa: E501
        :rtype: float
        """
        return self._reconnect_window

    @reconnect_window.setter
    def reconnect_window(self, reconnect_window):
        """Sets the reconnect_window of this LiveStream.


        :param reconnect_window: The reconnect_window of this LiveStream.  # noqa: E501
        :type: float
        """

        self._reconnect_window = reconnect_window

    @property
    def reduced_latency(self):
        """Gets the reduced_latency of this LiveStream.  # noqa: E501


        :return: The reduced_latency of this LiveStream.  # noqa: E501
        :rtype: bool
        """
        return self._reduced_latency

    @reduced_latency.setter
    def reduced_latency(self, reduced_latency):
        """Sets the reduced_latency of this LiveStream.


        :param reduced_latency: The reduced_latency of this LiveStream.  # noqa: E501
        :type: bool
        """

        self._reduced_latency = reduced_latency

    @property
    def simulcast_targets(self):
        """Gets the simulcast_targets of this LiveStream.  # noqa: E501


        :return: The simulcast_targets of this LiveStream.  # noqa: E501
        :rtype: list[SimulcastTarget]
        """
        return self._simulcast_targets

    @simulcast_targets.setter
    def simulcast_targets(self, simulcast_targets):
        """Sets the simulcast_targets of this LiveStream.


        :param simulcast_targets: The simulcast_targets of this LiveStream.  # noqa: E501
        :type: list[SimulcastTarget]
        """

        self._simulcast_targets = simulcast_targets

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
        if not isinstance(other, LiveStream):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
