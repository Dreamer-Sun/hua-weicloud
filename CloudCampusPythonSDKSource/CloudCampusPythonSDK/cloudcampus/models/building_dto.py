# coding: utf-8

"""
    室内地图信息查询

    室内地图第三方北向接口。 · 查询站点中所有楼栋基本信息 · 查询楼栋中所有楼层基本信息 · 查询楼栋中所有楼层详细信息 · 查询楼栋中楼层和设备布放信息 · 查询楼栋中楼层已布放设备详细信息 · 查询楼层已布放设备位置信息 

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class BuildingDto(object):
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
        'floor_list': 'list[FloorDto]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'floor_list': 'floorList'
    }

    def __init__(self, id=None, name=None, floor_list=None):
        """
        BuildingDto - a model defined in Swagger
        """

        self._id = None
        self._name = None
        self._floor_list = None

        if id is not None:
          self.id = id
        if name is not None:
          self.name = name
        if floor_list is not None:
          self.floor_list = floor_list

    @property
    def id(self):
        """
        Gets the id of this BuildingDto.
        楼栋ID，格式UUID。

        :return: The id of this BuildingDto.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this BuildingDto.
        楼栋ID，格式UUID。

        :param id: The id of this BuildingDto.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this BuildingDto.
        楼栋名称。

        :return: The name of this BuildingDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this BuildingDto.
        楼栋名称。

        :param name: The name of this BuildingDto.
        :type: str
        """

        self._name = name

    @property
    def floor_list(self):
        """
        Gets the floor_list of this BuildingDto.
        楼层列表。

        :return: The floor_list of this BuildingDto.
        :rtype: list[FloorDto]
        """
        return self._floor_list

    @floor_list.setter
    def floor_list(self, floor_list):
        """
        Sets the floor_list of this BuildingDto.
        楼层列表。

        :param floor_list: The floor_list of this BuildingDto.
        :type: list[FloorDto]
        """

        self._floor_list = floor_list

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
        if not isinstance(other, BuildingDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
