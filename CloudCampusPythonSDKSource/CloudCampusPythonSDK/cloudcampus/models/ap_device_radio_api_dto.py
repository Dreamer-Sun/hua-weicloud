# coding: utf-8

"""
    AP设备射频配置

    AP设备射频配置第三方接口说明。 

    OpenAPI spec version: 1.1.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ApDeviceRadioApiDto(object):
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
        'radio2dot4_enabled': 'bool',
        'radio2dot4_power': 'str',
        'radio2dot4_channel': 'str',
        'radio2dot4_bandwidth': 'str',
        'antenna2_dot4_gain': 'str',
        'radio5_enabled': 'bool',
        'radio5_power': 'str',
        'radio5_channel': 'str',
        'antenna5_gain': 'str',
        'radio5_bandwidth': 'str'
    }

    attribute_map = {
        'radio2dot4_enabled': 'radio2dot4Enabled',
        'radio2dot4_power': 'radio2dot4Power',
        'radio2dot4_channel': 'radio2dot4Channel',
        'radio2dot4_bandwidth': 'radio2dot4Bandwidth',
        'antenna2_dot4_gain': 'antenna2Dot4Gain',
        'radio5_enabled': 'radio5Enabled',
        'radio5_power': 'radio5Power',
        'radio5_channel': 'radio5Channel',
        'antenna5_gain': 'antenna5Gain',
        'radio5_bandwidth': 'radio5Bandwidth'
    }

    def __init__(self, radio2dot4_enabled=None, radio2dot4_power=None, radio2dot4_channel=None, radio2dot4_bandwidth=None, antenna2_dot4_gain=None, radio5_enabled=None, radio5_power=None, radio5_channel=None, antenna5_gain=None, radio5_bandwidth=None):
        """
        ApDeviceRadioApiDto - a model defined in Swagger
        """

        self._radio2dot4_enabled = None
        self._radio2dot4_power = None
        self._radio2dot4_channel = None
        self._radio2dot4_bandwidth = None
        self._antenna2_dot4_gain = None
        self._radio5_enabled = None
        self._radio5_power = None
        self._radio5_channel = None
        self._antenna5_gain = None
        self._radio5_bandwidth = None

        if radio2dot4_enabled is not None:
          self.radio2dot4_enabled = radio2dot4_enabled
        if radio2dot4_power is not None:
          self.radio2dot4_power = radio2dot4_power
        if radio2dot4_channel is not None:
          self.radio2dot4_channel = radio2dot4_channel
        if radio2dot4_bandwidth is not None:
          self.radio2dot4_bandwidth = radio2dot4_bandwidth
        if antenna2_dot4_gain is not None:
          self.antenna2_dot4_gain = antenna2_dot4_gain
        if radio5_enabled is not None:
          self.radio5_enabled = radio5_enabled
        if radio5_power is not None:
          self.radio5_power = radio5_power
        if radio5_channel is not None:
          self.radio5_channel = radio5_channel
        if antenna5_gain is not None:
          self.antenna5_gain = antenna5_gain
        if radio5_bandwidth is not None:
          self.radio5_bandwidth = radio5_bandwidth

    @property
    def radio2dot4_enabled(self):
        """
        Gets the radio2dot4_enabled of this ApDeviceRadioApiDto.
        2.4G射频使能状态。

        :return: The radio2dot4_enabled of this ApDeviceRadioApiDto.
        :rtype: bool
        """
        return self._radio2dot4_enabled

    @radio2dot4_enabled.setter
    def radio2dot4_enabled(self, radio2dot4_enabled):
        """
        Sets the radio2dot4_enabled of this ApDeviceRadioApiDto.
        2.4G射频使能状态。

        :param radio2dot4_enabled: The radio2dot4_enabled of this ApDeviceRadioApiDto.
        :type: bool
        """

        self._radio2dot4_enabled = radio2dot4_enabled

    @property
    def radio2dot4_power(self):
        """
        Gets the radio2dot4_power of this ApDeviceRadioApiDto.
        2.4G射频发射功率，auto，[1,127]。

        :return: The radio2dot4_power of this ApDeviceRadioApiDto.
        :rtype: str
        """
        return self._radio2dot4_power

    @radio2dot4_power.setter
    def radio2dot4_power(self, radio2dot4_power):
        """
        Sets the radio2dot4_power of this ApDeviceRadioApiDto.
        2.4G射频发射功率，auto，[1,127]。

        :param radio2dot4_power: The radio2dot4_power of this ApDeviceRadioApiDto.
        :type: str
        """

        self._radio2dot4_power = radio2dot4_power

    @property
    def radio2dot4_channel(self):
        """
        Gets the radio2dot4_channel of this ApDeviceRadioApiDto.
        2.4G射频信道，不同国家码，对应不同的射频信道范围。

        :return: The radio2dot4_channel of this ApDeviceRadioApiDto.
        :rtype: str
        """
        return self._radio2dot4_channel

    @radio2dot4_channel.setter
    def radio2dot4_channel(self, radio2dot4_channel):
        """
        Sets the radio2dot4_channel of this ApDeviceRadioApiDto.
        2.4G射频信道，不同国家码，对应不同的射频信道范围。

        :param radio2dot4_channel: The radio2dot4_channel of this ApDeviceRadioApiDto.
        :type: str
        """

        self._radio2dot4_channel = radio2dot4_channel

    @property
    def radio2dot4_bandwidth(self):
        """
        Gets the radio2dot4_bandwidth of this ApDeviceRadioApiDto.
        2.4G调优频宽，调优带宽时选择auto，此时2.4G信道也应该为auto。

        :return: The radio2dot4_bandwidth of this ApDeviceRadioApiDto.
        :rtype: str
        """
        return self._radio2dot4_bandwidth

    @radio2dot4_bandwidth.setter
    def radio2dot4_bandwidth(self, radio2dot4_bandwidth):
        """
        Sets the radio2dot4_bandwidth of this ApDeviceRadioApiDto.
        2.4G调优频宽，调优带宽时选择auto，此时2.4G信道也应该为auto。

        :param radio2dot4_bandwidth: The radio2dot4_bandwidth of this ApDeviceRadioApiDto.
        :type: str
        """

        self._radio2dot4_bandwidth = radio2dot4_bandwidth

    @property
    def antenna2_dot4_gain(self):
        """
        Gets the antenna2_dot4_gain of this ApDeviceRadioApiDto.
        2.4G射频天线增益，0~30，室内AP天线增益不支持修改。

        :return: The antenna2_dot4_gain of this ApDeviceRadioApiDto.
        :rtype: str
        """
        return self._antenna2_dot4_gain

    @antenna2_dot4_gain.setter
    def antenna2_dot4_gain(self, antenna2_dot4_gain):
        """
        Sets the antenna2_dot4_gain of this ApDeviceRadioApiDto.
        2.4G射频天线增益，0~30，室内AP天线增益不支持修改。

        :param antenna2_dot4_gain: The antenna2_dot4_gain of this ApDeviceRadioApiDto.
        :type: str
        """

        self._antenna2_dot4_gain = antenna2_dot4_gain

    @property
    def radio5_enabled(self):
        """
        Gets the radio5_enabled of this ApDeviceRadioApiDto.
        5G射频使能状态。

        :return: The radio5_enabled of this ApDeviceRadioApiDto.
        :rtype: bool
        """
        return self._radio5_enabled

    @radio5_enabled.setter
    def radio5_enabled(self, radio5_enabled):
        """
        Sets the radio5_enabled of this ApDeviceRadioApiDto.
        5G射频使能状态。

        :param radio5_enabled: The radio5_enabled of this ApDeviceRadioApiDto.
        :type: bool
        """

        self._radio5_enabled = radio5_enabled

    @property
    def radio5_power(self):
        """
        Gets the radio5_power of this ApDeviceRadioApiDto.
        5G射频发射功率，auto，[1,127]。

        :return: The radio5_power of this ApDeviceRadioApiDto.
        :rtype: str
        """
        return self._radio5_power

    @radio5_power.setter
    def radio5_power(self, radio5_power):
        """
        Sets the radio5_power of this ApDeviceRadioApiDto.
        5G射频发射功率，auto，[1,127]。

        :param radio5_power: The radio5_power of this ApDeviceRadioApiDto.
        :type: str
        """

        self._radio5_power = radio5_power

    @property
    def radio5_channel(self):
        """
        Gets the radio5_channel of this ApDeviceRadioApiDto.
        5G射频信道，不同国家码，对应不同的射频信道范围。

        :return: The radio5_channel of this ApDeviceRadioApiDto.
        :rtype: str
        """
        return self._radio5_channel

    @radio5_channel.setter
    def radio5_channel(self, radio5_channel):
        """
        Sets the radio5_channel of this ApDeviceRadioApiDto.
        5G射频信道，不同国家码，对应不同的射频信道范围。

        :param radio5_channel: The radio5_channel of this ApDeviceRadioApiDto.
        :type: str
        """

        self._radio5_channel = radio5_channel

    @property
    def antenna5_gain(self):
        """
        Gets the antenna5_gain of this ApDeviceRadioApiDto.
        5G射频天线增益，0~30，室内AP天线增益不支持修改。

        :return: The antenna5_gain of this ApDeviceRadioApiDto.
        :rtype: str
        """
        return self._antenna5_gain

    @antenna5_gain.setter
    def antenna5_gain(self, antenna5_gain):
        """
        Sets the antenna5_gain of this ApDeviceRadioApiDto.
        5G射频天线增益，0~30，室内AP天线增益不支持修改。

        :param antenna5_gain: The antenna5_gain of this ApDeviceRadioApiDto.
        :type: str
        """

        self._antenna5_gain = antenna5_gain

    @property
    def radio5_bandwidth(self):
        """
        Gets the radio5_bandwidth of this ApDeviceRadioApiDto.
        5G射频频宽，调优带宽时选择auto，此时5G信道也应该为auto。

        :return: The radio5_bandwidth of this ApDeviceRadioApiDto.
        :rtype: str
        """
        return self._radio5_bandwidth

    @radio5_bandwidth.setter
    def radio5_bandwidth(self, radio5_bandwidth):
        """
        Sets the radio5_bandwidth of this ApDeviceRadioApiDto.
        5G射频频宽，调优带宽时选择auto，此时5G信道也应该为auto。

        :param radio5_bandwidth: The radio5_bandwidth of this ApDeviceRadioApiDto.
        :type: str
        """

        self._radio5_bandwidth = radio5_bandwidth

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
        if not isinstance(other, ApDeviceRadioApiDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
