# coding: utf-8

"""
    License管理

    公有云license管理接口。 场景：对租户license操作的第三方接口。 

    OpenAPI spec version: 1.0.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ImportActiveCodeOutData(object):
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
        'code': 'str',
        'result_code': 'int',
        'detail': 'str'
    }

    attribute_map = {
        'code': 'code',
        'result_code': 'resultCode',
        'detail': 'detail'
    }

    def __init__(self, code=None, result_code=None, detail=None):
        """
        ImportActiveCodeOutData - a model defined in Swagger
        """

        self._code = None
        self._result_code = None
        self._detail = None

        if code is not None:
          self.code = code
        if result_code is not None:
          self.result_code = result_code
        if detail is not None:
          self.detail = detail

    @property
    def code(self):
        """
        Gets the code of this ImportActiveCodeOutData.
        激活码。

        :return: The code of this ImportActiveCodeOutData.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this ImportActiveCodeOutData.
        激活码。

        :param code: The code of this ImportActiveCodeOutData.
        :type: str
        """

        self._code = code

    @property
    def result_code(self):
        """
        Gets the result_code of this ImportActiveCodeOutData.
        导入结果。0---成功；1---失败。

        :return: The result_code of this ImportActiveCodeOutData.
        :rtype: int
        """
        return self._result_code

    @result_code.setter
    def result_code(self, result_code):
        """
        Sets the result_code of this ImportActiveCodeOutData.
        导入结果。0---成功；1---失败。

        :param result_code: The result_code of this ImportActiveCodeOutData.
        :type: int
        """

        self._result_code = result_code

    @property
    def detail(self):
        """
        Gets the detail of this ImportActiveCodeOutData.
        导入结果详情。

        :return: The detail of this ImportActiveCodeOutData.
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """
        Sets the detail of this ImportActiveCodeOutData.
        导入结果详情。

        :param detail: The detail of this ImportActiveCodeOutData.
        :type: str
        """

        self._detail = detail

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
        if not isinstance(other, ImportActiveCodeOutData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
