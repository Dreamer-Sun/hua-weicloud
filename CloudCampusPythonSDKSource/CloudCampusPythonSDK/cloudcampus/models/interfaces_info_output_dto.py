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


class InterfacesInfoOutputDto(object):
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
        'interface_info_list': 'list[InterfaceInfoDto]'
    }

    attribute_map = {
        'interface_info_list': 'interfaceInfoList'
    }

    def __init__(self, interface_info_list=None):
        """
        InterfacesInfoOutputDto - a model defined in Swagger
        """

        self._interface_info_list = None

        if interface_info_list is not None:
          self.interface_info_list = interface_info_list

    @property
    def interface_info_list(self):
        """
        Gets the interface_info_list of this InterfacesInfoOutputDto.
        接口信息列表。

        :return: The interface_info_list of this InterfacesInfoOutputDto.
        :rtype: list[InterfaceInfoDto]
        """
        return self._interface_info_list

    @interface_info_list.setter
    def interface_info_list(self, interface_info_list):
        """
        Sets the interface_info_list of this InterfacesInfoOutputDto.
        接口信息列表。

        :param interface_info_list: The interface_info_list of this InterfacesInfoOutputDto.
        :type: list[InterfaceInfoDto]
        """

        self._interface_info_list = interface_info_list

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
        if not isinstance(other, InterfacesInfoOutputDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
