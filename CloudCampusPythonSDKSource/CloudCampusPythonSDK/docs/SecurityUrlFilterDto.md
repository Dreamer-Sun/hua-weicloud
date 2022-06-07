# SecurityUrlFilterDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** | 是否使能URL过滤。创建SSID时，若未填写此字段，默认值为true。该黑白名单机制对使用代理服务器的浏览器不生效。 | [optional] 
**mode** | **int** | URL过滤类型，当enable为true时mode字段必填。 0---黑名单 1---白名单 | [optional] 
**urls** | **list[str]** | URL列表。URL长度4-80个字符。当enable为true时有效。mode为0时，urls表示允许访问未匹配的url；mode为1时，urls表示禁止访问未匹配的url。每个URL限制要求：&#39;*&#39;只能出现在首尾，&#39;*&#39;不算做有效字符，前后空格忽略，前缀&#39;http://&#39;忽略，且不能含有全角字符。 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


