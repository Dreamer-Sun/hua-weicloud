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


class QuerySitesOutData(object):
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
        'tenant_id': 'str',
        'name': 'str',
        'description': 'str',
        'type': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'tenant_id': 'tenantId',
        'name': 'name',
        'description': 'description',
        'type': 'type'
    }

    def __init__(self, id=None, tenant_id=None, name=None, description=None, type=None):
        """
        QuerySitesOutData - a model defined in Swagger
        """

        self._id = None
        self._tenant_id = None
        self._name = None
        self._description = None
        self._type = None

        if id is not None:
          self.id = id
        if tenant_id is not None:
          self.tenant_id = tenant_id
        if name is not None:
          self.name = name
        if description is not None:
          self.description = description
        if type is not None:
          self.type = type

    @property
    def id(self):
        """
        Gets the id of this QuerySitesOutData.
        站点ID。

        :return: The id of this QuerySitesOutData.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this QuerySitesOutData.
        站点ID。

        :param id: The id of this QuerySitesOutData.
        :type: str
        """

        self._id = id

    @property
    def tenant_id(self):
        """
        Gets the tenant_id of this QuerySitesOutData.
        租户ID。

        :return: The tenant_id of this QuerySitesOutData.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """
        Sets the tenant_id of this QuerySitesOutData.
        租户ID。

        :param tenant_id: The tenant_id of this QuerySitesOutData.
        :type: str
        """

        self._tenant_id = tenant_id

    @property
    def name(self):
        """
        Gets the name of this QuerySitesOutData.
        站点名称。

        :return: The name of this QuerySitesOutData.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this QuerySitesOutData.
        站点名称。

        :param name: The name of this QuerySitesOutData.
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this QuerySitesOutData.
        站点描述。

        :return: The description of this QuerySitesOutData.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this QuerySitesOutData.
        站点描述。

        :param description: The description of this QuerySitesOutData.
        :type: str
        """

        self._description = description

    @property
    def type(self):
        """
        Gets the type of this QuerySitesOutData.
        站点类型。

        :return: The type of this QuerySitesOutData.
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this QuerySitesOutData.
        站点类型。

        :param type: The type of this QuerySitesOutData.
        :type: list[str]
        """

        self._type = type

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
        if not isinstance(other, QuerySitesOutData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other