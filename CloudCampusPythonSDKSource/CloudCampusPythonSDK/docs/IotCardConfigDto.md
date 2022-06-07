# IotCardConfigDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card_name** | **str** | 插卡名称 | [optional] 
**card_configured** | **bool** | 该卡槽是否配置，true代表已经配置，false代表没配置。 | [optional] 
**port_type** | **str** | 端口类型。ethernet---以太网口，serial---串口。 | 
**communication_port** | **int** | 通信端口。 | [optional] 
**communication_protocol** | **str** | 通信协议。 | [optional] 
**share_key** | **str** | 共享秘钥，至少包含小写字母、大写字母、数字、特殊符号（除问号和空格）中的两种，不能包含全角字符。 | [optional] 
**trusted_host_address** | **str** | 信任主机地址，格式为IP/掩码。 | [optional] 
**iot_server2** | **str** | 第二通道IoT服务器，支持域名和IP地址。 | [optional] 
**port2** | **int** | 第二通道IoT端口。 | [optional] 
**administrative_status** | **bool** | 使能管理状态。 | [optional] 
**default_vlan** | **int** | 默认放通VLAN。 | [optional] 
**description** | **str** | 描述，不能输入中文和特殊字符。 | [optional] 
**iot_server1_config** | [**list[IotServer1Dto]**](IotServer1Dto.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


