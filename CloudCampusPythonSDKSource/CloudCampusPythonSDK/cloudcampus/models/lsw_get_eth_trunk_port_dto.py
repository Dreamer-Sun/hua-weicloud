# coding: utf-8

"""
    交换机端口配置

    LSW端口配置北向接口，主要特性： · 查询交换机所有接口信息 · 修改交换机以太接口配置 · 创建交换机Eth-Trunk接口 · 修改交换机Eth-Trunk接口 · 删除交换机Eth-Trunk接口 

    OpenAPI spec version: 1.4.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class LSWGetEthTrunkPortDto(object):
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
        'status': 'bool',
        'description': 'str',
        'link_type': 'str',
        'default_vlan': 'int',
        'allow_pass_vlan': 'str',
        'dhcp_snooping': 'bool',
        'dhcp_snooping_trusted': 'bool',
        'nd_snooping': 'bool',
        'nd_snooping_trusted': 'bool',
        'port_isolation': 'bool',
        'stp': 'bool',
        'stp_edgedport': 'str',
        'enable_relay': 'bool',
        'enable_mad_detection': 'bool',
        'domain_id': 'int',
        'na_msg_check': 'bool',
        'ns_msg_check': 'bool',
        'rs_msg_check': 'bool',
        'ipsg_check': 'bool',
        'dai_check': 'bool',
        'ip_subnet_vlan_enable': 'bool',
        'eth_trunk_mode': 'str',
        'port_member_list': 'list[str]',
        'name': 'str',
        'is_up_stream': 'bool'
    }

    attribute_map = {
        'status': 'status',
        'description': 'description',
        'link_type': 'linkType',
        'default_vlan': 'defaultVlan',
        'allow_pass_vlan': 'allowPassVlan',
        'dhcp_snooping': 'dhcpSnooping',
        'dhcp_snooping_trusted': 'dhcpSnoopingTrusted',
        'nd_snooping': 'ndSnooping',
        'nd_snooping_trusted': 'ndSnoopingTrusted',
        'port_isolation': 'portIsolation',
        'stp': 'stp',
        'stp_edgedport': 'stpEdgedport',
        'enable_relay': 'enableRelay',
        'enable_mad_detection': 'enableMadDetection',
        'domain_id': 'domainId',
        'na_msg_check': 'naMsgCheck',
        'ns_msg_check': 'nsMsgCheck',
        'rs_msg_check': 'rsMsgCheck',
        'ipsg_check': 'ipsgCheck',
        'dai_check': 'daiCheck',
        'ip_subnet_vlan_enable': 'ipSubnetVlanEnable',
        'eth_trunk_mode': 'ethTrunkMode',
        'port_member_list': 'portMemberList',
        'name': 'name',
        'is_up_stream': 'isUpStream'
    }

    def __init__(self, status=None, description=None, link_type=None, default_vlan=None, allow_pass_vlan=None, dhcp_snooping=None, dhcp_snooping_trusted=None, nd_snooping=None, nd_snooping_trusted=None, port_isolation=None, stp=None, stp_edgedport=None, enable_relay=None, enable_mad_detection=None, domain_id=None, na_msg_check=None, ns_msg_check=None, rs_msg_check=None, ipsg_check=None, dai_check=None, ip_subnet_vlan_enable=None, eth_trunk_mode=None, port_member_list=None, name=None, is_up_stream=None):
        """
        LSWGetEthTrunkPortDto - a model defined in Swagger
        """

        self._status = None
        self._description = None
        self._link_type = None
        self._default_vlan = None
        self._allow_pass_vlan = None
        self._dhcp_snooping = None
        self._dhcp_snooping_trusted = None
        self._nd_snooping = None
        self._nd_snooping_trusted = None
        self._port_isolation = None
        self._stp = None
        self._stp_edgedport = None
        self._enable_relay = None
        self._enable_mad_detection = None
        self._domain_id = None
        self._na_msg_check = None
        self._ns_msg_check = None
        self._rs_msg_check = None
        self._ipsg_check = None
        self._dai_check = None
        self._ip_subnet_vlan_enable = None
        self._eth_trunk_mode = None
        self._port_member_list = None
        self._name = None
        self._is_up_stream = None

        if status is not None:
          self.status = status
        if description is not None:
          self.description = description
        if link_type is not None:
          self.link_type = link_type
        if default_vlan is not None:
          self.default_vlan = default_vlan
        if allow_pass_vlan is not None:
          self.allow_pass_vlan = allow_pass_vlan
        if dhcp_snooping is not None:
          self.dhcp_snooping = dhcp_snooping
        if dhcp_snooping_trusted is not None:
          self.dhcp_snooping_trusted = dhcp_snooping_trusted
        if nd_snooping is not None:
          self.nd_snooping = nd_snooping
        if nd_snooping_trusted is not None:
          self.nd_snooping_trusted = nd_snooping_trusted
        if port_isolation is not None:
          self.port_isolation = port_isolation
        if stp is not None:
          self.stp = stp
        if stp_edgedport is not None:
          self.stp_edgedport = stp_edgedport
        if enable_relay is not None:
          self.enable_relay = enable_relay
        if enable_mad_detection is not None:
          self.enable_mad_detection = enable_mad_detection
        if domain_id is not None:
          self.domain_id = domain_id
        if na_msg_check is not None:
          self.na_msg_check = na_msg_check
        if ns_msg_check is not None:
          self.ns_msg_check = ns_msg_check
        if rs_msg_check is not None:
          self.rs_msg_check = rs_msg_check
        if ipsg_check is not None:
          self.ipsg_check = ipsg_check
        if dai_check is not None:
          self.dai_check = dai_check
        if ip_subnet_vlan_enable is not None:
          self.ip_subnet_vlan_enable = ip_subnet_vlan_enable
        if eth_trunk_mode is not None:
          self.eth_trunk_mode = eth_trunk_mode
        if port_member_list is not None:
          self.port_member_list = port_member_list
        if name is not None:
          self.name = name
        if is_up_stream is not None:
          self.is_up_stream = is_up_stream

    @property
    def status(self):
        """
        Gets the status of this LSWGetEthTrunkPortDto.
        接口管理状态（true为undo shutdown，false为shutdown）。

        :return: The status of this LSWGetEthTrunkPortDto.
        :rtype: bool
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this LSWGetEthTrunkPortDto.
        接口管理状态（true为undo shutdown，false为shutdown）。

        :param status: The status of this LSWGetEthTrunkPortDto.
        :type: bool
        """

        self._status = status

    @property
    def description(self):
        """
        Gets the description of this LSWGetEthTrunkPortDto.
        接口描述。

        :return: The description of this LSWGetEthTrunkPortDto.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this LSWGetEthTrunkPortDto.
        接口描述。

        :param description: The description of this LSWGetEthTrunkPortDto.
        :type: str
        """
        if description is not None and len(description) > 242:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `242`")
        if description is not None and len(description) < 0:
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")

        self._description = description

    @property
    def link_type(self):
        """
        Gets the link_type of this LSWGetEthTrunkPortDto.
        链路类型，若当前是以太接口，其加入Eth-Trunk后不能配置此参数。取值：access；trunk。

        :return: The link_type of this LSWGetEthTrunkPortDto.
        :rtype: str
        """
        return self._link_type

    @link_type.setter
    def link_type(self, link_type):
        """
        Sets the link_type of this LSWGetEthTrunkPortDto.
        链路类型，若当前是以太接口，其加入Eth-Trunk后不能配置此参数。取值：access；trunk。

        :param link_type: The link_type of this LSWGetEthTrunkPortDto.
        :type: str
        """

        self._link_type = link_type

    @property
    def default_vlan(self):
        """
        Gets the default_vlan of this LSWGetEthTrunkPortDto.
        access类型下缺省VLAN；或trunk类型下pvid。若当前是以太接口，其加入Eth-Trunk后不能配置此参数。

        :return: The default_vlan of this LSWGetEthTrunkPortDto.
        :rtype: int
        """
        return self._default_vlan

    @default_vlan.setter
    def default_vlan(self, default_vlan):
        """
        Sets the default_vlan of this LSWGetEthTrunkPortDto.
        access类型下缺省VLAN；或trunk类型下pvid。若当前是以太接口，其加入Eth-Trunk后不能配置此参数。

        :param default_vlan: The default_vlan of this LSWGetEthTrunkPortDto.
        :type: int
        """
        if default_vlan is not None and default_vlan > 4094:
            raise ValueError("Invalid value for `default_vlan`, must be a value less than or equal to `4094`")
        if default_vlan is not None and default_vlan < 1:
            raise ValueError("Invalid value for `default_vlan`, must be a value greater than or equal to `1`")

        self._default_vlan = default_vlan

    @property
    def allow_pass_vlan(self):
        """
        Gets the allow_pass_vlan of this LSWGetEthTrunkPortDto.
        trunk类型下允许通过VLAN，接口为trunk类型时必填。

        :return: The allow_pass_vlan of this LSWGetEthTrunkPortDto.
        :rtype: str
        """
        return self._allow_pass_vlan

    @allow_pass_vlan.setter
    def allow_pass_vlan(self, allow_pass_vlan):
        """
        Sets the allow_pass_vlan of this LSWGetEthTrunkPortDto.
        trunk类型下允许通过VLAN，接口为trunk类型时必填。

        :param allow_pass_vlan: The allow_pass_vlan of this LSWGetEthTrunkPortDto.
        :type: str
        """
        if allow_pass_vlan is not None and len(allow_pass_vlan) > 100:
            raise ValueError("Invalid value for `allow_pass_vlan`, length must be less than or equal to `100`")
        if allow_pass_vlan is not None and len(allow_pass_vlan) < 0:
            raise ValueError("Invalid value for `allow_pass_vlan`, length must be greater than or equal to `0`")

        self._allow_pass_vlan = allow_pass_vlan

    @property
    def dhcp_snooping(self):
        """
        Gets the dhcp_snooping of this LSWGetEthTrunkPortDto.
        DHCP Snooping使能，若当前是以太接口，其加入Eth-Trunk后不能配置此参数。

        :return: The dhcp_snooping of this LSWGetEthTrunkPortDto.
        :rtype: bool
        """
        return self._dhcp_snooping

    @dhcp_snooping.setter
    def dhcp_snooping(self, dhcp_snooping):
        """
        Sets the dhcp_snooping of this LSWGetEthTrunkPortDto.
        DHCP Snooping使能，若当前是以太接口，其加入Eth-Trunk后不能配置此参数。

        :param dhcp_snooping: The dhcp_snooping of this LSWGetEthTrunkPortDto.
        :type: bool
        """

        self._dhcp_snooping = dhcp_snooping

    @property
    def dhcp_snooping_trusted(self):
        """
        Gets the dhcp_snooping_trusted of this LSWGetEthTrunkPortDto.
        配置接口为DHCP Snooping信任状态，默认为非信任状态。

        :return: The dhcp_snooping_trusted of this LSWGetEthTrunkPortDto.
        :rtype: bool
        """
        return self._dhcp_snooping_trusted

    @dhcp_snooping_trusted.setter
    def dhcp_snooping_trusted(self, dhcp_snooping_trusted):
        """
        Sets the dhcp_snooping_trusted of this LSWGetEthTrunkPortDto.
        配置接口为DHCP Snooping信任状态，默认为非信任状态。

        :param dhcp_snooping_trusted: The dhcp_snooping_trusted of this LSWGetEthTrunkPortDto.
        :type: bool
        """

        self._dhcp_snooping_trusted = dhcp_snooping_trusted

    @property
    def nd_snooping(self):
        """
        Gets the nd_snooping of this LSWGetEthTrunkPortDto.
        ND Snooping使能，若当前是以太接口，其加入Eth-Trunk后不能配置此参数。

        :return: The nd_snooping of this LSWGetEthTrunkPortDto.
        :rtype: bool
        """
        return self._nd_snooping

    @nd_snooping.setter
    def nd_snooping(self, nd_snooping):
        """
        Sets the nd_snooping of this LSWGetEthTrunkPortDto.
        ND Snooping使能，若当前是以太接口，其加入Eth-Trunk后不能配置此参数。

        :param nd_snooping: The nd_snooping of this LSWGetEthTrunkPortDto.
        :type: bool
        """

        self._nd_snooping = nd_snooping

    @property
    def nd_snooping_trusted(self):
        """
        Gets the nd_snooping_trusted of this LSWGetEthTrunkPortDto.
        配置接口为ND Snooping信任状态，默认为非信任状态。

        :return: The nd_snooping_trusted of this LSWGetEthTrunkPortDto.
        :rtype: bool
        """
        return self._nd_snooping_trusted

    @nd_snooping_trusted.setter
    def nd_snooping_trusted(self, nd_snooping_trusted):
        """
        Sets the nd_snooping_trusted of this LSWGetEthTrunkPortDto.
        配置接口为ND Snooping信任状态，默认为非信任状态。

        :param nd_snooping_trusted: The nd_snooping_trusted of this LSWGetEthTrunkPortDto.
        :type: bool
        """

        self._nd_snooping_trusted = nd_snooping_trusted

    @property
    def port_isolation(self):
        """
        Gets the port_isolation of this LSWGetEthTrunkPortDto.
        端口隔离使能，若当前是以太接口，其加入Eth-Trunk后不能配置此参数。

        :return: The port_isolation of this LSWGetEthTrunkPortDto.
        :rtype: bool
        """
        return self._port_isolation

    @port_isolation.setter
    def port_isolation(self, port_isolation):
        """
        Sets the port_isolation of this LSWGetEthTrunkPortDto.
        端口隔离使能，若当前是以太接口，其加入Eth-Trunk后不能配置此参数。

        :param port_isolation: The port_isolation of this LSWGetEthTrunkPortDto.
        :type: bool
        """

        self._port_isolation = port_isolation

    @property
    def stp(self):
        """
        Gets the stp of this LSWGetEthTrunkPortDto.
        STP功能状态，取值：true（使能）；false（未使能）。当STP为false时，stpEdgedport自动赋值为normal，传入其他参数无效。

        :return: The stp of this LSWGetEthTrunkPortDto.
        :rtype: bool
        """
        return self._stp

    @stp.setter
    def stp(self, stp):
        """
        Sets the stp of this LSWGetEthTrunkPortDto.
        STP功能状态，取值：true（使能）；false（未使能）。当STP为false时，stpEdgedport自动赋值为normal，传入其他参数无效。

        :param stp: The stp of this LSWGetEthTrunkPortDto.
        :type: bool
        """

        self._stp = stp

    @property
    def stp_edgedport(self):
        """
        Gets the stp_edgedport of this LSWGetEthTrunkPortDto.
        STP边缘端口状态，若当前是以太接口，其加入Eth-Trunk后不能配置此参数。取值：enable（使能）；normal（遵从全局状态）；disable（未使能）。

        :return: The stp_edgedport of this LSWGetEthTrunkPortDto.
        :rtype: str
        """
        return self._stp_edgedport

    @stp_edgedport.setter
    def stp_edgedport(self, stp_edgedport):
        """
        Sets the stp_edgedport of this LSWGetEthTrunkPortDto.
        STP边缘端口状态，若当前是以太接口，其加入Eth-Trunk后不能配置此参数。取值：enable（使能）；normal（遵从全局状态）；disable（未使能）。

        :param stp_edgedport: The stp_edgedport of this LSWGetEthTrunkPortDto.
        :type: str
        """

        self._stp_edgedport = stp_edgedport

    @property
    def enable_relay(self):
        """
        Gets the enable_relay of this LSWGetEthTrunkPortDto.
        堆叠多主检测场景下，设为检测代理设备。

        :return: The enable_relay of this LSWGetEthTrunkPortDto.
        :rtype: bool
        """
        return self._enable_relay

    @enable_relay.setter
    def enable_relay(self, enable_relay):
        """
        Sets the enable_relay of this LSWGetEthTrunkPortDto.
        堆叠多主检测场景下，设为检测代理设备。

        :param enable_relay: The enable_relay of this LSWGetEthTrunkPortDto.
        :type: bool
        """

        self._enable_relay = enable_relay

    @property
    def enable_mad_detection(self):
        """
        Gets the enable_mad_detection of this LSWGetEthTrunkPortDto.
        堆叠多主检测场景下，代理模式双主检测开关。

        :return: The enable_mad_detection of this LSWGetEthTrunkPortDto.
        :rtype: bool
        """
        return self._enable_mad_detection

    @enable_mad_detection.setter
    def enable_mad_detection(self, enable_mad_detection):
        """
        Sets the enable_mad_detection of this LSWGetEthTrunkPortDto.
        堆叠多主检测场景下，代理模式双主检测开关。

        :param enable_mad_detection: The enable_mad_detection of this LSWGetEthTrunkPortDto.
        :type: bool
        """

        self._enable_mad_detection = enable_mad_detection

    @property
    def domain_id(self):
        """
        Gets the domain_id of this LSWGetEthTrunkPortDto.
        堆叠多主检测场景下，堆叠域编号，两个堆叠互相检测时，堆叠域编号需不同。

        :return: The domain_id of this LSWGetEthTrunkPortDto.
        :rtype: int
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """
        Sets the domain_id of this LSWGetEthTrunkPortDto.
        堆叠多主检测场景下，堆叠域编号，两个堆叠互相检测时，堆叠域编号需不同。

        :param domain_id: The domain_id of this LSWGetEthTrunkPortDto.
        :type: int
        """
        if domain_id is not None and domain_id > 255:
            raise ValueError("Invalid value for `domain_id`, must be a value less than or equal to `255`")
        if domain_id is not None and domain_id < 0:
            raise ValueError("Invalid value for `domain_id`, must be a value greater than or equal to `0`")

        self._domain_id = domain_id

    @property
    def na_msg_check(self):
        """
        Gets the na_msg_check of this LSWGetEthTrunkPortDto.
        NA报文检测，若当前是以太接口，其加入Eth-Trunk后不能配置此参数。

        :return: The na_msg_check of this LSWGetEthTrunkPortDto.
        :rtype: bool
        """
        return self._na_msg_check

    @na_msg_check.setter
    def na_msg_check(self, na_msg_check):
        """
        Sets the na_msg_check of this LSWGetEthTrunkPortDto.
        NA报文检测，若当前是以太接口，其加入Eth-Trunk后不能配置此参数。

        :param na_msg_check: The na_msg_check of this LSWGetEthTrunkPortDto.
        :type: bool
        """

        self._na_msg_check = na_msg_check

    @property
    def ns_msg_check(self):
        """
        Gets the ns_msg_check of this LSWGetEthTrunkPortDto.
        NS报文检测，若当前是以太接口，其加入Eth-Trunk后不能配置此参数。

        :return: The ns_msg_check of this LSWGetEthTrunkPortDto.
        :rtype: bool
        """
        return self._ns_msg_check

    @ns_msg_check.setter
    def ns_msg_check(self, ns_msg_check):
        """
        Sets the ns_msg_check of this LSWGetEthTrunkPortDto.
        NS报文检测，若当前是以太接口，其加入Eth-Trunk后不能配置此参数。

        :param ns_msg_check: The ns_msg_check of this LSWGetEthTrunkPortDto.
        :type: bool
        """

        self._ns_msg_check = ns_msg_check

    @property
    def rs_msg_check(self):
        """
        Gets the rs_msg_check of this LSWGetEthTrunkPortDto.
        RS报文检测，若当前是以太接口，其加入Eth-Trunk后不能配置此参数。

        :return: The rs_msg_check of this LSWGetEthTrunkPortDto.
        :rtype: bool
        """
        return self._rs_msg_check

    @rs_msg_check.setter
    def rs_msg_check(self, rs_msg_check):
        """
        Sets the rs_msg_check of this LSWGetEthTrunkPortDto.
        RS报文检测，若当前是以太接口，其加入Eth-Trunk后不能配置此参数。

        :param rs_msg_check: The rs_msg_check of this LSWGetEthTrunkPortDto.
        :type: bool
        """

        self._rs_msg_check = rs_msg_check

    @property
    def ipsg_check(self):
        """
        Gets the ipsg_check of this LSWGetEthTrunkPortDto.
        IPSG检测使能开关。

        :return: The ipsg_check of this LSWGetEthTrunkPortDto.
        :rtype: bool
        """
        return self._ipsg_check

    @ipsg_check.setter
    def ipsg_check(self, ipsg_check):
        """
        Sets the ipsg_check of this LSWGetEthTrunkPortDto.
        IPSG检测使能开关。

        :param ipsg_check: The ipsg_check of this LSWGetEthTrunkPortDto.
        :type: bool
        """

        self._ipsg_check = ipsg_check

    @property
    def dai_check(self):
        """
        Gets the dai_check of this LSWGetEthTrunkPortDto.
        DAI检测使能开关。

        :return: The dai_check of this LSWGetEthTrunkPortDto.
        :rtype: bool
        """
        return self._dai_check

    @dai_check.setter
    def dai_check(self, dai_check):
        """
        Sets the dai_check of this LSWGetEthTrunkPortDto.
        DAI检测使能开关。

        :param dai_check: The dai_check of this LSWGetEthTrunkPortDto.
        :type: bool
        """

        self._dai_check = dai_check

    @property
    def ip_subnet_vlan_enable(self):
        """
        Gets the ip_subnet_vlan_enable of this LSWGetEthTrunkPortDto.
        IP子网划分Vlan开关。

        :return: The ip_subnet_vlan_enable of this LSWGetEthTrunkPortDto.
        :rtype: bool
        """
        return self._ip_subnet_vlan_enable

    @ip_subnet_vlan_enable.setter
    def ip_subnet_vlan_enable(self, ip_subnet_vlan_enable):
        """
        Sets the ip_subnet_vlan_enable of this LSWGetEthTrunkPortDto.
        IP子网划分Vlan开关。

        :param ip_subnet_vlan_enable: The ip_subnet_vlan_enable of this LSWGetEthTrunkPortDto.
        :type: bool
        """

        self._ip_subnet_vlan_enable = ip_subnet_vlan_enable

    @property
    def eth_trunk_mode(self):
        """
        Gets the eth_trunk_mode of this LSWGetEthTrunkPortDto.
        ethTrunk接口的工作模式。取值：lacp（lacp模式）；manual（手工模式）。

        :return: The eth_trunk_mode of this LSWGetEthTrunkPortDto.
        :rtype: str
        """
        return self._eth_trunk_mode

    @eth_trunk_mode.setter
    def eth_trunk_mode(self, eth_trunk_mode):
        """
        Sets the eth_trunk_mode of this LSWGetEthTrunkPortDto.
        ethTrunk接口的工作模式。取值：lacp（lacp模式）；manual（手工模式）。

        :param eth_trunk_mode: The eth_trunk_mode of this LSWGetEthTrunkPortDto.
        :type: str
        """

        self._eth_trunk_mode = eth_trunk_mode

    @property
    def port_member_list(self):
        """
        Gets the port_member_list of this LSWGetEthTrunkPortDto.
        EthTrunk接口成员列表。

        :return: The port_member_list of this LSWGetEthTrunkPortDto.
        :rtype: list[str]
        """
        return self._port_member_list

    @port_member_list.setter
    def port_member_list(self, port_member_list):
        """
        Sets the port_member_list of this LSWGetEthTrunkPortDto.
        EthTrunk接口成员列表。

        :param port_member_list: The port_member_list of this LSWGetEthTrunkPortDto.
        :type: list[str]
        """

        self._port_member_list = port_member_list

    @property
    def name(self):
        """
        Gets the name of this LSWGetEthTrunkPortDto.
        EthTrunk端口名称，必须是Eth-Trunk[数字]的格式，数字最大63。

        :return: The name of this LSWGetEthTrunkPortDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this LSWGetEthTrunkPortDto.
        EthTrunk端口名称，必须是Eth-Trunk[数字]的格式，数字最大63。

        :param name: The name of this LSWGetEthTrunkPortDto.
        :type: str
        """
        if name is not None and len(name) > 11:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `11`")
        if name is not None and len(name) < 10:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `10`")

        self._name = name

    @property
    def is_up_stream(self):
        """
        Gets the is_up_stream of this LSWGetEthTrunkPortDto.
        端口是否为上行口（只读）。

        :return: The is_up_stream of this LSWGetEthTrunkPortDto.
        :rtype: bool
        """
        return self._is_up_stream

    @is_up_stream.setter
    def is_up_stream(self, is_up_stream):
        """
        Sets the is_up_stream of this LSWGetEthTrunkPortDto.
        端口是否为上行口（只读）。

        :param is_up_stream: The is_up_stream of this LSWGetEthTrunkPortDto.
        :type: bool
        """

        self._is_up_stream = is_up_stream

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
        if not isinstance(other, LSWGetEthTrunkPortDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
