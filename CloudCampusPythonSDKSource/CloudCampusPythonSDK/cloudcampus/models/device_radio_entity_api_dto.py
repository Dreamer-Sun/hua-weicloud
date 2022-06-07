# coding: utf-8

"""
    AP站点射频配置

    AP站点射频配置第三方接口说明。 

    OpenAPI spec version: 1.1.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class DeviceRadioEntityApiDto(object):
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
        'device_id': 'str',
        'device_name': 'str',
        'radio2dot4_enabled': 'bool',
        'radio2dot4_power': 'str',
        'radio2dot4_channel': 'str',
        'radio2_support': 'bool',
        'antenna2_dot4_gain': 'str',
        'radio2_dot4_bandwidth': 'str',
        'radio5_enabled': 'bool',
        'radio5_power': 'str',
        'radio5_channel': 'str',
        'radio5_support': 'bool',
        'antenna5_gain': 'str',
        'radio5_bandwidth': 'str'
    }

    attribute_map = {
        'device_id': 'deviceId',
        'device_name': 'deviceName',
        'radio2dot4_enabled': 'radio2dot4Enabled',
        'radio2dot4_power': 'radio2dot4Power',
        'radio2dot4_channel': 'radio2dot4Channel',
        'radio2_support': 'radio2Support',
        'antenna2_dot4_gain': 'antenna2Dot4Gain',
        'radio2_dot4_bandwidth': 'radio2Dot4Bandwidth',
        'radio5_enabled': 'radio5Enabled',
        'radio5_power': 'radio5Power',
        'radio5_channel': 'radio5Channel',
        'radio5_support': 'radio5Support',
        'antenna5_gain': 'antenna5Gain',
        'radio5_bandwidth': 'radio5Bandwidth'
    }

    def __init__(self, device_id=None, device_name=None, radio2dot4_enabled=None, radio2dot4_power=None, radio2dot4_channel=None, radio2_support=None, antenna2_dot4_gain=None, radio2_dot4_bandwidth=None, radio5_enabled=None, radio5_power=None, radio5_channel=None, radio5_support=None, antenna5_gain=None, radio5_bandwidth=None):
        """
        DeviceRadioEntityApiDto - a model defined in Swagger
        """

        self._device_id = None
        self._device_name = None
        self._radio2dot4_enabled = None
        self._radio2dot4_power = None
        self._radio2dot4_channel = None
        self._radio2_support = None
        self._antenna2_dot4_gain = None
        self._radio2_dot4_bandwidth = None
        self._radio5_enabled = None
        self._radio5_power = None
        self._radio5_channel = None
        self._radio5_support = None
        self._antenna5_gain = None
        self._radio5_bandwidth = None

        if device_id is not None:
          self.device_id = device_id
        if device_name is not None:
          self.device_name = device_name
        if radio2dot4_enabled is not None:
          self.radio2dot4_enabled = radio2dot4_enabled
        if radio2dot4_power is not None:
          self.radio2dot4_power = radio2dot4_power
        if radio2dot4_channel is not None:
          self.radio2dot4_channel = radio2dot4_channel
        if radio2_support is not None:
          self.radio2_support = radio2_support
        if antenna2_dot4_gain is not None:
          self.antenna2_dot4_gain = antenna2_dot4_gain
        if radio2_dot4_bandwidth is not None:
          self.radio2_dot4_bandwidth = radio2_dot4_bandwidth
        if radio5_enabled is not None:
          self.radio5_enabled = radio5_enabled
        if radio5_power is not None:
          self.radio5_power = radio5_power
        if radio5_channel is not None:
          self.radio5_channel = radio5_channel
        if radio5_support is not None:
          self.radio5_support = radio5_support
        if antenna5_gain is not None:
          self.antenna5_gain = antenna5_gain
        if radio5_bandwidth is not None:
          self.radio5_bandwidth = radio5_bandwidth

    @property
    def device_id(self):
        """
        Gets the device_id of this DeviceRadioEntityApiDto.
        设备ID。

        :return: The device_id of this DeviceRadioEntityApiDto.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """
        Sets the device_id of this DeviceRadioEntityApiDto.
        设备ID。

        :param device_id: The device_id of this DeviceRadioEntityApiDto.
        :type: str
        """

        self._device_id = device_id

    @property
    def device_name(self):
        """
        Gets the device_name of this DeviceRadioEntityApiDto.
        设备名称。

        :return: The device_name of this DeviceRadioEntityApiDto.
        :rtype: str
        """
        return self._device_name

    @device_name.setter
    def device_name(self, device_name):
        """
        Sets the device_name of this DeviceRadioEntityApiDto.
        设备名称。

        :param device_name: The device_name of this DeviceRadioEntityApiDto.
        :type: str
        """
        if device_name is not None and len(device_name) > 64:
            raise ValueError("Invalid value for `device_name`, length must be less than or equal to `64`")
        if device_name is not None and len(device_name) < 1:
            raise ValueError("Invalid value for `device_name`, length must be greater than or equal to `1`")

        self._device_name = device_name

    @property
    def radio2dot4_enabled(self):
        """
        Gets the radio2dot4_enabled of this DeviceRadioEntityApiDto.
        2.4G射频使能。

        :return: The radio2dot4_enabled of this DeviceRadioEntityApiDto.
        :rtype: bool
        """
        return self._radio2dot4_enabled

    @radio2dot4_enabled.setter
    def radio2dot4_enabled(self, radio2dot4_enabled):
        """
        Sets the radio2dot4_enabled of this DeviceRadioEntityApiDto.
        2.4G射频使能。

        :param radio2dot4_enabled: The radio2dot4_enabled of this DeviceRadioEntityApiDto.
        :type: bool
        """

        self._radio2dot4_enabled = radio2dot4_enabled

    @property
    def radio2dot4_power(self):
        """
        Gets the radio2dot4_power of this DeviceRadioEntityApiDto.
        2.4G射频发射功率，auto，[1,127]。

        :return: The radio2dot4_power of this DeviceRadioEntityApiDto.
        :rtype: str
        """
        return self._radio2dot4_power

    @radio2dot4_power.setter
    def radio2dot4_power(self, radio2dot4_power):
        """
        Sets the radio2dot4_power of this DeviceRadioEntityApiDto.
        2.4G射频发射功率，auto，[1,127]。

        :param radio2dot4_power: The radio2dot4_power of this DeviceRadioEntityApiDto.
        :type: str
        """

        self._radio2dot4_power = radio2dot4_power

    @property
    def radio2dot4_channel(self):
        """
        Gets the radio2dot4_channel of this DeviceRadioEntityApiDto.
        2.4G射频信道，不同国家码，对应不同的射频信道范围。

        :return: The radio2dot4_channel of this DeviceRadioEntityApiDto.
        :rtype: str
        """
        return self._radio2dot4_channel

    @radio2dot4_channel.setter
    def radio2dot4_channel(self, radio2dot4_channel):
        """
        Sets the radio2dot4_channel of this DeviceRadioEntityApiDto.
        2.4G射频信道，不同国家码，对应不同的射频信道范围。

        :param radio2dot4_channel: The radio2dot4_channel of this DeviceRadioEntityApiDto.
        :type: str
        """

        self._radio2dot4_channel = radio2dot4_channel

    @property
    def radio2_support(self):
        """
        Gets the radio2_support of this DeviceRadioEntityApiDto.
        是否支持2.4G射频。

        :return: The radio2_support of this DeviceRadioEntityApiDto.
        :rtype: bool
        """
        return self._radio2_support

    @radio2_support.setter
    def radio2_support(self, radio2_support):
        """
        Sets the radio2_support of this DeviceRadioEntityApiDto.
        是否支持2.4G射频。

        :param radio2_support: The radio2_support of this DeviceRadioEntityApiDto.
        :type: bool
        """

        self._radio2_support = radio2_support

    @property
    def antenna2_dot4_gain(self):
        """
        Gets the antenna2_dot4_gain of this DeviceRadioEntityApiDto.
        2.4G射频天线增益，0~30。

        :return: The antenna2_dot4_gain of this DeviceRadioEntityApiDto.
        :rtype: str
        """
        return self._antenna2_dot4_gain

    @antenna2_dot4_gain.setter
    def antenna2_dot4_gain(self, antenna2_dot4_gain):
        """
        Sets the antenna2_dot4_gain of this DeviceRadioEntityApiDto.
        2.4G射频天线增益，0~30。

        :param antenna2_dot4_gain: The antenna2_dot4_gain of this DeviceRadioEntityApiDto.
        :type: str
        """

        self._antenna2_dot4_gain = antenna2_dot4_gain

    @property
    def radio2_dot4_bandwidth(self):
        """
        Gets the radio2_dot4_bandwidth of this DeviceRadioEntityApiDto.
        2.4G射频频宽。

        :return: The radio2_dot4_bandwidth of this DeviceRadioEntityApiDto.
        :rtype: str
        """
        return self._radio2_dot4_bandwidth

    @radio2_dot4_bandwidth.setter
    def radio2_dot4_bandwidth(self, radio2_dot4_bandwidth):
        """
        Sets the radio2_dot4_bandwidth of this DeviceRadioEntityApiDto.
        2.4G射频频宽。

        :param radio2_dot4_bandwidth: The radio2_dot4_bandwidth of this DeviceRadioEntityApiDto.
        :type: str
        """

        self._radio2_dot4_bandwidth = radio2_dot4_bandwidth

    @property
    def radio5_enabled(self):
        """
        Gets the radio5_enabled of this DeviceRadioEntityApiDto.
        5G射频使能。

        :return: The radio5_enabled of this DeviceRadioEntityApiDto.
        :rtype: bool
        """
        return self._radio5_enabled

    @radio5_enabled.setter
    def radio5_enabled(self, radio5_enabled):
        """
        Sets the radio5_enabled of this DeviceRadioEntityApiDto.
        5G射频使能。

        :param radio5_enabled: The radio5_enabled of this DeviceRadioEntityApiDto.
        :type: bool
        """

        self._radio5_enabled = radio5_enabled

    @property
    def radio5_power(self):
        """
        Gets the radio5_power of this DeviceRadioEntityApiDto.
        5G射频发射功率，auto，[1,127]。

        :return: The radio5_power of this DeviceRadioEntityApiDto.
        :rtype: str
        """
        return self._radio5_power

    @radio5_power.setter
    def radio5_power(self, radio5_power):
        """
        Sets the radio5_power of this DeviceRadioEntityApiDto.
        5G射频发射功率，auto，[1,127]。

        :param radio5_power: The radio5_power of this DeviceRadioEntityApiDto.
        :type: str
        """

        self._radio5_power = radio5_power

    @property
    def radio5_channel(self):
        """
        Gets the radio5_channel of this DeviceRadioEntityApiDto.
        5G射频信道，不同国家码，对应不同的射频信道范围。

        :return: The radio5_channel of this DeviceRadioEntityApiDto.
        :rtype: str
        """
        return self._radio5_channel

    @radio5_channel.setter
    def radio5_channel(self, radio5_channel):
        """
        Sets the radio5_channel of this DeviceRadioEntityApiDto.
        5G射频信道，不同国家码，对应不同的射频信道范围。

        :param radio5_channel: The radio5_channel of this DeviceRadioEntityApiDto.
        :type: str
        """

        self._radio5_channel = radio5_channel

    @property
    def radio5_support(self):
        """
        Gets the radio5_support of this DeviceRadioEntityApiDto.
        是否支持5G射频。

        :return: The radio5_support of this DeviceRadioEntityApiDto.
        :rtype: bool
        """
        return self._radio5_support

    @radio5_support.setter
    def radio5_support(self, radio5_support):
        """
        Sets the radio5_support of this DeviceRadioEntityApiDto.
        是否支持5G射频。

        :param radio5_support: The radio5_support of this DeviceRadioEntityApiDto.
        :type: bool
        """

        self._radio5_support = radio5_support

    @property
    def antenna5_gain(self):
        """
        Gets the antenna5_gain of this DeviceRadioEntityApiDto.
        5G射频天线增益，0~30。

        :return: The antenna5_gain of this DeviceRadioEntityApiDto.
        :rtype: str
        """
        return self._antenna5_gain

    @antenna5_gain.setter
    def antenna5_gain(self, antenna5_gain):
        """
        Sets the antenna5_gain of this DeviceRadioEntityApiDto.
        5G射频天线增益，0~30。

        :param antenna5_gain: The antenna5_gain of this DeviceRadioEntityApiDto.
        :type: str
        """

        self._antenna5_gain = antenna5_gain

    @property
    def radio5_bandwidth(self):
        """
        Gets the radio5_bandwidth of this DeviceRadioEntityApiDto.
        5G射频频宽。

        :return: The radio5_bandwidth of this DeviceRadioEntityApiDto.
        :rtype: str
        """
        return self._radio5_bandwidth

    @radio5_bandwidth.setter
    def radio5_bandwidth(self, radio5_bandwidth):
        """
        Sets the radio5_bandwidth of this DeviceRadioEntityApiDto.
        5G射频频宽。

        :param radio5_bandwidth: The radio5_bandwidth of this DeviceRadioEntityApiDto.
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
        if not isinstance(other, DeviceRadioEntityApiDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other