# coding: utf-8

"""
    TACACS模板管理

    TACACS模板配置北向接口，主要特性：  * 创建tacacs模板。 * 修改tacacs模板。 * 查询tacacs模板。 * 删除tacacs模板。 

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class EditTacacsTmplResponse(object):
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
        'errcode': 'str',
        'errmsg': 'str'
    }

    attribute_map = {
        'errcode': 'errcode',
        'errmsg': 'errmsg'
    }

    def __init__(self, errcode=None, errmsg=None):
        """
        EditTacacsTmplResponse - a model defined in Swagger
        """

        self._errcode = None
        self._errmsg = None

        if errcode is not None:
          self.errcode = errcode
        if errmsg is not None:
          self.errmsg = errmsg

    @property
    def errcode(self):
        """
        Gets the errcode of this EditTacacsTmplResponse.
        错误码。

        :return: The errcode of this EditTacacsTmplResponse.
        :rtype: str
        """
        return self._errcode

    @errcode.setter
    def errcode(self, errcode):
        """
        Sets the errcode of this EditTacacsTmplResponse.
        错误码。

        :param errcode: The errcode of this EditTacacsTmplResponse.
        :type: str
        """

        self._errcode = errcode

    @property
    def errmsg(self):
        """
        Gets the errmsg of this EditTacacsTmplResponse.
        错误信息。

        :return: The errmsg of this EditTacacsTmplResponse.
        :rtype: str
        """
        return self._errmsg

    @errmsg.setter
    def errmsg(self, errmsg):
        """
        Sets the errmsg of this EditTacacsTmplResponse.
        错误信息。

        :param errmsg: The errmsg of this EditTacacsTmplResponse.
        :type: str
        """

        self._errmsg = errmsg

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
        if not isinstance(other, EditTacacsTmplResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
