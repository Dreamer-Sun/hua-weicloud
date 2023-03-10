# coding: utf-8

"""
    Portal在线用户查询

    查询Portal在线用户第三方北向接口。提供了Portal在线用户的查询、强制下线接口。 

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class CutPortalOnlineUserOutputDto(object):
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
        'errmsg': 'str',
        'success': 'list[str]',
        'failure': 'list[CutPortalOnlineUserResultDto]'
    }

    attribute_map = {
        'errcode': 'errcode',
        'errmsg': 'errmsg',
        'success': 'success',
        'failure': 'failure'
    }

    def __init__(self, errcode=None, errmsg=None, success=None, failure=None):
        """
        CutPortalOnlineUserOutputDto - a model defined in Swagger
        """

        self._errcode = None
        self._errmsg = None
        self._success = None
        self._failure = None

        if errcode is not None:
          self.errcode = errcode
        if errmsg is not None:
          self.errmsg = errmsg
        if success is not None:
          self.success = success
        if failure is not None:
          self.failure = failure

    @property
    def errcode(self):
        """
        Gets the errcode of this CutPortalOnlineUserOutputDto.
        错误码。

        :return: The errcode of this CutPortalOnlineUserOutputDto.
        :rtype: str
        """
        return self._errcode

    @errcode.setter
    def errcode(self, errcode):
        """
        Sets the errcode of this CutPortalOnlineUserOutputDto.
        错误码。

        :param errcode: The errcode of this CutPortalOnlineUserOutputDto.
        :type: str
        """

        self._errcode = errcode

    @property
    def errmsg(self):
        """
        Gets the errmsg of this CutPortalOnlineUserOutputDto.
        错误信息。

        :return: The errmsg of this CutPortalOnlineUserOutputDto.
        :rtype: str
        """
        return self._errmsg

    @errmsg.setter
    def errmsg(self, errmsg):
        """
        Sets the errmsg of this CutPortalOnlineUserOutputDto.
        错误信息。

        :param errmsg: The errmsg of this CutPortalOnlineUserOutputDto.
        :type: str
        """

        self._errmsg = errmsg

    @property
    def success(self):
        """
        Gets the success of this CutPortalOnlineUserOutputDto.
        成功列表。

        :return: The success of this CutPortalOnlineUserOutputDto.
        :rtype: list[str]
        """
        return self._success

    @success.setter
    def success(self, success):
        """
        Sets the success of this CutPortalOnlineUserOutputDto.
        成功列表。

        :param success: The success of this CutPortalOnlineUserOutputDto.
        :type: list[str]
        """

        self._success = success

    @property
    def failure(self):
        """
        Gets the failure of this CutPortalOnlineUserOutputDto.
        失败列表。

        :return: The failure of this CutPortalOnlineUserOutputDto.
        :rtype: list[CutPortalOnlineUserResultDto]
        """
        return self._failure

    @failure.setter
    def failure(self, failure):
        """
        Sets the failure of this CutPortalOnlineUserOutputDto.
        失败列表。

        :param failure: The failure of this CutPortalOnlineUserOutputDto.
        :type: list[CutPortalOnlineUserResultDto]
        """

        self._failure = failure

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
        if not isinstance(other, CutPortalOnlineUserOutputDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
