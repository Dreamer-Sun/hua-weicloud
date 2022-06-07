# IotCmdResultInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | 该条记录的唯一标识ID。 | [optional] 
**device_name** | **str** | 设备名称。 | [optional] 
**device_esn** | **str** | 设备ESN。 | [optional] 
**card_mac** | **str** | 插卡MAC。 | [optional] 
**iot_sn** | **str** | IOT插卡SN号。 | [optional] 
**interface** | **str** | AP接口名称。 | [optional] 
**issue_time** | **str** | 命令下发时间。 | [optional] 
**status** | **str** | 插卡命令执行的状态。WAITTING等待执行命令，EXECUTING表示正在执行命令，SUCCESS表示执行命令成功，FAILED表示执行命令失败。 | [optional] 
**detail** | **str** | 插卡命令执行返回详情。 | [optional] 
**fail_reason** | **str** | 插卡命令执行失败的原因。 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


