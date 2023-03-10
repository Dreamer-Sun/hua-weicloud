# coding: utf-8

"""
    AP SSID配置管理

    AP SSID第三方接口。

    OpenAPI spec version: 1.4.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class PortalContentDto(object):
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
        'mode': 'str',
        'free_auth_enable': 'bool',
        'auth_expire_unit': 'str',
        'auth_expire': 'int',
        'escape_strategy': 'int',
        'free_acl_tmpl_id': 'str',
        'free_acl_tmpl_name': 'str'
    }

    attribute_map = {
        'mode': 'mode',
        'free_auth_enable': 'freeAuthEnable',
        'auth_expire_unit': 'authExpireUnit',
        'auth_expire': 'authExpire',
        'escape_strategy': 'escapeStrategy',
        'free_acl_tmpl_id': 'freeAclTmplId',
        'free_acl_tmpl_name': 'freeAclTmplName'
    }

    def __init__(self, mode=None, free_auth_enable=None, auth_expire_unit=None, auth_expire=None, escape_strategy=None, free_acl_tmpl_id=None, free_acl_tmpl_name=None):
        """
        PortalContentDto - a model defined in Swagger
        """

        self._mode = None
        self._free_auth_enable = None
        self._auth_expire_unit = None
        self._auth_expire = None
        self._escape_strategy = None
        self._free_acl_tmpl_id = None
        self._free_acl_tmpl_name = None

        if mode is not None:
          self.mode = mode
        if free_auth_enable is not None:
          self.free_auth_enable = free_auth_enable
        if auth_expire_unit is not None:
          self.auth_expire_unit = auth_expire_unit
        if auth_expire is not None:
          self.auth_expire = auth_expire
        if escape_strategy is not None:
          self.escape_strategy = escape_strategy
        if free_acl_tmpl_id is not None:
          self.free_acl_tmpl_id = free_acl_tmpl_id
        if free_acl_tmpl_name is not None:
          self.free_acl_tmpl_name = free_acl_tmpl_name

    @property
    def mode(self):
        """
        Gets the mode of this PortalContentDto.
        认证方式。 portalDisable---不启用Portal认证、portalThirdIndirect---云平台中继认证（对接方式：API）

        :return: The mode of this PortalContentDto.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """
        Sets the mode of this PortalContentDto.
        认证方式。 portalDisable---不启用Portal认证、portalThirdIndirect---云平台中继认证（对接方式：API）

        :param mode: The mode of this PortalContentDto.
        :type: str
        """

        self._mode = mode

    @property
    def free_auth_enable(self):
        """
        Gets the free_auth_enable of this PortalContentDto.
        有效期内免认证是否开启，当mode为portalThirdIndirect时必选。若值为true，则开启MAC优先的portal认证。

        :return: The free_auth_enable of this PortalContentDto.
        :rtype: bool
        """
        return self._free_auth_enable

    @free_auth_enable.setter
    def free_auth_enable(self, free_auth_enable):
        """
        Sets the free_auth_enable of this PortalContentDto.
        有效期内免认证是否开启，当mode为portalThirdIndirect时必选。若值为true，则开启MAC优先的portal认证。

        :param free_auth_enable: The free_auth_enable of this PortalContentDto.
        :type: bool
        """

        self._free_auth_enable = free_auth_enable

    @property
    def auth_expire_unit(self):
        """
        Gets the auth_expire_unit of this PortalContentDto.
        Portal认证有效期单位，ssid创建场景：freeAuthEnable为true时，此字段不传则默认值为minute；ssid更新场景：freeAuthEnable为true时，此字段不传则使用更新前的值。只能为day、hour、minute中的一个，大小写不敏感，前后空格忽略，且不能含有全角字符。

        :return: The auth_expire_unit of this PortalContentDto.
        :rtype: str
        """
        return self._auth_expire_unit

    @auth_expire_unit.setter
    def auth_expire_unit(self, auth_expire_unit):
        """
        Sets the auth_expire_unit of this PortalContentDto.
        Portal认证有效期单位，ssid创建场景：freeAuthEnable为true时，此字段不传则默认值为minute；ssid更新场景：freeAuthEnable为true时，此字段不传则使用更新前的值。只能为day、hour、minute中的一个，大小写不敏感，前后空格忽略，且不能含有全角字符。

        :param auth_expire_unit: The auth_expire_unit of this PortalContentDto.
        :type: str
        """

        self._auth_expire_unit = auth_expire_unit

    @property
    def auth_expire(self):
        """
        Gets the auth_expire of this PortalContentDto.
        Portal认证有效期，ssid创建场景：freeAuthEnable为true时，此字段不传则默认值为2；ssid更新场景：freeAuthEnable为true时，此字段不传则使用更新前的值。 authExpireUnit为minute时，范围为1~59。 authExpireUnit为hour时，范围为1~23。 authExpireUnit为day时，范围为1~365。

        :return: The auth_expire of this PortalContentDto.
        :rtype: int
        """
        return self._auth_expire

    @auth_expire.setter
    def auth_expire(self, auth_expire):
        """
        Sets the auth_expire of this PortalContentDto.
        Portal认证有效期，ssid创建场景：freeAuthEnable为true时，此字段不传则默认值为2；ssid更新场景：freeAuthEnable为true时，此字段不传则使用更新前的值。 authExpireUnit为minute时，范围为1~59。 authExpireUnit为hour时，范围为1~23。 authExpireUnit为day时，范围为1~365。

        :param auth_expire: The auth_expire of this PortalContentDto.
        :type: int
        """
        if auth_expire is not None and auth_expire > 365:
            raise ValueError("Invalid value for `auth_expire`, must be a value less than or equal to `365`")
        if auth_expire is not None and auth_expire < 1:
            raise ValueError("Invalid value for `auth_expire`, must be a value greater than or equal to `1`")

        self._auth_expire = auth_expire

    @property
    def escape_strategy(self):
        """
        Gets the escape_strategy of this PortalContentDto.
        逃生策略，当mode为portalThirdIndirect时有效。 1---允许已认证用户继续使用网络，新用户不允许接入，默认值 2---允许用户接入，不需要认证

        :return: The escape_strategy of this PortalContentDto.
        :rtype: int
        """
        return self._escape_strategy

    @escape_strategy.setter
    def escape_strategy(self, escape_strategy):
        """
        Sets the escape_strategy of this PortalContentDto.
        逃生策略，当mode为portalThirdIndirect时有效。 1---允许已认证用户继续使用网络，新用户不允许接入，默认值 2---允许用户接入，不需要认证

        :param escape_strategy: The escape_strategy of this PortalContentDto.
        :type: int
        """

        self._escape_strategy = escape_strategy

    @property
    def free_acl_tmpl_id(self):
        """
        Gets the free_acl_tmpl_id of this PortalContentDto.
        免认证ACL，当mode为portalThirdIndirect时必填。免认证ACL可以通过第三方开放接口/controller/campus/v3/profile/acl得到。UUID格式。

        :return: The free_acl_tmpl_id of this PortalContentDto.
        :rtype: str
        """
        return self._free_acl_tmpl_id

    @free_acl_tmpl_id.setter
    def free_acl_tmpl_id(self, free_acl_tmpl_id):
        """
        Sets the free_acl_tmpl_id of this PortalContentDto.
        免认证ACL，当mode为portalThirdIndirect时必填。免认证ACL可以通过第三方开放接口/controller/campus/v3/profile/acl得到。UUID格式。

        :param free_acl_tmpl_id: The free_acl_tmpl_id of this PortalContentDto.
        :type: str
        """
        if free_acl_tmpl_id is not None and len(free_acl_tmpl_id) > 36:
            raise ValueError("Invalid value for `free_acl_tmpl_id`, length must be less than or equal to `36`")
        if free_acl_tmpl_id is not None and len(free_acl_tmpl_id) < 0:
            raise ValueError("Invalid value for `free_acl_tmpl_id`, length must be greater than or equal to `0`")

        self._free_acl_tmpl_id = free_acl_tmpl_id

    @property
    def free_acl_tmpl_name(self):
        """
        Gets the free_acl_tmpl_name of this PortalContentDto.
        免认证ACL名称，当mode为portalThirdIndirect时有效。POST与PUT操作时，该字段无效。长度为1至32字节。

        :return: The free_acl_tmpl_name of this PortalContentDto.
        :rtype: str
        """
        return self._free_acl_tmpl_name

    @free_acl_tmpl_name.setter
    def free_acl_tmpl_name(self, free_acl_tmpl_name):
        """
        Sets the free_acl_tmpl_name of this PortalContentDto.
        免认证ACL名称，当mode为portalThirdIndirect时有效。POST与PUT操作时，该字段无效。长度为1至32字节。

        :param free_acl_tmpl_name: The free_acl_tmpl_name of this PortalContentDto.
        :type: str
        """
        if free_acl_tmpl_name is not None and len(free_acl_tmpl_name) > 32:
            raise ValueError("Invalid value for `free_acl_tmpl_name`, length must be less than or equal to `32`")
        if free_acl_tmpl_name is not None and len(free_acl_tmpl_name) < 1:
            raise ValueError("Invalid value for `free_acl_tmpl_name`, length must be greater than or equal to `1`")

        self._free_acl_tmpl_name = free_acl_tmpl_name

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
        if not isinstance(other, PortalContentDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
