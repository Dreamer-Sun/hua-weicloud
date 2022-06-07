# LSWGetEthPortDto

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
**name** | **str** | 接口名称。 | 
**auto_negotiation_enable** | **bool** | 接口自协商状态，根据款型确定默认值；端口支持自协商时必填。 | [optional] 
**speed** | **str** | 接口速率。可选值：1Gbps，100Mbps，10Mbps，根据款型确定默认值；自协商关闭时必填。 | [optional] 
**duplex** | **str** | 双工模式， 根据款型确定默认值，自协商关闭时必填。取值：half（半双工）；full（全双工）。 | [optional] 
**storm_control** | **bool** | 风暴控制使能。 | [optional] 
**storm_control_model** | **str** | 风暴控制模式。取值：packet（包模式），cir（字节模式）。 | [optional] 
**storm_control_max_rate** | **int** | 风暴控制包模式最大阈值，单位pps。当stormControl字段值为true时，该字段必填。 | [optional] 
**storm_control_min_rate** | **int** | 风暴控制包模式最小阈值，单位pps。当stormControl字段值为true时，该字段必填。 | [optional] 
**storm_control_interval** | **int** | 风暴控制检测时间间隔，单位s。当stormControl字段值为true时，该字段必填。 | [optional] 
**poe** | **bool** | 端口POE使能，支持poe的端口默认值为true；不支持的端口，不能传参。 | [optional] 
**lldp** | **bool** | 端口LLDP使能，默认值为true。若思科的交换机款型需要使用LLDP功能，需要将LLDP置为true，同时CDP为true。 | [optional] 
**cdp** | **bool** | 端口CDP使能，默认值为false。 | [optional] 
**loopback_detect_enabled** | **bool** | 环路检测使能开关。 | [optional] 
**loopback_detect_action** | **str** | 环路检测处理动作。取值范围：shutdown，alarm，block，nolearn，quitvlan。 | [optional] 
**loopback_detect_vlans** | **str** | 环路检测Vlan。1-4094范围内的数字或段，最多支持8个vlan | [optional] 
**is_support_auto_negotiation** | **bool** | 端口是否支持关闭自协商（只读），根据款型确定是否支持。 | [optional] 
**is_support_poe** | **bool** | 端口是否支持POE使能（只读）。 | [optional] 
**media** | **str** | 端口模式（只读）。fiber：光口模式；copper：电口模式。 | [optional] 
**is_up_stream** | **bool** | 端口是否为上行口（只读）。 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


