# coding: utf-8

"""
    射频管理国家码查询

    射频管理国家码第三方北向接口。     

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class RadioCountryChannelResult(object):
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
        'page_index': 'int',
        'page_size': 'int',
        'total_records': 'int',
        'errcode': 'str',
        'errmsg': 'str',
        'data': 'list[RadioCountryChannelDto]'
    }

    attribute_map = {
        'page_index': 'pageIndex',
        'page_size': 'pageSize',
        'total_records': 'totalRecords',
        'errcode': 'errcode',
        'errmsg': 'errmsg',
        'data': 'data'
    }

    def __init__(self, page_index=None, page_size=None, total_records=None, errcode=None, errmsg=None, data=None):
        """
        RadioCountryChannelResult - a model defined in Swagger
        """

        self._page_index = None
        self._page_size = None
        self._total_records = None
        self._errcode = None
        self._errmsg = None
        self._data = None

        if page_index is not None:
          self.page_index = page_index
        if page_size is not None:
          self.page_size = page_size
        if total_records is not None:
          self.total_records = total_records
        if errcode is not None:
          self.errcode = errcode
        if errmsg is not None:
          self.errmsg = errmsg
        if data is not None:
          self.data = data

    @property
    def page_index(self):
        """
        Gets the page_index of this RadioCountryChannelResult.
        当前字段不支持，返回null。

        :return: The page_index of this RadioCountryChannelResult.
        :rtype: int
        """
        return self._page_index

    @page_index.setter
    def page_index(self, page_index):
        """
        Sets the page_index of this RadioCountryChannelResult.
        当前字段不支持，返回null。

        :param page_index: The page_index of this RadioCountryChannelResult.
        :type: int
        """

        self._page_index = page_index

    @property
    def page_size(self):
        """
        Gets the page_size of this RadioCountryChannelResult.
        当前字段不支持，返回null。

        :return: The page_size of this RadioCountryChannelResult.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """
        Sets the page_size of this RadioCountryChannelResult.
        当前字段不支持，返回null。

        :param page_size: The page_size of this RadioCountryChannelResult.
        :type: int
        """
        if page_size is not None and page_size > 100:
            raise ValueError("Invalid value for `page_size`, must be a value less than or equal to `100`")
        if page_size is not None and page_size < 0:
            raise ValueError("Invalid value for `page_size`, must be a value greater than or equal to `0`")

        self._page_size = page_size

    @property
    def total_records(self):
        """
        Gets the total_records of this RadioCountryChannelResult.
        当前字段不支持，返回null。

        :return: The total_records of this RadioCountryChannelResult.
        :rtype: int
        """
        return self._total_records

    @total_records.setter
    def total_records(self, total_records):
        """
        Sets the total_records of this RadioCountryChannelResult.
        当前字段不支持，返回null。

        :param total_records: The total_records of this RadioCountryChannelResult.
        :type: int
        """

        self._total_records = total_records

    @property
    def errcode(self):
        """
        Gets the errcode of this RadioCountryChannelResult.
        错误码。

        :return: The errcode of this RadioCountryChannelResult.
        :rtype: str
        """
        return self._errcode

    @errcode.setter
    def errcode(self, errcode):
        """
        Sets the errcode of this RadioCountryChannelResult.
        错误码。

        :param errcode: The errcode of this RadioCountryChannelResult.
        :type: str
        """
        if errcode is not None and len(errcode) > 64:
            raise ValueError("Invalid value for `errcode`, length must be less than or equal to `64`")
        if errcode is not None and len(errcode) < 0:
            raise ValueError("Invalid value for `errcode`, length must be greater than or equal to `0`")

        self._errcode = errcode

    @property
    def errmsg(self):
        """
        Gets the errmsg of this RadioCountryChannelResult.
        错误信息。

        :return: The errmsg of this RadioCountryChannelResult.
        :rtype: str
        """
        return self._errmsg

    @errmsg.setter
    def errmsg(self, errmsg):
        """
        Sets the errmsg of this RadioCountryChannelResult.
        错误信息。

        :param errmsg: The errmsg of this RadioCountryChannelResult.
        :type: str
        """
        if errmsg is not None and len(errmsg) > 256:
            raise ValueError("Invalid value for `errmsg`, length must be less than or equal to `256`")
        if errmsg is not None and len(errmsg) < 0:
            raise ValueError("Invalid value for `errmsg`, length must be greater than or equal to `0`")

        self._errmsg = errmsg

    @property
    def data(self):
        """
        Gets the data of this RadioCountryChannelResult.
        国家码信息。

        :return: The data of this RadioCountryChannelResult.
        :rtype: list[RadioCountryChannelDto]
        """
        return self._data

    @data.setter
    def data(self, data):
        """
        Sets the data of this RadioCountryChannelResult.
        国家码信息。

        :param data: The data of this RadioCountryChannelResult.
        :type: list[RadioCountryChannelDto]
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
        if not isinstance(other, RadioCountryChannelResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
