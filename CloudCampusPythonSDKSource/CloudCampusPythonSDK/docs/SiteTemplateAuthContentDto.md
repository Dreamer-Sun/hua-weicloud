# SiteTemplateAuthContentDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** | 关联SSID时的认证模式，当mode为mac或dot1x时radius必填。 | 
**psk_encrypt_type** | **str** | 加密模式，当mode为psk或ppsk时必选。大小写敏感，前后不能有空格，且不能含有全角字符。当mode为ppsk时加密方式不支持wep。 | [optional] 
**security_key** | **str** | psk密钥，当mode为psk时必选。查询始终为null。 当pskEncryptType为wep时，5位字符与数字组合的字符串。 当pskEncryptType为wpa1AndWpa2或wpa2时，8-63位字母、数字及除问号与空格外的特殊字符组合。 | [optional] 
**security_key_type** | **str** | wpa2加密方法，当pskEncryptType为wpa2时必选，默认值为AES。大小写敏感，前后不能有空格，且不能含有全角字符。 | [optional] 
**dot1x_encrypt_type** | **str** | dot1x加密模式，当mode为dot1x时必选。大小写敏感，前后不能有空格，且不能含有全角字符。 | [optional] 
**mac_auto_binding** | **bool** | 是否MAC自动绑定。当mode为ppsk时，此参数必填。若值为true，则开启MAC自动绑定。 | [optional] 
**escape_strategy** | **str** | 逃生策略。当mode为ppsk时，此参数必填。 noNew：允许已认证用户继续使用网络，新用户不允许接入。默认值。 noAuth：允许已认证用户继续使用网络，新用户需要输入PPSK密钥。注意：此时PPSK用户数控制、MCA自动绑定功失效。  | [optional] 
**portal** | [**SiteTemplatePortalContentDto**](SiteTemplatePortalContentDto.md) |  | [optional] 
**radius** | [**SiteTemplateRadiusContentDto**](SiteTemplateRadiusContentDto.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


