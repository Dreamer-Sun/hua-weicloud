# PingReplyResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **str** | ping探测任务ID，格式UUID。 | 
**total_count** | **int** | 总探测次数。 | 
**success_count** | **int** | 成功探测次数。 | 
**loss_rate** | **float** | 丢失率。单位：百分比。 | 
**rtt_avg** | **int** | 报文平均响应时间，单位：毫秒。 | 
**status** | **int** | 探测状态。 0 --- 成功 1 --- 执行中 2 --- 超时  | 
**ping_reply** | [**PingReplyResultPingReply**](PingReplyResultPingReply.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


