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


class AuthContentDto(object):
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
        'psk_encrypt_type': 'str',
        'security_key': 'str',
        'security_key_type': 'str',
        'dot1x_encrypt_type': 'str',
        'portal': 'PortalContentDto',
        'radius': 'RadiusContentDto',
        'mac_auto_binding': 'bool',
        'escape_strategy': 'str'
    }

    attribute_map = {
        'mode': 'mode',
        'psk_encrypt_type': 'pskEncryptType',
        'security_key': 'securityKey',
        'security_key_type': 'securityKeyType',
        'dot1x_encrypt_type': 'dot1xEncryptType',
        'portal': 'portal',
        'radius': 'radius',
        'mac_auto_binding': 'macAutoBinding',
        'escape_strategy': 'escapeStrategy'
    }

    def __init__(self, mode=None, psk_encrypt_type=None, security_key=None, security_key_type=None, dot1x_encrypt_type=None, portal=None, radius=None, mac_auto_binding=None, escape_strategy=None):
        """
        AuthContentDto - a model defined in Swagger
        """

        self._mode = None
        self._psk_encrypt_type = None
        self._security_key = None
        self._security_key_type = None
        self._dot1x_encrypt_type = None
        self._portal = None
        self._radius = None
        self._mac_auto_binding = None
        self._escape_strategy = None

        if mode is not None:
          self.mode = mode
        if psk_encrypt_type is not None:
          self.psk_encrypt_type = psk_encrypt_type
        if security_key is not None:
          self.security_key = security_key
        if security_key_type is not None:
          self.security_key_type = security_key_type
        if dot1x_encrypt_type is not None:
          self.dot1x_encrypt_type = dot1x_encrypt_type
        if portal is not None:
          self.portal = portal
        if radius is not None:
          self.radius = radius
        if mac_auto_binding is not None:
          self.mac_auto_binding = mac_auto_binding
        if escape_strategy is not None:
          self.escape_strategy = escape_strategy

    @property
    def mode(self):
        """
        Gets the mode of this AuthContentDto.
        关联SSID时的认证模式。

        :return: The mode of this AuthContentDto.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """
        Sets the mode of this AuthContentDto.
        关联SSID时的认证模式。

        :param mode: The mode of this AuthContentDto.
        :type: str
        """

        self._mode = mode

    @property
    def psk_encrypt_type(self):
        """
        Gets the psk_encrypt_type of this AuthContentDto.
        加密模式，当mode为psk或ppsk时必选。大小写敏感，前后不能有空格，且不能含有全角字符。当mode为ppsk时加密方式不支持wep。

        :return: The psk_encrypt_type of this AuthContentDto.
        :rtype: str
        """
        return self._psk_encrypt_type

    @psk_encrypt_type.setter
    def psk_encrypt_type(self, psk_encrypt_type):
        """
        Sets the psk_encrypt_type of this AuthContentDto.
        加密模式，当mode为psk或ppsk时必选。大小写敏感，前后不能有空格，且不能含有全角字符。当mode为ppsk时加密方式不支持wep。

        :param psk_encrypt_type: The psk_encrypt_type of this AuthContentDto.
        :type: str
        """

        self._psk_encrypt_type = psk_encrypt_type

    @property
    def security_key(self):
        """
        Gets the security_key of this AuthContentDto.
        psk密钥，当mode为psk时必选。查询始终为null。 当pskEncryptType为wep时，5位字符与数字组合的字符串。 当pskEncryptType为wpa1AndWpa2或wpa2时，8-63位字母、数字及除问号与空格外的特殊字符组合。

        :return: The security_key of this AuthContentDto.
        :rtype: str
        """
        return self._security_key

    @security_key.setter
    def security_key(self, security_key):
        """
        Sets the security_key of this AuthContentDto.
        psk密钥，当mode为psk时必选。查询始终为null。 当pskEncryptType为wep时，5位字符与数字组合的字符串。 当pskEncryptType为wpa1AndWpa2或wpa2时，8-63位字母、数字及除问号与空格外的特殊字符组合。

        :param security_key: The security_key of this AuthContentDto.
        :type: str
        """

        self._security_key = security_key

    @property
    def security_key_type(self):
        """
        Gets the security_key_type of this AuthContentDto.
        wpa2加密方法，当pskEncryptType为wpa2时必选，默认值为AES。大小写敏感，前后不能有空格，且不能含有全角字符。

        :return: The security_key_type of this AuthContentDto.
        :rtype: str
        """
        return self._security_key_type

    @security_key_type.setter
    def security_key_type(self, security_key_type):
        """
        Sets the security_key_type of this AuthContentDto.
        wpa2加密方法，当pskEncryptType为wpa2时必选，默认值为AES。大小写敏感，前后不能有空格，且不能含有全角字符。

        :param security_key_type: The security_key_type of this AuthContentDto.
        :type: str
        """

        self._security_key_type = security_key_type

    @property
    def dot1x_encrypt_type(self):
        """
        Gets the dot1x_encrypt_type of this AuthContentDto.
        dot1x加密模式，当mode为dot1x时必选。大小写敏感，前后不能有空格，且不能含有全角字符。

        :return: The dot1x_encrypt_type of this AuthContentDto.
        :rtype: str
        """
        return self._dot1x_encrypt_type

    @dot1x_encrypt_type.setter
    def dot1x_encrypt_type(self, dot1x_encrypt_type):
        """
        Sets the dot1x_encrypt_type of this AuthContentDto.
        dot1x加密模式，当mode为dot1x时必选。大小写敏感，前后不能有空格，且不能含有全角字符。

        :param dot1x_encrypt_type: The dot1x_encrypt_type of this AuthContentDto.
        :type: str
        """

        self._dot1x_encrypt_type = dot1x_encrypt_type

    @property
    def portal(self):
        """
        Gets the portal of this AuthContentDto.

        :return: The portal of this AuthContentDto.
        :rtype: PortalContentDto
        """
        return self._portal

    @portal.setter
    def portal(self, portal):
        """
        Sets the portal of this AuthContentDto.

        :param portal: The portal of this AuthContentDto.
        :type: PortalContentDto
        """

        self._portal = portal

    @property
    def radius(self):
        """
        Gets the radius of this AuthContentDto.

        :return: The radius of this AuthContentDto.
        :rtype: RadiusContentDto
        """
        return self._radius

    @radius.setter
    def radius(self, radius):
        """
        Sets the radius of this AuthContentDto.

        :param radius: The radius of this AuthContentDto.
        :type: RadiusContentDto
        """

        self._radius = radius

    @property
    def mac_auto_binding(self):
        """
        Gets the mac_auto_binding of this AuthContentDto.
        是否MAC自动绑定。当mode为ppsk时，此参数必填。若值为true，则开启MAC自动绑定。

        :return: The mac_auto_binding of this AuthContentDto.
        :rtype: bool
        """
        return self._mac_auto_binding

    @mac_auto_binding.setter
    def mac_auto_binding(self, mac_auto_binding):
        """
        Sets the mac_auto_binding of this AuthContentDto.
        是否MAC自动绑定。当mode为ppsk时，此参数必填。若值为true，则开启MAC自动绑定。

        :param mac_auto_binding: The mac_auto_binding of this AuthContentDto.
        :type: bool
        """

        self._mac_auto_binding = mac_auto_binding

    @property
    def escape_strategy(self):
        """
        Gets the escape_strategy of this AuthContentDto.
        逃生策略。当mode为ppsk时，此参数必填。 noNew：允许已认证用户继续使用网络，新用户不允许接入。默认值。 noAuth：允许已认证用户继续使用网络，新用户需要输入PPSK密钥。注意：此时PPSK用户数控制、MCA自动绑定功失效。 

        :return: The escape_strategy of this AuthContentDto.
        :rtype: str
        """
        return self._escape_strategy

    @escape_strategy.setter
    def escape_strategy(self, escape_strategy):
        """
        Sets the escape_strategy of this AuthContentDto.
        逃生策略。当mode为ppsk时，此参数必填。 noNew：允许已认证用户继续使用网络，新用户不允许接入。默认值。 noAuth：允许已认证用户继续使用网络，新用户需要输入PPSK密钥。注意：此时PPSK用户数控制、MCA自动绑定功失效。 

        :param escape_strategy: The escape_strategy of this AuthContentDto.
        :type: str
        """

        self._escape_strategy = escape_strategy

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
        if not isinstance(other, AuthContentDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
