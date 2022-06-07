# coding: utf-8

"""
    RADIUS模板管理

    RADIUS模板配置第三方北向接口说明。 

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class RadiusTempDtoSlaveAuthServer(object):
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
        'server_address': 'str',
        'port': 'int'
    }

    attribute_map = {
        'server_address': 'serverAddress',
        'port': 'port'
    }

    def __init__(self, server_address=None, port=None):
        """
        RadiusTempDtoSlaveAuthServer - a model defined in Swagger
        """

        self._server_address = None
        self._port = None

        if server_address is not None:
          self.server_address = server_address
        if port is not None:
          self.port = port

    @property
    def server_address(self):
        """
        Gets the server_address of this RadiusTempDtoSlaveAuthServer.
        服务器IP地址。PUT操作时，如果备认证服务器中该字段设置为空字符串\"\"，则将备认证服务器设置为空。

        :return: The server_address of this RadiusTempDtoSlaveAuthServer.
        :rtype: str
        """
        return self._server_address

    @server_address.setter
    def server_address(self, server_address):
        """
        Sets the server_address of this RadiusTempDtoSlaveAuthServer.
        服务器IP地址。PUT操作时，如果备认证服务器中该字段设置为空字符串\"\"，则将备认证服务器设置为空。

        :param server_address: The server_address of this RadiusTempDtoSlaveAuthServer.
        :type: str
        """

        self._server_address = server_address

    @property
    def port(self):
        """
        Gets the port of this RadiusTempDtoSlaveAuthServer.
        服务器端口。

        :return: The port of this RadiusTempDtoSlaveAuthServer.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this RadiusTempDtoSlaveAuthServer.
        服务器端口。

        :param port: The port of this RadiusTempDtoSlaveAuthServer.
        :type: int
        """
        if port is not None and port > 65535:
            raise ValueError("Invalid value for `port`, must be a value less than or equal to `65535`")
        if port is not None and port < 1:
            raise ValueError("Invalid value for `port`, must be a value greater than or equal to `1`")

        self._port = port

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
        if not isinstance(other, RadiusTempDtoSlaveAuthServer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
