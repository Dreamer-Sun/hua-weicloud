# SiteApInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**select_all** | **bool** | 是否全选该站点的所有Fit AP。 当selectAll为true时，apDeviceIdList不生效，unselectedApDeviceIdList生效，表示将siteId下，且ID不在unselectedApDeviceIdList的Fit AP和指定的WAC设备创建/解除关联关系；当selectAll为false时，apDeviceIdList生效，unselectedApDeviceIdList不生效，表示将siteId下，且ID在apDeviceIdList的Fit AP和指定的WAC设备创建/解除关联关系。 | 
**site_id** | **str** | 站点的ID。 | 
**ap_device_id_list** | **list[str]** | Fit AP的ID的列表。 | [optional] 
**unselected_ap_device_id_list** | **list[str]** | 未选择的Fit AP的ID的列表。 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


