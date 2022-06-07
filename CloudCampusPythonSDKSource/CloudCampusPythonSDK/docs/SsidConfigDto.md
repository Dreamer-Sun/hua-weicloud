# SsidConfigDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | SSID名称。长度为1~32字节（UTF-8编码），不能包含特殊符号&amp;、&#x3D;、？、#、%、+。当以空格开头或结尾时，最大长度减少2字节；当以\&quot;开头时，最大长度减少1字节。 | 
**tags** | [**list[TagDto]**](TagDto.md) | 设备标签列表，总数不能超过10个。如果指定标签列表，SSID会下发给带有列表中标签的设备。如果不指定，会下发给站点所有设备。 | [optional] 
**enable** | **bool** | 工作状态开启。 | 
**connection_mode** | **str** | 网络连接方式，大小写敏感，前后不能有空格，且不能含有全角字符。 | 
**vlans** | [**list[VlanDto]**](VlanDto.md) | SSID所属的VLAN配置信息。当vlans参数为空时系统默认生成一条优先级为0的VLAN配置信息。 | [optional] 
**hided_enable** | **bool** | 是否隐藏SSID。 | 
**relative_radios** | **int** | 射频类型。 1 --- 2.4G(wlan-radio 0/0/0)。 2 --- 5G(wlan-radio 0/0/1)。 3 --- 2.4G(wlan-radio 0/0/0)&amp;5G(wlan-radio 0/0/1)。 4 --- 5G(wlan-radio 0/0/2)。 5 --- 2.4G(wlan-radio 0/0/0)&amp;5G(wlan-radio 0/0/2)。 6 --- 5G(wlan-radio 0/0/1)&amp;5G(wlan-radio 0/0/2)。 7 --- 2.4G(wlan-radio 0/0/0)&amp;5G(wlan-radio 0/0/1)&amp;5G(wlan-radio 0/0/2)。 | 
**frequency_navigation** | **bool** | 是否开启频谱导航。 | [optional] 
**max_user_number** | **int** | 最大用户数。 | 
**user_separation** | **bool** | 是否用户隔离。 | 
**ssid_auth** | [**AuthContentDto**](AuthContentDto.md) |  | 
**ssid_policy** | [**PolicyContentDto**](PolicyContentDto.md) |  | 
**dot11r** | **bool** | 使能802.11r快速漫游功能。 | [optional] 
**reassociate_timeout** | **int** | 重新关联的超时时间，单位为秒。 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


