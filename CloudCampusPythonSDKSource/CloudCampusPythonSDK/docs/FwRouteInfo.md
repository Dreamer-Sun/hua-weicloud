# FwRouteInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mask** | **int** | 掩码。 | 
**destination_prefix_ip** | **str** | 目的地址，必须是合法的IPv4地址，以127或者224~255开头的IP地址为非法IP地址。 | [optional] 
**next_hop_address** | **str** | 下一跳地址，必须是合法的IPv4地址，以127或者224~255开头的IP地址为非法IP地址。当nextInterface为空时，nextHopAddress必填。 | [optional] 
**next_interface** | **str** | 设备出接口。当nextHopAddress为空时，nextInterface必填。 | [optional] 
**track_iplink_id** | **str** | IP链接ID。 | [optional] 
**preference** | **int** | 优先级。取值越小，优先等级越高。 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


