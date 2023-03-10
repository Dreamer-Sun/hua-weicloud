# coding: utf-8

"""
    站点管理

    站点管理第三方接口。 场景：对站点增删改查操作的第三方接口。

    OpenAPI spec version: 1.3.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class CreateSiteDto(object):
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
        'sites': 'list[CreateSiteDtoData]'
    }

    attribute_map = {
        'sites': 'sites'
    }

    def __init__(self, sites=None):
        """
        CreateSiteDto - a model defined in Swagger
        """

        self._sites = None

        if sites is not None:
          self.sites = sites

    @property
    def sites(self):
        """
        Gets the sites of this CreateSiteDto.
        站点信息。

        :return: The sites of this CreateSiteDto.
        :rtype: list[CreateSiteDtoData]
        """
        return self._sites

    @sites.setter
    def sites(self, sites):
        """
        Sets the sites of this CreateSiteDto.
        站点信息。

        :param sites: The sites of this CreateSiteDto.
        :type: list[CreateSiteDtoData]
        """

        self._sites = sites

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
        if not isinstance(other, CreateSiteDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
