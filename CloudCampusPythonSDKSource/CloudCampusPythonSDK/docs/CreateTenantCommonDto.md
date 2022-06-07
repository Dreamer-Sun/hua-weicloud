# CreateTenantCommonDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit_account_num** | **int** | 帐号数量限制，默认值：20。 | [optional] 
**user_account** | **str** | 租户默认管理员帐号。 | [optional] 
**user_email** | **str** | 租户默认管理员邮箱，用于接收初始化密码邮件。如未填，将按照租户默认管理员帐号发送邮件。 | [optional] 
**send_init_email_enable** | **bool** | 是否发送初始化邮件，默认：true。 | [optional] 
**country_code** | **str** | 国家码，不填默认CN。 | [optional] 
**is_logo_inherit** | **bool** | 租户logo是否继承自MSP。 | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


