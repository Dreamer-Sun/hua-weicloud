# InterdictionDTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block_id** | **str** | 事件ID，UUID格式，必填。 | 
**tenant** | **str** | 租户ID，UUID格式。 | [optional] 
**producer** | **str** | 调用者。 | [optional] 
**direction** | **int** | 流量方向，0-单向，1-双向，默认为0，必填。 | 
**src_ips** | **list[str]** | 源IP列表，非必填；非空必须满足合法的IPV4，IPV6格式，最多8个IP；源IP列表和目的IP列表不可同时为空。 | [optional] 
**dst_ips** | **list[str]** | 目的IP列表，非必填；非空必须满足合法的IPV4，IPV6格式，最多只能填1个目的IP；源IP列表和目的IP列表不可同时为空。 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


