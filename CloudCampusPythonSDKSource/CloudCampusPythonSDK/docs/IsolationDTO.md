# IsolationDTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block_id** | **str** | 事件ID，UUID格式。 | 
**vm_ip** | **str** | 主机IP，只支持IPV4格式。 | 
**tenant** | **str** | 租户ID，UUID格式。 | [optional] 
**producer** | **str** | 调用者。 | [optional] 
**exception_ips** | **list[str]** | 例外IP列表，最多支持8个IP列表，支持IPV4和IPV6格式。 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


