# AddPortalPageRuleInputDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | 名称。 | 
**description** | **str** | 描述。 | [optional] 
**ss_ids** | **list[str]** | SSID列表，如果参数为空，则页面推送策略适用于站点下所有SSID，格式为UUID。 | [optional] 
**push_mode** | **int** | 推送方式，当前只支持0：第三方认证。 | 
**third_page_url** | **str** | 第三方推送URL，当pushMode为0时，必填。 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


