# coding: utf-8

"""
    CIS服务接口

    CIS操作接口说明： 1、创建CIS隔离 2、创建CIS阻断 3、撤销CIS阻断/隔离 4、阻断隔离应用状态查询 5、CIS策略命中率查询 

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class QueryHitsResponseDTO(object):
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
        'start_date': 'str',
        'end_date': 'str',
        'hit_status': 'list[PolicyHitsListBuilder]'
    }

    attribute_map = {
        'start_date': 'startDate',
        'end_date': 'endDate',
        'hit_status': 'hitStatus'
    }

    def __init__(self, start_date=None, end_date=None, hit_status=None):
        """
        QueryHitsResponseDTO - a model defined in Swagger
        """

        self._start_date = None
        self._end_date = None
        self._hit_status = None

        if start_date is not None:
          self.start_date = start_date
        if end_date is not None:
          self.end_date = end_date
        if hit_status is not None:
          self.hit_status = hit_status

    @property
    def start_date(self):
        """
        Gets the start_date of this QueryHitsResponseDTO.
        开始日期，yyyy-MM-dd HH:mm:ss。

        :return: The start_date of this QueryHitsResponseDTO.
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """
        Sets the start_date of this QueryHitsResponseDTO.
        开始日期，yyyy-MM-dd HH:mm:ss。

        :param start_date: The start_date of this QueryHitsResponseDTO.
        :type: str
        """
        if start_date is not None and len(start_date) > 19:
            raise ValueError("Invalid value for `start_date`, length must be less than or equal to `19`")
        if start_date is not None and len(start_date) < 19:
            raise ValueError("Invalid value for `start_date`, length must be greater than or equal to `19`")

        self._start_date = start_date

    @property
    def end_date(self):
        """
        Gets the end_date of this QueryHitsResponseDTO.
        结束日期，yyyy-MM-dd HH:mm:ss。

        :return: The end_date of this QueryHitsResponseDTO.
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """
        Sets the end_date of this QueryHitsResponseDTO.
        结束日期，yyyy-MM-dd HH:mm:ss。

        :param end_date: The end_date of this QueryHitsResponseDTO.
        :type: str
        """
        if end_date is not None and len(end_date) > 19:
            raise ValueError("Invalid value for `end_date`, length must be less than or equal to `19`")
        if end_date is not None and len(end_date) < 19:
            raise ValueError("Invalid value for `end_date`, length must be greater than or equal to `19`")

        self._end_date = end_date

    @property
    def hit_status(self):
        """
        Gets the hit_status of this QueryHitsResponseDTO.
        命中状态。

        :return: The hit_status of this QueryHitsResponseDTO.
        :rtype: list[PolicyHitsListBuilder]
        """
        return self._hit_status

    @hit_status.setter
    def hit_status(self, hit_status):
        """
        Sets the hit_status of this QueryHitsResponseDTO.
        命中状态。

        :param hit_status: The hit_status of this QueryHitsResponseDTO.
        :type: list[PolicyHitsListBuilder]
        """

        self._hit_status = hit_status

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
        if not isinstance(other, QueryHitsResponseDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other