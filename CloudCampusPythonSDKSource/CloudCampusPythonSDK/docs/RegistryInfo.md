# RegistryInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**system_id** | **str** | 第三方系统标识。(可为IP地址，1~64个字符，字符集合为英文半角：0-9a-zA-Z@_-(),.^$~&#x60;!) | 
**open_id** | **str** | 网管主动连接第三方系统的认证凭证，由第三方系统分配和利用此字符串认证。(1~1024个字符，字符集同systemID。) | 
**url** | **str** | 网管以POST方式向该URL发送通知消息。(需要通知消息订阅者确保URL的正确性，IP地址为OpenAPI白名单列表中地址。长度1~1024，字符串符合HTTP的URL编码规范。) | 
**data_type** | **str** | 通知报文的data字段类型。(目前仅支持\&quot;JSON\&quot;，缺省为\&quot;JSON\&quot;。) | [optional] 
**desc** | **str** | 第三方系统描述。(缺省为null不设置。如设置长度限制0~1024字符，字符集合不限制。) | [optional] [default to 'null']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


