# coding: utf-8

"""
    拓扑管理

    拓扑管理第三方北向接口。 1、查询LACP LAG信息 2、查询LLDP信息 

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class NeighborsInfoResultDtoData(object):
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
        'lldp': 'list[NeighborsInfoDto]'
    }

    attribute_map = {
        'lldp': 'lldp'
    }

    def __init__(self, lldp=None):
        """
        NeighborsInfoResultDtoData - a model defined in Swagger
        """

        self._lldp = None

        if lldp is not None:
          self.lldp = lldp

    @property
    def lldp(self):
        """
        Gets the lldp of this NeighborsInfoResultDtoData.
        LLDP数据。

        :return: The lldp of this NeighborsInfoResultDtoData.
        :rtype: list[NeighborsInfoDto]
        """
        return self._lldp

    @lldp.setter
    def lldp(self, lldp):
        """
        Sets the lldp of this NeighborsInfoResultDtoData.
        LLDP数据。

        :param lldp: The lldp of this NeighborsInfoResultDtoData.
        :type: list[NeighborsInfoDto]
        """

        self._lldp = lldp

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
        if not isinstance(other, NeighborsInfoResultDtoData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
