# coding: utf-8

"""
    路由器设备静态路由配置

    路由器设备静态路由配置第三方接口。

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class DeviceArStaticrouteInfoDto(object):
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
        'mask': 'str',
        'description': 'str',
        'next_address': 'str',
        'destination_ip': 'str',
        'priority': 'int',
        'next_interface': 'str',
        'nqa_id': 'str',
        'nqa_admin_name': 'str',
        'nqa_test_name': 'str',
        'dhcp': 'bool',
        'next_logic_interface': 'str',
        'id': 'str'
    }

    attribute_map = {
        'mask': 'mask',
        'description': 'description',
        'next_address': 'nextAddress',
        'destination_ip': 'destinationIp',
        'priority': 'priority',
        'next_interface': 'nextInterface',
        'nqa_id': 'nqaId',
        'nqa_admin_name': 'nqaAdminName',
        'nqa_test_name': 'nqaTestName',
        'dhcp': 'dhcp',
        'next_logic_interface': 'nextLogicInterface',
        'id': 'id'
    }

    def __init__(self, mask=None, description=None, next_address=None, destination_ip=None, priority=None, next_interface=None, nqa_id=None, nqa_admin_name=None, nqa_test_name=None, dhcp=None, next_logic_interface=None, id=None):
        """
        DeviceArStaticrouteInfoDto - a model defined in Swagger
        """

        self._mask = None
        self._description = None
        self._next_address = None
        self._destination_ip = None
        self._priority = None
        self._next_interface = None
        self._nqa_id = None
        self._nqa_admin_name = None
        self._nqa_test_name = None
        self._dhcp = None
        self._next_logic_interface = None
        self._id = None

        if mask is not None:
          self.mask = mask
        if description is not None:
          self.description = description
        if next_address is not None:
          self.next_address = next_address
        if destination_ip is not None:
          self.destination_ip = destination_ip
        if priority is not None:
          self.priority = priority
        if next_interface is not None:
          self.next_interface = next_interface
        if nqa_id is not None:
          self.nqa_id = nqa_id
        if nqa_admin_name is not None:
          self.nqa_admin_name = nqa_admin_name
        if nqa_test_name is not None:
          self.nqa_test_name = nqa_test_name
        if dhcp is not None:
          self.dhcp = dhcp
        if next_logic_interface is not None:
          self.next_logic_interface = next_logic_interface
        if id is not None:
          self.id = id

    @property
    def mask(self):
        """
        Gets the mask of this DeviceArStaticrouteInfoDto.
        掩码，0-32。创建后不允许修改。

        :return: The mask of this DeviceArStaticrouteInfoDto.
        :rtype: str
        """
        return self._mask

    @mask.setter
    def mask(self, mask):
        """
        Sets the mask of this DeviceArStaticrouteInfoDto.
        掩码，0-32。创建后不允许修改。

        :param mask: The mask of this DeviceArStaticrouteInfoDto.
        :type: str
        """
        if mask is not None and len(mask) > 32:
            raise ValueError("Invalid value for `mask`, length must be less than or equal to `32`")
        if mask is not None and len(mask) < 0:
            raise ValueError("Invalid value for `mask`, length must be greater than or equal to `0`")

        self._mask = mask

    @property
    def description(self):
        """
        Gets the description of this DeviceArStaticrouteInfoDto.
        描述。

        :return: The description of this DeviceArStaticrouteInfoDto.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this DeviceArStaticrouteInfoDto.
        描述。

        :param description: The description of this DeviceArStaticrouteInfoDto.
        :type: str
        """
        if description is not None and len(description) > 256:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `256`")
        if description is not None and len(description) < 0:
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")

        self._description = description

    @property
    def next_address(self):
        """
        Gets the next_address of this DeviceArStaticrouteInfoDto.
        下一跳地址，必须是合法的IPv4地址，以127或者224~255开头的IP地址为非法IP地址。当nextInterface为空时，nextAddress必填。

        :return: The next_address of this DeviceArStaticrouteInfoDto.
        :rtype: str
        """
        return self._next_address

    @next_address.setter
    def next_address(self, next_address):
        """
        Sets the next_address of this DeviceArStaticrouteInfoDto.
        下一跳地址，必须是合法的IPv4地址，以127或者224~255开头的IP地址为非法IP地址。当nextInterface为空时，nextAddress必填。

        :param next_address: The next_address of this DeviceArStaticrouteInfoDto.
        :type: str
        """
        if next_address is not None and len(next_address) > 64:
            raise ValueError("Invalid value for `next_address`, length must be less than or equal to `64`")
        if next_address is not None and len(next_address) < 0:
            raise ValueError("Invalid value for `next_address`, length must be greater than or equal to `0`")

        self._next_address = next_address

    @property
    def destination_ip(self):
        """
        Gets the destination_ip of this DeviceArStaticrouteInfoDto.
        目的IP地址，创建后不允许修改。必须是合法的IPv4地址，以127或者224~255开头的IP地址为非法IP地址。

        :return: The destination_ip of this DeviceArStaticrouteInfoDto.
        :rtype: str
        """
        return self._destination_ip

    @destination_ip.setter
    def destination_ip(self, destination_ip):
        """
        Sets the destination_ip of this DeviceArStaticrouteInfoDto.
        目的IP地址，创建后不允许修改。必须是合法的IPv4地址，以127或者224~255开头的IP地址为非法IP地址。

        :param destination_ip: The destination_ip of this DeviceArStaticrouteInfoDto.
        :type: str
        """
        if destination_ip is not None and len(destination_ip) > 64:
            raise ValueError("Invalid value for `destination_ip`, length must be less than or equal to `64`")
        if destination_ip is not None and len(destination_ip) < 0:
            raise ValueError("Invalid value for `destination_ip`, length must be greater than or equal to `0`")

        self._destination_ip = destination_ip

    @property
    def priority(self):
        """
        Gets the priority of this DeviceArStaticrouteInfoDto.
        优先级，取值越小优先级越高。

        :return: The priority of this DeviceArStaticrouteInfoDto.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """
        Sets the priority of this DeviceArStaticrouteInfoDto.
        优先级，取值越小优先级越高。

        :param priority: The priority of this DeviceArStaticrouteInfoDto.
        :type: int
        """
        if priority is not None and priority > 255:
            raise ValueError("Invalid value for `priority`, must be a value less than or equal to `255`")
        if priority is not None and priority < 1:
            raise ValueError("Invalid value for `priority`, must be a value greater than or equal to `1`")

        self._priority = priority

    @property
    def next_interface(self):
        """
        Gets the next_interface of this DeviceArStaticrouteInfoDto.
        路由出接口。当nextAddress为空时，nextInterface必填。

        :return: The next_interface of this DeviceArStaticrouteInfoDto.
        :rtype: str
        """
        return self._next_interface

    @next_interface.setter
    def next_interface(self, next_interface):
        """
        Sets the next_interface of this DeviceArStaticrouteInfoDto.
        路由出接口。当nextAddress为空时，nextInterface必填。

        :param next_interface: The next_interface of this DeviceArStaticrouteInfoDto.
        :type: str
        """
        if next_interface is not None and len(next_interface) > 25:
            raise ValueError("Invalid value for `next_interface`, length must be less than or equal to `25`")
        if next_interface is not None and len(next_interface) < 0:
            raise ValueError("Invalid value for `next_interface`, length must be greater than or equal to `0`")

        self._next_interface = next_interface

    @property
    def nqa_id(self):
        """
        Gets the nqa_id of this DeviceArStaticrouteInfoDto.
        NQA的ID。

        :return: The nqa_id of this DeviceArStaticrouteInfoDto.
        :rtype: str
        """
        return self._nqa_id

    @nqa_id.setter
    def nqa_id(self, nqa_id):
        """
        Sets the nqa_id of this DeviceArStaticrouteInfoDto.
        NQA的ID。

        :param nqa_id: The nqa_id of this DeviceArStaticrouteInfoDto.
        :type: str
        """
        if nqa_id is not None and len(nqa_id) > 32:
            raise ValueError("Invalid value for `nqa_id`, length must be less than or equal to `32`")
        if nqa_id is not None and len(nqa_id) < 0:
            raise ValueError("Invalid value for `nqa_id`, length must be greater than or equal to `0`")

        self._nqa_id = nqa_id

    @property
    def nqa_admin_name(self):
        """
        Gets the nqa_admin_name of this DeviceArStaticrouteInfoDto.
        NQA的admin名称。

        :return: The nqa_admin_name of this DeviceArStaticrouteInfoDto.
        :rtype: str
        """
        return self._nqa_admin_name

    @nqa_admin_name.setter
    def nqa_admin_name(self, nqa_admin_name):
        """
        Sets the nqa_admin_name of this DeviceArStaticrouteInfoDto.
        NQA的admin名称。

        :param nqa_admin_name: The nqa_admin_name of this DeviceArStaticrouteInfoDto.
        :type: str
        """
        if nqa_admin_name is not None and len(nqa_admin_name) > 32:
            raise ValueError("Invalid value for `nqa_admin_name`, length must be less than or equal to `32`")
        if nqa_admin_name is not None and len(nqa_admin_name) < 0:
            raise ValueError("Invalid value for `nqa_admin_name`, length must be greater than or equal to `0`")

        self._nqa_admin_name = nqa_admin_name

    @property
    def nqa_test_name(self):
        """
        Gets the nqa_test_name of this DeviceArStaticrouteInfoDto.
        NQA的测试名称。

        :return: The nqa_test_name of this DeviceArStaticrouteInfoDto.
        :rtype: str
        """
        return self._nqa_test_name

    @nqa_test_name.setter
    def nqa_test_name(self, nqa_test_name):
        """
        Sets the nqa_test_name of this DeviceArStaticrouteInfoDto.
        NQA的测试名称。

        :param nqa_test_name: The nqa_test_name of this DeviceArStaticrouteInfoDto.
        :type: str
        """
        if nqa_test_name is not None and len(nqa_test_name) > 32:
            raise ValueError("Invalid value for `nqa_test_name`, length must be less than or equal to `32`")
        if nqa_test_name is not None and len(nqa_test_name) < 0:
            raise ValueError("Invalid value for `nqa_test_name`, length must be greater than or equal to `0`")

        self._nqa_test_name = nqa_test_name

    @property
    def dhcp(self):
        """
        Gets the dhcp of this DeviceArStaticrouteInfoDto.
        DHCP开关使能。当nextAddress非空时，dhcp必须为false。

        :return: The dhcp of this DeviceArStaticrouteInfoDto.
        :rtype: bool
        """
        return self._dhcp

    @dhcp.setter
    def dhcp(self, dhcp):
        """
        Sets the dhcp of this DeviceArStaticrouteInfoDto.
        DHCP开关使能。当nextAddress非空时，dhcp必须为false。

        :param dhcp: The dhcp of this DeviceArStaticrouteInfoDto.
        :type: bool
        """

        self._dhcp = dhcp

    @property
    def next_logic_interface(self):
        """
        Gets the next_logic_interface of this DeviceArStaticrouteInfoDto.
        逻辑出接口。

        :return: The next_logic_interface of this DeviceArStaticrouteInfoDto.
        :rtype: str
        """
        return self._next_logic_interface

    @next_logic_interface.setter
    def next_logic_interface(self, next_logic_interface):
        """
        Sets the next_logic_interface of this DeviceArStaticrouteInfoDto.
        逻辑出接口。

        :param next_logic_interface: The next_logic_interface of this DeviceArStaticrouteInfoDto.
        :type: str
        """
        if next_logic_interface is not None and len(next_logic_interface) > 32:
            raise ValueError("Invalid value for `next_logic_interface`, length must be less than or equal to `32`")
        if next_logic_interface is not None and len(next_logic_interface) < 0:
            raise ValueError("Invalid value for `next_logic_interface`, length must be greater than or equal to `0`")

        self._next_logic_interface = next_logic_interface

    @property
    def id(self):
        """
        Gets the id of this DeviceArStaticrouteInfoDto.
        路由器静态路由ID。

        :return: The id of this DeviceArStaticrouteInfoDto.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DeviceArStaticrouteInfoDto.
        路由器静态路由ID。

        :param id: The id of this DeviceArStaticrouteInfoDto.
        :type: str
        """
        if id is not None and len(id) > 32:
            raise ValueError("Invalid value for `id`, length must be less than or equal to `32`")
        if id is not None and len(id) < 0:
            raise ValueError("Invalid value for `id`, length must be greater than or equal to `0`")

        self._id = id

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
        if not isinstance(other, DeviceArStaticrouteInfoDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other