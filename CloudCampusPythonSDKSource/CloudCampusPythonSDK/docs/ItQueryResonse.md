# ItQueryResonse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | 操作返回码。可以是如下值之一： 0：成功 非0：失败  | 
**data** | [**list[LinkInfoBo]**](LinkInfoBo.md) | 链路列表 | 
**description** | **str** | 接口调用结果的描述信息。 | 
**size** | **int** | 接口调用结果的描述信息。 | 
**total_page** | **int** | 分页查询的总页数：size/ pageSize，如果余数大于0说明有未满页的尾页，再+1。 | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


