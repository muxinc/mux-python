# coding: utf-8

"""
    Mux API

    Mux is how developers build online video. This API encompasses both Mux Video and Mux Data functionality to help you build your video-related projects better and faster than ever before.  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: devex@mux.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from mux_python.configuration import Configuration


class UpdateLiveStreamNewAssetSettings(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'mp4_support': 'str'
    }

    attribute_map = {
        'mp4_support': 'mp4_support'
    }

    def __init__(self, mp4_support=None, local_vars_configuration=None):  # noqa: E501
        """UpdateLiveStreamNewAssetSettings - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._mp4_support = None
        self.discriminator = None

        if mp4_support is not None:
            self.mp4_support = mp4_support

    @property
    def mp4_support(self):
        """Gets the mp4_support of this UpdateLiveStreamNewAssetSettings.  # noqa: E501

        Specify what level of support for mp4 playback should be added to new assets generated from this live stream. * The `none` option disables MP4 support for new assets. MP4 files will not be produced for an asset generated from this live stream. * The `capped-1080p` option produces a single MP4 file, called `capped-1080p.mp4`, with the video resolution capped at 1080p. This option produces an `audio.m4a` file for an audio-only asset. * The `audio-only` option produces a single M4A file, called `audio.m4a` for a video or an audio-only asset. MP4 generation will error when this option is specified for a video-only asset. * The `audio-only,capped-1080p` option produces both the `audio.m4a` and `capped-1080p.mp4` files. Only the `capped-1080p.mp4` file is produced for a video-only asset, while only the `audio.m4a` file is produced for an audio-only asset. * The `standard`(deprecated) option produces up to three MP4 files with different levels of resolution (`high.mp4`, `medium.mp4`, `low.mp4`, or `audio.m4a` for an audio-only asset).   # noqa: E501

        :return: The mp4_support of this UpdateLiveStreamNewAssetSettings.  # noqa: E501
        :rtype: str
        """
        return self._mp4_support

    @mp4_support.setter
    def mp4_support(self, mp4_support):
        """Sets the mp4_support of this UpdateLiveStreamNewAssetSettings.

        Specify what level of support for mp4 playback should be added to new assets generated from this live stream. * The `none` option disables MP4 support for new assets. MP4 files will not be produced for an asset generated from this live stream. * The `capped-1080p` option produces a single MP4 file, called `capped-1080p.mp4`, with the video resolution capped at 1080p. This option produces an `audio.m4a` file for an audio-only asset. * The `audio-only` option produces a single M4A file, called `audio.m4a` for a video or an audio-only asset. MP4 generation will error when this option is specified for a video-only asset. * The `audio-only,capped-1080p` option produces both the `audio.m4a` and `capped-1080p.mp4` files. Only the `capped-1080p.mp4` file is produced for a video-only asset, while only the `audio.m4a` file is produced for an audio-only asset. * The `standard`(deprecated) option produces up to three MP4 files with different levels of resolution (`high.mp4`, `medium.mp4`, `low.mp4`, or `audio.m4a` for an audio-only asset).   # noqa: E501

        :param mp4_support: The mp4_support of this UpdateLiveStreamNewAssetSettings.  # noqa: E501
        :type mp4_support: str
        """
        allowed_values = ["none", "standard", "capped-1080p", "audio-only", "audio-only,capped-1080p"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and mp4_support not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `mp4_support` ({0}), must be one of {1}"  # noqa: E501
                .format(mp4_support, allowed_values)
            )

        self._mp4_support = mp4_support

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateLiveStreamNewAssetSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateLiveStreamNewAssetSettings):
            return True

        return self.to_dict() != other.to_dict()