# UserAuthorizationInputDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_mac** | **str** | 设备MAC地址，MAC和ESN至少有一个必填。 | [optional] 
**device_esn** | **str** | 设备ESN地址，MAC和ESN至少有一个必填。 | [optional] 
**ap_mac** | **str** | AP的MAC地址。 | [optional] 
**ssid** | **str** | AP ssid名称的BASE64编码。 | 
**policy_name** | **str** | 访问控制策略名称，为空时不做访问策略控制。 | [optional] 
**terminal_ip_v4** | **str** | 终端IPV4地址，terminalIpV4和terminalIpV6有且只有一个必填。 | [optional] 
**terminal_ip_v6** | **str** | 终端IPV6地址，terminalIpV4和terminalIpV6有且只有一个必填。 | [optional] 
**terminal_mac** | **str** | 终端MAC。 | 
**user_name** | **str** | 用户名。 | 
**node_ip** | **str** | 授权节点地址。 | 
**tem_permit_time** | **int** | 临时放行时长，单位秒。报文中不传递此参数或取值为0时，终端用户访问网络无时间限制。 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


