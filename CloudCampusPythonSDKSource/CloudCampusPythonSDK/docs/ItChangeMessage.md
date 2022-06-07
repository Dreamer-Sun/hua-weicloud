# ItChangeMessage

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**msg_type** | **int** | 消息类型： 1：创建 2：删除  | [optional] 
**resource_uri** | **str** |  | [optional] [default to '/rest/openapi/notification/it/link']
**module_id** | **str** | 模块ID | [optional] [default to 'com.huawei.it.link.notification']
**data_object_json** | [**list[DataObjectJson]**](DataObjectJson.md) | 数据内容，为一个JSON 化的对象，此处应当link信息。 | [optional] 
**utc_timestamp** | **int** | 该事件对象产生的UTC时刻 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


