# IpBindingMacConfigApiDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**static_ip_address** | **str** | IP地址，不能与列表中其他IP重复。IP为上面网段（IP+mask计算得出）中的可分配IP地址，且不能为网关IP（上面配置IP）。 | 
**static_mac_address** | **str** | MAC地址，不能与列表中其他MAC地址重复。MAC不能为广播（全F），组播（第一段2进制表示以“1”结尾）。 | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


