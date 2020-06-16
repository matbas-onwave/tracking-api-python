# coding: utf-8

"""
    TrackingAPI

    API for retrieving tracking data and changing settings on LightBug & RemoteThings tracking devices  # noqa: E501

    OpenAPI spec version: 1.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Notification(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'created': 'datetime',
        'params': 'object',
        'message': 'str',
        'dismissed_on': 'datetime',
        'dismissed_by': 'object',
        'id': 'float',
        'device_id': 'float',
        'point_id': 'float',
        'user_id': 'float',
        'trigger_id': 'float'
    }

    attribute_map = {
        'created': 'created',
        'params': 'params',
        'message': 'message',
        'dismissed_on': 'dismissedOn',
        'dismissed_by': 'dismissedBy',
        'id': 'id',
        'device_id': 'deviceId',
        'point_id': 'pointId',
        'user_id': 'userId',
        'trigger_id': 'triggerId'
    }

    def __init__(self, created=None, params=None, message=None, dismissed_on=None, dismissed_by=None, id=None, device_id=None, point_id=None, user_id=None, trigger_id=None):  # noqa: E501
        """Notification - a model defined in Swagger"""  # noqa: E501

        self._created = None
        self._params = None
        self._message = None
        self._dismissed_on = None
        self._dismissed_by = None
        self._id = None
        self._device_id = None
        self._point_id = None
        self._user_id = None
        self._trigger_id = None
        self.discriminator = None

        self.created = created
        if params is not None:
            self.params = params
        if message is not None:
            self.message = message
        if dismissed_on is not None:
            self.dismissed_on = dismissed_on
        if dismissed_by is not None:
            self.dismissed_by = dismissed_by
        if id is not None:
            self.id = id
        if device_id is not None:
            self.device_id = device_id
        if point_id is not None:
            self.point_id = point_id
        if user_id is not None:
            self.user_id = user_id
        if trigger_id is not None:
            self.trigger_id = trigger_id

    @property
    def created(self):
        """Gets the created of this Notification.  # noqa: E501


        :return: The created of this Notification.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Notification.


        :param created: The created of this Notification.  # noqa: E501
        :type: datetime
        """
        if created is None:
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def params(self):
        """Gets the params of this Notification.  # noqa: E501


        :return: The params of this Notification.  # noqa: E501
        :rtype: object
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this Notification.


        :param params: The params of this Notification.  # noqa: E501
        :type: object
        """

        self._params = params

    @property
    def message(self):
        """Gets the message of this Notification.  # noqa: E501


        :return: The message of this Notification.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this Notification.


        :param message: The message of this Notification.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def dismissed_on(self):
        """Gets the dismissed_on of this Notification.  # noqa: E501


        :return: The dismissed_on of this Notification.  # noqa: E501
        :rtype: datetime
        """
        return self._dismissed_on

    @dismissed_on.setter
    def dismissed_on(self, dismissed_on):
        """Sets the dismissed_on of this Notification.


        :param dismissed_on: The dismissed_on of this Notification.  # noqa: E501
        :type: datetime
        """

        self._dismissed_on = dismissed_on

    @property
    def dismissed_by(self):
        """Gets the dismissed_by of this Notification.  # noqa: E501


        :return: The dismissed_by of this Notification.  # noqa: E501
        :rtype: object
        """
        return self._dismissed_by

    @dismissed_by.setter
    def dismissed_by(self, dismissed_by):
        """Sets the dismissed_by of this Notification.


        :param dismissed_by: The dismissed_by of this Notification.  # noqa: E501
        :type: object
        """

        self._dismissed_by = dismissed_by

    @property
    def id(self):
        """Gets the id of this Notification.  # noqa: E501


        :return: The id of this Notification.  # noqa: E501
        :rtype: float
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Notification.


        :param id: The id of this Notification.  # noqa: E501
        :type: float
        """

        self._id = id

    @property
    def device_id(self):
        """Gets the device_id of this Notification.  # noqa: E501


        :return: The device_id of this Notification.  # noqa: E501
        :rtype: float
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this Notification.


        :param device_id: The device_id of this Notification.  # noqa: E501
        :type: float
        """

        self._device_id = device_id

    @property
    def point_id(self):
        """Gets the point_id of this Notification.  # noqa: E501


        :return: The point_id of this Notification.  # noqa: E501
        :rtype: float
        """
        return self._point_id

    @point_id.setter
    def point_id(self, point_id):
        """Sets the point_id of this Notification.


        :param point_id: The point_id of this Notification.  # noqa: E501
        :type: float
        """

        self._point_id = point_id

    @property
    def user_id(self):
        """Gets the user_id of this Notification.  # noqa: E501


        :return: The user_id of this Notification.  # noqa: E501
        :rtype: float
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this Notification.


        :param user_id: The user_id of this Notification.  # noqa: E501
        :type: float
        """

        self._user_id = user_id

    @property
    def trigger_id(self):
        """Gets the trigger_id of this Notification.  # noqa: E501


        :return: The trigger_id of this Notification.  # noqa: E501
        :rtype: float
        """
        return self._trigger_id

    @trigger_id.setter
    def trigger_id(self, trigger_id):
        """Sets the trigger_id of this Notification.


        :param trigger_id: The trigger_id of this Notification.  # noqa: E501
        :type: float
        """

        self._trigger_id = trigger_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(Notification, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Notification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
