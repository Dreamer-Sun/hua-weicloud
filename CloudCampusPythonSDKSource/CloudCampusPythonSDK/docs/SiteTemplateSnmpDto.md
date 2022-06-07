# SiteTemplateSnmpDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snmp_enable** | **bool** | SNMP使能开关。 | 
**protocol_version** | **str** | 协议版本，只能为V1、V2C、V3其中一种，当snmpEnable为true时，protocolVersion生效且不能为空。 | [optional] 
**group_name** | **str** | 团体名，当snmpEnable为true且protocolVersion为V1或V2C时，groupName生效且不能为空。 | [optional] 
**user_infos** | [**list[UserInfosDto]**](UserInfosDto.md) | 用户列表，当snmpEnable为true且protocolVersion为V3时，userInfos生效且不能为空。 | [optional] 
**acl_ips** | **list[str]** | IP地址限定，当snmpEnable为true时，aclIps生效。 | [optional] 
**trap_enable** | **bool** | 告警服务器使能开关，当snmpEnable为true时，trapEnable生效。 | [optional] 
**target_hosts** | [**list[TargetHostsDto]**](TargetHostsDto.md) | 告警服务器列表，当trapEnable为true时，targetHosts生效且不能为空。 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


