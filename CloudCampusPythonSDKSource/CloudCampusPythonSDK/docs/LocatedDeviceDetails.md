# LocatedDeviceDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | 设备ID，格式UUID。 | 
**name** | **str** | 设备名称。 | 
**status** | **str** | 设备状态 0: 正常 1: 告警  3: 离线 4: 未注册  | 
**esn** | **str** | 设备ESN号。 | [optional] 
**mac** | **str** | MAC地址。 | [optional] 
**description** | **str** | 设备备注信息。 | [optional] 
**ap_type** | **str** | AP分类 cloud AP：云AP distributed AP：云分布式AP cloud central AP：云中心AP  | [optional] 
**position_x** | **int** | 设备布放坐标X，单位：像素。 | [optional] 
**position_y** | **int** | 设备布放坐标Y，单位：像素。 | [optional] 
**plan_position_x** | **int** | 设备规划坐标X，单位：像素。 | [optional] 
**plan_position_y** | **int** | 设备规划坐标Y，单位：像素。 | [optional] 
**plan_point_id** | **str** | 网规规划点ID，格式UUID。 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


