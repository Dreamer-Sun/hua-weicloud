# coding: utf-8

"""
    单板管理

    单板管理第三方接口。

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class BoardDeleteDto(object):
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
        'ids': 'list[str]'
    }

    attribute_map = {
        'ids': 'ids'
    }

    def __init__(self, ids=None):
        """
        BoardDeleteDto - a model defined in Swagger
        """

        self._ids = None

        if ids is not None:
          self.ids = ids

    @property
    def ids(self):
        """
        Gets the ids of this BoardDeleteDto.
        待删除的单板列表。

        :return: The ids of this BoardDeleteDto.
        :rtype: list[str]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        """
        Sets the ids of this BoardDeleteDto.
        待删除的单板列表。

        :param ids: The ids of this BoardDeleteDto.
        :type: list[str]
        """

        self._ids = ids

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
        if not isinstance(other, BoardDeleteDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
