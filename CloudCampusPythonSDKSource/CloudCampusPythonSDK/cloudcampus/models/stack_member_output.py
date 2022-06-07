# coding: utf-8

"""
    堆叠管理

    堆叠管理第三方接口。 场景：创建堆叠操作的第三方接口。

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class StackMemberOutput(object):
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
        'device_id': 'str',
        'esn': 'str',
        'stack_member_id': 'str',
        'slot_id': 'int',
        'priority': 'int'
    }

    attribute_map = {
        'errcode': 'errcode',
        'errmsg': 'errmsg',
        'device_id': 'deviceId',
        'esn': 'esn',
        'stack_member_id': 'stackMemberId',
        'slot_id': 'slotId',
        'priority': 'priority'
    }

    def __init__(self, errcode=None, errmsg=None, device_id=None, esn=None, stack_member_id=None, slot_id=None, priority=None):
        """
        StackMemberOutput - a model defined in Swagger
        """

        self._errcode = None
        self._errmsg = None
        self._device_id = None
        self._esn = None
        self._stack_member_id = None
        self._slot_id = None
        self._priority = None

        if errcode is not None:
          self.errcode = errcode
        if errmsg is not None:
          self.errmsg = errmsg
        if device_id is not None:
          self.device_id = device_id
        if esn is not None:
          self.esn = esn
        if stack_member_id is not None:
          self.stack_member_id = stack_member_id
        if slot_id is not None:
          self.slot_id = slot_id
        if priority is not None:
          self.priority = priority

    @property
    def errcode(self):
        """
        Gets the errcode of this StackMemberOutput.
        错误码。

        :return: The errcode of this StackMemberOutput.
        :rtype: str
        """
        return self._errcode

    @errcode.setter
    def errcode(self, errcode):
        """
        Sets the errcode of this StackMemberOutput.
        错误码。

        :param errcode: The errcode of this StackMemberOutput.
        :type: str
        """

        self._errcode = errcode

    @property
    def errmsg(self):
        """
        Gets the errmsg of this StackMemberOutput.
        错误信息。

        :return: The errmsg of this StackMemberOutput.
        :rtype: str
        """
        return self._errmsg

    @errmsg.setter
    def errmsg(self, errmsg):
        """
        Sets the errmsg of this StackMemberOutput.
        错误信息。

        :param errmsg: The errmsg of this StackMemberOutput.
        :type: str
        """

        self._errmsg = errmsg

    @property
    def device_id(self):
        """
        Gets the device_id of this StackMemberOutput.
        设备ID，UUID格式。

        :return: The device_id of this StackMemberOutput.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """
        Sets the device_id of this StackMemberOutput.
        设备ID，UUID格式。

        :param device_id: The device_id of this StackMemberOutput.
        :type: str
        """

        self._device_id = device_id

    @property
    def esn(self):
        """
        Gets the esn of this StackMemberOutput.
        设备ESN。

        :return: The esn of this StackMemberOutput.
        :rtype: str
        """
        return self._esn

    @esn.setter
    def esn(self, esn):
        """
        Sets the esn of this StackMemberOutput.
        设备ESN。

        :param esn: The esn of this StackMemberOutput.
        :type: str
        """

        self._esn = esn

    @property
    def stack_member_id(self):
        """
        Gets the stack_member_id of this StackMemberOutput.
        堆叠成员ID，UUID格式。

        :return: The stack_member_id of this StackMemberOutput.
        :rtype: str
        """
        return self._stack_member_id

    @stack_member_id.setter
    def stack_member_id(self, stack_member_id):
        """
        Sets the stack_member_id of this StackMemberOutput.
        堆叠成员ID，UUID格式。

        :param stack_member_id: The stack_member_id of this StackMemberOutput.
        :type: str
        """

        self._stack_member_id = stack_member_id

    @property
    def slot_id(self):
        """
        Gets the slot_id of this StackMemberOutput.
        设备堆叠编号。

        :return: The slot_id of this StackMemberOutput.
        :rtype: int
        """
        return self._slot_id

    @slot_id.setter
    def slot_id(self, slot_id):
        """
        Sets the slot_id of this StackMemberOutput.
        设备堆叠编号。

        :param slot_id: The slot_id of this StackMemberOutput.
        :type: int
        """

        self._slot_id = slot_id

    @property
    def priority(self):
        """
        Gets the priority of this StackMemberOutput.
        设备堆叠优先级。

        :return: The priority of this StackMemberOutput.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """
        Sets the priority of this StackMemberOutput.
        设备堆叠优先级。

        :param priority: The priority of this StackMemberOutput.
        :type: int
        """

        self._priority = priority

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
        if not isinstance(other, StackMemberOutput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other