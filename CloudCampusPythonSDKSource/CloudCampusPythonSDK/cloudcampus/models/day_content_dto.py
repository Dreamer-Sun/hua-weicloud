# coding: utf-8

"""
    时间模板管理

    时间模板第三方接口说明。 

    OpenAPI spec version: 1.2.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class DayContentDto(object):
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
        'switch_day': 'int',
        'start_time': 'str',
        'end_time': 'str',
        'on_off': 'bool'
    }

    attribute_map = {
        'switch_day': 'switchDay',
        'start_time': 'startTime',
        'end_time': 'endTime',
        'on_off': 'onOff'
    }

    def __init__(self, switch_day=None, start_time=None, end_time=None, on_off=None):
        """
        DayContentDto - a model defined in Swagger
        """

        self._switch_day = None
        self._start_time = None
        self._end_time = None
        self._on_off = None

        if switch_day is not None:
          self.switch_day = switch_day
        if start_time is not None:
          self.start_time = start_time
        if end_time is not None:
          self.end_time = end_time
        if on_off is not None:
          self.on_off = on_off

    @property
    def switch_day(self):
        """
        Gets the switch_day of this DayContentDto.
        日期选择。1代表周一，2代表周二，3代表周三，4代表周四，5代表周五，6代表周六，7代表周日。

        :return: The switch_day of this DayContentDto.
        :rtype: int
        """
        return self._switch_day

    @switch_day.setter
    def switch_day(self, switch_day):
        """
        Sets the switch_day of this DayContentDto.
        日期选择。1代表周一，2代表周二，3代表周三，4代表周四，5代表周五，6代表周六，7代表周日。

        :param switch_day: The switch_day of this DayContentDto.
        :type: int
        """

        self._switch_day = switch_day

    @property
    def start_time(self):
        """
        Gets the start_time of this DayContentDto.
        开始时间，HH:MM格式。

        :return: The start_time of this DayContentDto.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """
        Sets the start_time of this DayContentDto.
        开始时间，HH:MM格式。

        :param start_time: The start_time of this DayContentDto.
        :type: str
        """
        if start_time is not None and len(start_time) > 16:
            raise ValueError("Invalid value for `start_time`, length must be less than or equal to `16`")
        if start_time is not None and len(start_time) < 1:
            raise ValueError("Invalid value for `start_time`, length must be greater than or equal to `1`")

        self._start_time = start_time

    @property
    def end_time(self):
        """
        Gets the end_time of this DayContentDto.
        结束时间，HH:MM格式。

        :return: The end_time of this DayContentDto.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """
        Sets the end_time of this DayContentDto.
        结束时间，HH:MM格式。

        :param end_time: The end_time of this DayContentDto.
        :type: str
        """
        if end_time is not None and len(end_time) > 16:
            raise ValueError("Invalid value for `end_time`, length must be less than or equal to `16`")
        if end_time is not None and len(end_time) < 1:
            raise ValueError("Invalid value for `end_time`, length must be greater than or equal to `1`")

        self._end_time = end_time

    @property
    def on_off(self):
        """
        Gets the on_off of this DayContentDto.
        startTime至endTime时间段是启用或禁止。

        :return: The on_off of this DayContentDto.
        :rtype: bool
        """
        return self._on_off

    @on_off.setter
    def on_off(self, on_off):
        """
        Sets the on_off of this DayContentDto.
        startTime至endTime时间段是启用或禁止。

        :param on_off: The on_off of this DayContentDto.
        :type: bool
        """

        self._on_off = on_off

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
        if not isinstance(other, DayContentDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
