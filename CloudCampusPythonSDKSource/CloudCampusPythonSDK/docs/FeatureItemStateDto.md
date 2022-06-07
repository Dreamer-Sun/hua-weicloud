# FeatureItemStateDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | 单个特性ID。 | [optional] 
**name** | **str** | 单个特性名称。 | [optional] 
**message_id** | **str** | 下发单个特性的报文ID。 | [optional] 
**operation** | **int** | 单个特性对应的操作类型，取值范围：0---新增(Add)；1---删除(Delete)；2---修改(Update)。 | [optional] 
**state** | **int** | 单个特性的配置下发状态，取值范围：0---成功；1---告警；2---预配置；3---失败；4---正在下发。 | [optional] 
**error_message** | **str** | 错误信息。 | [optional] 
**update_time** | **str** | 更新时间。 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


