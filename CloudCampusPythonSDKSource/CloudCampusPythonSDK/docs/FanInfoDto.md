# FanInfoDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | 风扇ID。 | [optional] 
**online_state** | **str** | 风扇在线状态。取值范围：0（代表present在位），1（代表absent不在位）。 | [optional] 
**register_state** | **str** | 风扇注册状态。取值范围：0（代表unregisted未注册），1（代表registed已注册）。 | [optional] 
**running_state** | **str** | 风扇运行状态 。取值范围：0（代表unknown未知），1（代表normal正常），2（代表abnormal不正常）。 | [optional] 
**speed** | **int** | 风扇转速，转速与全速的百分比，取值范围1-100。 | [optional] 
**mode** | **str** | 风扇模式，取值范围：1（代表AUTO：自动调节转速）；2（代表MANUAL：固定转速）；0（代表UNKNOW：风扇不在位）。 | [optional] 
**air_flow** | **str** | 风扇的风向，取值范围：Back-to-Side（表示风由后面向两侧吹）；Side-to-Back（表示风由两侧向后面吹）；Side-to-Side（表示风由一侧往另外一侧吹）；-（风扇不在位）。 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


