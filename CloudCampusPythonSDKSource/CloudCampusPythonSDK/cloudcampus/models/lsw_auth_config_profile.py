# coding: utf-8

"""
    交换机有线认证模板配置

    交换机有线认证模板，主要包括： · 创建站点下交换机有线认证模板配置 · 查询站点下交换机有线认证模板配置 · 修改站点下交换机有线认证模板配置 · 删除站点下交换机有线认证模板配置 · 修改站点交换机有线认证部分模板配置 · 增量绑站点交换机有线认证模板配置定 

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class LswAuthConfigProfile(object):
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
        'auth_template_id': 'str',
        'lsw_auth_config_profile_core': 'LswAuthConfigProfileCore'
    }

    attribute_map = {
        'auth_template_id': 'authTemplateId',
        'lsw_auth_config_profile_core': 'lswAuthConfigProfileCore'
    }

    def __init__(self, auth_template_id=None, lsw_auth_config_profile_core=None):
        """
        LswAuthConfigProfile - a model defined in Swagger
        """

        self._auth_template_id = None
        self._lsw_auth_config_profile_core = None

        if auth_template_id is not None:
          self.auth_template_id = auth_template_id
        if lsw_auth_config_profile_core is not None:
          self.lsw_auth_config_profile_core = lsw_auth_config_profile_core

    @property
    def auth_template_id(self):
        """
        Gets the auth_template_id of this LswAuthConfigProfile.
        认证模板ID，UUID格式。

        :return: The auth_template_id of this LswAuthConfigProfile.
        :rtype: str
        """
        return self._auth_template_id

    @auth_template_id.setter
    def auth_template_id(self, auth_template_id):
        """
        Sets the auth_template_id of this LswAuthConfigProfile.
        认证模板ID，UUID格式。

        :param auth_template_id: The auth_template_id of this LswAuthConfigProfile.
        :type: str
        """
        if auth_template_id is not None and len(auth_template_id) > 36:
            raise ValueError("Invalid value for `auth_template_id`, length must be less than or equal to `36`")
        if auth_template_id is not None and len(auth_template_id) < 36:
            raise ValueError("Invalid value for `auth_template_id`, length must be greater than or equal to `36`")

        self._auth_template_id = auth_template_id

    @property
    def lsw_auth_config_profile_core(self):
        """
        Gets the lsw_auth_config_profile_core of this LswAuthConfigProfile.

        :return: The lsw_auth_config_profile_core of this LswAuthConfigProfile.
        :rtype: LswAuthConfigProfileCore
        """
        return self._lsw_auth_config_profile_core

    @lsw_auth_config_profile_core.setter
    def lsw_auth_config_profile_core(self, lsw_auth_config_profile_core):
        """
        Sets the lsw_auth_config_profile_core of this LswAuthConfigProfile.

        :param lsw_auth_config_profile_core: The lsw_auth_config_profile_core of this LswAuthConfigProfile.
        :type: LswAuthConfigProfileCore
        """

        self._lsw_auth_config_profile_core = lsw_auth_config_profile_core

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
        if not isinstance(other, LswAuthConfigProfile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
