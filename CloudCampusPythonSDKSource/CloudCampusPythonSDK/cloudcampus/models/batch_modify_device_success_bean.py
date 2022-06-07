# coding: utf-8

"""
    设备基本信息管理

    设备相关操作接口。 场景：对设备增删改查操作的第三方接口。

    OpenAPI spec version: 1.6.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class BatchModifyDeviceSuccessBean(object):
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
        'esn': 'str',
        'name': 'str',
        'description': 'str',
        'system_ip': 'str'
    }

    attribute_map = {
        'device_id': 'deviceId',
        'esn': 'esn',
        'name': 'name',
        'description': 'description',
        'system_ip': 'systemIp'
    }

    def __init__(self, device_id=None, esn=None, name=None, description=None, system_ip=None):
        """
        BatchModifyDeviceSuccessBean - a model defined in Swagger
        """

        self._device_id = None
        self._esn = None
        self._name = None
        self._description = None
        self._system_ip = None

        if device_id is not None:
          self.device_id = device_id
        if esn is not None:
          self.esn = esn
        if name is not None:
          self.name = name
        if description is not None:
          self.description = description
        if system_ip is not None:
          self.system_ip = system_ip

    @property
    def device_id(self):
        """
        Gets the device_id of this BatchModifyDeviceSuccessBean.
        设备ID。

        :return: The device_id of this BatchModifyDeviceSuccessBean.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """
        Sets the device_id of this BatchModifyDeviceSuccessBean.
        设备ID。

        :param device_id: The device_id of this BatchModifyDeviceSuccessBean.
        :type: str
        """

        self._device_id = device_id

    @property
    def esn(self):
        """
        Gets the esn of this BatchModifyDeviceSuccessBean.
        设备ESN号。

        :return: The esn of this BatchModifyDeviceSuccessBean.
        :rtype: str
        """
        return self._esn

    @esn.setter
    def esn(self, esn):
        """
        Sets the esn of this BatchModifyDeviceSuccessBean.
        设备ESN号。

        :param esn: The esn of this BatchModifyDeviceSuccessBean.
        :type: str
        """

        self._esn = esn

    @property
    def name(self):
        """
        Gets the name of this BatchModifyDeviceSuccessBean.
        设备名称。

        :return: The name of this BatchModifyDeviceSuccessBean.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this BatchModifyDeviceSuccessBean.
        设备名称。

        :param name: The name of this BatchModifyDeviceSuccessBean.
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this BatchModifyDeviceSuccessBean.
        设备详情描述。

        :return: The description of this BatchModifyDeviceSuccessBean.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this BatchModifyDeviceSuccessBean.
        设备详情描述。

        :param description: The description of this BatchModifyDeviceSuccessBean.
        :type: str
        """
        if description is not None and len(description) > 255:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `255`")
        if description is not None and len(description) < 0:
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")

        self._description = description

    @property
    def system_ip(self):
        """
        Gets the system_ip of this BatchModifyDeviceSuccessBean.
        系统IP地址。

        :return: The system_ip of this BatchModifyDeviceSuccessBean.
        :rtype: str
        """
        return self._system_ip

    @system_ip.setter
    def system_ip(self, system_ip):
        """
        Sets the system_ip of this BatchModifyDeviceSuccessBean.
        系统IP地址。

        :param system_ip: The system_ip of this BatchModifyDeviceSuccessBean.
        :type: str
        """
        if system_ip is not None and len(system_ip) > 64:
            raise ValueError("Invalid value for `system_ip`, length must be less than or equal to `64`")
        if system_ip is not None and len(system_ip) < 0:
            raise ValueError("Invalid value for `system_ip`, length must be greater than or equal to `0`")

        self._system_ip = system_ip

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
        if not isinstance(other, BatchModifyDeviceSuccessBean):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other