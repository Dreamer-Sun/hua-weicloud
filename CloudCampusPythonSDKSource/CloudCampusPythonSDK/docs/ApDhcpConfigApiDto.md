# ApDhcpConfigApiDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip** | **str** | 单播IP地址。 | 
**mask** | **str** | 子网掩码。 | 
**tenancy_config** | [**TenancyConfigApiDto**](TenancyConfigApiDto.md) |  | [optional] 
**master_wins** | **str** | 主wins，单播IP地址（主，备wins不能重复）。 | [optional] 
**slave_wins** | **str** | 备wins，单播IP地址。 | [optional] 
**ip_binding_mac_config_list** | [**list[IpBindingMacConfigApiDto]**](IpBindingMacConfigApiDto.md) | 静态绑定列表，最大8条。IP，MAC都不能重复。 | [optional] 
**lan_vlan_id** | **int** | 不能是已配置的业务VLAN，且修改该VLAN会造成NAT、IPSec用户下线。 | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


