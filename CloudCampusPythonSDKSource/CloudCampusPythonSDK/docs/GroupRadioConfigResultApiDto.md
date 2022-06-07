# GroupRadioConfigResultApiDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_code** | **str** | 国家码。 | 
**scan_duration** | **str** | 扫描时长，范围60~100，单位（ms）。 | 
**scan_interval** | **str** | 扫描间隔，范围300~600000，单位（ms）。 | 
**scan_channel** | **str** | 扫描信道。 | 
**dca2g_channel_set** | **str** | 2.4G调优信道集。可选\&quot;1，6，11\&quot;和\&quot;1，5，9，13\&quot;两种信道集。 | 
**dca_bandwidth** | **str** | 5G调优频宽，只能为20mhz，40mhz，80mhz其中一种。 | 
**dca5g_channel_set** | **str** | 5G调优信道集。当5G调优频宽为20MHz时，支持的信道有36，40，44，48，52，56，60，64，149，153，157，161，165； 当5G调优信道为40MHz或80MHz时，支持的信道有36，40，44，48，52，56，60，64，149，153，157，161。 为了确保校准结果，请选择至少三个选项。若可选信道少于三个，则此国家不支持配置此调优频宽。 | 
**calibrate** | **str** | 调优模式。 | 
**dca_start_time** | **str** | 自动调优模式下开始时间。 | 
**dca_interval** | **int** | 自动调优模式下周期，单位（min）。 | 
**dca_schedule_time** | **str** | 定时调优模式下调优时间。 | 
**tpc_max_tx_pwr** | **int** | TPC上限。 | 
**tpc_min_tx_pwr** | **int** | TPC下限。 | 
**tpc_coverage_threshold** | **int** | TPC阈值。 | 
**radio2_dot4_guard_interval_mode** | **str** | 2.4G射频间隔(GI)模式，可填default(默认)、short(短间隔)或normal(普通间隔)。普通间隔的时间为800ns，在802.11n和802.11ac标准中允许使用短间隔，为400ns，可以提高802.11n和802.11ac的传输率。 | [optional] 
**radio5_guard_interval_mode** | **str** | 5G射频间隔(GI)模式，可填default(默认)、short(短间隔)或normal(普通间隔)。普通间隔的时间为800ns，在802.11n和802.11ac标准中允许使用短间隔，为400ns，可以提高802.11n和802.11ac的传输率。 | [optional] 
**reference_data_analysis** | **bool** | 是否基于历史数据进行射频调优，可选值: true(默认)，false。 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


