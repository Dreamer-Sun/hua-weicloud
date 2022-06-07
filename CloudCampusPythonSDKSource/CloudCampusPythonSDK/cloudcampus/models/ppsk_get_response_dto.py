# coding: utf-8

"""
    PPSK帐号配置

    PPSK帐号管理北向接口，主要包括： · 创建PPSK帐号 · 修改PPSK帐号 · 删除PPSK帐号 · 查询PPSK帐号 

    OpenAPI spec version: 1.1.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class PpskGetResponseDto(object):
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
        'totalrecords': 'int',
        'data': 'list[PPSKResponseDto]'
    }

    attribute_map = {
        'errcode': 'errcode',
        'errmsg': 'errmsg',
        'totalrecords': 'totalrecords',
        'data': 'data'
    }

    def __init__(self, errcode=None, errmsg=None, totalrecords=None, data=None):
        """
        PpskGetResponseDto - a model defined in Swagger
        """

        self._errcode = None
        self._errmsg = None
        self._totalrecords = None
        self._data = None

        if errcode is not None:
          self.errcode = errcode
        if errmsg is not None:
          self.errmsg = errmsg
        if totalrecords is not None:
          self.totalrecords = totalrecords
        if data is not None:
          self.data = data

    @property
    def errcode(self):
        """
        Gets the errcode of this PpskGetResponseDto.
        错误码，错误码为0表示操作成功。

        :return: The errcode of this PpskGetResponseDto.
        :rtype: str
        """
        return self._errcode

    @errcode.setter
    def errcode(self, errcode):
        """
        Sets the errcode of this PpskGetResponseDto.
        错误码，错误码为0表示操作成功。

        :param errcode: The errcode of this PpskGetResponseDto.
        :type: str
        """

        self._errcode = errcode

    @property
    def errmsg(self):
        """
        Gets the errmsg of this PpskGetResponseDto.
        错误信息。

        :return: The errmsg of this PpskGetResponseDto.
        :rtype: str
        """
        return self._errmsg

    @errmsg.setter
    def errmsg(self, errmsg):
        """
        Sets the errmsg of this PpskGetResponseDto.
        错误信息。

        :param errmsg: The errmsg of this PpskGetResponseDto.
        :type: str
        """

        self._errmsg = errmsg

    @property
    def totalrecords(self):
        """
        Gets the totalrecords of this PpskGetResponseDto.
        总记录数。

        :return: The totalrecords of this PpskGetResponseDto.
        :rtype: int
        """
        return self._totalrecords

    @totalrecords.setter
    def totalrecords(self, totalrecords):
        """
        Sets the totalrecords of this PpskGetResponseDto.
        总记录数。

        :param totalrecords: The totalrecords of this PpskGetResponseDto.
        :type: int
        """

        self._totalrecords = totalrecords

    @property
    def data(self):
        """
        Gets the data of this PpskGetResponseDto.
        PSK帐号数据列表。

        :return: The data of this PpskGetResponseDto.
        :rtype: list[PPSKResponseDto]
        """
        return self._data

    @data.setter
    def data(self, data):
        """
        Sets the data of this PpskGetResponseDto.
        PSK帐号数据列表。

        :param data: The data of this PpskGetResponseDto.
        :type: list[PPSKResponseDto]
        """

        self._data = data

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
        if not isinstance(other, PpskGetResponseDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other