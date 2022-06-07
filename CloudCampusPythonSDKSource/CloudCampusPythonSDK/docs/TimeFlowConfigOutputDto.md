# TimeFlowConfigOutputDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_flow_name** | **str** | 计费策略名。 | 
**site_id** | **str** | 站点ID，UUID格式。 | 
**enable_traffic_limit_mode** | **bool** | 启用流量控制。 | [optional] 
**traffic_limit_mode** | **int** | 流量限制方式（1---每天，2---每月，3---每周，4---每年），启用流量控制后必填。 | [optional] 
**traffic_limit** | **float** | 流量限制值（兆），启用流量控制后必填。 | [optional] 
**enable_duration_limit_mode** | **bool** | 启用时长控制。 | [optional] 
**duration_limit_mode** | **int** | 时长限制方式（1---每天，2---每月，3---每周，4---每年），启用时长控制后必填。 | [optional] 
**duration_limit** | **float** | 时长限制值（分钟），启用时长控制后必填。 | [optional] 
**is_re_count** | **bool** | 重认证后流量和时长清零并重新计算。 | [optional] 
**is_anonymous** | **bool** | 策略适用于匿名账号。 | [optional] [default to False]
**user_group_ids** | **list[str]** | 用户组ID列表。 | [optional] 
**description** | **str** | 计费策略描述。 | [optional] 
**id** | **str** | 计费策略ID。 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


