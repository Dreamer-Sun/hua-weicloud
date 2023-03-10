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


class DelMstpRegion(object):
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
        'mstp_region_instances': 'list[DelMstpRegionInstance]',
        'region_device_list': 'list[str]'
    }

    attribute_map = {
        'region_id': 'regionId',
        'mstp_region_instances': 'mstpRegionInstances',
        'region_device_list': 'regionDeviceList'
    }

    def __init__(self, region_id=None, mstp_region_instances=None, region_device_list=None):
        """
        DelMstpRegion - a model defined in Swagger
        """

        self._region_id = None
        self._mstp_region_instances = None
        self._region_device_list = None

        if region_id is not None:
          self.region_id = region_id
        if mstp_region_instances is not None:
          self.mstp_region_instances = mstp_region_instances
        if region_device_list is not None:
          self.region_device_list = region_device_list

    @property
    def region_id(self):
        """
        Gets the region_id of this DelMstpRegion.
        域ID。

        :return: The region_id of this DelMstpRegion.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """
        Sets the region_id of this DelMstpRegion.
        域ID。

        :param region_id: The region_id of this DelMstpRegion.
        :type: str
        """

        self._region_id = region_id

    @property
    def mstp_region_instances(self):
        """
        Gets the mstp_region_instances of this DelMstpRegion.
        生成树实例集合。

        :return: The mstp_region_instances of this DelMstpRegion.
        :rtype: list[DelMstpRegionInstance]
        """
        return self._mstp_region_instances

    @mstp_region_instances.setter
    def mstp_region_instances(self, mstp_region_instances):
        """
        Sets the mstp_region_instances of this DelMstpRegion.
        生成树实例集合。

        :param mstp_region_instances: The mstp_region_instances of this DelMstpRegion.
        :type: list[DelMstpRegionInstance]
        """

        self._mstp_region_instances = mstp_region_instances

    @property
    def region_device_list(self):
        """
        Gets the region_device_list of this DelMstpRegion.
        设备ID实例集合。

        :return: The region_device_list of this DelMstpRegion.
        :rtype: list[str]
        """
        return self._region_device_list

    @region_device_list.setter
    def region_device_list(self, region_device_list):
        """
        Sets the region_device_list of this DelMstpRegion.
        设备ID实例集合。

        :param region_device_list: The region_device_list of this DelMstpRegion.
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
        if not isinstance(other, DelMstpRegion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
