# QueryStatusResponseDTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block_id** | **str** | 事件ID，UUID格式。 | [optional] 
**status** | **str** | 查询状态。NO_DATA--查询不到数据，SUCCESS--成功，RETRY--需要重试，CE_FAILURE--失败。 | [optional] 
**failed_policy_ids** | **list[str]** | 失败策略列表，UUID格式。 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


