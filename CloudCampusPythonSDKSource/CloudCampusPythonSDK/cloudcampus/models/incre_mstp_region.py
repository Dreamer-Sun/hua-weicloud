# coding: utf-8

"""
    交换机STP配置

    LSW STP配置北向接口，主要特性： · 查询交换STP配置信息 · 修改交换机STP配置 · 删除交换机STP配置 

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class IncreMstpRegion(object):
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
        'region_id': 'str',
        'region_name': 'str',
        'revision_level': 'int',
        'mstp_region_instances': 'list[IncreMstpRegionInstance]',
        'region_device_list': 'list[str]'
    }

    attribute_map = {
        'region_id': 'regionId',
        'region_name': 'regionName',
        'revision_level': 'revisionLevel',
        'mstp_region_instances': 'mstpRegionInstances',
        'region_device_list': 'regionDeviceList'
    }

    def __init__(self, region_id=None, region_name=None, revision_level=None, mstp_region_instances=None, region_device_list=None):
        """
        IncreMstpRegion - a model defined in Swagger
        """

        self._region_id = None
        self._region_name = None
        self._revision_level = None
        self._mstp_region_instances = None
        self._region_device_list = None

        if region_id is not None:
          self.region_id = region_id
        if region_name is not None:
          self.region_name = region_name
        if revision_level is not None:
          self.revision_level = revision_level
        if mstp_region_instances is not None:
          self.mstp_region_instances = mstp_region_instances
        if region_device_list is not None:
          self.region_device_list = region_device_list

    @property
    def region_id(self):
        """
        Gets the region_id of this IncreMstpRegion.
        域ID。

        :return: The region_id of this IncreMstpRegion.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """
        Sets the region_id of this IncreMstpRegion.
        域ID。

        :param region_id: The region_id of this IncreMstpRegion.
        :type: str
        """

        self._region_id = region_id

    @property
    def region_name(self):
        """
        Gets the region_name of this IncreMstpRegion.
        域名。

        :return: The region_name of this IncreMstpRegion.
        :rtype: str
        """
        return self._region_name

    @region_name.setter
    def region_name(self, region_name):
        """
        Sets the region_name of this IncreMstpRegion.
        域名。

        :param region_name: The region_name of this IncreMstpRegion.
        :type: str
        """
        if region_name is not None and len(region_name) > 32:
            raise ValueError("Invalid value for `region_name`, length must be less than or equal to `32`")
        if region_name is not None and len(region_name) < 1:
            raise ValueError("Invalid value for `region_name`, length must be greater than or equal to `1`")

        self._region_name = region_name

    @property
    def revision_level(self):
        """
        Gets the revision_level of this IncreMstpRegion.
        修订级别。

        :return: The revision_level of this IncreMstpRegion.
        :rtype: int
        """
        return self._revision_level

    @revision_level.setter
    def revision_level(self, revision_level):
        """
        Sets the revision_level of this IncreMstpRegion.
        修订级别。

        :param revision_level: The revision_level of this IncreMstpRegion.
        :type: int
        """
        if revision_level is not None and revision_level > 65535:
            raise ValueError("Invalid value for `revision_level`, must be a value less than or equal to `65535`")
        if revision_level is not None and revision_level < 0:
            raise ValueError("Invalid value for `revision_level`, must be a value greater than or equal to `0`")

        self._revision_level = revision_level

    @property
    def mstp_region_instances(self):
        """
        Gets the mstp_region_instances of this IncreMstpRegion.
        生成树实例集合。

        :return: The mstp_region_instances of this IncreMstpRegion.
        :rtype: list[IncreMstpRegionInstance]
        """
        return self._mstp_region_instances

    @mstp_region_instances.setter
    def mstp_region_instances(self, mstp_region_instances):
        """
        Sets the mstp_region_instances of this IncreMstpRegion.
        生成树实例集合。

        :param mstp_region_instances: The mstp_region_instances of this IncreMstpRegion.
        :type: list[IncreMstpRegionInstance]
        """

        self._mstp_region_instances = mstp_region_instances

    @property
    def region_device_list(self):
        """
        Gets the region_device_list of this IncreMstpRegion.
        设备ID实例集合。

        :return: The region_device_list of this IncreMstpRegion.
        :rtype: list[str]
        """
        return self._region_device_list

    @region_device_list.setter
    def region_device_list(self, region_device_list):
        """
        Sets the region_device_list of this IncreMstpRegion.
        设备ID实例集合。

        :param region_device_list: The region_device_list of this IncreMstpRegion.
        :type: list[str]
        """

        self._region_device_list = region_device_list

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
        if not isinstance(other, IncreMstpRegion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other