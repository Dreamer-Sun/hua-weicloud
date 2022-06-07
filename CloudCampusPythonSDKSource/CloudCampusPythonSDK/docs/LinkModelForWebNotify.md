# LinkModelForWebNotify

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**linkdn** | **str** |  | [optional] 
**linkname** | **str** |  | [optional] 
**anedn** | **str** |  | [optional] 
**anename** | **str** |  | [optional] 
**anestate** | **int** | 源网元状态： 0：未管理状态 1：在线状态 2：离线状态 3：未知状态 4：错误状态  | [optional] 
**aportdn** | **str** |  | [optional] 
**aportname** | **str** |  | [optional] 
**aportip** | **str** |  | [optional] 
**aportadminstatus** | **int** | 源端口管理状态： 1：正常状态 2：故障状态 3：测试状态  | [optional] 
**aportoperstatus** | **int** | 源端口运行状态： 1：正常状态 2：故障状态 3：测试状态 4：未知状态 5：休眠状态 6：不存在状态 7：下层状态down状态  | [optional] 
**znedn** | **str** |  | [optional] 
**znename** | **str** |  | [optional] 
**znestate** | **int** | 宿网元状态： 0：未管理状态 1：在线状态 2：离线状态 3：未知状态 4：错误状态  | [optional] 
**zportdn** | **str** |  | [optional] 
**zportname** | **str** |  | [optional] 
**zportip** | **str** |  | [optional] 
**zportadminstatus** | **int** | 宿端口管理状态： 1：正常状态 2：故障状态 3：测试状态  | [optional] 
**zportoperstatus** | **int** | 宿端口运行状态： 1：正常状态 2：故障状态 3：测试状态 4：未知状态 5：休眠状态 6：不存在状态 7：下层状态down状态  | [optional] 
**linkstatus** | **int** | 链路状态： 0：正常 1：未知 2：重要故障 3：紧急故障 4：离线 5：未管理  | [optional] 
**linktype** | **int** | 链路类型： 1：lldp链路 2：Side-By-Side链路 3：mac链路 4：cdp链路 5：非30位掩码的IP链路 6：由物理链路生成Eth-Trunk链路 99：手工  | [optional] 
**speed** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


