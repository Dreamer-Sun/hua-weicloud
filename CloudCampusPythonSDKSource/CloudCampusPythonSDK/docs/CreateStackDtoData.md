# CreateStackDtoData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stack_name** | **str** | 堆叠名称。如果堆叠名称已存在，则将设备加入堆叠；否则，创建堆叠并加入设备。堆叠名称不能包含\&quot;?\&quot;或者制表符TAB。 | 
**stack_member** | [**list[StackMemberInput]**](StackMemberInput.md) | 堆叠成员。 | 
**stack_roles** | **str** | 堆叠角色信息。非必填，默认为ACC。 | [optional] [default to 'ACC']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


