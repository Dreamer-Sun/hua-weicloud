# AuthenticationLogDetailOutputDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**row_key** | **str** | 数据主键rowkey。 | [optional] 
**access_device_group_name** | **str** | 站点名称。 | [optional] 
**auth_result** | **str** | 认证结果（0---成功，1---失败）。 | [optional] 
**online_time** | **str** | 用户上线起始时间（接口调用方格林威治时间戳）。 | [optional] 
**offline_time** | **str** | 用户上线的结束时间（接口调用方格林威治时间戳）。 | [optional] 
**account** | **str** | 用户名。 | [optional] 
**terminal_ip** | **str** | 终端IP地址。 | [optional] 
**user_group** | **str** | 终端用户所属用户组。 | [optional] 
**terminal_mac** | **str** | 终端MAC地址。 | [optional] 
**auth_type** | **str** | 认证方式（1---Portal认证。2---MAC免认证。3---第三方认证）。 | [optional] 
**user_type** | **str** | 用户类型（0---普通用户。1---短信用户。2---自注册用户。4---社交媒体用户。5---微信用户。6---Passcode用户。7---第三方用户。20---普通访客。64---匿名用户）。 | [optional] 
**auth_server_ip** | **str** | 认证服务器IP地址。 | [optional] 
**access_ssid** | **str** | 接入SSID。 | [optional] 
**device_mac** | **str** | 接入设备MAC地址。 | [optional] 
**device_ip** | **str** | 接入设备IP。 | [optional] 
**access_policy** | **str** | 接入授权策略。 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


