# coding: utf-8

"""
    框式交换机板卡信息操作

    框式上云相关操作接口： 场景：对框式交换机信息查询操作的第三方接口。

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class InterfaceInfoDto(object):
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
        'interface_id': 'str',
        'if_index': 'int',
        'if_name': 'str',
        'device_id': 'str',
        'if_oper_status': 'str',
        'if_admin_status': 'str',
        'ip_address': 'str',
        'if_speeds': 'str',
        'if_mtu': 'str',
        'if_duplex_model': 'str',
        'if_type': 'str'
    }

    attribute_map = {
        'interface_id': 'interfaceId',
        'if_index': 'ifIndex',
        'if_name': 'ifName',
        'device_id': 'deviceId',
        'if_oper_status': 'ifOperStatus',
        'if_admin_status': 'ifAdminStatus',
        'ip_address': 'ipAddress',
        'if_speeds': 'ifSpeeds',
        'if_mtu': 'ifMtu',
        'if_duplex_model': 'ifDuplexModel',
        'if_type': 'ifType'
    }

    def __init__(self, interface_id=None, if_index=None, if_name=None, device_id=None, if_oper_status=None, if_admin_status=None, ip_address=None, if_speeds=None, if_mtu=None, if_duplex_model=None, if_type=None):
        """
        InterfaceInfoDto - a model defined in Swagger
        """

        self._interface_id = None
        self._if_index = None
        self._if_name = None
        self._device_id = None
        self._if_oper_status = None
        self._if_admin_status = None
        self._ip_address = None
        self._if_speeds = None
        self._if_mtu = None
        self._if_duplex_model = None
        self._if_type = None

        if interface_id is not None:
          self.interface_id = interface_id
        if if_index is not None:
          self.if_index = if_index
        if if_name is not None:
          self.if_name = if_name
        if device_id is not None:
          self.device_id = device_id
        if if_oper_status is not None:
          self.if_oper_status = if_oper_status
        if if_admin_status is not None:
          self.if_admin_status = if_admin_status
        if ip_address is not None:
          self.ip_address = ip_address
        if if_speeds is not None:
          self.if_speeds = if_speeds
        if if_mtu is not None:
          self.if_mtu = if_mtu
        if if_duplex_model is not None:
          self.if_duplex_model = if_duplex_model
        if if_type is not None:
          self.if_type = if_type

    @property
    def interface_id(self):
        """
        Gets the interface_id of this InterfaceInfoDto.
        接口ID，UUID格式。

        :return: The interface_id of this InterfaceInfoDto.
        :rtype: str
        """
        return self._interface_id

    @interface_id.setter
    def interface_id(self, interface_id):
        """
        Sets the interface_id of this InterfaceInfoDto.
        接口ID，UUID格式。

        :param interface_id: The interface_id of this InterfaceInfoDto.
        :type: str
        """
        if interface_id is not None and len(interface_id) > 256:
            raise ValueError("Invalid value for `interface_id`, length must be less than or equal to `256`")
        if interface_id is not None and len(interface_id) < 0:
            raise ValueError("Invalid value for `interface_id`, length must be greater than or equal to `0`")

        self._interface_id = interface_id

    @property
    def if_index(self):
        """
        Gets the if_index of this InterfaceInfoDto.
        接口索引。

        :return: The if_index of this InterfaceInfoDto.
        :rtype: int
        """
        return self._if_index

    @if_index.setter
    def if_index(self, if_index):
        """
        Sets the if_index of this InterfaceInfoDto.
        接口索引。

        :param if_index: The if_index of this InterfaceInfoDto.
        :type: int
        """
        if if_index is not None and if_index > 64:
            raise ValueError("Invalid value for `if_index`, must be a value less than or equal to `64`")
        if if_index is not None and if_index < 0:
            raise ValueError("Invalid value for `if_index`, must be a value greater than or equal to `0`")

        self._if_index = if_index

    @property
    def if_name(self):
        """
        Gets the if_name of this InterfaceInfoDto.
        接口名称。

        :return: The if_name of this InterfaceInfoDto.
        :rtype: str
        """
        return self._if_name

    @if_name.setter
    def if_name(self, if_name):
        """
        Sets the if_name of this InterfaceInfoDto.
        接口名称。

        :param if_name: The if_name of this InterfaceInfoDto.
        :type: str
        """
        if if_name is not None and len(if_name) > 256:
            raise ValueError("Invalid value for `if_name`, length must be less than or equal to `256`")
        if if_name is not None and len(if_name) < 0:
            raise ValueError("Invalid value for `if_name`, length must be greater than or equal to `0`")

        self._if_name = if_name

    @property
    def device_id(self):
        """
        Gets the device_id of this InterfaceInfoDto.
        设备ID，UUID格式。

        :return: The device_id of this InterfaceInfoDto.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """
        Sets the device_id of this InterfaceInfoDto.
        设备ID，UUID格式。

        :param device_id: The device_id of this InterfaceInfoDto.
        :type: str
        """
        if device_id is not None and len(device_id) > 256:
            raise ValueError("Invalid value for `device_id`, length must be less than or equal to `256`")
        if device_id is not None and len(device_id) < 0:
            raise ValueError("Invalid value for `device_id`, length must be greater than or equal to `0`")

        self._device_id = device_id

    @property
    def if_oper_status(self):
        """
        Gets the if_oper_status of this InterfaceInfoDto.
        接口运行态。

        :return: The if_oper_status of this InterfaceInfoDto.
        :rtype: str
        """
        return self._if_oper_status

    @if_oper_status.setter
    def if_oper_status(self, if_oper_status):
        """
        Sets the if_oper_status of this InterfaceInfoDto.
        接口运行态。

        :param if_oper_status: The if_oper_status of this InterfaceInfoDto.
        :type: str
        """
        if if_oper_status is not None and len(if_oper_status) > 256:
            raise ValueError("Invalid value for `if_oper_status`, length must be less than or equal to `256`")
        if if_oper_status is not None and len(if_oper_status) < 0:
            raise ValueError("Invalid value for `if_oper_status`, length must be greater than or equal to `0`")

        self._if_oper_status = if_oper_status

    @property
    def if_admin_status(self):
        """
        Gets the if_admin_status of this InterfaceInfoDto.
        接口管理态。

        :return: The if_admin_status of this InterfaceInfoDto.
        :rtype: str
        """
        return self._if_admin_status

    @if_admin_status.setter
    def if_admin_status(self, if_admin_status):
        """
        Sets the if_admin_status of this InterfaceInfoDto.
        接口管理态。

        :param if_admin_status: The if_admin_status of this InterfaceInfoDto.
        :type: str
        """
        if if_admin_status is not None and len(if_admin_status) > 256:
            raise ValueError("Invalid value for `if_admin_status`, length must be less than or equal to `256`")
        if if_admin_status is not None and len(if_admin_status) < 0:
            raise ValueError("Invalid value for `if_admin_status`, length must be greater than or equal to `0`")

        self._if_admin_status = if_admin_status

    @property
    def ip_address(self):
        """
        Gets the ip_address of this InterfaceInfoDto.
        接口IP地址。

        :return: The ip_address of this InterfaceInfoDto.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """
        Sets the ip_address of this InterfaceInfoDto.
        接口IP地址。

        :param ip_address: The ip_address of this InterfaceInfoDto.
        :type: str
        """
        if ip_address is not None and len(ip_address) > 256:
            raise ValueError("Invalid value for `ip_address`, length must be less than or equal to `256`")
        if ip_address is not None and len(ip_address) < 0:
            raise ValueError("Invalid value for `ip_address`, length must be greater than or equal to `0`")

        self._ip_address = ip_address

    @property
    def if_speeds(self):
        """
        Gets the if_speeds of this InterfaceInfoDto.
        接口速率，单位是bps。

        :return: The if_speeds of this InterfaceInfoDto.
        :rtype: str
        """
        return self._if_speeds

    @if_speeds.setter
    def if_speeds(self, if_speeds):
        """
        Sets the if_speeds of this InterfaceInfoDto.
        接口速率，单位是bps。

        :param if_speeds: The if_speeds of this InterfaceInfoDto.
        :type: str
        """
        if if_speeds is not None and len(if_speeds) > 256:
            raise ValueError("Invalid value for `if_speeds`, length must be less than or equal to `256`")
        if if_speeds is not None and len(if_speeds) < 0:
            raise ValueError("Invalid value for `if_speeds`, length must be greater than or equal to `0`")

        self._if_speeds = if_speeds

    @property
    def if_mtu(self):
        """
        Gets the if_mtu of this InterfaceInfoDto.
        接口mtu，单位是Bytes。

        :return: The if_mtu of this InterfaceInfoDto.
        :rtype: str
        """
        return self._if_mtu

    @if_mtu.setter
    def if_mtu(self, if_mtu):
        """
        Sets the if_mtu of this InterfaceInfoDto.
        接口mtu，单位是Bytes。

        :param if_mtu: The if_mtu of this InterfaceInfoDto.
        :type: str
        """
        if if_mtu is not None and len(if_mtu) > 256:
            raise ValueError("Invalid value for `if_mtu`, length must be less than or equal to `256`")
        if if_mtu is not None and len(if_mtu) < 0:
            raise ValueError("Invalid value for `if_mtu`, length must be greater than or equal to `0`")

        self._if_mtu = if_mtu

    @property
    def if_duplex_model(self):
        """
        Gets the if_duplex_model of this InterfaceInfoDto.
        双工模式。

        :return: The if_duplex_model of this InterfaceInfoDto.
        :rtype: str
        """
        return self._if_duplex_model

    @if_duplex_model.setter
    def if_duplex_model(self, if_duplex_model):
        """
        Sets the if_duplex_model of this InterfaceInfoDto.
        双工模式。

        :param if_duplex_model: The if_duplex_model of this InterfaceInfoDto.
        :type: str
        """
        if if_duplex_model is not None and len(if_duplex_model) > 256:
            raise ValueError("Invalid value for `if_duplex_model`, length must be less than or equal to `256`")
        if if_duplex_model is not None and len(if_duplex_model) < 0:
            raise ValueError("Invalid value for `if_duplex_model`, length must be greater than or equal to `0`")

        self._if_duplex_model = if_duplex_model

    @property
    def if_type(self):
        """
        Gets the if_type of this InterfaceInfoDto.
        接口类型。

        :return: The if_type of this InterfaceInfoDto.
        :rtype: str
        """
        return self._if_type

    @if_type.setter
    def if_type(self, if_type):
        """
        Sets the if_type of this InterfaceInfoDto.
        接口类型。

        :param if_type: The if_type of this InterfaceInfoDto.
        :type: str
        """
        if if_type is not None and len(if_type) > 256:
            raise ValueError("Invalid value for `if_type`, length must be less than or equal to `256`")
        if if_type is not None and len(if_type) < 0:
            raise ValueError("Invalid value for `if_type`, length must be greater than or equal to `0`")

        self._if_type = if_type

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
        if not isinstance(other, InterfaceInfoDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
