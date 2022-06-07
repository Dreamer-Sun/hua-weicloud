# UpdatePortalPageRuleInputDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | 名称。 | 
**description** | **str** | 描述。 | [optional] 
**priority** | **str** | 优先级。如果priority的值与修改前相同，那么修改操作只处理除priority以外的信息，否则修改操作只处理优先级。优先级数值越小，越优先匹配。 | [optional] 
**ss_ids** | **list[str]** | SSID列表，如果参数为空，则页面推送策略适用于站点下所有SSID，格式为UUID。 | [optional] 
**push_mode** | **int** | 推送方式，当前只支持0：第三方认证。 | 
**third_page_url** | **str** | 第三方推送URL，当pushMode为0时，必填。 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


