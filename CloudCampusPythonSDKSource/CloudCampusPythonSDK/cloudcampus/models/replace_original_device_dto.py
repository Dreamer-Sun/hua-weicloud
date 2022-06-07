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


class ReplaceOriginalDeviceDto(object):
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
        'original_device_id': 'str',
        'new_esn': 'str'
    }

    attribute_map = {
        'original_device_id': 'originalDeviceId',
        'new_esn': 'newEsn'
    }

    def __init__(self, original_device_id=None, new_esn=None):
        """
        ReplaceOriginalDeviceDto - a model defined in Swagger
        """

        self._original_device_id = None
        self._new_esn = None

        if original_device_id is not None:
          self.original_device_id = original_device_id
        if new_esn is not None:
          self.new_esn = new_esn

    @property
    def original_device_id(self):
        """
        Gets the original_device_id of this ReplaceOriginalDeviceDto.
        待替换设备的ID。

        :return: The original_device_id of this ReplaceOriginalDeviceDto.
        :rtype: str
        """
        return self._original_device_id

    @original_device_id.setter
    def original_device_id(self, original_device_id):
        """
        Sets the original_device_id of this ReplaceOriginalDeviceDto.
        待替换设备的ID。

        :param original_device_id: The original_device_id of this ReplaceOriginalDeviceDto.
        :type: str
        """

        self._original_device_id = original_device_id

    @property
    def new_esn(self):
        """
        Gets the new_esn of this ReplaceOriginalDeviceDto.
        该字段必填。newEsn字段合法则替换原有esn。

        :return: The new_esn of this ReplaceOriginalDeviceDto.
        :rtype: str
        """
        return self._new_esn

    @new_esn.setter
    def new_esn(self, new_esn):
        """
        Sets the new_esn of this ReplaceOriginalDeviceDto.
        该字段必填。newEsn字段合法则替换原有esn。

        :param new_esn: The new_esn of this ReplaceOriginalDeviceDto.
        :type: str
        """
        if new_esn is not None and len(new_esn) > 64:
            raise ValueError("Invalid value for `new_esn`, length must be less than or equal to `64`")

        self._new_esn = new_esn

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
        if not isinstance(other, ReplaceOriginalDeviceDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
