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


class GenerateTrackSubtitlesRequest(object):
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
        'generated_subtitles': 'list[AssetGeneratedSubtitleSettings]'
    }

    attribute_map = {
        'generated_subtitles': 'generated_subtitles'
    }

    def __init__(self, generated_subtitles=None, local_vars_configuration=None):  # noqa: E501
        """GenerateTrackSubtitlesRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._generated_subtitles = None
        self.discriminator = None

        if generated_subtitles is not None:
            self.generated_subtitles = generated_subtitles

    @property
    def generated_subtitles(self):
        """Gets the generated_subtitles of this GenerateTrackSubtitlesRequest.  # noqa: E501

        Generate subtitle tracks using automatic speech recognition with this configuration.  # noqa: E501

        :return: The generated_subtitles of this GenerateTrackSubtitlesRequest.  # noqa: E501
        :rtype: list[AssetGeneratedSubtitleSettings]
        """
        return self._generated_subtitles

    @generated_subtitles.setter
    def generated_subtitles(self, generated_subtitles):
        """Sets the generated_subtitles of this GenerateTrackSubtitlesRequest.

        Generate subtitle tracks using automatic speech recognition with this configuration.  # noqa: E501

        :param generated_subtitles: The generated_subtitles of this GenerateTrackSubtitlesRequest.  # noqa: E501
        :type generated_subtitles: list[AssetGeneratedSubtitleSettings]
        """

        self._generated_subtitles = generated_subtitles

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
        if not isinstance(other, GenerateTrackSubtitlesRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GenerateTrackSubtitlesRequest):
            return True

        return self.to_dict() != other.to_dict()
