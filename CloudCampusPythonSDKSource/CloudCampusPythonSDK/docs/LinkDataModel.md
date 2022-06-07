# LinkDataModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**linkdn** | **str** | 链路DN | [optional] 
**linkname** | **str** | 链路名称 | [optional] 
**anedn** | **str** | 源网元DN | [optional] 
**anename** | **str** | 源网元名称 | [optional] 
**aneip** | **str** | 源网元IP | [optional] 
**anestate** | **int** | 源网元状态： 0：未管理 1：在线 2：离线 3：未知  | [optional] 
**aportdn** | **str** | 源端口DN | [optional] 
**aportname** | **str** | 源端口名称 | [optional] 
**aportip** | **str** | 源端口IP | [optional] 
**aportadminstatus** | **int** | 源端口管理状态： 1：up 2：down 3：testing  | [optional] 
**aportoperstatus** | **int** | 源端口运行状态： 1：up 2：down 3：testing 4：unknown 5：dormant 6：notPresent 7：lowerLayerDown  | [optional] 
**znedn** | **str** | 宿网元DN | [optional] 
**znename** | **str** | 宿网元名称 | [optional] 
**zneip** | **str** | 宿网元IP | [optional] 
**znestate** | **int** | 宿网元状态： 0：未管理 1：在线 2：离线 3：未知  | [optional] 
**zportdn** | **str** | 宿端口DN | [optional] 
**zportname** | **str** | 宿端口名称 | [optional] 
**zportip** | **str** | 宿端口IP | [optional] 
**zportadminstatus** | **int** | 宿端口管理状态： 1：up 2：down 3：testing  | [optional] 
**zportoperstatus** | **int** | 宿端口运行状态： 1：up 2：down 3：testing 4：unknown 5：dormant 6：notPresent 7：lowerLayerDown  | [optional] 
**linkstatus** | **int** | 链路状态： 0：正常 1：未知 2：重要故障 3：紧急故障 4：离线 5：不管理  | [optional] 
**linktype** | **int** | 链路类型： 1：LLDP 2：Side-By-Side链路 3：MACARP 4：CDP 5：IP 6：由物理链路生成Eth-Trunk链路 99：手工  | [optional] 
**speed** | **str** | 单位：Mbit/s | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


