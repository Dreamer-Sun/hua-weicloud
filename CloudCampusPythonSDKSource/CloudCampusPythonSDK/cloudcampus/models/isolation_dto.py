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


class IsolationDTO(object):
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
        'block_id': 'str',
        'vm_ip': 'str',
        'tenant': 'str',
        'producer': 'str',
        'exception_ips': 'list[str]'
    }

    attribute_map = {
        'block_id': 'blockId',
        'vm_ip': 'vmIp',
        'tenant': 'tenant',
        'producer': 'producer',
        'exception_ips': 'exceptionIps'
    }

    def __init__(self, block_id=None, vm_ip=None, tenant=None, producer=None, exception_ips=None):
        """
        IsolationDTO - a model defined in Swagger
        """

        self._block_id = None
        self._vm_ip = None
        self._tenant = None
        self._producer = None
        self._exception_ips = None

        if block_id is not None:
          self.block_id = block_id
        if vm_ip is not None:
          self.vm_ip = vm_ip
        if tenant is not None:
          self.tenant = tenant
        if producer is not None:
          self.producer = producer
        if exception_ips is not None:
          self.exception_ips = exception_ips

    @property
    def block_id(self):
        """
        Gets the block_id of this IsolationDTO.
        事件ID，UUID格式。

        :return: The block_id of this IsolationDTO.
        :rtype: str
        """
        return self._block_id

    @block_id.setter
    def block_id(self, block_id):
        """
        Sets the block_id of this IsolationDTO.
        事件ID，UUID格式。

        :param block_id: The block_id of this IsolationDTO.
        :type: str
        """
        if block_id is not None and len(block_id) > 36:
            raise ValueError("Invalid value for `block_id`, length must be less than or equal to `36`")
        if block_id is not None and len(block_id) < 36:
            raise ValueError("Invalid value for `block_id`, length must be greater than or equal to `36`")

        self._block_id = block_id

    @property
    def vm_ip(self):
        """
        Gets the vm_ip of this IsolationDTO.
        主机IP，只支持IPV4格式。

        :return: The vm_ip of this IsolationDTO.
        :rtype: str
        """
        return self._vm_ip

    @vm_ip.setter
    def vm_ip(self, vm_ip):
        """
        Sets the vm_ip of this IsolationDTO.
        主机IP，只支持IPV4格式。

        :param vm_ip: The vm_ip of this IsolationDTO.
        :type: str
        """

        self._vm_ip = vm_ip

    @property
    def tenant(self):
        """
        Gets the tenant of this IsolationDTO.
        租户ID，UUID格式。

        :return: The tenant of this IsolationDTO.
        :rtype: str
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant):
        """
        Sets the tenant of this IsolationDTO.
        租户ID，UUID格式。

        :param tenant: The tenant of this IsolationDTO.
        :type: str
        """
        if tenant is not None and len(tenant) > 36:
            raise ValueError("Invalid value for `tenant`, length must be less than or equal to `36`")
        if tenant is not None and len(tenant) < 36:
            raise ValueError("Invalid value for `tenant`, length must be greater than or equal to `36`")

        self._tenant = tenant

    @property
    def producer(self):
        """
        Gets the producer of this IsolationDTO.
        调用者。

        :return: The producer of this IsolationDTO.
        :rtype: str
        """
        return self._producer

    @producer.setter
    def producer(self, producer):
        """
        Sets the producer of this IsolationDTO.
        调用者。

        :param producer: The producer of this IsolationDTO.
        :type: str
        """
        if producer is not None and len(producer) > 10:
            raise ValueError("Invalid value for `producer`, length must be less than or equal to `10`")

        self._producer = producer

    @property
    def exception_ips(self):
        """
        Gets the exception_ips of this IsolationDTO.
        例外IP列表，最多支持8个IP列表，支持IPV4和IPV6格式。

        :return: The exception_ips of this IsolationDTO.
        :rtype: list[str]
        """
        return self._exception_ips

    @exception_ips.setter
    def exception_ips(self, exception_ips):
        """
        Sets the exception_ips of this IsolationDTO.
        例外IP列表，最多支持8个IP列表，支持IPV4和IPV6格式。

        :param exception_ips: The exception_ips of this IsolationDTO.
        :type: list[str]
        """

        self._exception_ips = exception_ips

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
        if not isinstance(other, IsolationDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other