# coding: utf-8

"""
    ACL模板管理

    ACL模板第三方管理接口说明。 

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class RuleList(object):
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
        'rule_id': 'str',
        'ip': 'str',
        'domain': 'str',
        'policy': 'str',
        'protocol': 'str',
        'src_ip': 'str',
        'src_port': 'str',
        'dst_ip': 'str',
        'dst_port': 'str',
        'description': 'str'
    }

    attribute_map = {
        'rule_id': 'ruleId',
        'ip': 'ip',
        'domain': 'domain',
        'policy': 'policy',
        'protocol': 'protocol',
        'src_ip': 'srcIp',
        'src_port': 'srcPort',
        'dst_ip': 'dstIp',
        'dst_port': 'dstPort',
        'description': 'description'
    }

    def __init__(self, rule_id=None, ip=None, domain=None, policy=None, protocol=None, src_ip=None, src_port=None, dst_ip=None, dst_port=None, description=None):
        """
        RuleList - a model defined in Swagger
        """

        self._rule_id = None
        self._ip = None
        self._domain = None
        self._policy = None
        self._protocol = None
        self._src_ip = None
        self._src_port = None
        self._dst_ip = None
        self._dst_port = None
        self._description = None

        if rule_id is not None:
          self.rule_id = rule_id
        if ip is not None:
          self.ip = ip
        if domain is not None:
          self.domain = domain
        if policy is not None:
          self.policy = policy
        if protocol is not None:
          self.protocol = protocol
        if src_ip is not None:
          self.src_ip = src_ip
        if src_port is not None:
          self.src_port = src_port
        if dst_ip is not None:
          self.dst_ip = dst_ip
        if dst_port is not None:
          self.dst_port = dst_port
        if description is not None:
          self.description = description

    @property
    def rule_id(self):
        """
        Gets the rule_id of this RuleList.
        规则优先级编号，仅高级ACL有效且必填。

        :return: The rule_id of this RuleList.
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        """
        Sets the rule_id of this RuleList.
        规则优先级编号，仅高级ACL有效且必填。

        :param rule_id: The rule_id of this RuleList.
        :type: str
        """

        self._rule_id = rule_id

    @property
    def ip(self):
        """
        Gets the ip of this RuleList.
        IP地址，仅用户ACL有效且必填。与domain共存时，优先级高于domain。例如：192.168.1.0/24

        :return: The ip of this RuleList.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """
        Sets the ip of this RuleList.
        IP地址，仅用户ACL有效且必填。与domain共存时，优先级高于domain。例如：192.168.1.0/24

        :param ip: The ip of this RuleList.
        :type: str
        """

        self._ip = ip

    @property
    def domain(self):
        """
        Gets the domain of this RuleList.
        域名，仅用户ACL有效且必填。例如：www.example.com

        :return: The domain of this RuleList.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """
        Sets the domain of this RuleList.
        域名，仅用户ACL有效且必填。例如：www.example.com

        :param domain: The domain of this RuleList.
        :type: str
        """

        self._domain = domain

    @property
    def policy(self):
        """
        Gets the policy of this RuleList.
        策略，aclType为高级acl时有效且必填，有效值permit，deny。

        :return: The policy of this RuleList.
        :rtype: str
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """
        Sets the policy of this RuleList.
        策略，aclType为高级acl时有效且必填，有效值permit，deny。

        :param policy: The policy of this RuleList.
        :type: str
        """

        self._policy = policy

    @property
    def protocol(self):
        """
        Gets the protocol of this RuleList.
        协议，aclType为高级acl时有效且必填，有效值udp，tcp，any，icmp。

        :return: The protocol of this RuleList.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """
        Sets the protocol of this RuleList.
        协议，aclType为高级acl时有效且必填，有效值udp，tcp，any，icmp。

        :param protocol: The protocol of this RuleList.
        :type: str
        """

        self._protocol = protocol

    @property
    def src_ip(self):
        """
        Gets the src_ip of this RuleList.
        源IP地址，可以输入Any表示任意IP，仅高级ACL有效且必填。

        :return: The src_ip of this RuleList.
        :rtype: str
        """
        return self._src_ip

    @src_ip.setter
    def src_ip(self, src_ip):
        """
        Sets the src_ip of this RuleList.
        源IP地址，可以输入Any表示任意IP，仅高级ACL有效且必填。

        :param src_ip: The src_ip of this RuleList.
        :type: str
        """

        self._src_ip = src_ip

    @property
    def src_port(self):
        """
        Gets the src_port of this RuleList.
        源端口号，或源端口段，仅高级ACL有效，范围：整数（例如1000）或者整数段（1-100），且整数和整数段包含的值在0~65535。

        :return: The src_port of this RuleList.
        :rtype: str
        """
        return self._src_port

    @src_port.setter
    def src_port(self, src_port):
        """
        Sets the src_port of this RuleList.
        源端口号，或源端口段，仅高级ACL有效，范围：整数（例如1000）或者整数段（1-100），且整数和整数段包含的值在0~65535。

        :param src_port: The src_port of this RuleList.
        :type: str
        """

        self._src_port = src_port

    @property
    def dst_ip(self):
        """
        Gets the dst_ip of this RuleList.
        目的IP地址，可以输入Any表示任意IP，仅高级ACL有效且必填。

        :return: The dst_ip of this RuleList.
        :rtype: str
        """
        return self._dst_ip

    @dst_ip.setter
    def dst_ip(self, dst_ip):
        """
        Sets the dst_ip of this RuleList.
        目的IP地址，可以输入Any表示任意IP，仅高级ACL有效且必填。

        :param dst_ip: The dst_ip of this RuleList.
        :type: str
        """

        self._dst_ip = dst_ip

    @property
    def dst_port(self):
        """
        Gets the dst_port of this RuleList.
        目的端口号，或目的端口段，仅高级ACL有效，范围：整数（例如1000）或者整数段（1-100），且整数和整数段包含的值在0~65535。

        :return: The dst_port of this RuleList.
        :rtype: str
        """
        return self._dst_port

    @dst_port.setter
    def dst_port(self, dst_port):
        """
        Sets the dst_port of this RuleList.
        目的端口号，或目的端口段，仅高级ACL有效，范围：整数（例如1000）或者整数段（1-100），且整数和整数段包含的值在0~65535。

        :param dst_port: The dst_port of this RuleList.
        :type: str
        """

        self._dst_port = dst_port

    @property
    def description(self):
        """
        Gets the description of this RuleList.
        规则描述。

        :return: The description of this RuleList.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this RuleList.
        规则描述。

        :param description: The description of this RuleList.
        :type: str
        """
        if description is not None and len(description) > 127:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `127`")
        if description is not None and len(description) < 0:
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")

        self._description = description

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
        if not isinstance(other, RuleList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other