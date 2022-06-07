# DeviceBean

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | 设备ID。 | [optional] 
**name** | **str** | 设备名称。 | [optional] 
**esn** | **str** | 设备ESN号。 | [optional] 
**device_model** | **str** | 设备款型。 | [optional] 
**device_type** | **str** | 设备类型，支持以下几种：“AR”、“AP”、“FW”或者“LSW”。 | [optional] 
**status** | **str** | 设备状态，0---正常、1---告警、3---离线、4---未注册。 | [optional] [default to '0']
**site_id** | **str** | 设备所属站点的ID。 | [optional] 
**mac** | **str** | 设备MAC。 | [optional] 
**ip** | **str** | 设备IP。 | [optional] 
**ne_type** | **str** | 设备款型。 | [optional] 
**version** | **str** | 设备软件版本。 | [optional] 
**vendor** | **str** | 设备制造商。 | [optional] 
**description** | **str** | 设备备注信息。 | [optional] 
**tenant_id** | **str** | 租户ID。 | [optional] 
**tenant_name** | **str** | 租户名称。 | [optional] 
**site_name** | **str** | 站点名称。 | [optional] 
**create_time** | **str** | 创建时间。 | [optional] 
**register_time** | **str** | 设备首次注册时间。 | [optional] 
**modify_time** | **str** | 修改时间。 | [optional] 
**startup_time** | **str** | 设备重启时间。 | [optional] 
**tags** | **list[str]** | 设备标签列表。 | [optional] 
**system_ip** | **str** | 系统IP地址。 | [optional] 
**patch_version** | **str** | 设备补丁版本。 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


