# PolicyHitsDTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **str** | 开始日期，非空时要求是合法的日期格式；如果开始日期和结束日期同时为空，默认查过去一个月的数据，yyyy-MM-dd HH:mm:ss。 | [optional] 
**end_date** | **str** | 结束日期，非空时要求是合法的日期格式；如果开始日期和结束日期同时为空，默认查过去一个月的数据，yyyy-MM-dd HH:mm:ss。 | [optional] 
**producer** | **str** | 调用者。 | [optional] 
**block_ids** | **list[str]** | 事件ID列表，UUID格式；Campus融合场景，blockIds为必填字段；DCN融合场景，blockIds和policyNames不可同时为空，都传的情况下，以blockIds为准。 | 
**policy_names** | **list[str]** | 策略名称。Campus融合，该字段没有业务上的意义，不需要填写；DCN融合场景，blockIds和policyNames不可同时为空，都传的情况下，以blockIds为准。 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


