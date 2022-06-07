# SiteTemplateSsidConfigOut

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | SSID名称。长度为1~32字节（UTF-8编码），不能包含特殊符号&amp;、&#x3D;、？、#、%、+。当以空格开头或结尾时，最大长度减少2字节；当以\&quot;开头时，最大长度减少1字节。 | 
**enable** | **bool** | 工作状态开启。 | 
**time_template_id** | **str** | 时间模板ID。时间模板可以通过第三方开放接口https://host:port/controller/campus/v3/networkconfig/timetemplate得到。 | [optional] 
**connection_mode** | **str** | 网络连接方式，大小写敏感，前后不能有空格，且不能含有全角字符。 | 
**vlans** | [**list[SiteTemplateVlanDto]**](SiteTemplateVlanDto.md) | SSID所属的VLAN配置信息。站点模板与站点配置的AP SSID不同，此处站点模板的同一SSID所属VLAN不支持按照标签进行差异化配置，最大仅可以配置一个SiteTemplateVlanDto对象，考虑后续扩展，采用数组方式。 | [optional] 
**hided_enable** | **bool** | 是否隐藏SSID。 | 
**relative_radios** | **int** | 射频类型。 1 --- 2.4G(wlan-radio 0/0/0)。 2 --- 5G(wlan-radio 0/0/1)。 3 --- 2.4G(wlan-radio 0/0/0)&amp;5G(wlan-radio 0/0/1)。 4 --- 5G(wlan-radio 0/0/2)。 5 --- 2.4G(wlan-radio 0/0/0)&amp;5G(wlan-radio 0/0/2)。 6 --- 5G(wlan-radio 0/0/1)&amp;5G(wlan-radio 0/0/2)。 7 --- 2.4G(wlan-radio 0/0/0)&amp;5G(wlan-radio 0/0/1)&amp;5G(wlan-radio 0/0/2)。 | 
**frequency_navigation** | **bool** | 是否开启频谱导航。 | [optional] 
**max_user_number** | **int** | 最大用户数。 | 
**user_separation** | **bool** | 是否用户隔离。 | 
**ssid_auth** | [**SiteTemplateAuthContentDto**](SiteTemplateAuthContentDto.md) |  | 
**ssid_policy** | [**SiteTemplatePolicyContentDto**](SiteTemplatePolicyContentDto.md) |  | [optional] 
**dot11r** | **bool** | 使能802.11r快速漫游功能。 | [optional] 
**reassociate_timeout** | **int** | 重新关联的超时时间，单位为秒。 | [optional] 
**id** | **str** | SSID唯一标识。 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


