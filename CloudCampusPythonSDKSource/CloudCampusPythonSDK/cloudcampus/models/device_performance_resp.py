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


class DevicePerformanceResp(object):
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
        'errcode': 'str',
        'errmsg': 'str',
        'data': 'list[DevicePerformance]'
    }

    attribute_map = {
        'errcode': 'errcode',
        'errmsg': 'errmsg',
        'data': 'data'
    }

    def __init__(self, errcode=None, errmsg=None, data=None):
        """
        DevicePerformanceResp - a model defined in Swagger
        """

        self._errcode = None
        self._errmsg = None
        self._data = None

        if errcode is not None:
          self.errcode = errcode
        if errmsg is not None:
          self.errmsg = errmsg
        if data is not None:
          self.data = data

    @property
    def errcode(self):
        """
        Gets the errcode of this DevicePerformanceResp.
        错误码。

        :return: The errcode of this DevicePerformanceResp.
        :rtype: str
        """
        return self._errcode

    @errcode.setter
    def errcode(self, errcode):
        """
        Sets the errcode of this DevicePerformanceResp.
        错误码。

        :param errcode: The errcode of this DevicePerformanceResp.
        :type: str
        """
        if errcode is not None and len(errcode) > 10:
            raise ValueError("Invalid value for `errcode`, length must be less than or equal to `10`")
        if errcode is not None and len(errcode) < 0:
            raise ValueError("Invalid value for `errcode`, length must be greater than or equal to `0`")

        self._errcode = errcode

    @property
    def errmsg(self):
        """
        Gets the errmsg of this DevicePerformanceResp.
        错误信息。

        :return: The errmsg of this DevicePerformanceResp.
        :rtype: str
        """
        return self._errmsg

    @errmsg.setter
    def errmsg(self, errmsg):
        """
        Sets the errmsg of this DevicePerformanceResp.
        错误信息。

        :param errmsg: The errmsg of this DevicePerformanceResp.
        :type: str
        """
        if errmsg is not None and len(errmsg) > 256:
            raise ValueError("Invalid value for `errmsg`, length must be less than or equal to `256`")
        if errmsg is not None and len(errmsg) < 0:
            raise ValueError("Invalid value for `errmsg`, length must be greater than or equal to `0`")

        self._errmsg = errmsg

    @property
    def data(self):
        """
        Gets the data of this DevicePerformanceResp.
        查询到的网络速率信息。

        :return: The data of this DevicePerformanceResp.
        :rtype: list[DevicePerformance]
        """
        return self._data

    @data.setter
    def data(self, data):
        """
        Sets the data of this DevicePerformanceResp.
        查询到的网络速率信息。

        :param data: The data of this DevicePerformanceResp.
        :type: list[DevicePerformance]
        """

        self._data = data

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
        if not isinstance(other, DevicePerformanceResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
