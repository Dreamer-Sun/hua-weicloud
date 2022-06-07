# coding: utf-8

"""
    本地用户配置管理

    本地用户配置北向接口，主要特性： · 查询本地用户配置 · 修改本地用户配置 · 创建本地用户配置 

    OpenAPI spec version: 1.2.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class InitLocalUserInfoRequst(object):
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
        'password': 'str'
    }

    attribute_map = {
        'password': 'password'
    }

    def __init__(self, password=None):
        """
        InitLocalUserInfoRequst - a model defined in Swagger
        """

        self._password = None

        if password is not None:
          self.password = password

    @property
    def password(self):
        """
        Gets the password of this InitLocalUserInfoRequst.
        1、密码长度必须在8-128位（防火墙设备的密码最大长度为64，如果站点内存在防火墙，请输入64位以内字符）。 2、密码必须满足复杂度，即至少包含英文大写字母（A~Z）、英文小写字母（a~z）、数字（0~9）、特殊字符（如！、@、#、$、%）等中的三种，不允许包含'、?和空格。 3、密码中不能包含两个以上连续的相同字符。 4、密码不能为用户名或用户名的倒写。 

        :return: The password of this InitLocalUserInfoRequst.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this InitLocalUserInfoRequst.
        1、密码长度必须在8-128位（防火墙设备的密码最大长度为64，如果站点内存在防火墙，请输入64位以内字符）。 2、密码必须满足复杂度，即至少包含英文大写字母（A~Z）、英文小写字母（a~z）、数字（0~9）、特殊字符（如！、@、#、$、%）等中的三种，不允许包含'、?和空格。 3、密码中不能包含两个以上连续的相同字符。 4、密码不能为用户名或用户名的倒写。 

        :param password: The password of this InitLocalUserInfoRequst.
        :type: str
        """
        if password is not None and len(password) > 128:
            raise ValueError("Invalid value for `password`, length must be less than or equal to `128`")
        if password is not None and len(password) < 8:
            raise ValueError("Invalid value for `password`, length must be greater than or equal to `8`")

        self._password = password

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
        if not isinstance(other, InitLocalUserInfoRequst):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other