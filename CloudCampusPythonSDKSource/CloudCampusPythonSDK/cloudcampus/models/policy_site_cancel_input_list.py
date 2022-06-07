# coding: utf-8

"""
    设备升级

    · 查询设备文件 · 创建站点升级 · 查询站点升级 · 查询设备升级 · 取消设备升级 · 删除站点升级 · 重新升级设备 

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class PolicySiteCancelInputList(object):
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
        'policy_site_cancel_input': 'list[PolicySiteInput]'
    }

    attribute_map = {
        'policy_site_cancel_input': 'policySiteCancelInput'
    }

    def __init__(self, policy_site_cancel_input=None):
        """
        PolicySiteCancelInputList - a model defined in Swagger
        """

        self._policy_site_cancel_input = None

        if policy_site_cancel_input is not None:
          self.policy_site_cancel_input = policy_site_cancel_input

    @property
    def policy_site_cancel_input(self):
        """
        Gets the policy_site_cancel_input of this PolicySiteCancelInputList.
        站点入参。

        :return: The policy_site_cancel_input of this PolicySiteCancelInputList.
        :rtype: list[PolicySiteInput]
        """
        return self._policy_site_cancel_input

    @policy_site_cancel_input.setter
    def policy_site_cancel_input(self, policy_site_cancel_input):
        """
        Sets the policy_site_cancel_input of this PolicySiteCancelInputList.
        站点入参。

        :param policy_site_cancel_input: The policy_site_cancel_input of this PolicySiteCancelInputList.
        :type: list[PolicySiteInput]
        """

        self._policy_site_cancel_input = policy_site_cancel_input

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
        if not isinstance(other, PolicySiteCancelInputList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
