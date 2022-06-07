# Device

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**esn** | **str** | 设备ESN号。 | [optional] 
**name** | **str** | 设备名称，若不传或传值为空，则以ESN号命名设备，设备名称不能包含\&quot;?\&quot;或者制表符TAB。 | [optional] 
**site_id** | **str** | 站点ID，如果不传，则不添加到任意站点。 | [optional] 
**description** | **str** | 设备详情描述。 | [optional] 
**device_model** | **str** | 设备款型。 | [optional] 
**system_ip** | **str** | 系统IP地址。若systemIp不传或为空，则从地址池中自动分配IP下发给设备的loopback口；若非空，则将指定的systemIp下发给设备的loopback口。 | [optional] 
**tags** | **list[str]** | 设备标签列表，关联标签列表时，站点ID不能为空，只支持AP设备。 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


