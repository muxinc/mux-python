# coding: utf-8

"""
Mux Python - Copyright 2019 Mux Inc.

NOTE: This class is auto generated. Do not edit the class manually.
"""


import pprint
import re  # noqa: F401
import six

class Asset(object):


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
        'deleted_at': 'str',
        'status': 'str',
        'duration': 'float',
        'max_stored_resolution': 'str',
        'max_stored_frame_rate': 'float',
        'aspect_ratio': 'str',
        'playback_ids': 'list[PlaybackID]',
        'tracks': 'list[Track]',
        'demo': 'bool',
        'errors': 'AssetErrors',
        'per_title_encode': 'bool',
        'is_live': 'bool',
        'passthrough': 'str',
        'live_stream_id': 'str',
        'master': 'AssetMaster',
        'master_access': 'str',
        'mp4_support': 'str',
        'normalize_audio': 'bool',
        'static_renditions': 'AssetStaticRenditions'
    }

    attribute_map = {
        'id': 'id',
        'created_at': 'created_at',
        'deleted_at': 'deleted_at',
        'status': 'status',
        'duration': 'duration',
        'max_stored_resolution': 'max_stored_resolution',
        'max_stored_frame_rate': 'max_stored_frame_rate',
        'aspect_ratio': 'aspect_ratio',
        'playback_ids': 'playback_ids',
        'tracks': 'tracks',
        'demo': 'demo',
        'errors': 'errors',
        'per_title_encode': 'per_title_encode',
        'is_live': 'is_live',
        'passthrough': 'passthrough',
        'live_stream_id': 'live_stream_id',
        'master': 'master',
        'master_access': 'master_access',
        'mp4_support': 'mp4_support',
        'normalize_audio': 'normalize_audio',
        'static_renditions': 'static_renditions'
    }

    def __init__(self, id=None, created_at=None, deleted_at=None, status=None, duration=None, max_stored_resolution=None, max_stored_frame_rate=None, aspect_ratio=None, playback_ids=None, tracks=None, demo=None, errors=None, per_title_encode=None, is_live=None, passthrough=None, live_stream_id=None, master=None, master_access='none', mp4_support='none', normalize_audio=False, static_renditions=None):  # noqa: E501
        """Asset - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._created_at = None
        self._deleted_at = None
        self._status = None
        self._duration = None
        self._max_stored_resolution = None
        self._max_stored_frame_rate = None
        self._aspect_ratio = None
        self._playback_ids = None
        self._tracks = None
        self._demo = None
        self._errors = None
        self._per_title_encode = None
        self._is_live = None
        self._passthrough = None
        self._live_stream_id = None
        self._master = None
        self._master_access = None
        self._mp4_support = None
        self._normalize_audio = None
        self._static_renditions = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if created_at is not None:
            self.created_at = created_at
        if deleted_at is not None:
            self.deleted_at = deleted_at
        if status is not None:
            self.status = status
        if duration is not None:
            self.duration = duration
        if max_stored_resolution is not None:
            self.max_stored_resolution = max_stored_resolution
        if max_stored_frame_rate is not None:
            self.max_stored_frame_rate = max_stored_frame_rate
        if aspect_ratio is not None:
            self.aspect_ratio = aspect_ratio
        if playback_ids is not None:
            self.playback_ids = playback_ids
        if tracks is not None:
            self.tracks = tracks
        if demo is not None:
            self.demo = demo
        if errors is not None:
            self.errors = errors
        if per_title_encode is not None:
            self.per_title_encode = per_title_encode
        if is_live is not None:
            self.is_live = is_live
        if passthrough is not None:
            self.passthrough = passthrough
        if live_stream_id is not None:
            self.live_stream_id = live_stream_id
        if master is not None:
            self.master = master
        if master_access is not None:
            self.master_access = master_access
        if mp4_support is not None:
            self.mp4_support = mp4_support
        if normalize_audio is not None:
            self.normalize_audio = normalize_audio
        if static_renditions is not None:
            self.static_renditions = static_renditions

    @property
    def id(self):
        """Gets the id of this Asset.  # noqa: E501


        :return: The id of this Asset.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Asset.


        :param id: The id of this Asset.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def created_at(self):
        """Gets the created_at of this Asset.  # noqa: E501


        :return: The created_at of this Asset.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Asset.


        :param created_at: The created_at of this Asset.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def deleted_at(self):
        """Gets the deleted_at of this Asset.  # noqa: E501


        :return: The deleted_at of this Asset.  # noqa: E501
        :rtype: str
        """
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at):
        """Sets the deleted_at of this Asset.


        :param deleted_at: The deleted_at of this Asset.  # noqa: E501
        :type: str
        """

        self._deleted_at = deleted_at

    @property
    def status(self):
        """Gets the status of this Asset.  # noqa: E501


        :return: The status of this Asset.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Asset.


        :param status: The status of this Asset.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def duration(self):
        """Gets the duration of this Asset.  # noqa: E501


        :return: The duration of this Asset.  # noqa: E501
        :rtype: float
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this Asset.


        :param duration: The duration of this Asset.  # noqa: E501
        :type: float
        """

        self._duration = duration

    @property
    def max_stored_resolution(self):
        """Gets the max_stored_resolution of this Asset.  # noqa: E501


        :return: The max_stored_resolution of this Asset.  # noqa: E501
        :rtype: str
        """
        return self._max_stored_resolution

    @max_stored_resolution.setter
    def max_stored_resolution(self, max_stored_resolution):
        """Sets the max_stored_resolution of this Asset.


        :param max_stored_resolution: The max_stored_resolution of this Asset.  # noqa: E501
        :type: str
        """

        self._max_stored_resolution = max_stored_resolution

    @property
    def max_stored_frame_rate(self):
        """Gets the max_stored_frame_rate of this Asset.  # noqa: E501


        :return: The max_stored_frame_rate of this Asset.  # noqa: E501
        :rtype: float
        """
        return self._max_stored_frame_rate

    @max_stored_frame_rate.setter
    def max_stored_frame_rate(self, max_stored_frame_rate):
        """Sets the max_stored_frame_rate of this Asset.


        :param max_stored_frame_rate: The max_stored_frame_rate of this Asset.  # noqa: E501
        :type: float
        """

        self._max_stored_frame_rate = max_stored_frame_rate

    @property
    def aspect_ratio(self):
        """Gets the aspect_ratio of this Asset.  # noqa: E501


        :return: The aspect_ratio of this Asset.  # noqa: E501
        :rtype: str
        """
        return self._aspect_ratio

    @aspect_ratio.setter
    def aspect_ratio(self, aspect_ratio):
        """Sets the aspect_ratio of this Asset.


        :param aspect_ratio: The aspect_ratio of this Asset.  # noqa: E501
        :type: str
        """

        self._aspect_ratio = aspect_ratio

    @property
    def playback_ids(self):
        """Gets the playback_ids of this Asset.  # noqa: E501


        :return: The playback_ids of this Asset.  # noqa: E501
        :rtype: list[PlaybackID]
        """
        return self._playback_ids

    @playback_ids.setter
    def playback_ids(self, playback_ids):
        """Sets the playback_ids of this Asset.


        :param playback_ids: The playback_ids of this Asset.  # noqa: E501
        :type: list[PlaybackID]
        """

        self._playback_ids = playback_ids

    @property
    def tracks(self):
        """Gets the tracks of this Asset.  # noqa: E501


        :return: The tracks of this Asset.  # noqa: E501
        :rtype: list[Track]
        """
        return self._tracks

    @tracks.setter
    def tracks(self, tracks):
        """Sets the tracks of this Asset.


        :param tracks: The tracks of this Asset.  # noqa: E501
        :type: list[Track]
        """

        self._tracks = tracks

    @property
    def demo(self):
        """Gets the demo of this Asset.  # noqa: E501


        :return: The demo of this Asset.  # noqa: E501
        :rtype: bool
        """
        return self._demo

    @demo.setter
    def demo(self, demo):
        """Sets the demo of this Asset.


        :param demo: The demo of this Asset.  # noqa: E501
        :type: bool
        """

        self._demo = demo

    @property
    def errors(self):
        """Gets the errors of this Asset.  # noqa: E501


        :return: The errors of this Asset.  # noqa: E501
        :rtype: AssetErrors
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this Asset.


        :param errors: The errors of this Asset.  # noqa: E501
        :type: AssetErrors
        """

        self._errors = errors

    @property
    def per_title_encode(self):
        """Gets the per_title_encode of this Asset.  # noqa: E501


        :return: The per_title_encode of this Asset.  # noqa: E501
        :rtype: bool
        """
        return self._per_title_encode

    @per_title_encode.setter
    def per_title_encode(self, per_title_encode):
        """Sets the per_title_encode of this Asset.


        :param per_title_encode: The per_title_encode of this Asset.  # noqa: E501
        :type: bool
        """

        self._per_title_encode = per_title_encode

    @property
    def is_live(self):
        """Gets the is_live of this Asset.  # noqa: E501


        :return: The is_live of this Asset.  # noqa: E501
        :rtype: bool
        """
        return self._is_live

    @is_live.setter
    def is_live(self, is_live):
        """Sets the is_live of this Asset.


        :param is_live: The is_live of this Asset.  # noqa: E501
        :type: bool
        """

        self._is_live = is_live

    @property
    def passthrough(self):
        """Gets the passthrough of this Asset.  # noqa: E501


        :return: The passthrough of this Asset.  # noqa: E501
        :rtype: str
        """
        return self._passthrough

    @passthrough.setter
    def passthrough(self, passthrough):
        """Sets the passthrough of this Asset.


        :param passthrough: The passthrough of this Asset.  # noqa: E501
        :type: str
        """

        self._passthrough = passthrough

    @property
    def live_stream_id(self):
        """Gets the live_stream_id of this Asset.  # noqa: E501


        :return: The live_stream_id of this Asset.  # noqa: E501
        :rtype: str
        """
        return self._live_stream_id

    @live_stream_id.setter
    def live_stream_id(self, live_stream_id):
        """Sets the live_stream_id of this Asset.


        :param live_stream_id: The live_stream_id of this Asset.  # noqa: E501
        :type: str
        """

        self._live_stream_id = live_stream_id

    @property
    def master(self):
        """Gets the master of this Asset.  # noqa: E501


        :return: The master of this Asset.  # noqa: E501
        :rtype: AssetMaster
        """
        return self._master

    @master.setter
    def master(self, master):
        """Sets the master of this Asset.


        :param master: The master of this Asset.  # noqa: E501
        :type: AssetMaster
        """

        self._master = master

    @property
    def master_access(self):
        """Gets the master_access of this Asset.  # noqa: E501


        :return: The master_access of this Asset.  # noqa: E501
        :rtype: str
        """
        return self._master_access

    @master_access.setter
    def master_access(self, master_access):
        """Sets the master_access of this Asset.


        :param master_access: The master_access of this Asset.  # noqa: E501
        :type: str
        """
        allowed_values = ["temporary", "none"]  # noqa: E501
        if master_access not in allowed_values:
            raise ValueError(
                "Invalid value for `master_access` ({0}), must be one of {1}"  # noqa: E501
                .format(master_access, allowed_values)
            )

        self._master_access = master_access

    @property
    def mp4_support(self):
        """Gets the mp4_support of this Asset.  # noqa: E501


        :return: The mp4_support of this Asset.  # noqa: E501
        :rtype: str
        """
        return self._mp4_support

    @mp4_support.setter
    def mp4_support(self, mp4_support):
        """Sets the mp4_support of this Asset.


        :param mp4_support: The mp4_support of this Asset.  # noqa: E501
        :type: str
        """
        allowed_values = ["standard", "none"]  # noqa: E501
        if mp4_support not in allowed_values:
            raise ValueError(
                "Invalid value for `mp4_support` ({0}), must be one of {1}"  # noqa: E501
                .format(mp4_support, allowed_values)
            )

        self._mp4_support = mp4_support

    @property
    def normalize_audio(self):
        """Gets the normalize_audio of this Asset.  # noqa: E501


        :return: The normalize_audio of this Asset.  # noqa: E501
        :rtype: bool
        """
        return self._normalize_audio

    @normalize_audio.setter
    def normalize_audio(self, normalize_audio):
        """Sets the normalize_audio of this Asset.


        :param normalize_audio: The normalize_audio of this Asset.  # noqa: E501
        :type: bool
        """

        self._normalize_audio = normalize_audio

    @property
    def static_renditions(self):
        """Gets the static_renditions of this Asset.  # noqa: E501


        :return: The static_renditions of this Asset.  # noqa: E501
        :rtype: AssetStaticRenditions
        """
        return self._static_renditions

    @static_renditions.setter
    def static_renditions(self, static_renditions):
        """Sets the static_renditions of this Asset.


        :param static_renditions: The static_renditions of this Asset.  # noqa: E501
        :type: AssetStaticRenditions
        """

        self._static_renditions = static_renditions

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
        if not isinstance(other, Asset):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
