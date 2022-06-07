# coding: utf-8

"""
    WAC关联Fit AP管理

    WAC关联Fit AP第三方接口，主要特性：  · 根据指定的WAC设备ID查询关联的Fit AP列表 · 根据指定的WAC设备关联Fit AP列表 · 根据指定的WAC设备解除关联的Fit AP列表 

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class FitApInfo(object):
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
        'device_id': 'str',
        'esn': 'str',
        'device_model': 'str',
        'site_id': 'str',
        'status': 'int',
        'ap_id': 'int',
        'illegal_status': 'int'
    }

    attribute_map = {
        'device_id': 'deviceId',
        'esn': 'esn',
        'device_model': 'deviceModel',
        'site_id': 'siteId',
        'status': 'status',
        'ap_id': 'apId',
        'illegal_status': 'illegalStatus'
    }

    def __init__(self, device_id=None, esn=None, device_model=None, site_id=None, status=None, ap_id=None, illegal_status=None):
        """
        FitApInfo - a model defined in Swagger
        """

        self._device_id = None
        self._esn = None
        self._device_model = None
        self._site_id = None
        self._status = None
        self._ap_id = None
        self._illegal_status = None

        if device_id is not None:
          self.device_id = device_id
        if esn is not None:
          self.esn = esn
        if device_model is not None:
          self.device_model = device_model
        if site_id is not None:
          self.site_id = site_id
        if status is not None:
          self.status = status
        if ap_id is not None:
          self.ap_id = ap_id
        if illegal_status is not None:
          self.illegal_status = illegal_status

    @property
    def device_id(self):
        """
        Gets the device_id of this FitApInfo.
        Fit AP设备ID。

        :return: The device_id of this FitApInfo.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """
        Sets the device_id of this FitApInfo.
        Fit AP设备ID。

        :param device_id: The device_id of this FitApInfo.
        :type: str
        """

        self._device_id = device_id

    @property
    def esn(self):
        """
        Gets the esn of this FitApInfo.
        Fit AP设备ESN。

        :return: The esn of this FitApInfo.
        :rtype: str
        """
        return self._esn

    @esn.setter
    def esn(self, esn):
        """
        Sets the esn of this FitApInfo.
        Fit AP设备ESN。

        :param esn: The esn of this FitApInfo.
        :type: str
        """

        self._esn = esn

    @property
    def device_model(self):
        """
        Gets the device_model of this FitApInfo.
        Fit AP设备型号。

        :return: The device_model of this FitApInfo.
        :rtype: str
        """
        return self._device_model

    @device_model.setter
    def device_model(self, device_model):
        """
        Sets the device_model of this FitApInfo.
        Fit AP设备型号。

        :param device_model: The device_model of this FitApInfo.
        :type: str
        """

        self._device_model = device_model

    @property
    def site_id(self):
        """
        Gets the site_id of this FitApInfo.
        Fit AP设备归属的站点ID。

        :return: The site_id of this FitApInfo.
        :rtype: str
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        """
        Sets the site_id of this FitApInfo.
        Fit AP设备归属的站点ID。

        :param site_id: The site_id of this FitApInfo.
        :type: str
        """

        self._site_id = site_id

    @property
    def status(self):
        """
        Gets the status of this FitApInfo.
        设备状态。0---正常、1---告警、3---离线、4---未注册。

        :return: The status of this FitApInfo.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this FitApInfo.
        设备状态。0---正常、1---告警、3---离线、4---未注册。

        :param status: The status of this FitApInfo.
        :type: int
        """

        self._status = status

    @property
    def ap_id(self):
        """
        Gets the ap_id of this FitApInfo.
        给Fit AP设备分配的ID。

        :return: The ap_id of this FitApInfo.
        :rtype: int
        """
        return self._ap_id

    @ap_id.setter
    def ap_id(self, ap_id):
        """
        Sets the ap_id of this FitApInfo.
        给Fit AP设备分配的ID。

        :param ap_id: The ap_id of this FitApInfo.
        :type: int
        """

        self._ap_id = ap_id

    @property
    def illegal_status(self):
        """
        Gets the illegal_status of this FitApInfo.
        设备异常状态。0---合法、1---未纳管、2---不在AC组内。

        :return: The illegal_status of this FitApInfo.
        :rtype: int
        """
        return self._illegal_status

    @illegal_status.setter
    def illegal_status(self, illegal_status):
        """
        Sets the illegal_status of this FitApInfo.
        设备异常状态。0---合法、1---未纳管、2---不在AC组内。

        :param illegal_status: The illegal_status of this FitApInfo.
        :type: int
        """

        self._illegal_status = illegal_status

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
        if not isinstance(other, FitApInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other