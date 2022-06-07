# coding: utf-8

"""
    用户流量信息查询

    控制器支持查询指定时间内流量和时长发生变化的用户流量信息分页查询北向接口。 

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class TimeFlowStInfosOutputDto(object):
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
        'data': 'list[TimeFlowStDetailInfosOutputDto]'
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
        TimeFlowStInfosOutputDto - a model defined in Swagger
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
        Gets the page_index of this TimeFlowStInfosOutputDto.
        当前页数。

        :return: The page_index of this TimeFlowStInfosOutputDto.
        :rtype: int
        """
        return self._page_index

    @page_index.setter
    def page_index(self, page_index):
        """
        Sets the page_index of this TimeFlowStInfosOutputDto.
        当前页数。

        :param page_index: The page_index of this TimeFlowStInfosOutputDto.
        :type: int
        """
        if page_index is not None and page_index > 2147483647:
            raise ValueError("Invalid value for `page_index`, must be a value less than or equal to `2147483647`")
        if page_index is not None and page_index < 0:
            raise ValueError("Invalid value for `page_index`, must be a value greater than or equal to `0`")

        self._page_index = page_index

    @property
    def page_size(self):
        """
        Gets the page_size of this TimeFlowStInfosOutputDto.
        每页最大显示数量。

        :return: The page_size of this TimeFlowStInfosOutputDto.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """
        Sets the page_size of this TimeFlowStInfosOutputDto.
        每页最大显示数量。

        :param page_size: The page_size of this TimeFlowStInfosOutputDto.
        :type: int
        """
        if page_size is not None and page_size > 1000:
            raise ValueError("Invalid value for `page_size`, must be a value less than or equal to `1000`")
        if page_size is not None and page_size < 0:
            raise ValueError("Invalid value for `page_size`, must be a value greater than or equal to `0`")

        self._page_size = page_size

    @property
    def total_records(self):
        """
        Gets the total_records of this TimeFlowStInfosOutputDto.
        查询到的总结果数。

        :return: The total_records of this TimeFlowStInfosOutputDto.
        :rtype: int
        """
        return self._total_records

    @total_records.setter
    def total_records(self, total_records):
        """
        Sets the total_records of this TimeFlowStInfosOutputDto.
        查询到的总结果数。

        :param total_records: The total_records of this TimeFlowStInfosOutputDto.
        :type: int
        """
        if total_records is not None and total_records > 2147483647:
            raise ValueError("Invalid value for `total_records`, must be a value less than or equal to `2147483647`")
        if total_records is not None and total_records < 0:
            raise ValueError("Invalid value for `total_records`, must be a value greater than or equal to `0`")

        self._total_records = total_records

    @property
    def errcode(self):
        """
        Gets the errcode of this TimeFlowStInfosOutputDto.
        错误码。

        :return: The errcode of this TimeFlowStInfosOutputDto.
        :rtype: str
        """
        return self._errcode

    @errcode.setter
    def errcode(self, errcode):
        """
        Sets the errcode of this TimeFlowStInfosOutputDto.
        错误码。

        :param errcode: The errcode of this TimeFlowStInfosOutputDto.
        :type: str
        """

        self._errcode = errcode

    @property
    def errmsg(self):
        """
        Gets the errmsg of this TimeFlowStInfosOutputDto.
        错误信息描述。

        :return: The errmsg of this TimeFlowStInfosOutputDto.
        :rtype: str
        """
        return self._errmsg

    @errmsg.setter
    def errmsg(self, errmsg):
        """
        Sets the errmsg of this TimeFlowStInfosOutputDto.
        错误信息描述。

        :param errmsg: The errmsg of this TimeFlowStInfosOutputDto.
        :type: str
        """

        self._errmsg = errmsg

    @property
    def data(self):
        """
        Gets the data of this TimeFlowStInfosOutputDto.

        :return: The data of this TimeFlowStInfosOutputDto.
        :rtype: list[TimeFlowStDetailInfosOutputDto]
        """
        return self._data

    @data.setter
    def data(self, data):
        """
        Sets the data of this TimeFlowStInfosOutputDto.

        :param data: The data of this TimeFlowStInfosOutputDto.
        :type: list[TimeFlowStDetailInfosOutputDto]
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
        if not isinstance(other, TimeFlowStInfosOutputDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other