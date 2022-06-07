# AuthenticationLogOutputDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_row_key** | **str** | 查询结果中起始rowkey值。 | [optional] 
**end_row_key** | **str** | 查询结果中结束rowkey值。 | [optional] 
**total_records** | **int** | 本次查询到的总结果数。最大取值为101，不足101条时表示当前数据已查询完；等于101条表示后续还有数据。 | [optional] 
**errcode** | **str** | 错误码。0表示没有错误。 | [optional] 
**errmsg** | **str** | 错误信息描述。 | [optional] 
**search_result_list** | [**list[AuthenticationLogDetailOutputDto]**](AuthenticationLogDetailOutputDto.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


