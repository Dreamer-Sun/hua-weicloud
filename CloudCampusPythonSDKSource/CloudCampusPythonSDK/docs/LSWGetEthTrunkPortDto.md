# LSWGetEthTrunkPortDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** | 接口管理状态（true为undo shutdown，false为shutdown）。 | [optional] 
**description** | **str** | 接口描述。 | [optional] 
**link_type** | **str** | 链路类型，若当前是以太接口，其加入Eth-Trunk后不能配置此参数。取值：access；trunk。 | [optional] 
**default_vlan** | **int** | access类型下缺省VLAN；或trunk类型下pvid。若当前是以太接口，其加入Eth-Trunk后不能配置此参数。 | [optional] 
**allow_pass_vlan** | **str** | trunk类型下允许通过VLAN，接口为trunk类型时必填。 | [optional] 
**dhcp_snooping** | **bool** | DHCP Snooping使能，若当前是以太接口，其加入Eth-Trunk后不能配置此参数。 | [optional] 
**dhcp_snooping_trusted** | **bool** | 配置接口为DHCP Snooping信任状态，默认为非信任状态。 | [optional] 
**nd_snooping** | **bool** | ND Snooping使能，若当前是以太接口，其加入Eth-Trunk后不能配置此参数。 | [optional] 
**nd_snooping_trusted** | **bool** | 配置接口为ND Snooping信任状态，默认为非信任状态。 | [optional] 
**port_isolation** | **bool** | 端口隔离使能，若当前是以太接口，其加入Eth-Trunk后不能配置此参数。 | [optional] 
**stp** | **bool** | STP功能状态，取值：true（使能）；false（未使能）。当STP为false时，stpEdgedport自动赋值为normal，传入其他参数无效。 | [optional] 
**stp_edgedport** | **str** | STP边缘端口状态，若当前是以太接口，其加入Eth-Trunk后不能配置此参数。取值：enable（使能）；normal（遵从全局状态）；disable（未使能）。 | [optional] 
**enable_relay** | **bool** | 堆叠多主检测场景下，设为检测代理设备。 | [optional] 
**enable_mad_detection** | **bool** | 堆叠多主检测场景下，代理模式双主检测开关。 | [optional] 
**domain_id** | **int** | 堆叠多主检测场景下，堆叠域编号，两个堆叠互相检测时，堆叠域编号需不同。 | [optional] 
**na_msg_check** | **bool** | NA报文检测，若当前是以太接口，其加入Eth-Trunk后不能配置此参数。 | [optional] 
**ns_msg_check** | **bool** | NS报文检测，若当前是以太接口，其加入Eth-Trunk后不能配置此参数。 | [optional] 
**rs_msg_check** | **bool** | RS报文检测，若当前是以太接口，其加入Eth-Trunk后不能配置此参数。 | [optional] 
**ipsg_check** | **bool** | IPSG检测使能开关。 | [optional] 
**dai_check** | **bool** | DAI检测使能开关。 | [optional] 
**ip_subnet_vlan_enable** | **bool** | IP子网划分Vlan开关。 | [optional] 
**eth_trunk_mode** | **str** | ethTrunk接口的工作模式。取值：lacp（lacp模式）；manual（手工模式）。 | [optional] 
**port_member_list** | **list[str]** | EthTrunk接口成员列表。 | 
**name** | **str** | EthTrunk端口名称，必须是Eth-Trunk[数字]的格式，数字最大63。 | 
**is_up_stream** | **bool** | 端口是否为上行口（只读）。 | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


