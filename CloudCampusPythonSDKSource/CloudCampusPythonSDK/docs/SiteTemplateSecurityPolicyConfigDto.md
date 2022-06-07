# SiteTemplateSecurityPolicyConfigDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**security_acl_tmpl_id** | **str** | 安全ACL模板ID。安全ACL模板可以通过第三方开放接口/controller/campus/v3/profile/acl得到。UUID格式。 | [optional] 
**security_acl_tmpl_name** | **str** | ACL模板名称。POST与PUT操作时，该字段无效。长度为1至32字节。 | [optional] 
**ipsec_acl_tmpl_id** | **str** | IPSEC ACL模板ID。IPSEC ACL模板可以通过第三方开放接口https://host:port/controller/campus/v3/profile/acl得到。UUID格式。 | [optional] 
**ipsec_acl_tmpl_name** | **str** | IPSEC ACL模板名称。POST与PUT操作时，该字段无效。长度为1至32字节。 | [optional] 
**url_filter** | [**SiteTemplateSecurityUrlFilterDto**](SiteTemplateSecurityUrlFilterDto.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


