# CreateTacacsTmplInfoDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | 名称（不支持$&amp;?&#x3D;+%][^_,#\&quot;相关特殊字符）。 | 
**description** | **str** | 描述。 | [optional] 
**master_authen_server_ip** | **str** | 主认证服务器IP地址。 | 
**master_authen_server_port** | **int** | 主认证服务器端口。 | 
**slave_authen_server_ip** | **str** | 备认证服务器IP地址。 | [optional] 
**slave_authen_server_port** | **int** | 备认证服务器端口。 | [optional] 
**master_author_server_ip** | **str** | 主授权服务器IP地址。 | [optional] 
**master_author_server_port** | **int** | 主授权服务器端口。 | [optional] 
**slave_author_server_ip** | **str** | 备授权服务器IP地址。 | [optional] 
**slave_author_server_port** | **int** | 备授权服务器端口。 | [optional] 
**master_acc_server_ip** | **str** | 主计费服务器IP地址。 | [optional] 
**master_acc_server_port** | **int** | 主计费服务器端口。 | [optional] 
**slave_acc_server_ip** | **str** | 备计费服务器IP地址。 | [optional] 
**slave_acc_server_port** | **int** | 备计费服务器端口。 | [optional] 
**include_domain** | **bool** | 向Tacacs服务器发起认证的用户名是否包含域名。 | [optional] 
**share_key** | **str** | 秘钥（英文字母、数字、除空格和问号外特殊符号，建议长度为6位以上）。 | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


