# ModifyDeviceDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | 设备名称，名字为空或者不传时，名字修改为ESN号，设备名称不能包含\&quot;?\&quot;或者制表符TAB。 | [optional] 
**description** | **str** | 描述。 | [optional] 
**site_id** | **str** | 站点ID，如果传入字符串为空，则从站点中移除设备。修改站点ID后，设备的标签列表会清空。 | [optional] 
**esn** | **str** | 设备ESN，未注册状态的设备可以修改。 | [optional] 
**tags** | **list[str]** | 设备标签列表，修改标签列表时，设备的siteId不能为空，只支持AP设备。 | [optional] 
**system_ip** | **str** | 系统IP地址。SD-WAN场景下，创建TNP、站点激活之后不能修改。 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


