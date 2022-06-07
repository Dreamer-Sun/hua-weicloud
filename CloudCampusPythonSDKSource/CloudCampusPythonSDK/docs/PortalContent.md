# PortalContent

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_type_selection** | **str** | Portal认证类型。目前只支持portalController。 | 
**fast_push_enable** | **bool** | 使能快速推送。 | [optional] 
**portal_page_id** | **str** | 页面推送模板ID。当fastPushEnable为true时，portalPageId必填。 | [optional] 
**wechat_enable** | **bool** | 使能微信认证。当fastPushEnable为false时，wechatEnable生效。若fastPushEnable为true，则必须先配置微信认证参数。 | [optional] 
**anonymous_enable** | **bool** | 使能匿名认证。当fastPushEnable为false时，anonymousEnable生效。 | [optional] 
**pass_code_enable** | **bool** | 使能passCode认证。当fastPushEnable为false时，passCodeEnable生效。 | [optional] 
**social_media_enable** | **bool** | 使能facebook认证。若值为true，则必须先配置facebook认证参数。当fastPushEnable为false时，socialMediaEnable生效。 | [optional] 
**normal_enable** | **bool** | 使能用户名密码认证。当fastPushEnable为false时，normalEnable生效。 | [optional] 
**register_enable** | **bool** | 用户自注册使能。当normalEnable为true时，registerEnable生效。 | [optional] 
**register_expire_unit** | **str** | 用户注册有效期单位。当registerEnable为true时，registerExpireUnit生效。 | [optional] 
**register_expire** | **int** | 用户注册有效期。当registerEnable为true时，registerExpire生效。当registerExpireUnit为minute时，registerExpire取值范围为1~59。当registerExpireUnit为hour时，registerExpire取值范围为1~23。当registerExpireUnit为day时，registerExpire取值范围为1~365。 | [optional] 
**user_register_max_access_number** | **int** | 用户最大接入数。当registerEnable为true时，userRegisterMaxAccessNumber生效。 | [optional] 
**user_group_id** | **str** | 用户名密码认证的自注册用户注册后所属的用户组ID，UUID格式。当registerEnable为true时，userGroupId生效。 | [optional] 
**user_group_name** | **str** | 用户名密码认证的自注册用户注册后所属的用户组名称。当registerEnable为true时，userGroupName生效。 | [optional] 
**free_auth_mode** | **str** | 有效期内免认证方式。mac表示开启免认证，reAuth则表示不开启免认证。 | 
**auth_expire** | **int** | Portal认证有效期，当freeAuthMode为mac时，authExpire必填。当authExpireUnit为minute时，authExpire取值范围为1~59。当authExpireUnit为hour时，authExpire取值范围为1~23。当authExpireUnit为day时，authExpire取值范围为1~365。 | [optional] 
**auth_expire_unit** | **str** | Portal认证有效期单位，当freeAuthMode为mac时，authExpireUnit必填。只能为day、hour、minute中的一个，大小写不敏感，前后空格忽略，且不能含有全角字符。 | [optional] 
**sms_auth_enable** | **bool** | 是否启用短信认证。若smsAuthEnable值为true，则必须配置短信服务器。当fastPushEnable为false时，smsAuthEnable生效。 | [optional] 
**sms_user_expire** | **int** | 短信认证用户有效期，当smsAuthEnable为true时，smsUserExpire生效。当smsUserExpireUnit为minute时，smsUserExpire取值范围为1~59。当smsUserExpireUnit为hour时，smsUserExpire取值范围为1~23。当smsUserExpireUnit为day时，smsUserExpire取值范围为1~365。 | [optional] 
**sms_user_expire_unit** | **str** | 短信认证用户有效期单位只能为day、hour、minute中的一个，大小写不敏感，前后空格忽略，且不能含有全角字符。当smsAuthEnable为true时，smsUserExpireUnit生效。 | [optional] 
**sms_user_max_access_number** | **int** | 短信认证用户最大接入数。当smsAuthEnable为true时，smsUserMaxAccessNumber生效。 | [optional] 
**sms_password_expire** | **int** | 密码有效期。当smsAuthEnable为true时，smsUserMaxAccessNumber生效。当smsPasswordExpireUnit为minute时，smsPasswordExpire取值范围为1~59。当smsPasswordExpireUnit为hour时，smsPasswordExpire取值范围为1~23。当smsPasswordExpireUnit为day时，smsPasswordExpire取值范围为1~365。 | [optional] 
**sms_password_expire_unit** | **str** | 密码有效期单位。只能为day、hour、minute中的一个，大小写不敏感，前后空格忽略，且不能含有全角字符。当smsAuthEnable为true时，smsUserMaxAccessNumber生效。 | [optional] 
**sms_user_group_id** | **str** | 短信认证用户所属组ID，UUID格式。当smsAuthEnable为true时，smsUserMaxAccessNumber生效。 | [optional] 
**sms_user_group_name** | **str** | 短信认证用户所属组名。当smsAuthEnable为true时，smsUserMaxAccessNumber生效。 | [optional] 
**accounting_enable** | **bool** | 使能实时计费。 | 
**accounting_expire** | **int** | 实时计费上报周期。当accountingExpireUnit为minute时，范围为1~65535。 accountingEnable为true时，accountingExpire生效。 | [optional] 
**accounting_expire_unit** | **str** | 实时计费上报周期单位，只能为minute，大小写不敏感，前后空格忽略，且不能含有全角字符。accountingEnable为true时，accountingExpireUnit生效。 | [optional] 
**ip_v6_auth_enable** | **bool** | IPV6是否开启。 | [optional] 
**escape_strategy** | **str** | 逃生策略。noNew：允许已认证用户继续使用网络，新用户不允许接入。默认值。noAuth：允许已认证用户继续使用网络，新用户需要输入PPSK密钥。注意：此时PPSK用户数控制MCA自动绑定功失效。  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


