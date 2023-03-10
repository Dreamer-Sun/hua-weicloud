# coding: utf-8

"""
    交换机STP保护配置

    主要特性： · 创建交换机STP保护配置 · 修改交换机STP保护配置 · 查询交换机STP保护配置 · 删除交换机STP保护配置 

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class StpProtectionViewDto(object):
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
        'stp_protection_configs': 'list[LSWStpProtectionGetDto]'
    }

    attribute_map = {
        'stp_protection_configs': 'stpProtectionConfigs'
    }

    def __init__(self, stp_protection_configs=None):
        """
        StpProtectionViewDto - a model defined in Swagger
        """

        self._stp_protection_configs = None

        if stp_protection_configs is not None:
          self.stp_protection_configs = stp_protection_configs

    @property
    def stp_protection_configs(self):
        """
        Gets the stp_protection_configs of this StpProtectionViewDto.
        查询交换机STP保护配置数据列表。

        :return: The stp_protection_configs of this StpProtectionViewDto.
        :rtype: list[LSWStpProtectionGetDto]
        """
        return self._stp_protection_configs

    @stp_protection_configs.setter
    def stp_protection_configs(self, stp_protection_configs):
        """
        Sets the stp_protection_configs of this StpProtectionViewDto.
        查询交换机STP保护配置数据列表。

        :param stp_protection_configs: The stp_protection_configs of this StpProtectionViewDto.
        :type: list[LSWStpProtectionGetDto]
        """

        self._stp_protection_configs = stp_protection_configs

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
        if not isinstance(other, StpProtectionViewDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
