# BatchModifyDevices

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **str** | 设备ID。 | [optional] 
**esn** | **str** | 设备ESN，未注册状态的设备可以修改。 | [optional] 
**name** | **str** | 设备名称，若不传或传值为空，则以ESN号命名设备，设备名称不能包含\&quot;?\&quot;或者制表符TAB。 | [optional] 
**description** | **str** | 设备详情描述。 | [optional] 
**system_ip** | **str** | 系统IP地址。SD-WAN场景下，创建TNP、站点激活之后不能修改。 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


