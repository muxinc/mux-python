# coding: utf-8

"""
Mux Python - Copyright 2019 Mux Inc.

NOTE: This class is auto generated. Do not edit the class manually.
"""


import pprint
import re  # noqa: F401
import six

class UpdateAssetMasterAccessRequest(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'master_access': 'str'
    }

    attribute_map = {
        'master_access': 'master_access'
    }

    def __init__(self, master_access=None):  # noqa: E501
        """UpdateAssetMasterAccessRequest - a model defined in OpenAPI"""  # noqa: E501

        self._master_access = None
        self.discriminator = None

        if master_access is not None:
            self.master_access = master_access

    @property
    def master_access(self):
        """Gets the master_access of this UpdateAssetMasterAccessRequest.  # noqa: E501

        Add or remove access to the master version of the video.  # noqa: E501

        :return: The master_access of this UpdateAssetMasterAccessRequest.  # noqa: E501
        :rtype: str
        """
        return self._master_access

    @master_access.setter
    def master_access(self, master_access):
        """Sets the master_access of this UpdateAssetMasterAccessRequest.

        Add or remove access to the master version of the video.  # noqa: E501

        :param master_access: The master_access of this UpdateAssetMasterAccessRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["temporary", "none"]  # noqa: E501
        if master_access not in allowed_values:
            raise ValueError(
                "Invalid value for `master_access` ({0}), must be one of {1}"  # noqa: E501
                .format(master_access, allowed_values)
            )

        self._master_access = master_access

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
        if not isinstance(other, UpdateAssetMasterAccessRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
