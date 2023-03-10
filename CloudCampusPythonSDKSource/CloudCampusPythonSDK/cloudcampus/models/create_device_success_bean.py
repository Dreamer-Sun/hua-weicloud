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


class CreateDeviceSuccessBean(object):
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
        'id': 'str',
        'name': 'str',
        'esn': 'str',
        'description': 'str',
        'tenant_id': 'str',
        'site_id': 'str',
        'device_model': 'str',
        'tags': 'list[str]',
        'system_ip': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'esn': 'esn',
        'description': 'description',
        'tenant_id': 'tenantId',
        'site_id': 'siteId',
        'device_model': 'deviceModel',
        'tags': 'tags',
        'system_ip': 'systemIp'
    }

    def __init__(self, id=None, name=None, esn=None, description=None, tenant_id=None, site_id=None, device_model=None, tags=None, system_ip=None):
        """
        CreateDeviceSuccessBean - a model defined in Swagger
        """

        self._id = None
        self._name = None
        self._esn = None
        self._description = None
        self._tenant_id = None
        self._site_id = None
        self._device_model = None
        self._tags = None
        self._system_ip = None

        if id is not None:
          self.id = id
        if name is not None:
          self.name = name
        if esn is not None:
          self.esn = esn
        if description is not None:
          self.description = description
        if tenant_id is not None:
          self.tenant_id = tenant_id
        if site_id is not None:
          self.site_id = site_id
        if device_model is not None:
          self.device_model = device_model
        if tags is not None:
          self.tags = tags
        if system_ip is not None:
          self.system_ip = system_ip

    @property
    def id(self):
        """
        Gets the id of this CreateDeviceSuccessBean.
        设备ID。

        :return: The id of this CreateDeviceSuccessBean.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CreateDeviceSuccessBean.
        设备ID。

        :param id: The id of this CreateDeviceSuccessBean.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this CreateDeviceSuccessBean.
        设备名称。

        :return: The name of this CreateDeviceSuccessBean.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateDeviceSuccessBean.
        设备名称。

        :param name: The name of this CreateDeviceSuccessBean.
        :type: str
        """
        if name is not None and len(name) > 64:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `64`")
        if name is not None and len(name) < 0:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `0`")

        self._name = name

    @property
    def esn(self):
        """
        Gets the esn of this CreateDeviceSuccessBean.
        设备ESN号。

        :return: The esn of this CreateDeviceSuccessBean.
        :rtype: str
        """
        return self._esn

    @esn.setter
    def esn(self, esn):
        """
        Sets the esn of this CreateDeviceSuccessBean.
        设备ESN号。

        :param esn: The esn of this CreateDeviceSuccessBean.
        :type: str
        """
        if esn is not None and len(esn) > 64:
            raise ValueError("Invalid value for `esn`, length must be less than or equal to `64`")
        if esn is not None and len(esn) < 0:
            raise ValueError("Invalid value for `esn`, length must be greater than or equal to `0`")

        self._esn = esn

    @property
    def description(self):
        """
        Gets the description of this CreateDeviceSuccessBean.
        设备备注信息。

        :return: The description of this CreateDeviceSuccessBean.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateDeviceSuccessBean.
        设备备注信息。

        :param description: The description of this CreateDeviceSuccessBean.
        :type: str
        """
        if description is not None and len(description) > 255:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `255`")
        if description is not None and len(description) < 0:
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")

        self._description = description

    @property
    def tenant_id(self):
        """
        Gets the tenant_id of this CreateDeviceSuccessBean.
        租户ID。

        :return: The tenant_id of this CreateDeviceSuccessBean.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """
        Sets the tenant_id of this CreateDeviceSuccessBean.
        租户ID。

        :param tenant_id: The tenant_id of this CreateDeviceSuccessBean.
        :type: str
        """

        self._tenant_id = tenant_id

    @property
    def site_id(self):
        """
        Gets the site_id of this CreateDeviceSuccessBean.
        站点ID。

        :return: The site_id of this CreateDeviceSuccessBean.
        :rtype: str
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        """
        Sets the site_id of this CreateDeviceSuccessBean.
        站点ID。

        :param site_id: The site_id of this CreateDeviceSuccessBean.
        :type: str
        """

        self._site_id = site_id

    @property
    def device_model(self):
        """
        Gets the device_model of this CreateDeviceSuccessBean.
        设备款型。

        :return: The device_model of this CreateDeviceSuccessBean.
        :rtype: str
        """
        return self._device_model

    @device_model.setter
    def device_model(self, device_model):
        """
        Sets the device_model of this CreateDeviceSuccessBean.
        设备款型。

        :param device_model: The device_model of this CreateDeviceSuccessBean.
        :type: str
        """
        if device_model is not None and len(device_model) > 64:
            raise ValueError("Invalid value for `device_model`, length must be less than or equal to `64`")
        if device_model is not None and len(device_model) < 0:
            raise ValueError("Invalid value for `device_model`, length must be greater than or equal to `0`")

        self._device_model = device_model

    @property
    def tags(self):
        """
        Gets the tags of this CreateDeviceSuccessBean.
        设备标签列表。

        :return: The tags of this CreateDeviceSuccessBean.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this CreateDeviceSuccessBean.
        设备标签列表。

        :param tags: The tags of this CreateDeviceSuccessBean.
        :type: list[str]
        """

        self._tags = tags

    @property
    def system_ip(self):
        """
        Gets the system_ip of this CreateDeviceSuccessBean.
        系统IP。

        :return: The system_ip of this CreateDeviceSuccessBean.
        :rtype: str
        """
        return self._system_ip

    @system_ip.setter
    def system_ip(self, system_ip):
        """
        Sets the system_ip of this CreateDeviceSuccessBean.
        系统IP。

        :param system_ip: The system_ip of this CreateDeviceSuccessBean.
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
        if not isinstance(other, CreateDeviceSuccessBean):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
