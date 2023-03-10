# coding: utf-8

"""
    设备基础性能数据信息查询

    · 查询设备网络速率历史数据 · 查询站点维度TopN设备或者全部设备的上行流量、下行流量 · 查询站点维度设备连接终端数历史数据 · 查询单设备连接终端数历史数据 · 查询租户维度下设备状态历史数据 · 查询基于站点的站点健康度和设备健康度 · 查询站点下TOP N SSID流量和最近在线用户数 

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class DeviceStationStatisticInfo(object):
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
        'timestamp': 'int',
        'clients': 'float'
    }

    attribute_map = {
        'timestamp': 'timestamp',
        'clients': 'clients'
    }

    def __init__(self, timestamp=None, clients=None):
        """
        DeviceStationStatisticInfo - a model defined in Swagger
        """

        self._timestamp = None
        self._clients = None

        if timestamp is not None:
          self.timestamp = timestamp
        if clients is not None:
          self.clients = clients

    @property
    def timestamp(self):
        """
        Gets the timestamp of this DeviceStationStatisticInfo.
        格林威治时间。

        :return: The timestamp of this DeviceStationStatisticInfo.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this DeviceStationStatisticInfo.
        格林威治时间。

        :param timestamp: The timestamp of this DeviceStationStatisticInfo.
        :type: int
        """
        if timestamp is not None and timestamp > 2147483647:
            raise ValueError("Invalid value for `timestamp`, must be a value less than or equal to `2147483647`")
        if timestamp is not None and timestamp < 0:
            raise ValueError("Invalid value for `timestamp`, must be a value greater than or equal to `0`")

        self._timestamp = timestamp

    @property
    def clients(self):
        """
        Gets the clients of this DeviceStationStatisticInfo.
        终端数量。

        :return: The clients of this DeviceStationStatisticInfo.
        :rtype: float
        """
        return self._clients

    @clients.setter
    def clients(self, clients):
        """
        Sets the clients of this DeviceStationStatisticInfo.
        终端数量。

        :param clients: The clients of this DeviceStationStatisticInfo.
        :type: float
        """
        if clients is not None and clients > 2147483647:
            raise ValueError("Invalid value for `clients`, must be a value less than or equal to `2147483647`")
        if clients is not None and clients < 0:
            raise ValueError("Invalid value for `clients`, must be a value greater than or equal to `0`")

        self._clients = clients

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
        if not isinstance(other, DeviceStationStatisticInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
