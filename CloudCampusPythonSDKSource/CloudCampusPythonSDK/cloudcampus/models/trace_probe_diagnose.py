# coding: utf-8

"""
    运维ping/trace探测

    ping/trace探测第三方接口。 · 创建ping探测任务 · 查询ping探测结果 · 创建trace探测任务 · 查询trace探测结果 

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class TraceProbeDiagnose(object):
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
        'probe_index': 'int',
        'result': 'int',
        'delta_time': 'int',
        'probe_address': 'str'
    }

    attribute_map = {
        'probe_index': 'probeIndex',
        'result': 'result',
        'delta_time': 'deltaTime',
        'probe_address': 'probeAddress'
    }

    def __init__(self, probe_index=None, result=None, delta_time=None, probe_address=None):
        """
        TraceProbeDiagnose - a model defined in Swagger
        """

        self._probe_index = None
        self._result = None
        self._delta_time = None
        self._probe_address = None

        if probe_index is not None:
          self.probe_index = probe_index
        if result is not None:
          self.result = result
        if delta_time is not None:
          self.delta_time = delta_time
        if probe_address is not None:
          self.probe_address = probe_address

    @property
    def probe_index(self):
        """
        Gets the probe_index of this TraceProbeDiagnose.
        单跳探测索引。

        :return: The probe_index of this TraceProbeDiagnose.
        :rtype: int
        """
        return self._probe_index

    @probe_index.setter
    def probe_index(self, probe_index):
        """
        Sets the probe_index of this TraceProbeDiagnose.
        单跳探测索引。

        :param probe_index: The probe_index of this TraceProbeDiagnose.
        :type: int
        """

        self._probe_index = probe_index

    @property
    def result(self):
        """
        Gets the result of this TraceProbeDiagnose.
        探测状态。 0 --- 已完成 1 --- 执行中 2 --- 超时 3 --- 失败 

        :return: The result of this TraceProbeDiagnose.
        :rtype: int
        """
        return self._result

    @result.setter
    def result(self, result):
        """
        Sets the result of this TraceProbeDiagnose.
        探测状态。 0 --- 已完成 1 --- 执行中 2 --- 超时 3 --- 失败 

        :param result: The result of this TraceProbeDiagnose.
        :type: int
        """

        self._result = result

    @property
    def delta_time(self):
        """
        Gets the delta_time of this TraceProbeDiagnose.
        探测增量时间。

        :return: The delta_time of this TraceProbeDiagnose.
        :rtype: int
        """
        return self._delta_time

    @delta_time.setter
    def delta_time(self, delta_time):
        """
        Sets the delta_time of this TraceProbeDiagnose.
        探测增量时间。

        :param delta_time: The delta_time of this TraceProbeDiagnose.
        :type: int
        """

        self._delta_time = delta_time

    @property
    def probe_address(self):
        """
        Gets the probe_address of this TraceProbeDiagnose.
        单跳探测地址。可以是IP地址或域名，域名中不能包含空格。

        :return: The probe_address of this TraceProbeDiagnose.
        :rtype: str
        """
        return self._probe_address

    @probe_address.setter
    def probe_address(self, probe_address):
        """
        Sets the probe_address of this TraceProbeDiagnose.
        单跳探测地址。可以是IP地址或域名，域名中不能包含空格。

        :param probe_address: The probe_address of this TraceProbeDiagnose.
        :type: str
        """

        self._probe_address = probe_address

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
        if not isinstance(other, TraceProbeDiagnose):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
