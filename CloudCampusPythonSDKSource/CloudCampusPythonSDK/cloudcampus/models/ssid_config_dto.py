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


class SsidConfigDto(object):
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
        'tags': 'list[TagDto]',
        'enable': 'bool',
        'connection_mode': 'str',
        'vlans': 'list[VlanDto]',
        'hided_enable': 'bool',
        'relative_radios': 'int',
        'frequency_navigation': 'bool',
        'max_user_number': 'int',
        'user_separation': 'bool',
        'ssid_auth': 'AuthContentDto',
        'ssid_policy': 'PolicyContentDto',
        'dot11r': 'bool',
        'reassociate_timeout': 'int'
    }

    attribute_map = {
        'name': 'name',
        'tags': 'tags',
        'enable': 'enable',
        'connection_mode': 'connectionMode',
        'vlans': 'vlans',
        'hided_enable': 'hidedEnable',
        'relative_radios': 'relativeRadios',
        'frequency_navigation': 'frequencyNavigation',
        'max_user_number': 'maxUserNumber',
        'user_separation': 'userSeparation',
        'ssid_auth': 'ssidAuth',
        'ssid_policy': 'ssidPolicy',
        'dot11r': 'dot11r',
        'reassociate_timeout': 'reassociateTimeout'
    }

    def __init__(self, name=None, tags=None, enable=None, connection_mode=None, vlans=None, hided_enable=None, relative_radios=None, frequency_navigation=None, max_user_number=None, user_separation=None, ssid_auth=None, ssid_policy=None, dot11r=None, reassociate_timeout=None):
        """
        SsidConfigDto - a model defined in Swagger
        """

        self._name = None
        self._tags = None
        self._enable = None
        self._connection_mode = None
        self._vlans = None
        self._hided_enable = None
        self._relative_radios = None
        self._frequency_navigation = None
        self._max_user_number = None
        self._user_separation = None
        self._ssid_auth = None
        self._ssid_policy = None
        self._dot11r = None
        self._reassociate_timeout = None

        if name is not None:
          self.name = name
        if tags is not None:
          self.tags = tags
        if enable is not None:
          self.enable = enable
        if connection_mode is not None:
          self.connection_mode = connection_mode
        if vlans is not None:
          self.vlans = vlans
        if hided_enable is not None:
          self.hided_enable = hided_enable
        if relative_radios is not None:
          self.relative_radios = relative_radios
        if frequency_navigation is not None:
          self.frequency_navigation = frequency_navigation
        if max_user_number is not None:
          self.max_user_number = max_user_number
        if user_separation is not None:
          self.user_separation = user_separation
        if ssid_auth is not None:
          self.ssid_auth = ssid_auth
        if ssid_policy is not None:
          self.ssid_policy = ssid_policy
        if dot11r is not None:
          self.dot11r = dot11r
        if reassociate_timeout is not None:
          self.reassociate_timeout = reassociate_timeout

    @property
    def name(self):
        """
        Gets the name of this SsidConfigDto.
        SSID名称。长度为1~32字节（UTF-8编码），不能包含特殊符号&、=、？、#、%、+。当以空格开头或结尾时，最大长度减少2字节；当以\"开头时，最大长度减少1字节。

        :return: The name of this SsidConfigDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SsidConfigDto.
        SSID名称。长度为1~32字节（UTF-8编码），不能包含特殊符号&、=、？、#、%、+。当以空格开头或结尾时，最大长度减少2字节；当以\"开头时，最大长度减少1字节。

        :param name: The name of this SsidConfigDto.
        :type: str
        """
        if name is not None and len(name) > 32:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `32`")
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")

        self._name = name

    @property
    def tags(self):
        """
        Gets the tags of this SsidConfigDto.
        设备标签列表，总数不能超过10个。如果指定标签列表，SSID会下发给带有列表中标签的设备。如果不指定，会下发给站点所有设备。

        :return: The tags of this SsidConfigDto.
        :rtype: list[TagDto]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this SsidConfigDto.
        设备标签列表，总数不能超过10个。如果指定标签列表，SSID会下发给带有列表中标签的设备。如果不指定，会下发给站点所有设备。

        :param tags: The tags of this SsidConfigDto.
        :type: list[TagDto]
        """

        self._tags = tags

    @property
    def enable(self):
        """
        Gets the enable of this SsidConfigDto.
        工作状态开启。

        :return: The enable of this SsidConfigDto.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """
        Sets the enable of this SsidConfigDto.
        工作状态开启。

        :param enable: The enable of this SsidConfigDto.
        :type: bool
        """

        self._enable = enable

    @property
    def connection_mode(self):
        """
        Gets the connection_mode of this SsidConfigDto.
        网络连接方式，大小写敏感，前后不能有空格，且不能含有全角字符。

        :return: The connection_mode of this SsidConfigDto.
        :rtype: str
        """
        return self._connection_mode

    @connection_mode.setter
    def connection_mode(self, connection_mode):
        """
        Sets the connection_mode of this SsidConfigDto.
        网络连接方式，大小写敏感，前后不能有空格，且不能含有全角字符。

        :param connection_mode: The connection_mode of this SsidConfigDto.
        :type: str
        """

        self._connection_mode = connection_mode

    @property
    def vlans(self):
        """
        Gets the vlans of this SsidConfigDto.
        SSID所属的VLAN配置信息。当vlans参数为空时系统默认生成一条优先级为0的VLAN配置信息。

        :return: The vlans of this SsidConfigDto.
        :rtype: list[VlanDto]
        """
        return self._vlans

    @vlans.setter
    def vlans(self, vlans):
        """
        Sets the vlans of this SsidConfigDto.
        SSID所属的VLAN配置信息。当vlans参数为空时系统默认生成一条优先级为0的VLAN配置信息。

        :param vlans: The vlans of this SsidConfigDto.
        :type: list[VlanDto]
        """

        self._vlans = vlans

    @property
    def hided_enable(self):
        """
        Gets the hided_enable of this SsidConfigDto.
        是否隐藏SSID。

        :return: The hided_enable of this SsidConfigDto.
        :rtype: bool
        """
        return self._hided_enable

    @hided_enable.setter
    def hided_enable(self, hided_enable):
        """
        Sets the hided_enable of this SsidConfigDto.
        是否隐藏SSID。

        :param hided_enable: The hided_enable of this SsidConfigDto.
        :type: bool
        """

        self._hided_enable = hided_enable

    @property
    def relative_radios(self):
        """
        Gets the relative_radios of this SsidConfigDto.
        射频类型。 1 --- 2.4G(wlan-radio 0/0/0)。 2 --- 5G(wlan-radio 0/0/1)。 3 --- 2.4G(wlan-radio 0/0/0)&5G(wlan-radio 0/0/1)。 4 --- 5G(wlan-radio 0/0/2)。 5 --- 2.4G(wlan-radio 0/0/0)&5G(wlan-radio 0/0/2)。 6 --- 5G(wlan-radio 0/0/1)&5G(wlan-radio 0/0/2)。 7 --- 2.4G(wlan-radio 0/0/0)&5G(wlan-radio 0/0/1)&5G(wlan-radio 0/0/2)。

        :return: The relative_radios of this SsidConfigDto.
        :rtype: int
        """
        return self._relative_radios

    @relative_radios.setter
    def relative_radios(self, relative_radios):
        """
        Sets the relative_radios of this SsidConfigDto.
        射频类型。 1 --- 2.4G(wlan-radio 0/0/0)。 2 --- 5G(wlan-radio 0/0/1)。 3 --- 2.4G(wlan-radio 0/0/0)&5G(wlan-radio 0/0/1)。 4 --- 5G(wlan-radio 0/0/2)。 5 --- 2.4G(wlan-radio 0/0/0)&5G(wlan-radio 0/0/2)。 6 --- 5G(wlan-radio 0/0/1)&5G(wlan-radio 0/0/2)。 7 --- 2.4G(wlan-radio 0/0/0)&5G(wlan-radio 0/0/1)&5G(wlan-radio 0/0/2)。

        :param relative_radios: The relative_radios of this SsidConfigDto.
        :type: int
        """

        self._relative_radios = relative_radios

    @property
    def frequency_navigation(self):
        """
        Gets the frequency_navigation of this SsidConfigDto.
        是否开启频谱导航。

        :return: The frequency_navigation of this SsidConfigDto.
        :rtype: bool
        """
        return self._frequency_navigation

    @frequency_navigation.setter
    def frequency_navigation(self, frequency_navigation):
        """
        Sets the frequency_navigation of this SsidConfigDto.
        是否开启频谱导航。

        :param frequency_navigation: The frequency_navigation of this SsidConfigDto.
        :type: bool
        """

        self._frequency_navigation = frequency_navigation

    @property
    def max_user_number(self):
        """
        Gets the max_user_number of this SsidConfigDto.
        最大用户数。

        :return: The max_user_number of this SsidConfigDto.
        :rtype: int
        """
        return self._max_user_number

    @max_user_number.setter
    def max_user_number(self, max_user_number):
        """
        Sets the max_user_number of this SsidConfigDto.
        最大用户数。

        :param max_user_number: The max_user_number of this SsidConfigDto.
        :type: int
        """
        if max_user_number is not None and max_user_number > 512:
            raise ValueError("Invalid value for `max_user_number`, must be a value less than or equal to `512`")
        if max_user_number is not None and max_user_number < 1:
            raise ValueError("Invalid value for `max_user_number`, must be a value greater than or equal to `1`")

        self._max_user_number = max_user_number

    @property
    def user_separation(self):
        """
        Gets the user_separation of this SsidConfigDto.
        是否用户隔离。

        :return: The user_separation of this SsidConfigDto.
        :rtype: bool
        """
        return self._user_separation

    @user_separation.setter
    def user_separation(self, user_separation):
        """
        Sets the user_separation of this SsidConfigDto.
        是否用户隔离。

        :param user_separation: The user_separation of this SsidConfigDto.
        :type: bool
        """

        self._user_separation = user_separation

    @property
    def ssid_auth(self):
        """
        Gets the ssid_auth of this SsidConfigDto.

        :return: The ssid_auth of this SsidConfigDto.
        :rtype: AuthContentDto
        """
        return self._ssid_auth

    @ssid_auth.setter
    def ssid_auth(self, ssid_auth):
        """
        Sets the ssid_auth of this SsidConfigDto.

        :param ssid_auth: The ssid_auth of this SsidConfigDto.
        :type: AuthContentDto
        """

        self._ssid_auth = ssid_auth

    @property
    def ssid_policy(self):
        """
        Gets the ssid_policy of this SsidConfigDto.

        :return: The ssid_policy of this SsidConfigDto.
        :rtype: PolicyContentDto
        """
        return self._ssid_policy

    @ssid_policy.setter
    def ssid_policy(self, ssid_policy):
        """
        Sets the ssid_policy of this SsidConfigDto.

        :param ssid_policy: The ssid_policy of this SsidConfigDto.
        :type: PolicyContentDto
        """

        self._ssid_policy = ssid_policy

    @property
    def dot11r(self):
        """
        Gets the dot11r of this SsidConfigDto.
        使能802.11r快速漫游功能。

        :return: The dot11r of this SsidConfigDto.
        :rtype: bool
        """
        return self._dot11r

    @dot11r.setter
    def dot11r(self, dot11r):
        """
        Sets the dot11r of this SsidConfigDto.
        使能802.11r快速漫游功能。

        :param dot11r: The dot11r of this SsidConfigDto.
        :type: bool
        """

        self._dot11r = dot11r

    @property
    def reassociate_timeout(self):
        """
        Gets the reassociate_timeout of this SsidConfigDto.
        重新关联的超时时间，单位为秒。

        :return: The reassociate_timeout of this SsidConfigDto.
        :rtype: int
        """
        return self._reassociate_timeout

    @reassociate_timeout.setter
    def reassociate_timeout(self, reassociate_timeout):
        """
        Sets the reassociate_timeout of this SsidConfigDto.
        重新关联的超时时间，单位为秒。

        :param reassociate_timeout: The reassociate_timeout of this SsidConfigDto.
        :type: int
        """
        if reassociate_timeout is not None and reassociate_timeout > 10:
            raise ValueError("Invalid value for `reassociate_timeout`, must be a value less than or equal to `10`")
        if reassociate_timeout is not None and reassociate_timeout < 1:
            raise ValueError("Invalid value for `reassociate_timeout`, must be a value greater than or equal to `1`")

        self._reassociate_timeout = reassociate_timeout

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
        if not isinstance(other, SsidConfigDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other