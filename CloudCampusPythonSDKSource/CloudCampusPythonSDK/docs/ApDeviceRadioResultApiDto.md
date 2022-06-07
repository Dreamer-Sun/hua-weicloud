# ApDeviceRadioResultApiDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**radio2dot4_enabled** | **bool** | 2.4G射频使能状态。 | 
**radio2dot4_power** | **str** | 2.4G射频发射功率，auto，[1,127]。 | 
**radio2dot4_channel** | **str** | 2.4G射频信道，不同国家码，对应不同的射频信道范围。 | 
**radio2dot4_bandwidth** | **str** | 2.4G调优频宽，调优带宽时选择auto，此时2.4G信道也应该为auto。 | 
**antenna2_dot4_gain** | **str** | 2.4G射频天线增益，0~30，室内AP天线增益不支持修改。 | 
**radio5_enabled** | **bool** | 5G射频使能状态。 | 
**radio5_power** | **str** | 5G射频发射功率，auto，[1,127]。 | 
**radio5_channel** | **str** | 5G射频信道，不同国家码，对应不同的射频信道范围。 | 
**antenna5_gain** | **str** | 5G射频天线增益，0~30，室内AP天线增益不支持修改。 | 
**radio5_bandwidth** | **str** | 5G射频频宽，调优带宽时选择auto，此时5G信道也应该为auto。 | 
**device_id** | **str** | 设备ID。 | [optional] 
**device_name** | **str** | 设备名称。 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


