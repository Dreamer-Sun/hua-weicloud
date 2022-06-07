# AclDtoInResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | ACL模板名称，包括汉字、字母、数字、下划线、.、@、-不能与已有的名称重复。 | 
**acl_number** | **str** | ACL模板编号，必须为数字，aclType为Advanced时，aclNumber范围：3001-3999，aclType为User时，aclNumber范围：6000-6031。 | 
**description** | **str** | ACL模板描述。 | [optional] 
**acl_type** | **str** | ACL模板类型。 | 
**rule_list** | [**list[RuleList]**](RuleList.md) | 规则列表。 | 
**id** | **str** | ACL模板标识，UUID格式。 | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


