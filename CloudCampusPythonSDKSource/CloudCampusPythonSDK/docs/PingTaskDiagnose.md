# PingTaskDiagnose

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **str** | ping探测任务ID，格式UUID。 | 
**destination** | **str** | 目的地址。可以是IP地址或域名，域名中不能包含空格。 | 
**status** | **int** | 探测状态。当探测状态为1时，会根据任务ID查询任务结果。探测状态取值如下： 0 --- 成功 1 --- 执行中 2 --- 超时  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


