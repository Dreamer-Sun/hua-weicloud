# coding: utf-8

"""
    ACL模板管理

    ACL模板第三方管理接口说明。 

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class UpadateAclDto(object):
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
        'name': 'str',
        'description': 'str',
        'rule_list': 'list[RuleList]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'rule_list': 'ruleList'
    }

    def __init__(self, name=None, description=None, rule_list=None):
        """
        UpadateAclDto - a model defined in Swagger
        """

        self._name = None
        self._description = None
        self._rule_list = None

        if name is not None:
          self.name = name
        if description is not None:
          self.description = description
        if rule_list is not None:
          self.rule_list = rule_list

    @property
    def name(self):
        """
        Gets the name of this UpadateAclDto.
        ACL模板名称，包括汉字、字母、数字、下划线、.、@、-不能与已有的名称重复。

        :return: The name of this UpadateAclDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this UpadateAclDto.
        ACL模板名称，包括汉字、字母、数字、下划线、.、@、-不能与已有的名称重复。

        :param name: The name of this UpadateAclDto.
        :type: str
        """
        if name is not None and len(name) > 32:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `32`")
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this UpadateAclDto.
        ACL模板描述。

        :return: The description of this UpadateAclDto.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpadateAclDto.
        ACL模板描述。

        :param description: The description of this UpadateAclDto.
        :type: str
        """
        if description is not None and len(description) > 127:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `127`")
        if description is not None and len(description) < 0:
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")

        self._description = description

    @property
    def rule_list(self):
        """
        Gets the rule_list of this UpadateAclDto.
        规则列表。

        :return: The rule_list of this UpadateAclDto.
        :rtype: list[RuleList]
        """
        return self._rule_list

    @rule_list.setter
    def rule_list(self, rule_list):
        """
        Sets the rule_list of this UpadateAclDto.
        规则列表。

        :param rule_list: The rule_list of this UpadateAclDto.
        :type: list[RuleList]
        """

        self._rule_list = rule_list

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
        if not isinstance(other, UpadateAclDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
