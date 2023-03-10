# coding: utf-8

"""
    室内地图信息查询

    室内地图第三方北向接口。 · 查询站点中所有楼栋基本信息 · 查询楼栋中所有楼层基本信息 · 查询楼栋中所有楼层详细信息 · 查询楼栋中楼层和设备布放信息 · 查询楼栋中楼层已布放设备详细信息 · 查询楼层已布放设备位置信息 

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class FloorDetails(object):
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
        'number': 'str',
        'image': 'str',
        'scale': 'float'
    }

    attribute_map = {
        'name': 'name',
        'number': 'number',
        'image': 'image',
        'scale': 'scale'
    }

    def __init__(self, name=None, number=None, image=None, scale=None):
        """
        FloorDetails - a model defined in Swagger
        """

        self._name = None
        self._number = None
        self._image = None
        self._scale = None

        if name is not None:
          self.name = name
        if number is not None:
          self.number = number
        if image is not None:
          self.image = image
        if scale is not None:
          self.scale = scale

    @property
    def name(self):
        """
        Gets the name of this FloorDetails.
        楼层名称。

        :return: The name of this FloorDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this FloorDetails.
        楼层名称。

        :param name: The name of this FloorDetails.
        :type: str
        """

        self._name = name

    @property
    def number(self):
        """
        Gets the number of this FloorDetails.
        楼层号。

        :return: The number of this FloorDetails.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """
        Sets the number of this FloorDetails.
        楼层号。

        :param number: The number of this FloorDetails.
        :type: str
        """

        self._number = number

    @property
    def image(self):
        """
        Gets the image of this FloorDetails.
        楼层图纸。

        :return: The image of this FloorDetails.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """
        Sets the image of this FloorDetails.
        楼层图纸。

        :param image: The image of this FloorDetails.
        :type: str
        """
        if image is not None and not re.search('^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$', image):
            raise ValueError("Invalid value for `image`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`")

        self._image = image

    @property
    def scale(self):
        """
        Gets the scale of this FloorDetails.
        比例尺，表示图上距离与实际距离的比，例如：图上0.01米代表实际1米，则比例尺为0.01。

        :return: The scale of this FloorDetails.
        :rtype: float
        """
        return self._scale

    @scale.setter
    def scale(self, scale):
        """
        Sets the scale of this FloorDetails.
        比例尺，表示图上距离与实际距离的比，例如：图上0.01米代表实际1米，则比例尺为0.01。

        :param scale: The scale of this FloorDetails.
        :type: float
        """

        self._scale = scale

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
        if not isinstance(other, FloorDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
