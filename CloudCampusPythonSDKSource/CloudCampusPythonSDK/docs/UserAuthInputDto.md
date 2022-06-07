# UserAuthInputDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_type** | **int** | 认证类型。用户名密码：1；匿名认证：2；短信认证：3；passcode认证：6。默认为用户名密码认证(1)。 | [optional] 
**device_mac** | **str** | 设备MAC地址。支持的格式：xx-xx-xx-xx-xx-xx/xx:xx:xx:xx:xx:xx/xxxxxxxxxxxx。 | 
**ssid** | **str** | AP SSID名称。 | 
**terminal_ip** | **str** | 终端IP地址，支持Ipv4和Ipv6地址，Ipv6地址例如：2000:0000:0000:0000:0000:0001。 | 
**terminal_mac** | **str** | 终端MAC地址。支持的格式：xx-xx-xx-xx-xx-xx/xx:xx:xx:xx:xx:xx/xxxxxxxxxxxx。 | 
**user_name** | **str** | 用户名。 | 
**password** | **str** | 用户密码。 | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


