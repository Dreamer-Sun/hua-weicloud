# FlowDistrModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_name** | **str** | \&quot;capture_rate\&quot;：终端捕获率。 \&quot;passersby\&quot;：客户类型，路人。 \&quot;visitors\&quot;：客户数量，访客。 \&quot;connected\&quot;：客户数量，接入用户。 \&quot;within_one_hr\&quot;：驻留时长小于一小时的客户数量。 \&quot;one_hr_to_six_hrs\&quot;：驻留时长大于一小时小于6小时的客户数量。 \&quot;more_than_six_hrs\&quot;：驻留时长大于6小时的客户数量。 \&quot;average_staytime\&quot;：平均驻留时长的客户数量。 \&quot;first_time\&quot;：首次访问的客户数量。 \&quot;occasionally\&quot;：偶尔访问的客户数量。 \&quot;regularly\&quot;：经常访问的客户数量。 \&quot;frequently\&quot;：频繁访问的客户数量。 \&quot;repeat_rate\&quot;：重复访问率。 \&quot;humanflow\&quot;：客流量。  | [optional] 
**counts** | [**list[Count]**](Count.md) | 对应时间的客流量。 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


