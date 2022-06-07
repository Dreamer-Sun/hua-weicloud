# AuthenProfileDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | 认证模板ID，UUID格式，创建的时候非必填，更新则不允许修改此值。 | [optional] 
**name** | **str** | 认证模板名称，创建不允许创建相同的名称，更新不允许修改。 | 
**portal_enable** | **bool** | portal认证是否使能，默认为false。 | 
**mac_enable** | **bool** | mac认证是否使能，默认为false。 | 
**dot1x_enable** | **bool** | dot1x认证是否使能，默认为false。 | 
**radius_profile_id** | **str** | RADIUS模板ID，UUID格式。 | 
**radius_name** | **str** | RADIUS模板名称，要和radiusProfileId同属于同一个RADIUS模板。 | 
**portal_profile_id** | **str** | Portal模板ID，UUID格式。 | [optional] 
**portal_name** | **str** | Portal模板名称，要和portalProfileId同属于同一个portal模板。 | [optional] 
**domain** | **str** | 域名称。 | [optional] 
**radius_author** | **int** | RADIUS动态授权服务器模式，0表示默认，1表示自定义。 | 
**author_server_address** | **str** | 动态授权服务器IP，当radiusAuthor为0时，authorServerAddress不生效；当radiusAuthor为1时，authorServerAddress必填。 | [optional] 
**author_server_key** | **str** | 动态授权服务器密码，当radiusAuthor为0时，authorServerKey不生效；当radiusAuthor为1时，authorServerKey必填。 | [optional] 
**voice_auth_enable** | **bool** | 话机认证是否使能，默认为false。 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


