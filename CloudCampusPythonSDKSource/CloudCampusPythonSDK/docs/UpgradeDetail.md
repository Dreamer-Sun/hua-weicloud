# UpgradeDetail

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **str** | 设备ID。 | [optional] 
**device_name** | **str** | 设备名称。 | [optional] 
**esn** | **str** | 设备ESN。 | [optional] 
**device_status** | **int** | 设备状态。 0：正常 1：告警 3：离线 4：未注册  | [optional] 
**device_model** | **str** | 设备款型。 | [optional] 
**device_type** | **str** | 设备类型，取值为AP，AR，LSW，FW其中之一。 | [optional] 
**site_name** | **str** | 站点名称。 | [optional] 
**pkg_ver** | **str** | 软件包版本。 | [optional] 
**pkg_percent** | **int** | 软件包下载进度。 | [optional] 
**pkg_up_status** | **int** | 大包升级状态。 0：已创建升级任务，未升级 1：正在下载 2：已下载 5：升级完成 6：无需升级 8：升级失败 9：等待重启上线 10：正在激活大包 11：激活完成 16：取消升级成功 17：取消升级失败 18：下载停止  | [optional] 
**pat_ver** | **str** | 补丁版本。 | [optional] 
**pat_percent** | **int** | 补丁下载进度。 | [optional] 
**pat_up_status** | **int** | 补丁升级状态。 0：已创建升级任务，未升级 1：正在下载 2：已下载 5：升级完成 6：无需升级 8：升级失败 9：等待重启上线 12：正在补丁操作 13：补丁操作完成 16：取消升级成功 17：取消升级失败 18：下载停止  | [optional] 
**failure_cause** | **str** | 失败原因。 | [optional] 
**reboot_time** | **int** | 重启时间。UTC时间。 | [optional] 
**download_time** | **int** | 下载时间。UTC时间。 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


