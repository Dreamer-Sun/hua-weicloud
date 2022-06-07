# RestartPolicyDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | 重启策略，immediately（立即重启），weektime（周期重启）二者之一。 如果是立即重启场景，type填写immediately； 如果是周期重启场景，type填写|weektime，day，daytime和timeZoneOffSet会生效。  | [optional] 
**day** | **str** | 周几。 | [optional] 
**daytime** | **str** | 按周重启，配置重启时间，格式为hh:mm:ss。 | [optional] 
**time_zone_off_set** | **str** | 时区，UTC+08:00。 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


