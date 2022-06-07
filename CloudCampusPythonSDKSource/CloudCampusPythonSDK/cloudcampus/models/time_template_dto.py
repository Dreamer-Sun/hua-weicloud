# coding: utf-8

"""
    时间模板管理

    时间模板第三方接口说明。 

    OpenAPI spec version: 1.2.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class TimeTemplateDto(object):
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
        'template_name': 'str',
        'day_content_dto_list': 'list[DayContentDto]',
        'id': 'str'
    }

    attribute_map = {
        'template_name': 'templateName',
        'day_content_dto_list': 'dayContentDtoList',
        'id': 'id'
    }

    def __init__(self, template_name=None, day_content_dto_list=None, id=None):
        """
        TimeTemplateDto - a model defined in Swagger
        """

        self._template_name = None
        self._day_content_dto_list = None
        self._id = None

        if template_name is not None:
          self.template_name = template_name
        if day_content_dto_list is not None:
          self.day_content_dto_list = day_content_dto_list
        if id is not None:
          self.id = id

    @property
    def template_name(self):
        """
        Gets the template_name of this TimeTemplateDto.
        模板名称。

        :return: The template_name of this TimeTemplateDto.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        """
        Sets the template_name of this TimeTemplateDto.
        模板名称。

        :param template_name: The template_name of this TimeTemplateDto.
        :type: str
        """
        if template_name is not None and len(template_name) > 32:
            raise ValueError("Invalid value for `template_name`, length must be less than or equal to `32`")
        if template_name is not None and len(template_name) < 1:
            raise ValueError("Invalid value for `template_name`, length must be greater than or equal to `1`")

        self._template_name = template_name

    @property
    def day_content_dto_list(self):
        """
        Gets the day_content_dto_list of this TimeTemplateDto.
        时间段列表，列表必须分别为周一至周日7天时间段数据。

        :return: The day_content_dto_list of this TimeTemplateDto.
        :rtype: list[DayContentDto]
        """
        return self._day_content_dto_list

    @day_content_dto_list.setter
    def day_content_dto_list(self, day_content_dto_list):
        """
        Sets the day_content_dto_list of this TimeTemplateDto.
        时间段列表，列表必须分别为周一至周日7天时间段数据。

        :param day_content_dto_list: The day_content_dto_list of this TimeTemplateDto.
        :type: list[DayContentDto]
        """

        self._day_content_dto_list = day_content_dto_list

    @property
    def id(self):
        """
        Gets the id of this TimeTemplateDto.
        模板标识，UUID格式。

        :return: The id of this TimeTemplateDto.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this TimeTemplateDto.
        模板标识，UUID格式。

        :param id: The id of this TimeTemplateDto.
        :type: str
        """
        if id is not None and len(id) > 36:
            raise ValueError("Invalid value for `id`, length must be less than or equal to `36`")
        if id is not None and len(id) < 36:
            raise ValueError("Invalid value for `id`, length must be greater than or equal to `36`")

        self._id = id

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
        if not isinstance(other, TimeTemplateDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
