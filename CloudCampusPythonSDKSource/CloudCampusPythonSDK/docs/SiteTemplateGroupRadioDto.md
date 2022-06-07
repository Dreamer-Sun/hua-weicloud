# SiteTemplateGroupRadioDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_code** | **str** | 国家码。 | [optional] 
**calibrate** | **str** | 调优模式，只能为manual，auto，schedule其中一种。 | [optional] 
**dca_start_time** | **str** | 自动调优模式下有效。自动调优开始时间，时间格式hh:mm:ss。 | [optional] 
**dca_interval** | **int** | 自动调优模式下有效。自动调优时间周期，取值范围为30到1440之间的整数，单位（min）。 | [optional] 
**dca_schedule_time** | **str** | 定时调优模式下有效。定时调优开始时间，时间格式hh:mm:ss。 | [optional] 
**scan_duration** | **str** | 扫描时长，范围60~100，单位（ms）。 | [optional] 
**scan_interval** | **str** | 扫描间隔，范围300~600000，单位（ms）。 | [optional] 
**scan_channel** | **str** | 扫描信道，只能为country-channel，dca-channel，work-channel其中一种。 | [optional] 
**beacon_cycle** | **int** | beacon周期。取值范围为60到1000之间的整数。单位（TUs）。 | [optional] 
**dynamic_switch** | **bool** | 负载均衡。 | [optional] 
**reference_data_analysis** | **bool** | 是否基于历史数据进行射频调优，可选值: true(默认)，false。 | [optional] 
**group_radio2g** | [**GroupRadio2gConfigDto**](GroupRadio2gConfigDto.md) |  | [optional] 
**group_radio5g** | [**GroupRadio5gConfigDto**](GroupRadio5gConfigDto.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


