# coding: utf-8

"""
    AP网口IOT插卡管理

    AP网口IOT插卡查询及操作接口。 场景：对AP网口IOT插卡查询及操作的第三方接口。

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class IotCardOperationDto(object):
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
        'device_id': 'str',
        'slot': 'int',
        'operation': 'str'
    }

    attribute_map = {
        'device_id': 'deviceId',
        'slot': 'slot',
        'operation': 'operation'
    }

    def __init__(self, device_id=None, slot=None, operation=None):
        """
        IotCardOperationDto - a model defined in Swagger
        """

        self._device_id = None
        self._slot = None
        self._operation = None

        if device_id is not None:
          self.device_id = device_id
        if slot is not None:
          self.slot = slot
        if operation is not None:
          self.operation = operation

    @property
    def device_id(self):
        """
        Gets the device_id of this IotCardOperationDto.
        AP的设备ID，UUID格式。

        :return: The device_id of this IotCardOperationDto.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """
        Sets the device_id of this IotCardOperationDto.
        AP的设备ID，UUID格式。

        :param device_id: The device_id of this IotCardOperationDto.
        :type: str
        """
        if device_id is not None and len(device_id) > 64:
            raise ValueError("Invalid value for `device_id`, length must be less than or equal to `64`")
        if device_id is not None and len(device_id) < 0:
            raise ValueError("Invalid value for `device_id`, length must be greater than or equal to `0`")

        self._device_id = device_id

    @property
    def slot(self):
        """
        Gets the slot of this IotCardOperationDto.
        插卡槽位号。

        :return: The slot of this IotCardOperationDto.
        :rtype: int
        """
        return self._slot

    @slot.setter
    def slot(self, slot):
        """
        Sets the slot of this IotCardOperationDto.
        插卡槽位号。

        :param slot: The slot of this IotCardOperationDto.
        :type: int
        """
        if slot is not None and slot > 8:
            raise ValueError("Invalid value for `slot`, must be a value less than or equal to `8`")
        if slot is not None and slot < 0:
            raise ValueError("Invalid value for `slot`, must be a value greater than or equal to `0`")

        self._slot = slot

    @property
    def operation(self):
        """
        Gets the operation of this IotCardOperationDto.
        下发操作。取值范围：reboot---重启、reset-factory-configuration---恢复出厂配置、switch-firmware---切换分区、reset-network-configuration---重置网络配置。

        :return: The operation of this IotCardOperationDto.
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """
        Sets the operation of this IotCardOperationDto.
        下发操作。取值范围：reboot---重启、reset-factory-configuration---恢复出厂配置、switch-firmware---切换分区、reset-network-configuration---重置网络配置。

        :param operation: The operation of this IotCardOperationDto.
        :type: str
        """

        self._operation = operation

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
        if not isinstance(other, IotCardOperationDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
