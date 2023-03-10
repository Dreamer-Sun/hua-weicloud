# coding: utf-8

"""
    AP站点模板SSID配置

    AP站点模板SSID第三方接口说明。 

    OpenAPI spec version: 1.5.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class SiteTemplateSecurityUrlFilterDto(object):
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
        'enable': 'bool',
        'mode': 'int',
        'urls': 'list[str]'
    }

    attribute_map = {
        'enable': 'enable',
        'mode': 'mode',
        'urls': 'urls'
    }

    def __init__(self, enable=None, mode=None, urls=None):
        """
        SiteTemplateSecurityUrlFilterDto - a model defined in Swagger
        """

        self._enable = None
        self._mode = None
        self._urls = None

        if enable is not None:
          self.enable = enable
        if mode is not None:
          self.mode = mode
        if urls is not None:
          self.urls = urls

    @property
    def enable(self):
        """
        Gets the enable of this SiteTemplateSecurityUrlFilterDto.
        是否使能URL过滤。创建SSID时，若未填写此字段，默认值为false。该黑白名单机制对使用代理服务器的浏览器不生效。

        :return: The enable of this SiteTemplateSecurityUrlFilterDto.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """
        Sets the enable of this SiteTemplateSecurityUrlFilterDto.
        是否使能URL过滤。创建SSID时，若未填写此字段，默认值为false。该黑白名单机制对使用代理服务器的浏览器不生效。

        :param enable: The enable of this SiteTemplateSecurityUrlFilterDto.
        :type: bool
        """

        self._enable = enable

    @property
    def mode(self):
        """
        Gets the mode of this SiteTemplateSecurityUrlFilterDto.
        URL过滤类型，当enable为true时mode字段必填且有效。 0---黑名单 1---白名单

        :return: The mode of this SiteTemplateSecurityUrlFilterDto.
        :rtype: int
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """
        Sets the mode of this SiteTemplateSecurityUrlFilterDto.
        URL过滤类型，当enable为true时mode字段必填且有效。 0---黑名单 1---白名单

        :param mode: The mode of this SiteTemplateSecurityUrlFilterDto.
        :type: int
        """

        self._mode = mode

    @property
    def urls(self):
        """
        Gets the urls of this SiteTemplateSecurityUrlFilterDto.
        URL列表。URL长度4-80个字符。当enable为true时有效。mode为0时，urls表示允许访问未匹配的url；mode为1时，urls表示禁止访问未匹配的url。每个URL限制要求：'*'只能出现在首尾，'*'不算做有效字符，前后空格忽略，前缀'http://'忽略，且不能含有全角字符。

        :return: The urls of this SiteTemplateSecurityUrlFilterDto.
        :rtype: list[str]
        """
        return self._urls

    @urls.setter
    def urls(self, urls):
        """
        Sets the urls of this SiteTemplateSecurityUrlFilterDto.
        URL列表。URL长度4-80个字符。当enable为true时有效。mode为0时，urls表示允许访问未匹配的url；mode为1时，urls表示禁止访问未匹配的url。每个URL限制要求：'*'只能出现在首尾，'*'不算做有效字符，前后空格忽略，前缀'http://'忽略，且不能含有全角字符。

        :param urls: The urls of this SiteTemplateSecurityUrlFilterDto.
        :type: list[str]
        """

        self._urls = urls

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
        if not isinstance(other, SiteTemplateSecurityUrlFilterDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
