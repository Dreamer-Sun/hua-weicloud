# StpDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stp_mode** | **int** | STP模式。1表示MSTP，2表示RSTP。 | 
**mstp_regions** | [**list[MstpRegion]**](MstpRegion.md) | MST域集合。MSTP模式下需要配置。 | [optional] 
**rstp_config** | [**list[RegionInstanceDevice]**](RegionInstanceDevice.md) | RSTP优先级。RSTP模式下需要配置。 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


