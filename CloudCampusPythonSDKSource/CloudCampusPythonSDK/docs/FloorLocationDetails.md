# FloorLocationDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | 楼层名称。 | 
**building_name** | **str** | 楼层所属楼栋名称。 | 
**image** | **str** | 楼层图纸。 | 
**scale** | **float** | 比例尺，表示图上距离与实际距离的比，例如：图上0.01米代表实际1米，则比例尺为0.01。 | [optional] 
**located_device_list** | [**list[LocatedDeviceInfo]**](LocatedDeviceInfo.md) | 已布放设备列表。 | 
**un_located_device_list** | [**list[DeviceInfo]**](DeviceInfo.md) | 未布放设备列表。 | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


