# DeviceArStaticrouteInfoDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mask** | **str** | 掩码，0-32。创建后不允许修改。 | 
**description** | **str** | 描述。 | [optional] 
**next_address** | **str** | 下一跳地址，必须是合法的IPv4地址，以127或者224~255开头的IP地址为非法IP地址。当nextInterface为空时，nextAddress必填。 | [optional] 
**destination_ip** | **str** | 目的IP地址，创建后不允许修改。必须是合法的IPv4地址，以127或者224~255开头的IP地址为非法IP地址。 | 
**priority** | **int** | 优先级，取值越小优先级越高。 | [optional] 
**next_interface** | **str** | 路由出接口。当nextAddress为空时，nextInterface必填。 | [optional] 
**nqa_id** | **str** | NQA的ID。 | [optional] 
**nqa_admin_name** | **str** | NQA的admin名称。 | [optional] 
**nqa_test_name** | **str** | NQA的测试名称。 | [optional] 
**dhcp** | **bool** | DHCP开关使能。当nextAddress非空时，dhcp必须为false。 | [optional] 
**next_logic_interface** | **str** | 逻辑出接口。 | [optional] 
**id** | **str** | 路由器静态路由ID。 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


