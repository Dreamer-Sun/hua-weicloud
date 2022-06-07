# coding: utf-8

"""
    控制器支持第三方系统通过API接口获取用户上下线信息

    控制器支持第三方系统通过API接口获取用户上下线信息 

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class AuthenticationLogOutputDto(object):
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
        'start_row_key': 'str',
        'end_row_key': 'str',
        'total_records': 'int',
        'errcode': 'str',
        'errmsg': 'str',
        'search_result_list': 'list[AuthenticationLogDetailOutputDto]'
    }

    attribute_map = {
        'start_row_key': 'startRowKey',
        'end_row_key': 'endRowKey',
        'total_records': 'totalRecords',
        'errcode': 'errcode',
        'errmsg': 'errmsg',
        'search_result_list': 'searchResultList'
    }

    def __init__(self, start_row_key=None, end_row_key=None, total_records=None, errcode=None, errmsg=None, search_result_list=None):
        """
        AuthenticationLogOutputDto - a model defined in Swagger
        """

        self._start_row_key = None
        self._end_row_key = None
        self._total_records = None
        self._errcode = None
        self._errmsg = None
        self._search_result_list = None

        if start_row_key is not None:
          self.start_row_key = start_row_key
        if end_row_key is not None:
          self.end_row_key = end_row_key
        if total_records is not None:
          self.total_records = total_records
        if errcode is not None:
          self.errcode = errcode
        if errmsg is not None:
          self.errmsg = errmsg
        if search_result_list is not None:
          self.search_result_list = search_result_list

    @property
    def start_row_key(self):
        """
        Gets the start_row_key of this AuthenticationLogOutputDto.
        查询结果中起始rowkey值。

        :return: The start_row_key of this AuthenticationLogOutputDto.
        :rtype: str
        """
        return self._start_row_key

    @start_row_key.setter
    def start_row_key(self, start_row_key):
        """
        Sets the start_row_key of this AuthenticationLogOutputDto.
        查询结果中起始rowkey值。

        :param start_row_key: The start_row_key of this AuthenticationLogOutputDto.
        :type: str
        """
        if start_row_key is not None and len(start_row_key) > 256:
            raise ValueError("Invalid value for `start_row_key`, length must be less than or equal to `256`")
        if start_row_key is not None and len(start_row_key) < 0:
            raise ValueError("Invalid value for `start_row_key`, length must be greater than or equal to `0`")

        self._start_row_key = start_row_key

    @property
    def end_row_key(self):
        """
        Gets the end_row_key of this AuthenticationLogOutputDto.
        查询结果中结束rowkey值。

        :return: The end_row_key of this AuthenticationLogOutputDto.
        :rtype: str
        """
        return self._end_row_key

    @end_row_key.setter
    def end_row_key(self, end_row_key):
        """
        Sets the end_row_key of this AuthenticationLogOutputDto.
        查询结果中结束rowkey值。

        :param end_row_key: The end_row_key of this AuthenticationLogOutputDto.
        :type: str
        """
        if end_row_key is not None and len(end_row_key) > 256:
            raise ValueError("Invalid value for `end_row_key`, length must be less than or equal to `256`")
        if end_row_key is not None and len(end_row_key) < 0:
            raise ValueError("Invalid value for `end_row_key`, length must be greater than or equal to `0`")

        self._end_row_key = end_row_key

    @property
    def total_records(self):
        """
        Gets the total_records of this AuthenticationLogOutputDto.
        本次查询到的总结果数。最大取值为101，不足101条时表示当前数据已查询完；等于101条表示后续还有数据。

        :return: The total_records of this AuthenticationLogOutputDto.
        :rtype: int
        """
        return self._total_records

    @total_records.setter
    def total_records(self, total_records):
        """
        Sets the total_records of this AuthenticationLogOutputDto.
        本次查询到的总结果数。最大取值为101，不足101条时表示当前数据已查询完；等于101条表示后续还有数据。

        :param total_records: The total_records of this AuthenticationLogOutputDto.
        :type: int
        """
        if total_records is not None and total_records > 101:
            raise ValueError("Invalid value for `total_records`, must be a value less than or equal to `101`")
        if total_records is not None and total_records < 0:
            raise ValueError("Invalid value for `total_records`, must be a value greater than or equal to `0`")

        self._total_records = total_records

    @property
    def errcode(self):
        """
        Gets the errcode of this AuthenticationLogOutputDto.
        错误码。0表示没有错误。

        :return: The errcode of this AuthenticationLogOutputDto.
        :rtype: str
        """
        return self._errcode

    @errcode.setter
    def errcode(self, errcode):
        """
        Sets the errcode of this AuthenticationLogOutputDto.
        错误码。0表示没有错误。

        :param errcode: The errcode of this AuthenticationLogOutputDto.
        :type: str
        """
        if errcode is not None and len(errcode) > 32:
            raise ValueError("Invalid value for `errcode`, length must be less than or equal to `32`")
        if errcode is not None and len(errcode) < 0:
            raise ValueError("Invalid value for `errcode`, length must be greater than or equal to `0`")

        self._errcode = errcode

    @property
    def errmsg(self):
        """
        Gets the errmsg of this AuthenticationLogOutputDto.
        错误信息描述。

        :return: The errmsg of this AuthenticationLogOutputDto.
        :rtype: str
        """
        return self._errmsg

    @errmsg.setter
    def errmsg(self, errmsg):
        """
        Sets the errmsg of this AuthenticationLogOutputDto.
        错误信息描述。

        :param errmsg: The errmsg of this AuthenticationLogOutputDto.
        :type: str
        """
        if errmsg is not None and len(errmsg) > 512:
            raise ValueError("Invalid value for `errmsg`, length must be less than or equal to `512`")
        if errmsg is not None and len(errmsg) < 0:
            raise ValueError("Invalid value for `errmsg`, length must be greater than or equal to `0`")

        self._errmsg = errmsg

    @property
    def search_result_list(self):
        """
        Gets the search_result_list of this AuthenticationLogOutputDto.

        :return: The search_result_list of this AuthenticationLogOutputDto.
        :rtype: list[AuthenticationLogDetailOutputDto]
        """
        return self._search_result_list

    @search_result_list.setter
    def search_result_list(self, search_result_list):
        """
        Sets the search_result_list of this AuthenticationLogOutputDto.

        :param search_result_list: The search_result_list of this AuthenticationLogOutputDto.
        :type: list[AuthenticationLogDetailOutputDto]
        """

        self._search_result_list = search_result_list

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
        if not isinstance(other, AuthenticationLogOutputDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
