# ReriodRebootDeviceParam

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **int** | 设备重启类型。 0---CANCEL，取消重启任务。 1---NOW，立即重启。 2---IN，延时重启。 3---AT，定时重启。 | [optional] 
**reboot_in** | **str** | DD:HH:MM，延时重启时间，mode为IN时必填。必须大于0天，小于等于30天。 | [optional] 
**reboot_at** | **int** | 定时重启时间，mode为AT时必填，时间戳格式，单位为秒。必须大于当前时间，且与当前时间间隔小于等于30天。 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


