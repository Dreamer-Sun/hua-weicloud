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


class Device(object):
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
        'esn': 'str',
        'name': 'str',
        'site_id': 'str',
        'description': 'str',
        'device_model': 'str',
        'system_ip': 'str',
        'tags': 'list[str]'
    }

    attribute_map = {
        'esn': 'esn',
        'name': 'name',
        'site_id': 'siteId',
        'description': 'description',
        'device_model': 'deviceModel',
        'system_ip': 'systemIp',
        'tags': 'tags'
    }

    def __init__(self, esn=None, name=None, site_id=None, description=None, device_model=None, system_ip=None, tags=None):
        """
        Device - a model defined in Swagger
        """

        self._esn = None
        self._name = None
        self._site_id = None
        self._description = None
        self._device_model = None
        self._system_ip = None
        self._tags = None

        if esn is not None:
          self.esn = esn
        if name is not None:
          self.name = name
        if site_id is not None:
          self.site_id = site_id
        if description is not None:
          self.description = description
        if device_model is not None:
          self.device_model = device_model
        if system_ip is not None:
          self.system_ip = system_ip
        if tags is not None:
          self.tags = tags

    @property
    def esn(self):
        """
        Gets the esn of this Device.
        设备ESN号。

        :return: The esn of this Device.
        :rtype: str
        """
        return self._esn

    @esn.setter
    def esn(self, esn):
        """
        Sets the esn of this Device.
        设备ESN号。

        :param esn: The esn of this Device.
        :type: str
        """
        if esn is not None and len(esn) > 64:
            raise ValueError("Invalid value for `esn`, length must be less than or equal to `64`")
        if esn is not None and len(esn) < 0:
            raise ValueError("Invalid value for `esn`, length must be greater than or equal to `0`")

        self._esn = esn

    @property
    def name(self):
        """
        Gets the name of this Device.
        设备名称，若不传或传值为空，则以ESN号命名设备，设备名称不能包含\"?\"或者制表符TAB。

        :return: The name of this Device.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Device.
        设备名称，若不传或传值为空，则以ESN号命名设备，设备名称不能包含\"?\"或者制表符TAB。

        :param name: The name of this Device.
        :type: str
        """
        if name is not None and len(name) > 64:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `64`")
        if name is not None and len(name) < 0:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `0`")

        self._name = name

    @property
    def site_id(self):
        """
        Gets the site_id of this Device.
        站点ID，如果不传，则不添加到任意站点。

        :return: The site_id of this Device.
        :rtype: str
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        """
        Sets the site_id of this Device.
        站点ID，如果不传，则不添加到任意站点。

        :param site_id: The site_id of this Device.
        :type: str
        """

        self._site_id = site_id

    @property
    def description(self):
        """
        Gets the description of this Device.
        设备详情描述。

        :return: The description of this Device.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Device.
        设备详情描述。

        :param description: The description of this Device.
        :type: str
        """
        if description is not None and len(description) > 255:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `255`")
        if description is not None and len(description) < 0:
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")

        self._description = description

    @property
    def device_model(self):
        """
        Gets the device_model of this Device.
        设备款型。

        :return: The device_model of this Device.
        :rtype: str
        """
        return self._device_model

    @device_model.setter
    def device_model(self, device_model):
        """
        Sets the device_model of this Device.
        设备款型。

        :param device_model: The device_model of this Device.
        :type: str
        """
        if device_model is not None and len(device_model) > 64:
            raise ValueError("Invalid value for `device_model`, length must be less than or equal to `64`")
        if device_model is not None and len(device_model) < 0:
            raise ValueError("Invalid value for `device_model`, length must be greater than or equal to `0`")

        self._device_model = device_model

    @property
    def system_ip(self):
        """
        Gets the system_ip of this Device.
        系统IP地址。若systemIp不传或为空，则从地址池中自动分配IP下发给设备的loopback口；若非空，则将指定的systemIp下发给设备的loopback口。

        :return: The system_ip of this Device.
        :rtype: str
        """
        return self._system_ip

    @system_ip.setter
    def system_ip(self, system_ip):
        """
        Sets the system_ip of this Device.
        系统IP地址。若systemIp不传或为空，则从地址池中自动分配IP下发给设备的loopback口；若非空，则将指定的systemIp下发给设备的loopback口。

        :param system_ip: The system_ip of this Device.
        :type: str
        """
        if system_ip is not None and len(system_ip) > 64:
            raise ValueError("Invalid value for `system_ip`, length must be less than or equal to `64`")
        if system_ip is not None and len(system_ip) < 0:
            raise ValueError("Invalid value for `system_ip`, length must be greater than or equal to `0`")

        self._system_ip = system_ip

    @property
    def tags(self):
        """
        Gets the tags of this Device.
        设备标签列表，关联标签列表时，站点ID不能为空，只支持AP设备。

        :return: The tags of this Device.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this Device.
        设备标签列表，关联标签列表时，站点ID不能为空，只支持AP设备。

        :param tags: The tags of this Device.
        :type: list[str]
        """

        self._tags = tags

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
        if not isinstance(other, Device):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other