# coding: utf-8

"""
    RADIUS模板管理

    RADIUS模板配置第三方北向接口说明。 

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class DeleteRadiusTempResponseDto(object):
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
        'fail': 'list[DeleteRadiusTempResponseDtoFail]'
    }

    attribute_map = {
        'errcode': 'errcode',
        'errmsg': 'errmsg',
        'success': 'success',
        'fail': 'fail'
    }

    def __init__(self, errcode=None, errmsg=None, success=None, fail=None):
        """
        DeleteRadiusTempResponseDto - a model defined in Swagger
        """

        self._errcode = None
        self._errmsg = None
        self._success = None
        self._fail = None

        if errcode is not None:
          self.errcode = errcode
        if errmsg is not None:
          self.errmsg = errmsg
        if success is not None:
          self.success = success
        if fail is not None:
          self.fail = fail

    @property
    def errcode(self):
        """
        Gets the errcode of this DeleteRadiusTempResponseDto.
        错误码。

        :return: The errcode of this DeleteRadiusTempResponseDto.
        :rtype: str
        """
        return self._errcode

    @errcode.setter
    def errcode(self, errcode):
        """
        Sets the errcode of this DeleteRadiusTempResponseDto.
        错误码。

        :param errcode: The errcode of this DeleteRadiusTempResponseDto.
        :type: str
        """

        self._errcode = errcode

    @property
    def errmsg(self):
        """
        Gets the errmsg of this DeleteRadiusTempResponseDto.
        错误信息。

        :return: The errmsg of this DeleteRadiusTempResponseDto.
        :rtype: str
        """
        return self._errmsg

    @errmsg.setter
    def errmsg(self, errmsg):
        """
        Sets the errmsg of this DeleteRadiusTempResponseDto.
        错误信息。

        :param errmsg: The errmsg of this DeleteRadiusTempResponseDto.
        :type: str
        """

        self._errmsg = errmsg

    @property
    def success(self):
        """
        Gets the success of this DeleteRadiusTempResponseDto.
        删除成功的模板ID列表，每个元素为UUID格式。

        :return: The success of this DeleteRadiusTempResponseDto.
        :rtype: list[str]
        """
        return self._success

    @success.setter
    def success(self, success):
        """
        Sets the success of this DeleteRadiusTempResponseDto.
        删除成功的模板ID列表，每个元素为UUID格式。

        :param success: The success of this DeleteRadiusTempResponseDto.
        :type: list[str]
        """

        self._success = success

    @property
    def fail(self):
        """
        Gets the fail of this DeleteRadiusTempResponseDto.
        删除失败的模板ID列表结构。

        :return: The fail of this DeleteRadiusTempResponseDto.
        :rtype: list[DeleteRadiusTempResponseDtoFail]
        """
        return self._fail

    @fail.setter
    def fail(self, fail):
        """
        Sets the fail of this DeleteRadiusTempResponseDto.
        删除失败的模板ID列表结构。

        :param fail: The fail of this DeleteRadiusTempResponseDto.
        :type: list[DeleteRadiusTempResponseDtoFail]
        """

        self._fail = fail

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
        if not isinstance(other, DeleteRadiusTempResponseDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
