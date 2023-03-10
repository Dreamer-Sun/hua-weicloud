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


class LswAuthConfigProfileCore(object):
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
        'auth_template_name': 'str',
        'auth_mode': 'str',
        'radius_template_id': 'str',
        'portal': 'PortalContent'
    }

    attribute_map = {
        'auth_template_name': 'authTemplateName',
        'auth_mode': 'authMode',
        'radius_template_id': 'radiusTemplateId',
        'portal': 'portal'
    }

    def __init__(self, auth_template_name=None, auth_mode=None, radius_template_id=None, portal=None):
        """
        LswAuthConfigProfileCore - a model defined in Swagger
        """

        self._auth_template_name = None
        self._auth_mode = None
        self._radius_template_id = None
        self._portal = None

        if auth_template_name is not None:
          self.auth_template_name = auth_template_name
        if auth_mode is not None:
          self.auth_mode = auth_mode
        if radius_template_id is not None:
          self.radius_template_id = radius_template_id
        if portal is not None:
          self.portal = portal

    @property
    def auth_template_name(self):
        """
        Gets the auth_template_name of this LswAuthConfigProfileCore.
        认证模板名称。

        :return: The auth_template_name of this LswAuthConfigProfileCore.
        :rtype: str
        """
        return self._auth_template_name

    @auth_template_name.setter
    def auth_template_name(self, auth_template_name):
        """
        Sets the auth_template_name of this LswAuthConfigProfileCore.
        认证模板名称。

        :param auth_template_name: The auth_template_name of this LswAuthConfigProfileCore.
        :type: str
        """
        if auth_template_name is not None and len(auth_template_name) > 32:
            raise ValueError("Invalid value for `auth_template_name`, length must be less than or equal to `32`")
        if auth_template_name is not None and len(auth_template_name) < 1:
            raise ValueError("Invalid value for `auth_template_name`, length must be greater than or equal to `1`")

        self._auth_template_name = auth_template_name

    @property
    def auth_mode(self):
        """
        Gets the auth_mode of this LswAuthConfigProfileCore.
        认证模式（开放网络，半开放网络---dot1x，安全网络---mac）。

        :return: The auth_mode of this LswAuthConfigProfileCore.
        :rtype: str
        """
        return self._auth_mode

    @auth_mode.setter
    def auth_mode(self, auth_mode):
        """
        Sets the auth_mode of this LswAuthConfigProfileCore.
        认证模式（开放网络，半开放网络---dot1x，安全网络---mac）。

        :param auth_mode: The auth_mode of this LswAuthConfigProfileCore.
        :type: str
        """

        self._auth_mode = auth_mode

    @property
    def radius_template_id(self):
        """
        Gets the radius_template_id of this LswAuthConfigProfileCore.
        RADIUS模板ID，UUID格式。

        :return: The radius_template_id of this LswAuthConfigProfileCore.
        :rtype: str
        """
        return self._radius_template_id

    @radius_template_id.setter
    def radius_template_id(self, radius_template_id):
        """
        Sets the radius_template_id of this LswAuthConfigProfileCore.
        RADIUS模板ID，UUID格式。

        :param radius_template_id: The radius_template_id of this LswAuthConfigProfileCore.
        :type: str
        """
        if radius_template_id is not None and len(radius_template_id) > 36:
            raise ValueError("Invalid value for `radius_template_id`, length must be less than or equal to `36`")
        if radius_template_id is not None and len(radius_template_id) < 36:
            raise ValueError("Invalid value for `radius_template_id`, length must be greater than or equal to `36`")

        self._radius_template_id = radius_template_id

    @property
    def portal(self):
        """
        Gets the portal of this LswAuthConfigProfileCore.

        :return: The portal of this LswAuthConfigProfileCore.
        :rtype: PortalContent
        """
        return self._portal

    @portal.setter
    def portal(self, portal):
        """
        Sets the portal of this LswAuthConfigProfileCore.

        :param portal: The portal of this LswAuthConfigProfileCore.
        :type: PortalContent
        """

        self._portal = portal

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
        if not isinstance(other, LswAuthConfigProfileCore):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
