# UpgradePolicydetail

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **str** | 设备标识，UUID格式。 | [optional] 
**signature_database_type** | **str** | 设备特征库升级类型。 | [optional] 
**version** | **str** | 设备特征库版本。 | [optional] 
**status** | **int** | 设备特征库升级状态。取值如下：-1---升级失败，0---未配置，1---初始化 ，10---升级完成，11---升级中。 | [optional] 
**last_upgrade_time** | **int** | 上次特征库升级时间，UTC时间格式。 | [optional] 
**next_upgrade_time** | **int** | 下次特征库升级时间，UTC时间格式。 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


