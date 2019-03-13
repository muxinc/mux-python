# coding: utf-8

"""
Mux Python - Copyright 2019 Mux Inc.

NOTE: This class is auto generated. Do not edit the class manually.
"""


import pprint
import re  # noqa: F401
import six

class Upload(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'id': 'str',
        'timeout': 'int',
        'status': 'str',
        'new_asset_settings': 'Asset',
        'asset_id': 'str',
        'error': 'UploadError',
        'cors_origin': 'str',
        'url': 'str'
    }

    attribute_map = {
        'id': 'id',
        'timeout': 'timeout',
        'status': 'status',
        'new_asset_settings': 'new_asset_settings',
        'asset_id': 'asset_id',
        'error': 'error',
        'cors_origin': 'cors_origin',
        'url': 'url'
    }

    def __init__(self, id=None, timeout=3600, status=None, new_asset_settings=None, asset_id=None, error=None, cors_origin=None, url=None):  # noqa: E501
        """Upload - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._timeout = None
        self._status = None
        self._new_asset_settings = None
        self._asset_id = None
        self._error = None
        self._cors_origin = None
        self._url = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if timeout is not None:
            self.timeout = timeout
        if status is not None:
            self.status = status
        if new_asset_settings is not None:
            self.new_asset_settings = new_asset_settings
        if asset_id is not None:
            self.asset_id = asset_id
        if error is not None:
            self.error = error
        if cors_origin is not None:
            self.cors_origin = cors_origin
        if url is not None:
            self.url = url

    @property
    def id(self):
        """Gets the id of this Upload.  # noqa: E501


        :return: The id of this Upload.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Upload.


        :param id: The id of this Upload.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def timeout(self):
        """Gets the timeout of this Upload.  # noqa: E501

        Max time in seconds for the signed upload URL to be valid. If a successful upload has not occurred before the timeout limit, the direct upload is marked `timed_out`  # noqa: E501

        :return: The timeout of this Upload.  # noqa: E501
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this Upload.

        Max time in seconds for the signed upload URL to be valid. If a successful upload has not occurred before the timeout limit, the direct upload is marked `timed_out`  # noqa: E501

        :param timeout: The timeout of this Upload.  # noqa: E501
        :type: int
        """
        if timeout is not None and timeout > 604800:  # noqa: E501
            raise ValueError("Invalid value for `timeout`, must be a value less than or equal to `604800`")  # noqa: E501
        if timeout is not None and timeout < 60:  # noqa: E501
            raise ValueError("Invalid value for `timeout`, must be a value greater than or equal to `60`")  # noqa: E501

        self._timeout = timeout

    @property
    def status(self):
        """Gets the status of this Upload.  # noqa: E501


        :return: The status of this Upload.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Upload.


        :param status: The status of this Upload.  # noqa: E501
        :type: str
        """
        allowed_values = ["waiting", "asset_created", "errored", "cancelled", "timed_out"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def new_asset_settings(self):
        """Gets the new_asset_settings of this Upload.  # noqa: E501


        :return: The new_asset_settings of this Upload.  # noqa: E501
        :rtype: Asset
        """
        return self._new_asset_settings

    @new_asset_settings.setter
    def new_asset_settings(self, new_asset_settings):
        """Sets the new_asset_settings of this Upload.


        :param new_asset_settings: The new_asset_settings of this Upload.  # noqa: E501
        :type: Asset
        """

        self._new_asset_settings = new_asset_settings

    @property
    def asset_id(self):
        """Gets the asset_id of this Upload.  # noqa: E501

        Only set once the upload is in the `asset_created` state.  # noqa: E501

        :return: The asset_id of this Upload.  # noqa: E501
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        """Sets the asset_id of this Upload.

        Only set once the upload is in the `asset_created` state.  # noqa: E501

        :param asset_id: The asset_id of this Upload.  # noqa: E501
        :type: str
        """

        self._asset_id = asset_id

    @property
    def error(self):
        """Gets the error of this Upload.  # noqa: E501


        :return: The error of this Upload.  # noqa: E501
        :rtype: UploadError
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this Upload.


        :param error: The error of this Upload.  # noqa: E501
        :type: UploadError
        """

        self._error = error

    @property
    def cors_origin(self):
        """Gets the cors_origin of this Upload.  # noqa: E501

        If the upload URL will be used in a browser, you must specify the origin in order for the signed URL to have the correct CORS headers.  # noqa: E501

        :return: The cors_origin of this Upload.  # noqa: E501
        :rtype: str
        """
        return self._cors_origin

    @cors_origin.setter
    def cors_origin(self, cors_origin):
        """Sets the cors_origin of this Upload.

        If the upload URL will be used in a browser, you must specify the origin in order for the signed URL to have the correct CORS headers.  # noqa: E501

        :param cors_origin: The cors_origin of this Upload.  # noqa: E501
        :type: str
        """

        self._cors_origin = cors_origin

    @property
    def url(self):
        """Gets the url of this Upload.  # noqa: E501

        The URL to upload the associated source media to.  # noqa: E501

        :return: The url of this Upload.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Upload.

        The URL to upload the associated source media to.  # noqa: E501

        :param url: The url of this Upload.  # noqa: E501
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
        if not isinstance(other, Upload):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
