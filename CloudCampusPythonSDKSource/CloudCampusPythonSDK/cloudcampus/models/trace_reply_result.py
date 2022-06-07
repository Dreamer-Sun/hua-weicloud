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


class TraceReplyResult(object):
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
        'task_id': 'str',
        'destination': 'str',
        'status': 'int',
        'trace_hop_list': 'TraceReplyResultTraceHopList'
    }

    attribute_map = {
        'task_id': 'taskId',
        'destination': 'destination',
        'status': 'status',
        'trace_hop_list': 'TraceHopList'
    }

    def __init__(self, task_id=None, destination=None, status=None, trace_hop_list=None):
        """
        TraceReplyResult - a model defined in Swagger
        """

        self._task_id = None
        self._destination = None
        self._status = None
        self._trace_hop_list = None

        if task_id is not None:
          self.task_id = task_id
        if destination is not None:
          self.destination = destination
        if status is not None:
          self.status = status
        if trace_hop_list is not None:
          self.trace_hop_list = trace_hop_list

    @property
    def task_id(self):
        """
        Gets the task_id of this TraceReplyResult.
        trace探测任务ID，格式UUID。

        :return: The task_id of this TraceReplyResult.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """
        Sets the task_id of this TraceReplyResult.
        trace探测任务ID，格式UUID。

        :param task_id: The task_id of this TraceReplyResult.
        :type: str
        """

        self._task_id = task_id

    @property
    def destination(self):
        """
        Gets the destination of this TraceReplyResult.
        目的地址。可以是IP地址或域名，域名中不能包含空格。

        :return: The destination of this TraceReplyResult.
        :rtype: str
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """
        Sets the destination of this TraceReplyResult.
        目的地址。可以是IP地址或域名，域名中不能包含空格。

        :param destination: The destination of this TraceReplyResult.
        :type: str
        """

        self._destination = destination

    @property
    def status(self):
        """
        Gets the status of this TraceReplyResult.
        探测状态。 0 --- 已完成 1 --- 执行中 2 --- 超时 3 --- 失败 

        :return: The status of this TraceReplyResult.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this TraceReplyResult.
        探测状态。 0 --- 已完成 1 --- 执行中 2 --- 超时 3 --- 失败 

        :param status: The status of this TraceReplyResult.
        :type: int
        """

        self._status = status

    @property
    def trace_hop_list(self):
        """
        Gets the trace_hop_list of this TraceReplyResult.

        :return: The trace_hop_list of this TraceReplyResult.
        :rtype: TraceReplyResultTraceHopList
        """
        return self._trace_hop_list

    @trace_hop_list.setter
    def trace_hop_list(self, trace_hop_list):
        """
        Sets the trace_hop_list of this TraceReplyResult.

        :param trace_hop_list: The trace_hop_list of this TraceReplyResult.
        :type: TraceReplyResultTraceHopList
        """

        self._trace_hop_list = trace_hop_list

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
        if not isinstance(other, TraceReplyResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other