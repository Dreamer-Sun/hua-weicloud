# coding: utf-8

"""
    设备基本信息管理

    设备相关操作接口。 场景：对设备增删改查操作的第三方接口。

    OpenAPI spec version: 1.6.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class CommonResponseBean(object):
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
        CommonResponseBean - a model defined in Swagger
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
        Gets the errcode of this CommonResponseBean.
        错误码：当没有错误时返回0。

        :return: The errcode of this CommonResponseBean.
        :rtype: str
        """
        return self._errcode

    @errcode.setter
    def errcode(self, errcode):
        """
        Sets the errcode of this CommonResponseBean.
        错误码：当没有错误时返回0。

        :param errcode: The errcode of this CommonResponseBean.
        :type: str
        """

        self._errcode = errcode

    @property
    def errmsg(self):
        """
        Gets the errmsg of this CommonResponseBean.
        接口调用结果的描述信息。

        :return: The errmsg of this CommonResponseBean.
        :rtype: str
        """
        return self._errmsg

    @errmsg.setter
    def errmsg(self, errmsg):
        """
        Sets the errmsg of this CommonResponseBean.
        接口调用结果的描述信息。

        :param errmsg: The errmsg of this CommonResponseBean.
        :type: str
        """
        if errmsg is not None and len(errmsg) > 256:
            raise ValueError("Invalid value for `errmsg`, length must be less than or equal to `256`")

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
        if not isinstance(other, CommonResponseBean):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
