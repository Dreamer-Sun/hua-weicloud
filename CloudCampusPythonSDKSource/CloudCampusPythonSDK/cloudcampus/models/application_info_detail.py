# coding: utf-8

"""
    终端应用流量信息查询

    终端TopN应用流量查询。 

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ApplicationInfoDetail(object):
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
        'name': 'str',
        'percent': 'float',
        'traffic': 'float',
        'unit': 'str'
    }

    attribute_map = {
        'name': 'name',
        'percent': 'percent',
        'traffic': 'traffic',
        'unit': 'unit'
    }

    def __init__(self, name=None, percent=None, traffic=None, unit=None):
        """
        ApplicationInfoDetail - a model defined in Swagger
        """

        self._name = None
        self._percent = None
        self._traffic = None
        self._unit = None

        if name is not None:
          self.name = name
        if percent is not None:
          self.percent = percent
        if traffic is not None:
          self.traffic = traffic
        if unit is not None:
          self.unit = unit

    @property
    def name(self):
        """
        Gets the name of this ApplicationInfoDetail.
        应用或应用分类名称。

        :return: The name of this ApplicationInfoDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ApplicationInfoDetail.
        应用或应用分类名称。

        :param name: The name of this ApplicationInfoDetail.
        :type: str
        """
        if name is not None and len(name) > 256:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `256`")
        if name is not None and len(name) < 0:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `0`")

        self._name = name

    @property
    def percent(self):
        """
        Gets the percent of this ApplicationInfoDetail.
        流量占总流量的比值。

        :return: The percent of this ApplicationInfoDetail.
        :rtype: float
        """
        return self._percent

    @percent.setter
    def percent(self, percent):
        """
        Sets the percent of this ApplicationInfoDetail.
        流量占总流量的比值。

        :param percent: The percent of this ApplicationInfoDetail.
        :type: float
        """
        if percent is not None and percent > 1:
            raise ValueError("Invalid value for `percent`, must be a value less than or equal to `1`")
        if percent is not None and percent < 0:
            raise ValueError("Invalid value for `percent`, must be a value greater than or equal to `0`")

        self._percent = percent

    @property
    def traffic(self):
        """
        Gets the traffic of this ApplicationInfoDetail.
        应用或者应用类型上行流量与下行流量总和大小。

        :return: The traffic of this ApplicationInfoDetail.
        :rtype: float
        """
        return self._traffic

    @traffic.setter
    def traffic(self, traffic):
        """
        Sets the traffic of this ApplicationInfoDetail.
        应用或者应用类型上行流量与下行流量总和大小。

        :param traffic: The traffic of this ApplicationInfoDetail.
        :type: float
        """
        if traffic is not None and traffic > 340282350000000000000000000000000000000:
            raise ValueError("Invalid value for `traffic`, must be a value less than or equal to `340282350000000000000000000000000000000`")
        if traffic is not None and traffic < 0:
            raise ValueError("Invalid value for `traffic`, must be a value greater than or equal to `0`")

        self._traffic = traffic

    @property
    def unit(self):
        """
        Gets the unit of this ApplicationInfoDetail.
        流量单位。

        :return: The unit of this ApplicationInfoDetail.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """
        Sets the unit of this ApplicationInfoDetail.
        流量单位。

        :param unit: The unit of this ApplicationInfoDetail.
        :type: str
        """
        if unit is not None and len(unit) > 256:
            raise ValueError("Invalid value for `unit`, length must be less than or equal to `256`")
        if unit is not None and len(unit) < 0:
            raise ValueError("Invalid value for `unit`, length must be greater than or equal to `0`")

        self._unit = unit

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
        if not isinstance(other, ApplicationInfoDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
