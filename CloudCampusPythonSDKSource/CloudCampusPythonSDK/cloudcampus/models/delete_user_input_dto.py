# coding: utf-8

"""
    用户管理

    用户管理第三方北向接口。 

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class DeleteUserInputDto(object):
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
        'all_user_ids': 'list[str]'
    }

    attribute_map = {
        'all_user_ids': 'allUserIds'
    }

    def __init__(self, all_user_ids=None):
        """
        DeleteUserInputDto - a model defined in Swagger
        """

        self._all_user_ids = None

        if all_user_ids is not None:
          self.all_user_ids = all_user_ids

    @property
    def all_user_ids(self):
        """
        Gets the all_user_ids of this DeleteUserInputDto.
        用户ID集合。

        :return: The all_user_ids of this DeleteUserInputDto.
        :rtype: list[str]
        """
        return self._all_user_ids

    @all_user_ids.setter
    def all_user_ids(self, all_user_ids):
        """
        Sets the all_user_ids of this DeleteUserInputDto.
        用户ID集合。

        :param all_user_ids: The all_user_ids of this DeleteUserInputDto.
        :type: list[str]
        """

        self._all_user_ids = all_user_ids

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
        if not isinstance(other, DeleteUserInputDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other