# coding: utf-8

"""
    防火墙特征库升级

    防火墙特征库升级接口 

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ConfigUpgradePolicyListDto(object):
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
        'config_upgrade_policy_dto': 'list[ConfigUpgradePolicyDto]'
    }

    attribute_map = {
        'config_upgrade_policy_dto': 'configUpgradePolicyDto'
    }

    def __init__(self, config_upgrade_policy_dto=None):
        """
        ConfigUpgradePolicyListDto - a model defined in Swagger
        """

        self._config_upgrade_policy_dto = None

        if config_upgrade_policy_dto is not None:
          self.config_upgrade_policy_dto = config_upgrade_policy_dto

    @property
    def config_upgrade_policy_dto(self):
        """
        Gets the config_upgrade_policy_dto of this ConfigUpgradePolicyListDto.

        :return: The config_upgrade_policy_dto of this ConfigUpgradePolicyListDto.
        :rtype: list[ConfigUpgradePolicyDto]
        """
        return self._config_upgrade_policy_dto

    @config_upgrade_policy_dto.setter
    def config_upgrade_policy_dto(self, config_upgrade_policy_dto):
        """
        Sets the config_upgrade_policy_dto of this ConfigUpgradePolicyListDto.

        :param config_upgrade_policy_dto: The config_upgrade_policy_dto of this ConfigUpgradePolicyListDto.
        :type: list[ConfigUpgradePolicyDto]
        """

        self._config_upgrade_policy_dto = config_upgrade_policy_dto

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
        if not isinstance(other, ConfigUpgradePolicyListDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
