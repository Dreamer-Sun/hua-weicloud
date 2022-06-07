# DataUploadDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mu** | **bool** | 是否开启上传功能，将终端位置信息上报到指定服务器。 | [optional] 
**server_ip** | **str** | 服务器IP/域名。当mu为true时，serverIp必填。 | [optional] 
**server_port** | **int** | 端口号，必须为1-65535范围内的整数，不填默认为10031。端口号跟服务器IP/域名要么都填，要么都不填。 | [optional] 
**interver** | **int** | 上报周期，单位为ms，必须是500-60000范围内的整数，不填默认为20000。 | [optional] 
**rssi** | **int** | 阀值，必须为-95-0范围内的整数，不填默认为-75。 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


