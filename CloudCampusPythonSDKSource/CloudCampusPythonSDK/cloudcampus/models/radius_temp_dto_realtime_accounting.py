# coding: utf-8

"""
    RADIUS模板管理

    RADIUS模板配置第三方北向接口说明。 

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class RadiusTempDtoRealtimeAccounting(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'realtime_enable': 'bool',
        'realtime_interval': 'int'
    }

    attribute_map = {
        'realtime_enable': 'realtimeEnable',
        'realtime_interval': 'realtimeInterval'
    }

    def __init__(self, realtime_enable=None, realtime_interval=None):
        """
        RadiusTempDtoRealtimeAccounting - a model defined in Swagger
        """

        self._realtime_enable = None
        self._realtime_interval = None

        if realtime_enable is not None:
          self.realtime_enable = realtime_enable
        if realtime_interval is not None:
          self.realtime_interval = realtime_interval

    @property
    def realtime_enable(self):
        """
        Gets the realtime_enable of this RadiusTempDtoRealtimeAccounting.
        是否设置实时计费，如果为true，必须配置实时计费周期，且先配置主计费服务器。创建时，若不填则默认值为false。

        :return: The realtime_enable of this RadiusTempDtoRealtimeAccounting.
        :rtype: bool
        """
        return self._realtime_enable

    @realtime_enable.setter
    def realtime_enable(self, realtime_enable):
        """
        Sets the realtime_enable of this RadiusTempDtoRealtimeAccounting.
        是否设置实时计费，如果为true，必须配置实时计费周期，且先配置主计费服务器。创建时，若不填则默认值为false。

        :param realtime_enable: The realtime_enable of this RadiusTempDtoRealtimeAccounting.
        :type: bool
        """

        self._realtime_enable = realtime_enable

    @property
    def realtime_interval(self):
        """
        Gets the realtime_interval of this RadiusTempDtoRealtimeAccounting.
        实时计费周期，单位是分钟，当realTimeEnable为true时必填。

        :return: The realtime_interval of this RadiusTempDtoRealtimeAccounting.
        :rtype: int
        """
        return self._realtime_interval

    @realtime_interval.setter
    def realtime_interval(self, realtime_interval):
        """
        Sets the realtime_interval of this RadiusTempDtoRealtimeAccounting.
        实时计费周期，单位是分钟，当realTimeEnable为true时必填。

        :param realtime_interval: The realtime_interval of this RadiusTempDtoRealtimeAccounting.
        :type: int
        """
        if realtime_interval is not None and realtime_interval > 65535:
            raise ValueError("Invalid value for `realtime_interval`, must be a value less than or equal to `65535`")
        if realtime_interval is not None and realtime_interval < 1:
            raise ValueError("Invalid value for `realtime_interval`, must be a value greater than or equal to `1`")

        self._realtime_interval = realtime_interval

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, RadiusTempDtoRealtimeAccounting):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
