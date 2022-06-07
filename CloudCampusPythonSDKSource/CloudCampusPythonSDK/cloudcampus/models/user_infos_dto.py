# coding: utf-8

"""
    站点模板SNMP配置

    站点模板SNMP配置第三方接口说明。 

    OpenAPI spec version: 1.2.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class UserInfosDto(object):
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
        'snmp_user_name': 'str',
        'snmp_passwd': 'str',
        'snmp_auth': 'str'
    }

    attribute_map = {
        'snmp_user_name': 'snmpUserName',
        'snmp_passwd': 'snmpPasswd',
        'snmp_auth': 'snmpAuth'
    }

    def __init__(self, snmp_user_name=None, snmp_passwd=None, snmp_auth=None):
        """
        UserInfosDto - a model defined in Swagger
        """

        self._snmp_user_name = None
        self._snmp_passwd = None
        self._snmp_auth = None

        if snmp_user_name is not None:
          self.snmp_user_name = snmp_user_name
        if snmp_passwd is not None:
          self.snmp_passwd = snmp_passwd
        if snmp_auth is not None:
          self.snmp_auth = snmp_auth

    @property
    def snmp_user_name(self):
        """
        Gets the snmp_user_name of this UserInfosDto.
        用户名。

        :return: The snmp_user_name of this UserInfosDto.
        :rtype: str
        """
        return self._snmp_user_name

    @snmp_user_name.setter
    def snmp_user_name(self, snmp_user_name):
        """
        Sets the snmp_user_name of this UserInfosDto.
        用户名。

        :param snmp_user_name: The snmp_user_name of this UserInfosDto.
        :type: str
        """
        if snmp_user_name is not None and len(snmp_user_name) > 32:
            raise ValueError("Invalid value for `snmp_user_name`, length must be less than or equal to `32`")
        if snmp_user_name is not None and len(snmp_user_name) < 1:
            raise ValueError("Invalid value for `snmp_user_name`, length must be greater than or equal to `1`")

        self._snmp_user_name = snmp_user_name

    @property
    def snmp_passwd(self):
        """
        Gets the snmp_passwd of this UserInfosDto.
        加密密码，不可与snmpUserName或其倒序相同。

        :return: The snmp_passwd of this UserInfosDto.
        :rtype: str
        """
        return self._snmp_passwd

    @snmp_passwd.setter
    def snmp_passwd(self, snmp_passwd):
        """
        Sets the snmp_passwd of this UserInfosDto.
        加密密码，不可与snmpUserName或其倒序相同。

        :param snmp_passwd: The snmp_passwd of this UserInfosDto.
        :type: str
        """
        if snmp_passwd is not None and len(snmp_passwd) > 64:
            raise ValueError("Invalid value for `snmp_passwd`, length must be less than or equal to `64`")
        if snmp_passwd is not None and len(snmp_passwd) < 8:
            raise ValueError("Invalid value for `snmp_passwd`, length must be greater than or equal to `8`")

        self._snmp_passwd = snmp_passwd

    @property
    def snmp_auth(self):
        """
        Gets the snmp_auth of this UserInfosDto.
        认证密码，不可与snmpUserName或其倒序相同。

        :return: The snmp_auth of this UserInfosDto.
        :rtype: str
        """
        return self._snmp_auth

    @snmp_auth.setter
    def snmp_auth(self, snmp_auth):
        """
        Sets the snmp_auth of this UserInfosDto.
        认证密码，不可与snmpUserName或其倒序相同。

        :param snmp_auth: The snmp_auth of this UserInfosDto.
        :type: str
        """
        if snmp_auth is not None and len(snmp_auth) > 64:
            raise ValueError("Invalid value for `snmp_auth`, length must be less than or equal to `64`")
        if snmp_auth is not None and len(snmp_auth) < 8:
            raise ValueError("Invalid value for `snmp_auth`, length must be greater than or equal to `8`")

        self._snmp_auth = snmp_auth

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
        if not isinstance(other, UserInfosDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
