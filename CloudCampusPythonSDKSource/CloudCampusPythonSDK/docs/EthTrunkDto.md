# EthTrunkDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lag_id** | **int** | LAG ID。 | [optional] 
**mode** | **str** | trunk模式：lacp、manual。 | [optional] 
**hash** | **str** | 端口负载均衡的hash算法：dst-ip、dst-mac、src-ip、src-mac、src-dst-ip、src-dst-mac、enhanced、diffluence。 | [optional] 
**least_active** | **int** | Eth-trunk中活动链路数量的下限。 | [optional] 
**max_active** | **int** | 最大激活链路数。 | [optional] 
**op_status** | **str** | 操作状态：up、down。 | [optional] 
**port_count** | **int** | Eth-trunk上行端口数量。 | [optional] 
**sys_prio** | **int** | 本地系统优先级。 | [optional] 
**sys_id** | **str** | 本地系统ID。 | [optional] 
**interfaces** | [**list[EthTrunkInterfacesDto]**](EthTrunkInterfacesDto.md) | 接口列表。 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


