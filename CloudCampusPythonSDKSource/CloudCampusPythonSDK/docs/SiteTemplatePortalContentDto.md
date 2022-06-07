# SiteTemplatePortalContentDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** | 认证方式。 portalDisable---不启用Portal认证。 portalThirdIndirect---云平台中继认证（对接方式：API）。 | 
**free_auth_enable** | **bool** | 有效期内免认证是否开启，当mode为portalThirdIndirect时必选。 | [optional] 
**auth_expire_unit** | **str** | Portal认证有效期单位，ssid创建场景：freeAuthEnable为true时，此字段不传则默认值为minute；ssid更新场景：freeAuthEnable为true时，此字段不传则使用更新前的值。只能为day、hour、minute中的一个，大小写不敏感，前后空格忽略，且不能含有全角字符。 | [optional] 
**auth_expire** | **int** | Portal认证有效期，ssid创建场景：freeAuthEnable为true时，此字段不传则默认值为2；ssid更新场景：freeAuthEnable为true时，此字段不传则使用更新前的值。 authExpireUnit为minute时，范围为1~59。 authExpireUnit为hour时，范围为1~23。 authExpireUnit为day时，范围为1~365。 | [optional] 
**escape_strategy** | **int** | 逃生策略，当mode为portalThirdIndirect时有效。 1---允许已认证用户继续使用网络，新用户不允许接入，默认值 2---允许用户接入，不需要认证 | [optional] 
**free_acl_tmpl_id** | **str** | 免认证ACL，当mode为portalThirdIndirect时必填。免认证ACL可以通过第三方开放接口/controller/campus/v3/profile/acl得到。UUID格式。 | [optional] 
**free_acl_tmpl_name** | **str** | 免认证ACL名称，当mode为portalThirdIndirect时有效。POST与PUT操作时，该字段无效。长度为1至32字节。 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


