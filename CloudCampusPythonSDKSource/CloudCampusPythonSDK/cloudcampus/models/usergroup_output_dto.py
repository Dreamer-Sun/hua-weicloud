# coding: utf-8

"""
    用户组管理

    用户组管理开放API。 

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class UsergroupOutputDto(object):
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
        'description': 'str',
        'full_path_name': 'str',
        'bsid': 'str',
        'parent_id': 'str',
        'name': 'str',
        'address': 'str',
        'postal_code': 'str',
        'admin_email': 'str',
        'order_id': 'int'
    }

    attribute_map = {
        'id': 'id',
        'description': 'description',
        'full_path_name': 'fullPathName',
        'bsid': 'bsid',
        'parent_id': 'parentId',
        'name': 'name',
        'address': 'address',
        'postal_code': 'postalCode',
        'admin_email': 'adminEmail',
        'order_id': 'orderId'
    }

    def __init__(self, id=None, description=None, full_path_name=None, bsid=None, parent_id=None, name=None, address=None, postal_code=None, admin_email=None, order_id=None):
        """
        UsergroupOutputDto - a model defined in Swagger
        """

        self._id = None
        self._description = None
        self._full_path_name = None
        self._bsid = None
        self._parent_id = None
        self._name = None
        self._address = None
        self._postal_code = None
        self._admin_email = None
        self._order_id = None

        if id is not None:
          self.id = id
        if description is not None:
          self.description = description
        if full_path_name is not None:
          self.full_path_name = full_path_name
        if bsid is not None:
          self.bsid = bsid
        if parent_id is not None:
          self.parent_id = parent_id
        if name is not None:
          self.name = name
        if address is not None:
          self.address = address
        if postal_code is not None:
          self.postal_code = postal_code
        if admin_email is not None:
          self.admin_email = admin_email
        if order_id is not None:
          self.order_id = order_id

    @property
    def id(self):
        """
        Gets the id of this UsergroupOutputDto.
        用户组ID，UUID格式。

        :return: The id of this UsergroupOutputDto.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this UsergroupOutputDto.
        用户组ID，UUID格式。

        :param id: The id of this UsergroupOutputDto.
        :type: str
        """

        self._id = id

    @property
    def description(self):
        """
        Gets the description of this UsergroupOutputDto.
        用户组描述。

        :return: The description of this UsergroupOutputDto.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UsergroupOutputDto.
        用户组描述。

        :param description: The description of this UsergroupOutputDto.
        :type: str
        """

        self._description = description

    @property
    def full_path_name(self):
        """
        Gets the full_path_name of this UsergroupOutputDto.
        用户组全路径。

        :return: The full_path_name of this UsergroupOutputDto.
        :rtype: str
        """
        return self._full_path_name

    @full_path_name.setter
    def full_path_name(self, full_path_name):
        """
        Sets the full_path_name of this UsergroupOutputDto.
        用户组全路径。

        :param full_path_name: The full_path_name of this UsergroupOutputDto.
        :type: str
        """

        self._full_path_name = full_path_name

    @property
    def bsid(self):
        """
        Gets the bsid of this UsergroupOutputDto.
        用户组层级关系，UUID格式。

        :return: The bsid of this UsergroupOutputDto.
        :rtype: str
        """
        return self._bsid

    @bsid.setter
    def bsid(self, bsid):
        """
        Sets the bsid of this UsergroupOutputDto.
        用户组层级关系，UUID格式。

        :param bsid: The bsid of this UsergroupOutputDto.
        :type: str
        """

        self._bsid = bsid

    @property
    def parent_id(self):
        """
        Gets the parent_id of this UsergroupOutputDto.
        父用户组ID，UUID格式。

        :return: The parent_id of this UsergroupOutputDto.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """
        Sets the parent_id of this UsergroupOutputDto.
        父用户组ID，UUID格式。

        :param parent_id: The parent_id of this UsergroupOutputDto.
        :type: str
        """

        self._parent_id = parent_id

    @property
    def name(self):
        """
        Gets the name of this UsergroupOutputDto.
        用户组名。

        :return: The name of this UsergroupOutputDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this UsergroupOutputDto.
        用户组名。

        :param name: The name of this UsergroupOutputDto.
        :type: str
        """

        self._name = name

    @property
    def address(self):
        """
        Gets the address of this UsergroupOutputDto.
        地址。

        :return: The address of this UsergroupOutputDto.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets the address of this UsergroupOutputDto.
        地址。

        :param address: The address of this UsergroupOutputDto.
        :type: str
        """

        self._address = address

    @property
    def postal_code(self):
        """
        Gets the postal_code of this UsergroupOutputDto.
        邮编。

        :return: The postal_code of this UsergroupOutputDto.
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """
        Sets the postal_code of this UsergroupOutputDto.
        邮编。

        :param postal_code: The postal_code of this UsergroupOutputDto.
        :type: str
        """

        self._postal_code = postal_code

    @property
    def admin_email(self):
        """
        Gets the admin_email of this UsergroupOutputDto.
        管理员邮箱。

        :return: The admin_email of this UsergroupOutputDto.
        :rtype: str
        """
        return self._admin_email

    @admin_email.setter
    def admin_email(self, admin_email):
        """
        Sets the admin_email of this UsergroupOutputDto.
        管理员邮箱。

        :param admin_email: The admin_email of this UsergroupOutputDto.
        :type: str
        """

        self._admin_email = admin_email

    @property
    def order_id(self):
        """
        Gets the order_id of this UsergroupOutputDto.
        用于同一级用户组排序。

        :return: The order_id of this UsergroupOutputDto.
        :rtype: int
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """
        Sets the order_id of this UsergroupOutputDto.
        用于同一级用户组排序。

        :param order_id: The order_id of this UsergroupOutputDto.
        :type: int
        """

        self._order_id = order_id

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
        if not isinstance(other, UsergroupOutputDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other