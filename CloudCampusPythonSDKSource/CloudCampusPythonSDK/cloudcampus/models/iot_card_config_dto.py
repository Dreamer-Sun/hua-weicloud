# coding: utf-8

"""
    AP IOT配置

    AP IOT配置北向接口，主要特性： · 查询AP IOT配置信息 · 配置AP IOT信息 

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class IotCardConfigDto(object):
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
        'card_name': 'str',
        'card_configured': 'bool',
        'port_type': 'str',
        'communication_port': 'int',
        'communication_protocol': 'str',
        'share_key': 'str',
        'trusted_host_address': 'str',
        'iot_server2': 'str',
        'port2': 'int',
        'administrative_status': 'bool',
        'default_vlan': 'int',
        'description': 'str',
        'iot_server1_config': 'list[IotServer1Dto]'
    }

    attribute_map = {
        'card_name': 'cardName',
        'card_configured': 'cardConfigured',
        'port_type': 'portType',
        'communication_port': 'communicationPort',
        'communication_protocol': 'communicationProtocol',
        'share_key': 'shareKey',
        'trusted_host_address': 'trustedHostAddress',
        'iot_server2': 'iotServer2',
        'port2': 'port2',
        'administrative_status': 'administrativeStatus',
        'default_vlan': 'defaultVlan',
        'description': 'description',
        'iot_server1_config': 'iotServer1Config'
    }

    def __init__(self, card_name=None, card_configured=None, port_type=None, communication_port=None, communication_protocol=None, share_key=None, trusted_host_address=None, iot_server2=None, port2=None, administrative_status=None, default_vlan=None, description=None, iot_server1_config=None):
        """
        IotCardConfigDto - a model defined in Swagger
        """

        self._card_name = None
        self._card_configured = None
        self._port_type = None
        self._communication_port = None
        self._communication_protocol = None
        self._share_key = None
        self._trusted_host_address = None
        self._iot_server2 = None
        self._port2 = None
        self._administrative_status = None
        self._default_vlan = None
        self._description = None
        self._iot_server1_config = None

        if card_name is not None:
          self.card_name = card_name
        if card_configured is not None:
          self.card_configured = card_configured
        if port_type is not None:
          self.port_type = port_type
        if communication_port is not None:
          self.communication_port = communication_port
        if communication_protocol is not None:
          self.communication_protocol = communication_protocol
        if share_key is not None:
          self.share_key = share_key
        if trusted_host_address is not None:
          self.trusted_host_address = trusted_host_address
        if iot_server2 is not None:
          self.iot_server2 = iot_server2
        if port2 is not None:
          self.port2 = port2
        if administrative_status is not None:
          self.administrative_status = administrative_status
        if default_vlan is not None:
          self.default_vlan = default_vlan
        if description is not None:
          self.description = description
        if iot_server1_config is not None:
          self.iot_server1_config = iot_server1_config

    @property
    def card_name(self):
        """
        Gets the card_name of this IotCardConfigDto.
        插卡名称

        :return: The card_name of this IotCardConfigDto.
        :rtype: str
        """
        return self._card_name

    @card_name.setter
    def card_name(self, card_name):
        """
        Sets the card_name of this IotCardConfigDto.
        插卡名称

        :param card_name: The card_name of this IotCardConfigDto.
        :type: str
        """

        self._card_name = card_name

    @property
    def card_configured(self):
        """
        Gets the card_configured of this IotCardConfigDto.
        该卡槽是否配置，true代表已经配置，false代表没配置。

        :return: The card_configured of this IotCardConfigDto.
        :rtype: bool
        """
        return self._card_configured

    @card_configured.setter
    def card_configured(self, card_configured):
        """
        Sets the card_configured of this IotCardConfigDto.
        该卡槽是否配置，true代表已经配置，false代表没配置。

        :param card_configured: The card_configured of this IotCardConfigDto.
        :type: bool
        """

        self._card_configured = card_configured

    @property
    def port_type(self):
        """
        Gets the port_type of this IotCardConfigDto.
        端口类型。ethernet---以太网口，serial---串口。

        :return: The port_type of this IotCardConfigDto.
        :rtype: str
        """
        return self._port_type

    @port_type.setter
    def port_type(self, port_type):
        """
        Sets the port_type of this IotCardConfigDto.
        端口类型。ethernet---以太网口，serial---串口。

        :param port_type: The port_type of this IotCardConfigDto.
        :type: str
        """

        self._port_type = port_type

    @property
    def communication_port(self):
        """
        Gets the communication_port of this IotCardConfigDto.
        通信端口。

        :return: The communication_port of this IotCardConfigDto.
        :rtype: int
        """
        return self._communication_port

    @communication_port.setter
    def communication_port(self, communication_port):
        """
        Sets the communication_port of this IotCardConfigDto.
        通信端口。

        :param communication_port: The communication_port of this IotCardConfigDto.
        :type: int
        """
        if communication_port is not None and communication_port > 55535:
            raise ValueError("Invalid value for `communication_port`, must be a value less than or equal to `55535`")
        if communication_port is not None and communication_port < 1025:
            raise ValueError("Invalid value for `communication_port`, must be a value greater than or equal to `1025`")

        self._communication_port = communication_port

    @property
    def communication_protocol(self):
        """
        Gets the communication_protocol of this IotCardConfigDto.
        通信协议。

        :return: The communication_protocol of this IotCardConfigDto.
        :rtype: str
        """
        return self._communication_protocol

    @communication_protocol.setter
    def communication_protocol(self, communication_protocol):
        """
        Sets the communication_protocol of this IotCardConfigDto.
        通信协议。

        :param communication_protocol: The communication_protocol of this IotCardConfigDto.
        :type: str
        """

        self._communication_protocol = communication_protocol

    @property
    def share_key(self):
        """
        Gets the share_key of this IotCardConfigDto.
        共享秘钥，至少包含小写字母、大写字母、数字、特殊符号（除问号和空格）中的两种，不能包含全角字符。

        :return: The share_key of this IotCardConfigDto.
        :rtype: str
        """
        return self._share_key

    @share_key.setter
    def share_key(self, share_key):
        """
        Sets the share_key of this IotCardConfigDto.
        共享秘钥，至少包含小写字母、大写字母、数字、特殊符号（除问号和空格）中的两种，不能包含全角字符。

        :param share_key: The share_key of this IotCardConfigDto.
        :type: str
        """
        if share_key is not None and len(share_key) > 32:
            raise ValueError("Invalid value for `share_key`, length must be less than or equal to `32`")
        if share_key is not None and len(share_key) < 6:
            raise ValueError("Invalid value for `share_key`, length must be greater than or equal to `6`")

        self._share_key = share_key

    @property
    def trusted_host_address(self):
        """
        Gets the trusted_host_address of this IotCardConfigDto.
        信任主机地址，格式为IP/掩码。

        :return: The trusted_host_address of this IotCardConfigDto.
        :rtype: str
        """
        return self._trusted_host_address

    @trusted_host_address.setter
    def trusted_host_address(self, trusted_host_address):
        """
        Sets the trusted_host_address of this IotCardConfigDto.
        信任主机地址，格式为IP/掩码。

        :param trusted_host_address: The trusted_host_address of this IotCardConfigDto.
        :type: str
        """

        self._trusted_host_address = trusted_host_address

    @property
    def iot_server2(self):
        """
        Gets the iot_server2 of this IotCardConfigDto.
        第二通道IoT服务器，支持域名和IP地址。

        :return: The iot_server2 of this IotCardConfigDto.
        :rtype: str
        """
        return self._iot_server2

    @iot_server2.setter
    def iot_server2(self, iot_server2):
        """
        Sets the iot_server2 of this IotCardConfigDto.
        第二通道IoT服务器，支持域名和IP地址。

        :param iot_server2: The iot_server2 of this IotCardConfigDto.
        :type: str
        """

        self._iot_server2 = iot_server2

    @property
    def port2(self):
        """
        Gets the port2 of this IotCardConfigDto.
        第二通道IoT端口。

        :return: The port2 of this IotCardConfigDto.
        :rtype: int
        """
        return self._port2

    @port2.setter
    def port2(self, port2):
        """
        Sets the port2 of this IotCardConfigDto.
        第二通道IoT端口。

        :param port2: The port2 of this IotCardConfigDto.
        :type: int
        """
        if port2 is not None and port2 > 65535:
            raise ValueError("Invalid value for `port2`, must be a value less than or equal to `65535`")
        if port2 is not None and port2 < 1:
            raise ValueError("Invalid value for `port2`, must be a value greater than or equal to `1`")

        self._port2 = port2

    @property
    def administrative_status(self):
        """
        Gets the administrative_status of this IotCardConfigDto.
        使能管理状态。

        :return: The administrative_status of this IotCardConfigDto.
        :rtype: bool
        """
        return self._administrative_status

    @administrative_status.setter
    def administrative_status(self, administrative_status):
        """
        Sets the administrative_status of this IotCardConfigDto.
        使能管理状态。

        :param administrative_status: The administrative_status of this IotCardConfigDto.
        :type: bool
        """

        self._administrative_status = administrative_status

    @property
    def default_vlan(self):
        """
        Gets the default_vlan of this IotCardConfigDto.
        默认放通VLAN。

        :return: The default_vlan of this IotCardConfigDto.
        :rtype: int
        """
        return self._default_vlan

    @default_vlan.setter
    def default_vlan(self, default_vlan):
        """
        Sets the default_vlan of this IotCardConfigDto.
        默认放通VLAN。

        :param default_vlan: The default_vlan of this IotCardConfigDto.
        :type: int
        """
        if default_vlan is not None and default_vlan > 4094:
            raise ValueError("Invalid value for `default_vlan`, must be a value less than or equal to `4094`")
        if default_vlan is not None and default_vlan < 1:
            raise ValueError("Invalid value for `default_vlan`, must be a value greater than or equal to `1`")

        self._default_vlan = default_vlan

    @property
    def description(self):
        """
        Gets the description of this IotCardConfigDto.
        描述，不能输入中文和特殊字符。

        :return: The description of this IotCardConfigDto.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this IotCardConfigDto.
        描述，不能输入中文和特殊字符。

        :param description: The description of this IotCardConfigDto.
        :type: str
        """
        if description is not None and len(description) > 242:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `242`")
        if description is not None and len(description) < 1:
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `1`")

        self._description = description

    @property
    def iot_server1_config(self):
        """
        Gets the iot_server1_config of this IotCardConfigDto.

        :return: The iot_server1_config of this IotCardConfigDto.
        :rtype: list[IotServer1Dto]
        """
        return self._iot_server1_config

    @iot_server1_config.setter
    def iot_server1_config(self, iot_server1_config):
        """
        Sets the iot_server1_config of this IotCardConfigDto.

        :param iot_server1_config: The iot_server1_config of this IotCardConfigDto.
        :type: list[IotServer1Dto]
        """

        self._iot_server1_config = iot_server1_config

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
        if not isinstance(other, IotCardConfigDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
