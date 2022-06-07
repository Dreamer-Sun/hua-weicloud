# RuleList

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_id** | **str** | 规则优先级编号，仅高级ACL有效且必填。 | [optional] 
**ip** | **str** | IP地址，仅用户ACL有效且必填。与domain共存时，优先级高于domain。例如：192.168.1.0/24 | [optional] 
**domain** | **str** | 域名，仅用户ACL有效且必填。例如：www.example.com | [optional] 
**policy** | **str** | 策略，aclType为高级acl时有效且必填，有效值permit，deny。 | [optional] 
**protocol** | **str** | 协议，aclType为高级acl时有效且必填，有效值udp，tcp，any，icmp。 | [optional] 
**src_ip** | **str** | 源IP地址，可以输入Any表示任意IP，仅高级ACL有效且必填。 | [optional] 
**src_port** | **str** | 源端口号，或源端口段，仅高级ACL有效，范围：整数（例如1000）或者整数段（1-100），且整数和整数段包含的值在0~65535。 | [optional] 
**dst_ip** | **str** | 目的IP地址，可以输入Any表示任意IP，仅高级ACL有效且必填。 | [optional] 
**dst_port** | **str** | 目的端口号，或目的端口段，仅高级ACL有效，范围：整数（例如1000）或者整数段（1-100），且整数和整数段包含的值在0~65535。 | [optional] 
**description** | **str** | 规则描述。 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


